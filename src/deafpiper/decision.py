from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List, Mapping, Sequence

from .models import ComparisonResult, PromotionDecision, TestResult


class DecisionEngine:
    def decide(
        self,
        artifact_candidate_id: str,
        comparison_result: ComparisonResult,
        test_results: Sequence[TestResult],
        rework_budget_remaining: bool,
        failure_is_diagnosable: bool,
        override: bool = False,
        rationale: str = "",
        deferred_issues: Sequence[str] | None = None,
        decided_by: str = "agent:default",
        budget_state: Mapping[str, int] | None = None,
    ) -> PromotionDecision:
        deferred_issues = list(deferred_issues or [])
        budget_state = dict(budget_state or {})

        has_error = any(result.outcome == "error" for result in test_results)
        blocker_fail = any(result.outcome == "fail" and result.validation_rule_id != "lint" for result in test_results)

        if has_error:
            decision = "rework" if rework_budget_remaining else "reject"
            final_rationale = rationale or "execution error, not logical failure"
        elif blocker_fail:
            if failure_is_diagnosable and rework_budget_remaining:
                decision = "rework"
            else:
                decision = "reject"
            final_rationale = rationale or "blocker validation failed"
        elif comparison_result.classification == "regression":
            if override:
                decision = "promote"
                final_rationale = rationale or "human override accepted regression"
            else:
                decision = "rework" if rework_budget_remaining else "reject"
                final_rationale = rationale or "blocking regression detected"
        elif comparison_result.classification == "mixed":
            if override and rationale:
                decision = "promote"
                final_rationale = rationale
            else:
                decision = "rework" if rework_budget_remaining else "defer"
                final_rationale = rationale or "mixed result requires explicit tradeoff rationale"
        elif comparison_result.classification in {"improvement", "neutral", "no_baseline"}:
            decision = "promote"
            final_rationale = rationale or "validation passed and comparison eligible"
        else:
            decision = "reject"
            final_rationale = rationale or "unclassifiable comparison result"

        return PromotionDecision(
            id=f"pd-{artifact_candidate_id}",
            artifact_candidate_id=artifact_candidate_id,
            decision=decision,
            rationale=final_rationale,
            test_results=[result.id for result in test_results],
            comparison_result_id=comparison_result.id,
            deferred_issues=deferred_issues,
            decided_by=decided_by,
            decided_at=datetime.now(timezone.utc).isoformat(),
            budget_state=budget_state,
        )
