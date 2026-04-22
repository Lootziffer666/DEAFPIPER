import unittest

from deafpiper.models import ArtifactCandidate, Constraint
from deafpiper.validation import ValidationRunner, make_builtin_registry


class Phase3ValidationTests(unittest.TestCase):
    def test_runner_executes_builtin_rules_and_returns_result_per_rule(self):
        artifact = ArtifactCandidate(
            id="a1",
            step_id="s1",
            type="code_diff",
            content_ref="sha256:abc",
            produced_at="2026-01-01T00:00:00+00:00",
            producer="agent/v1",
            baseline_ref="baseline:1",
        )
        registry = make_builtin_registry()
        runner = ValidationRunner(registry=registry)

        result = runner.run(
            artifact=artifact,
            applicable_rule_ids=["structural", "test_suite", "lint", "policy", "schema"],
            environment_ref="env:1",
            context={
                "rule_outcomes": {
                    "lint": {"outcome": "warning", "detail": {"warnings": 1, "duration_ms": 3}}
                }
            },
        )
        self.assertEqual(len(result), 5)
        self.assertEqual([x.validation_rule_id for x in result], ["structural", "test_suite", "lint", "policy", "schema"])

    def test_constraint_violation_creates_fail_result(self):
        artifact = ArtifactCandidate(
            id="a2",
            step_id="s1",
            type="code_diff",
            content_ref="sha256:def",
            produced_at="2026-01-01T00:00:00+00:00",
            producer="agent/v1",
            baseline_ref="baseline:1",
        )
        registry = make_builtin_registry()
        runner = ValidationRunner(registry=registry)
        constraints = [
            Constraint(
                id="c1",
                scope="task",
                kind="path_deny",
                predicate={"paths": ["infra/"]},
                rationale="deny infra",
                source="policy",
            )
        ]

        result = runner.run(
            artifact=artifact,
            applicable_rule_ids=["structural"],
            environment_ref="env:1",
            context={"touched_paths": ["infra/"]},
            constraints=constraints,
        )

        self.assertEqual(result[0].validation_rule_id, "constraint_evaluator")
        self.assertEqual(result[0].outcome, "fail")


if __name__ == "__main__":
    unittest.main()
