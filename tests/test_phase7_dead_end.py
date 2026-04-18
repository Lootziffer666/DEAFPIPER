import unittest

from deafpiper.audit import AuditLogger, AuditQuery, ContentStore
from deafpiper.dead_end import EscalationHandler, StopDetector
from deafpiper.models import AuditEntryStore


class Phase7DeadEndTests(unittest.TestCase):
    def test_budget_exhaustion_detected(self):
        detector = StopDetector()
        event = detector.detect(
            {
                "budget": {
                    "cumulative_tokens": 120,
                    "tokens": 100,
                    "cumulative_cost": 0.1,
                    "cost_usd": 1.0,
                    "elapsed_time_s": 10,
                    "wall_time_s": 100,
                    "tool_call_count": 1,
                    "tool_calls": 10,
                }
            }
        )
        self.assertIsNotNone(event)
        self.assertEqual(event.category, "budget_exhaustion")

    def test_escalation_payload_is_logged(self):
        store = AuditEntryStore()
        content = ContentStore()
        logger = AuditLogger(store, content)
        handler = EscalationHandler(logger)

        event = StopDetector().detect({"ambiguity_marker": True})
        payload = handler.escalate(
            task_ref="task-1",
            step_ref="step-1",
            instruction_set_ref="ins-1",
            dead_end_event=event,
            full_rework_chain=["a1", "a2"],
            last_validation_results=["tr1"],
            last_comparison_result="cmp1",
            budget_state={"tokens": 10},
        )
        self.assertEqual(payload["dead_end_category"], "unresolvable_ambiguity")
        self.assertIn("audit_ref", payload)


if __name__ == "__main__":
    unittest.main()
