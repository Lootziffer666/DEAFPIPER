import unittest

from deafpiper.agent_instruction import InstructionBuilder, RequiredArtifact
from deafpiper.models import BudgetPolicy, Constraint, Step, Task


class Phase6AgentInstructionTests(unittest.TestCase):
    def test_builder_creates_valid_instruction_set(self):
        task = Task(
            id="t1",
            title="Build",
            objective="Implement something.",
            scope={"includes": ["src/"], "excludes": ["infra/"]},
            acceptance_criteria=["ac1"],
            constraints=["c1"],
            budget_policy_id="b1",
        )
        step = Step(
            id="s1",
            task_id="t1",
            index=2,
            kind="execute",
            objective="Implement feature",
            inputs=["diff-0"],
            expected_outputs=["code_diff"],
            constraints=["c1"],
        )
        constraints = [
            Constraint(
                id="c1",
                scope="task",
                kind="path_deny",
                predicate={"paths": ["infra/"]},
                rationale="no infra changes",
                source="user",
            )
        ]
        budget = BudgetPolicy(
            id="b1",
            limits={"tokens": 5000, "tool_calls": 20, "wall_time_s": 1200, "cost_usd": 2.5},
            on_breach="stop",
            scope="task",
        )

        builder = InstructionBuilder()
        instruction_set = builder.build(
            task=task,
            step=step,
            constraints=constraints,
            budget_policy=budget,
            required_artifacts=[RequiredArtifact(kind="code_diff", schema_ref="schema://diff", min_count=1, max_count=1)],
            applicable_rules=[{"id": "structural", "severity": "blocker"}],
        )

        self.assertEqual(instruction_set.task_ref, "t1")
        self.assertEqual(instruction_set.step_ref, "s1")
        self.assertEqual(instruction_set.budget.tokens, 5000)
        self.assertEqual(instruction_set.required_artifacts[0].kind, "code_diff")


if __name__ == "__main__":
    unittest.main()
