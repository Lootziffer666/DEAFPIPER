import unittest

from deafpiper.audit import AuditLogger, ContentStore
from deafpiper.budget import BudgetEnforcer
from deafpiper.models import AuditEntryStore, BudgetPolicy


class Phase8BudgetTests(unittest.TestCase):
    def test_budget_breach_detection_and_audit(self):
        policy = BudgetPolicy(id="b1", limits={"tokens": 100}, on_breach="stop", scope="task")
        logger = AuditLogger(AuditEntryStore(), ContentStore())
        enforcer = BudgetEnforcer(policy=policy, audit_logger=logger)

        enforcer.record_usage(tokens=120)
        result = enforcer.evaluate(subject_id="task-1")

        self.assertTrue(result["breached"])
        self.assertIn("tokens", result["breaches"])


if __name__ == "__main__":
    unittest.main()
