from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Mapping, Optional, Sequence

from .models import BudgetPolicy, Constraint, Step, Task


@dataclass(frozen=True)
class ObjectiveSpec:
    statement: str
    success_signal: str


@dataclass(frozen=True)
class ScopePath:
    path: str
    rationale: str


@dataclass(frozen=True)
class TouchLimit:
    max_files_changed: int
    max_lines_changed: int


@dataclass(frozen=True)
class ScopeSpec:
    includes: List[ScopePath]
    excludes: List[ScopePath]
    touch_limit: TouchLimit


@dataclass(frozen=True)
class InstructionConstraint:
    id: str
    kind: str
    predicate: Any
    severity: str


@dataclass(frozen=True)
class InstructionInput:
    ref: str
    kind: str
    required: bool


@dataclass(frozen=True)
class RequiredArtifact:
    kind: str
    schema_ref: str
    min_count: int
    max_count: int


@dataclass(frozen=True)
class ValidationSpec:
    applicable_rules: List[Dict[str, str]]
    pre_execution_checks: List[Dict[str, str]]


@dataclass(frozen=True)
class DeadEndSpec:
    max_iterations: int
    max_tool_calls: int
    max_wall_time_s: int
    on_repeated_identical_output: str
    on_ambiguous_requirement: str
    on_constraint_violation_attempt: str


@dataclass(frozen=True)
class EscalationPath:
    trigger: str
    destination: str
    payload_template: str


@dataclass(frozen=True)
class BudgetSpec:
    tokens: int
    cost_usd: float
    wall_time_s: int
    tool_calls: int
    on_breach: str


@dataclass(frozen=True)
class AllowedTool:
    tool_id: str
    scope: Dict[str, List[str]]


@dataclass(frozen=True)
class ContextRef:
    ref: str
    kind: str
    inclusion_reason: str


@dataclass(frozen=True)
class AgentInstructionSet:
    id: str
    version: str
    task_ref: str
    step_ref: str
    created_at: str
    objective: ObjectiveSpec
    scope: ScopeSpec
    constraints: List[InstructionConstraint]
    inputs: List[InstructionInput]
    required_artifacts: List[RequiredArtifact]
    validation: ValidationSpec
    dead_end: DeadEndSpec
    escalation_path: EscalationPath
    budget: BudgetSpec
    allowed_tools: List[AllowedTool]
    context_refs: List[ContextRef]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class InstructionValidator:
    @staticmethod
    def validate(instruction_set: AgentInstructionSet) -> None:
        if not instruction_set.objective.statement or "\n" in instruction_set.objective.statement:
            raise ValueError("objective.statement must be a non-empty single sentence")
        if not instruction_set.scope.includes:
            raise ValueError("scope.includes must not be empty")
        if not instruction_set.scope.excludes:
            raise ValueError("scope.excludes must declare forbidden paths")
        if not instruction_set.required_artifacts:
            raise ValueError("required_artifacts must not be empty")
        if not instruction_set.validation.applicable_rules:
            raise ValueError("validation.applicable_rules must not be empty")
        if instruction_set.dead_end.max_iterations <= 0:
            raise ValueError("dead_end.max_iterations must be > 0")
        if instruction_set.escalation_path.destination not in {"human_review", "parent_task", "policy_arbiter"}:
            raise ValueError("escalation_path.destination is invalid")
        if instruction_set.budget.tokens <= 0 and instruction_set.budget.tool_calls <= 0 and instruction_set.budget.wall_time_s <= 0:
            raise ValueError("budget must set at least one positive limit")
        if not instruction_set.allowed_tools:
            raise ValueError("allowed_tools must be an explicit allow-list")


class InstructionBuilder:
    def build(
        self,
        task: Task,
        step: Step,
        constraints: Sequence[Constraint],
        budget_policy: BudgetPolicy,
        required_artifacts: Sequence[RequiredArtifact],
        applicable_rules: Sequence[Dict[str, str]],
    ) -> AgentInstructionSet:
        includes = [ScopePath(path=p, rationale="task scope include") for p in task.scope.get("includes", [])]
        excludes = [ScopePath(path=p, rationale="task scope exclude") for p in task.scope.get("excludes", [])]

        instruction_set = AgentInstructionSet(
            id=f"ins-{task.id}-{step.id}",
            version="1.0.0",
            task_ref=task.id,
            step_ref=step.id,
            created_at=datetime.now(timezone.utc).isoformat(),
            objective=ObjectiveSpec(statement=step.objective, success_signal="expected outputs produced"),
            scope=ScopeSpec(
                includes=includes,
                excludes=excludes,
                touch_limit=TouchLimit(max_files_changed=20, max_lines_changed=800),
            ),
            constraints=[
                InstructionConstraint(
                    id=c.id,
                    kind=c.kind,
                    predicate=c.predicate,
                    severity="blocker",
                )
                for c in constraints
            ],
            inputs=[InstructionInput(ref=ref, kind="prior_diff", required=False) for ref in step.inputs],
            required_artifacts=list(required_artifacts),
            validation=ValidationSpec(applicable_rules=list(applicable_rules), pre_execution_checks=[]),
            dead_end=DeadEndSpec(
                max_iterations=2,
                max_tool_calls=int(budget_policy.limits.get("tool_calls", 50)),
                max_wall_time_s=int(budget_policy.limits.get("wall_time_s", 1800)),
                on_repeated_identical_output="stop",
                on_ambiguous_requirement="escalate",
                on_constraint_violation_attempt="stop",
            ),
            escalation_path=EscalationPath(
                trigger="dead_end",
                destination="human_review",
                payload_template="task={task_ref},step={step_ref},category={dead_end_category}",
            ),
            budget=BudgetSpec(
                tokens=int(budget_policy.limits.get("tokens", 0)),
                cost_usd=float(budget_policy.limits.get("cost_usd", 0)),
                wall_time_s=int(budget_policy.limits.get("wall_time_s", 0)),
                tool_calls=int(budget_policy.limits.get("tool_calls", 0)),
                on_breach=budget_policy.on_breach,
            ),
            allowed_tools=[AllowedTool(tool_id="filesystem", scope={"paths": task.scope.get("includes", [])})],
            context_refs=[ContextRef(ref="docs/ARCHITECTURE.md", kind="doc", inclusion_reason="primary spec")],
        )

        InstructionValidator.validate(instruction_set)
        return instruction_set
