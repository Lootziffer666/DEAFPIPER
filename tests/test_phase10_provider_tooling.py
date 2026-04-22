import unittest

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
from deafpiper.provider import CostAccountant, ModelCapabilityRegistry, ProviderResolver, ToolBroker


class Phase10ProviderToolingTests(unittest.TestCase):
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
            allowed_tools=[AllowedTool(tool_id="filesystem", scope={"paths": ["src/"]})],
            context_refs=[ContextRef(ref="docs/ARCHITECTURE.md", kind="doc", inclusion_reason="spec")],
        )

    def test_provider_resolver_and_cost_accountant(self):
        registry = ModelCapabilityRegistry()
        registry.register("model-x", {"supports_tool_use": True, "max_context_tokens": 200_000})
        resolver = ProviderResolver(registry)
        binding = resolver.resolve(self._instruction_set(), {"default_model": "model-x", "provider_id": "openai"})

        accountant = CostAccountant()
        accountant.record("task-1", tokens=123, duration=0.5, provider_binding=binding)
        summary = accountant.summarize("task-1")

        self.assertEqual(summary["tokens"], 123)
        self.assertEqual(binding.provider_id, "openai")

    def test_tool_broker_allowlist(self):
        instruction_set = self._instruction_set()
        broker = ToolBroker()
        allowed = broker.invoke("filesystem", {"action": "read"}, instruction_set)
        denied = broker.invoke("network", {"action": "fetch"}, instruction_set)

        self.assertEqual(allowed["status"], "ok")
        self.assertEqual(denied["status"], "denied")


if __name__ == "__main__":
    unittest.main()
