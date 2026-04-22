from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Sequence

from .audit import AuditLogger


DEAD_END_CATEGORIES = {
    "budget_exhaustion",
    "repeated_identical_output",
    "unresolvable_ambiguity",
    "constraint_conflict",
    "missing_input",
    "validation_loop",
    "scope_breach_attempt",
    "external_dependency_unavailable",
}


@dataclass(frozen=True)
class DeadEndEvent:
    category: str
    detector_output: Dict[str, Any]


class StopDetector:
    def detect(self, context: Mapping[str, Any]) -> DeadEndEvent | None:
        budget = context.get("budget", {})
        if budget and (
            budget.get("cumulative_tokens", 0) >= budget.get("tokens", float("inf"))
            or budget.get("cumulative_cost", 0.0) >= budget.get("cost_usd", float("inf"))
            or budget.get("elapsed_time_s", 0) >= budget.get("wall_time_s", float("inf"))
            or budget.get("tool_call_count", 0) >= budget.get("tool_calls", float("inf"))
        ):
            return DeadEndEvent("budget_exhaustion", {"budget": dict(budget)})

        hashes = context.get("last_artifact_hashes", [])
        if len(hashes) >= 2 and len(set(hashes[-2:])) == 1:
            return DeadEndEvent("repeated_identical_output", {"hash": hashes[-1]})

        if context.get("ambiguity_marker"):
            return DeadEndEvent("unresolvable_ambiguity", {"reason": "ambiguity marker emitted"})

        if context.get("constraint_conflict"):
            return DeadEndEvent("constraint_conflict", {"conflicts": context.get("constraint_conflict")})

        if context.get("missing_required_inputs"):
            return DeadEndEvent("missing_input", {"missing": context.get("missing_required_inputs")})

        if context.get("rework_iteration_count", 0) >= context.get("max_rework_iterations", float("inf")) and not context.get("progress_delta", True):
            return DeadEndEvent("validation_loop", {"rework_iteration_count": context.get("rework_iteration_count", 0)})

        scope_breaches = context.get("scope_breach_count", 0)
        if scope_breaches >= context.get("scope_breach_limit", 2):
            return DeadEndEvent("scope_breach_attempt", {"scope_breach_count": scope_breaches})

        if context.get("external_dependency_unavailable"):
            return DeadEndEvent("external_dependency_unavailable", {"dependency": context.get("external_dependency_unavailable")})

        return None


class EscalationHandler:
    def __init__(self, audit_logger: AuditLogger) -> None:
        self.audit_logger = audit_logger

    def escalate(
        self,
        task_ref: str,
        step_ref: str,
        instruction_set_ref: str,
        dead_end_event: DeadEndEvent,
        full_rework_chain: Sequence[str],
        last_validation_results: Sequence[str],
        last_comparison_result: str | None,
        budget_state: Mapping[str, Any],
    ) -> Dict[str, Any]:
        payload = {
            "task_ref": task_ref,
            "step_ref": step_ref,
            "instruction_set_ref": instruction_set_ref,
            "dead_end_category": dead_end_event.category,
            "detector_output": dead_end_event.detector_output,
            "full_rework_chain": list(full_rework_chain),
            "last_validation_results": list(last_validation_results),
            "last_comparison_result": last_comparison_result,
            "budget_state": dict(budget_state),
            "recommended_human_actions": [
                "Review dead-end payload",
                "Adjust constraints/budget or provide missing input",
                "Resume with new instruction set",
            ],
        }

        entry = self.audit_logger.log(
            actor={"type": "system", "id": "escalation_handler"},
            subject_type="Task",
            subject_id=task_ref,
            event="escalated",
            previous_state="running",
            new_state="blocked",
            payload=payload,
        )
        payload["audit_ref"] = entry.id
        return payload
