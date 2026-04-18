#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from deafpiper.agent_instruction import InstructionBuilder, RequiredArtifact
from deafpiper.audit import AuditLogger, AuditQuery, FileBackedAuditEntryStore, FileBackedContentStore
from deafpiper.budget import BudgetEnforcer
from deafpiper.comparison import Comparator
from deafpiper.decision import DecisionEngine
from deafpiper.models import ArtifactCandidate, BudgetPolicy, Constraint
from deafpiper.pipeline_runtime import PipelineRuntimeMapper
from deafpiper.provider import ModelCapabilityRegistry, ProviderResolver, ToolBroker
from deafpiper.reproducibility import ReproducibilitySurface
from deafpiper.validation import ValidationRunner, make_builtin_registry


def run_example(out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    audit_store = FileBackedAuditEntryStore(out_dir / "audit_entries.json")
    content_store = FileBackedContentStore(out_dir / "audit_content.json")
    logger = AuditLogger(audit_store, content_store)
    query = AuditQuery(audit_store, content_store)

    mapper = PipelineRuntimeMapper(ROOT)
    task = mapper.build_task("task-demo", "Pipeline Demo", "Run full task lifecycle")
    steps = mapper.build_steps(task)

    logger.log({"type": "agent", "id": "example"}, "Task", task.id, "created", None, task.status, task.to_dict())

    budget_policy = BudgetPolicy(
        id="budget-default",
        limits={"tokens": 100, "tool_calls": 2},
        on_breach="downgrade_deferred",
        scope="task",
    )
    budget = BudgetEnforcer(budget_policy, logger)

    builder = InstructionBuilder()
    instruction = builder.build(
        task=task,
        step=steps[0],
        constraints=[Constraint(id="c-paths", scope="task", kind="path_deny", predicate={"paths": ["infra/"]}, rationale="no infra", source="policy")],
        budget_policy=budget_policy,
        required_artifacts=[RequiredArtifact(kind="code_diff", schema_ref="schema://diff", min_count=1, max_count=1)],
        applicable_rules=[{"id": "structural", "severity": "blocker"}],
    )

    registry = make_builtin_registry()
    runner = ValidationRunner(registry)
    artifact = ArtifactCandidate(
        id="art-1",
        step_id=steps[0].id,
        type="diff",
        content_ref="diff://sample",
        produced_at=task.created_at,
        producer="example-agent",
        baseline_ref="baseline://main",
    )
    env_ref = ReproducibilitySurface.build_environment_ref({"example": True})
    results = runner.run(artifact, ["structural"], environment_ref=env_ref)

    comparator = Comparator()
    comparison = comparator.compare(
        artifact_candidate_id=artifact.id,
        baseline_ref="baseline://main",
        candidate_metrics={"quality": 0.1},
        baseline_metrics={"quality": 0.05},
        directions={"quality": "higher_is_better"},
        blocking_dimensions=["quality"],
    )
    decision = DecisionEngine().decide(
        artifact_candidate_id=artifact.id,
        comparison_result=comparison,
        test_results=results,
        rework_budget_remaining=True,
        failure_is_diagnosable=True,
        decided_by="example-agent",
        budget_state=budget.state.to_dict(),
    )

    capabilities = ModelCapabilityRegistry()
    capabilities.register("model-lite", {"supports_tool_use": True})
    binding = ProviderResolver(capabilities).resolve(instruction, {"default_model": "model-lite", "required_capabilities": ["supports_tool_use"]})
    tool_result = ToolBroker(logger).invoke(
        "filesystem",
        {"action": "read", "provider_capabilities": binding.capabilities},
        instruction,
    )

    budget.record_usage(tokens=120, tool_calls=1)
    breach_1 = budget.evaluate(task.id)
    budget.record_usage(tokens=1)
    breach_2 = budget.evaluate(task.id)

    summary = {
        "task": task.to_dict(),
        "step": steps[0].to_dict(),
        "decision": decision.to_dict(),
        "tool_result": tool_result,
        "breach_sequence": [breach_1, breach_2],
        "history_entries": len(query.get_history(task.id)),
    }
    return summary


if __name__ == "__main__":
    output = run_example(Path(".deafpiper_example"))
    print(json.dumps(output, indent=2))
