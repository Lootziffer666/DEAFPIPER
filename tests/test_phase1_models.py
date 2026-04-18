import json
import unittest

from deafpiper.models import (
    ArtifactCandidate,
    AuditEntry,
    AuditEntryStore,
    BudgetPolicy,
    Constraint,
    Step,
    Task,
    TestResult,
    ValidationRule,
)


class Phase1ModelTests(unittest.TestCase):
    def test_objects_serialize_cleanly(self):
        constraint = Constraint(
            id="c1",
            scope="task",
            kind="path_deny",
            predicate={"paths": ["infra/"]},
            rationale="limit scope",
            source="user",
        )
        budget = BudgetPolicy(id="b1", limits={"tokens": 1000}, on_breach="stop", scope="task")
        task = Task(
            id="t1",
            title="Task",
            objective="Build core objects.",
            scope={"includes": ["src/"], "excludes": ["infra/"]},
            acceptance_criteria=["serializable"],
            constraints=[constraint.id],
            budget_policy_id=budget.id,
        )
        step = Step(
            id="s1",
            task_id=task.id,
            index=0,
            kind="plan",
            objective="Create plan",
            inputs=[],
            expected_outputs=["plan"],
            constraints=[],
        )
        artifact = ArtifactCandidate(
            id="a1",
            step_id=step.id,
            type="plan",
            content_ref="sha256:abc",
            produced_at="2026-01-01T00:00:00+00:00",
            producer="agent/v1",
            baseline_ref=None,
        )
        rule = ValidationRule(
            id="r1",
            applies_to="plan",
            kind="schema",
            executor="builtin",
            pass_criteria={"must_parse": True},
            severity="blocker",
        )
        result = TestResult(
            id="tr1",
            artifact_candidate_id=artifact.id,
            validation_rule_id=rule.id,
            outcome="pass",
            detail={"log": "ok"},
            duration_ms=10,
            executed_at="2026-01-01T00:00:00+00:00",
            environment_ref="env:1",
        )
        payloads = [
            constraint.to_dict(),
            budget.to_dict(),
            task.to_dict(),
            step.to_dict(),
            artifact.to_dict(),
            rule.to_dict(),
            result.to_dict(),
        ]
        for payload in payloads:
            self.assertIsInstance(json.dumps(payload), str)

    def test_skipped_result_requires_reason(self):
        with self.assertRaises(ValueError):
            TestResult(
                id="tr2",
                artifact_candidate_id="a1",
                validation_rule_id="r1",
                outcome="skipped",
                detail={},
                duration_ms=1,
                executed_at="2026-01-01T00:00:00+00:00",
                environment_ref="env:1",
            )

    def test_append_only_audit_store(self):
        store = AuditEntryStore()
        store.append(
            AuditEntry(
                id=1,
                timestamp="2026-01-01T00:00:00+00:00",
                actor={"type": "agent", "id": "a"},
                subject_type="Task",
                subject_id="t1",
                event="created",
                previous_state=None,
                new_state="draft",
                payload_ref="sha256:1",
            )
        )
        with self.assertRaises(ValueError):
            store.append(
                AuditEntry(
                    id=3,
                    timestamp="2026-01-01T00:00:01+00:00",
                    actor={"type": "agent", "id": "a"},
                    subject_type="Task",
                    subject_id="t1",
                    event="transitioned",
                    previous_state="draft",
                    new_state="ready",
                    payload_ref="sha256:2",
                )
            )


if __name__ == "__main__":
    unittest.main()
