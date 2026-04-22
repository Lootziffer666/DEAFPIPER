from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Iterable, List, Mapping, Sequence, Tuple

from .models import ArtifactCandidate, Constraint, TestResult, ValidationRule


RuleEvaluator = Callable[[ArtifactCandidate, Mapping[str, Any]], Tuple[str, Dict[str, Any]]]


@dataclass(frozen=True)
class RegisteredRule:
    rule: ValidationRule
    evaluator: RuleEvaluator


class RuleRegistry:
    def __init__(self) -> None:
        self._rules: Dict[str, RegisteredRule] = {}

    def register(self, rule: ValidationRule, evaluator: RuleEvaluator) -> None:
        self._rules[rule.id] = RegisteredRule(rule=rule, evaluator=evaluator)

    def get(self, rule_id: str) -> RegisteredRule:
        if rule_id not in self._rules:
            raise KeyError(f"Unknown ValidationRule id: {rule_id}")
        return self._rules[rule_id]

    def list_rules(self) -> List[ValidationRule]:
        return [registered.rule for registered in self._rules.values()]


class ConstraintEvaluator:
    """Evaluates simple path and action constraints against a candidate execution context."""

    @staticmethod
    def evaluate(constraints: Sequence[Constraint], context: Mapping[str, Any]) -> List[str]:
        violations: List[str] = []
        touched_paths = set(context.get("touched_paths", []))
        actions = set(context.get("actions", []))

        for constraint in constraints:
            if constraint.kind == "path_deny":
                denied = set(constraint.predicate.get("paths", []))
                matched = touched_paths.intersection(denied)
                if matched:
                    violations.append(f"{constraint.id}: denied path touched: {sorted(matched)}")
            elif constraint.kind == "action_deny":
                denied = set(constraint.predicate.get("actions", []))
                matched = actions.intersection(denied)
                if matched:
                    violations.append(f"{constraint.id}: denied action used: {sorted(matched)}")

        return violations


class ValidationRunner:
    def __init__(self, registry: RuleRegistry, constraint_evaluator: ConstraintEvaluator | None = None) -> None:
        self.registry = registry
        self.constraint_evaluator = constraint_evaluator or ConstraintEvaluator()

    def run(
        self,
        artifact: ArtifactCandidate,
        applicable_rule_ids: Iterable[str],
        environment_ref: str,
        context: Mapping[str, Any] | None = None,
        constraints: Sequence[Constraint] | None = None,
    ) -> List[TestResult]:
        context = context or {}
        constraints = constraints or []
        executed_at = datetime.now(timezone.utc).isoformat()
        results: List[TestResult] = []

        violations = self.constraint_evaluator.evaluate(constraints, context)
        if violations:
            results.append(
                TestResult(
                    id=f"tr-{artifact.id}-constraint",
                    artifact_candidate_id=artifact.id,
                    validation_rule_id="constraint_evaluator",
                    outcome="fail",
                    detail={"violations": violations},
                    duration_ms=0,
                    executed_at=executed_at,
                    environment_ref=environment_ref,
                )
            )

        for rule_id in applicable_rule_ids:
            registered = self.registry.get(rule_id)
            outcome, detail = registered.evaluator(artifact, context)
            results.append(
                TestResult(
                    id=f"tr-{artifact.id}-{rule_id}",
                    artifact_candidate_id=artifact.id,
                    validation_rule_id=rule_id,
                    outcome=outcome,
                    detail=detail,
                    duration_ms=int(detail.get("duration_ms", 0)),
                    executed_at=executed_at,
                    environment_ref=environment_ref,
                )
            )

        return results


def make_builtin_registry() -> RuleRegistry:
    """Creates a registry with deterministic builtin rules for phase 3."""

    registry = RuleRegistry()

    builtin_rules = [
        ValidationRule(
            id="structural",
            applies_to="*",
            kind="static_check",
            executor="builtin",
            pass_criteria={"must_parse": True},
            severity="blocker",
        ),
        ValidationRule(
            id="test_suite",
            applies_to="*",
            kind="test_suite",
            executor="builtin",
            pass_criteria={"tests_must_pass": True},
            severity="blocker",
        ),
        ValidationRule(
            id="lint",
            applies_to="*",
            kind="policy",
            executor="builtin",
            pass_criteria={"max_warnings": 0},
            severity="warning",
        ),
        ValidationRule(
            id="policy",
            applies_to="*",
            kind="policy",
            executor="builtin",
            pass_criteria={"policy_violations": 0},
            severity="blocker",
        ),
        ValidationRule(
            id="schema",
            applies_to="*",
            kind="schema",
            executor="builtin",
            pass_criteria={"schema_valid": True},
            severity="blocker",
        ),
    ]

    def _context_outcome(rule_id: str) -> RuleEvaluator:
        def evaluator(_: ArtifactCandidate, context: Mapping[str, Any]) -> Tuple[str, Dict[str, Any]]:
            default = {"outcome": "pass", "detail": {"note": "default pass", "duration_ms": 1}}
            raw = context.get("rule_outcomes", {}).get(rule_id, default)
            return raw["outcome"], raw.get("detail", {"duration_ms": 1})

        return evaluator

    for rule in builtin_rules:
        registry.register(rule, _context_outcome(rule.id))

    return registry
