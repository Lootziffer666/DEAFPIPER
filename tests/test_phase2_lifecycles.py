import unittest

from deafpiper.lifecycle import ArtifactLifecycle, StepLifecycle, TaskLifecycle, TransitionError
from deafpiper.models import ArtifactCandidate, Step, Task


class Phase2LifecycleTests(unittest.TestCase):
    def test_task_lifecycle_happy_and_blocked_path(self):
        task = Task(
            id="t1",
            title="Title",
            objective="Objective.",
            scope={"includes": ["src/"], "excludes": ["infra/"]},
            acceptance_criteria=["all tests pass"],
            constraints=["c1"],
            budget_policy_id="b1",
        )
        TaskLifecycle.transition(task, "ready")
        TaskLifecycle.transition(task, "running")
        TaskLifecycle.transition(task, "blocked")
        TaskLifecycle.transition(task, "ready")
        self.assertEqual(task.status, "ready")

    def test_task_invalid_transition_rejected(self):
        task = Task(
            id="t1",
            title="Title",
            objective="Objective.",
            scope={"includes": ["src/"], "excludes": ["infra/"]},
            acceptance_criteria=["all tests pass"],
            constraints=["c1"],
            budget_policy_id="b1",
        )
        with self.assertRaises(TransitionError):
            TaskLifecycle.transition(task, "done")

    def test_step_lifecycle(self):
        step = Step(
            id="s1",
            task_id="t1",
            index=1,
            kind="execute",
            objective="Do thing",
            inputs=[],
            expected_outputs=["code_diff"],
            constraints=[],
        )
        for target in ["running", "produced", "validated", "compared", "decided"]:
            StepLifecycle.transition(step, target)
        self.assertEqual(step.status, "decided")

    def test_artifact_lifecycle_invalid_after_invalid(self):
        artifact = ArtifactCandidate(
            id="a1",
            step_id="s1",
            type="code_diff",
            content_ref="sha256:abc",
            produced_at="2026-01-01T00:00:00+00:00",
            producer="agent/v1",
            baseline_ref=None,
        )
        ArtifactLifecycle.transition(artifact, "validating")
        ArtifactLifecycle.transition(artifact, "invalid")
        with self.assertRaises(TransitionError):
            ArtifactLifecycle.transition(artifact, "validated")


if __name__ == "__main__":
    unittest.main()
