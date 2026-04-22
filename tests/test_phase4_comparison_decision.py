import unittest

from deafpiper.comparison import Comparator
from deafpiper.decision import DecisionEngine
from deafpiper.models import ComparisonResult, TestResult


class Phase4ComparisonDecisionTests(unittest.TestCase):
    def test_compare_improvement(self):
        comparator = Comparator()
        result = comparator.compare(
            artifact_candidate_id="a1",
            baseline_ref="base:1",
            candidate_metrics={"coverage": 0.85, "lint_warnings": 0},
            baseline_metrics={"coverage": 0.80, "lint_warnings": 1},
            directions={"coverage": "higher_is_better", "lint_warnings": "lower_is_better"},
            blocking_dimensions=["coverage", "lint_warnings"],
        )
        self.assertEqual(result.classification, "improvement")

    def test_compare_regression_on_blocking_dimension(self):
        comparator = Comparator()
        result = comparator.compare(
            artifact_candidate_id="a2",
            baseline_ref="base:1",
            candidate_metrics={"coverage": 0.75},
            baseline_metrics={"coverage": 0.80},
            directions={"coverage": "higher_is_better"},
            blocking_dimensions=["coverage"],
        )
        self.assertEqual(result.classification, "regression")
        self.assertEqual(result.blocking_regressions, ["coverage"])

    def test_decision_engine_promotes_valid_improvement(self):
        engine = DecisionEngine()
        comparison = ComparisonResult(
            id="cmp-a1",
            artifact_candidate_id="a1",
            baseline_ref="base:1",
            dimensions={"coverage": 0.05},
            classification="improvement",
            blocking_regressions=[],
        )
        test_results = [
            TestResult(
                id="tr-a1-structural",
                artifact_candidate_id="a1",
                validation_rule_id="structural",
                outcome="pass",
                detail={"log": "ok"},
                duration_ms=1,
                executed_at="2026-01-01T00:00:00+00:00",
                environment_ref="env:1",
            )
        ]
        decision = engine.decide(
            artifact_candidate_id="a1",
            comparison_result=comparison,
            test_results=test_results,
            rework_budget_remaining=True,
            failure_is_diagnosable=True,
            budget_state={"rework_remaining": 2},
        )
        self.assertEqual(decision.decision, "promote")

    def test_decision_engine_reworks_on_blocker_failure(self):
        engine = DecisionEngine()
        comparison = ComparisonResult(
            id="cmp-a2",
            artifact_candidate_id="a2",
            baseline_ref="base:1",
            dimensions={"coverage": -0.05},
            classification="regression",
            blocking_regressions=["coverage"],
        )
        test_results = [
            TestResult(
                id="tr-a2-policy",
                artifact_candidate_id="a2",
                validation_rule_id="policy",
                outcome="fail",
                detail={"log": "policy fail"},
                duration_ms=1,
                executed_at="2026-01-01T00:00:00+00:00",
                environment_ref="env:1",
            )
        ]
        decision = engine.decide(
            artifact_candidate_id="a2",
            comparison_result=comparison,
            test_results=test_results,
            rework_budget_remaining=True,
            failure_is_diagnosable=True,
            budget_state={"rework_remaining": 1},
        )
        self.assertEqual(decision.decision, "rework")


if __name__ == "__main__":
    unittest.main()
