import json
import tempfile
import unittest
from pathlib import Path

from deafpiper.agent_instruction import (
    AgentInstructionSet,
    AllowedTool,
    BudgetSpec,
    ContextRef,
    DeadEndSpec,
    EscalationPath,
    InstructionConstraint,
    InstructionInput,
    ObjectiveSpec,
    RequiredArtifact,
    ScopePath,
    ScopeSpec,
    TouchLimit,
    ValidationSpec,
)
from deafpiper.audit import FileBackedAuditEntryStore, FileBackedContentStore, AuditLogger
from deafpiper.budget import BudgetEnforcer
from deafpiper.models import BudgetPolicy
from deafpiper.pipeline_runtime import PipelineRuntimeMapper
from deafpiper.provider import ModelCapabilityRegistry, ProviderResolver, ToolBroker
from deafpiper.reproducibility import ReproducibilitySurface


class Phase11RuntimeExtensionsTests(unittest.TestCase):
    def _instruction_set(self) -> AgentInstructionSet:
        return AgentInstructionSet(
            id="ins-1",
            version="1.0.0",
            task_ref="task-1",
            step_ref="step-1",
            created_at="2026-01-01T00:00:00+00:00",
            objective=ObjectiveSpec(statement="Do thing.", success_signal="done"),
            scope=ScopeSpec(
                includes=[ScopePath(path="src/", rationale="include")],
                excludes=[ScopePath(path="infra/", rationale="exclude")],
                touch_limit=TouchLimit(max_files_changed=1, max_lines_changed=10),
            ),
            constraints=[InstructionConstraint(id="c1", kind="path_deny", predicate={"paths": ["infra/"]}, severity="blocker")],
            inputs=[InstructionInput(ref="r1", kind="spec", required=True)],
            required_artifacts=[RequiredArtifact(kind="code_diff", schema_ref="schema://x", min_count=1, max_count=1)],
            validation=ValidationSpec(applicable_rules=[{"id": "structural", "severity": "blocker"}], pre_execution_checks=[]),
            dead_end=DeadEndSpec(
                max_iterations=2,
                max_tool_calls=10,
                max_wall_time_s=60,
                on_repeated_identical_output="stop",
                on_ambiguous_requirement="escalate",
                on_constraint_violation_attempt="stop",
            ),
            escalation_path=EscalationPath(trigger="dead_end", destination="human_review", payload_template="x"),
            budget=BudgetSpec(tokens=100, cost_usd=1.0, wall_time_s=60, tool_calls=10, on_breach="stop"),
            allowed_tools=[
                AllowedTool(tool_id="filesystem", scope={"paths": ["src/"], "requires_capabilities": ["supports_tool_use"]})
            ],
            context_refs=[ContextRef(ref="docs/ARCHITECTURE.md", kind="doc", inclusion_reason="spec")],
        )

    def test_file_backed_stores_persist(self):
        with tempfile.TemporaryDirectory() as tmp:
            entry_path = Path(tmp) / "entries.json"
            content_path = Path(tmp) / "content.json"

            logger = AuditLogger(FileBackedAuditEntryStore(entry_path), FileBackedContentStore(content_path))
            logger.log(
                actor={"type": "agent", "id": "a1"},
                subject_type="Task",
                subject_id="task-1",
                event="created",
                previous_state=None,
                new_state="draft",
                payload={"x": 1},
            )

            reloaded_entries = json.loads(entry_path.read_text(encoding="utf-8"))
            reloaded_content = json.loads(content_path.read_text(encoding="utf-8"))
            self.assertEqual(len(reloaded_entries), 1)
            self.assertEqual(len(reloaded_content), 1)

    def test_deferred_budget_downgrade_requires_second_breach(self):
        policy = BudgetPolicy(id="b2", limits={"tokens": 10}, on_breach="downgrade_deferred", scope="task")
        enforcer = BudgetEnforcer(policy)

        enforcer.record_usage(tokens=10)
        first = enforcer.evaluate("task-1")
        enforcer.record_usage(tokens=1)
        second = enforcer.evaluate("task-1")

        self.assertEqual(first["resolved_action"], "defer_downgrade")
        self.assertEqual(second["resolved_action"], "downgrade")

    def test_resolver_and_tool_broker_capability_routing(self):
        registry = ModelCapabilityRegistry()
        registry.register("model-no-tools", {"supports_tool_use": False})
        registry.register("model-tools", {"supports_tool_use": True})

        instruction = self._instruction_set()
        binding = ProviderResolver(registry).resolve(
            instruction,
            {"default_model": "model-no-tools", "required_capabilities": ["supports_tool_use"]},
        )
        self.assertEqual(binding.model_id, "model-tools")

        broker = ToolBroker()
        denied = broker.invoke("filesystem", {"provider_capabilities": {"supports_tool_use": False}}, instruction)
        allowed = broker.invoke("filesystem", {"provider_capabilities": {"supports_tool_use": True}}, instruction)
        self.assertEqual(denied["status"], "denied")
        self.assertEqual(allowed["status"], "ok")

    def test_reproducibility_surface_hash_is_stable(self):
        h1 = ReproducibilitySurface.hash_payload({"a": 1, "b": 2})
        h2 = ReproducibilitySurface.hash_payload({"b": 2, "a": 1})
        self.assertEqual(h1, h2)

    def test_pipeline_runtime_mapper_creates_steps(self):
        mapper = PipelineRuntimeMapper(Path("."))
        task = mapper.build_task("task-x", "x", "y")
        steps = mapper.build_steps(task)
        self.assertGreater(len(steps), 0)
        self.assertTrue(steps[0].id.startswith("step-"))


if __name__ == "__main__":
    unittest.main()
