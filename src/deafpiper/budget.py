from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .audit import AuditLogger
from .models import BudgetPolicy


@dataclass
class BudgetState:
    tokens: int = 0
    cost_usd: float = 0.0
    wall_time_s: int = 0
    tool_calls: int = 0
    rework_iterations: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tokens": self.tokens,
            "cost_usd": self.cost_usd,
            "wall_time_s": self.wall_time_s,
            "tool_calls": self.tool_calls,
            "rework_iterations": self.rework_iterations,
        }


class BudgetEnforcer:
    def __init__(self, policy: BudgetPolicy, audit_logger: AuditLogger | None = None) -> None:
        self.policy = policy
        self.audit_logger = audit_logger
        self.state = BudgetState()
        self._deferred_downgrade_pending = False
        self._breach_count = 0

    def record_usage(
        self,
        tokens: int = 0,
        cost_usd: float = 0.0,
        wall_time_s: int = 0,
        tool_calls: int = 0,
        rework_iterations: int = 0,
    ) -> None:
        self.state.tokens += tokens
        self.state.cost_usd += cost_usd
        self.state.wall_time_s += wall_time_s
        self.state.tool_calls += tool_calls
        self.state.rework_iterations += rework_iterations

    def evaluate(self, subject_id: str) -> Dict[str, Any]:
        limits = self.policy.limits
        breaches: Dict[str, Any] = {}

        if "tokens" in limits and self.state.tokens >= int(limits["tokens"]):
            breaches["tokens"] = {"used": self.state.tokens, "limit": int(limits["tokens"])}
        if "cost_usd" in limits and self.state.cost_usd >= float(limits["cost_usd"]):
            breaches["cost_usd"] = {"used": self.state.cost_usd, "limit": float(limits["cost_usd"])}
        if "wall_time_s" in limits and self.state.wall_time_s >= int(limits["wall_time_s"]):
            breaches["wall_time_s"] = {"used": self.state.wall_time_s, "limit": int(limits["wall_time_s"])}
        if "tool_calls" in limits and self.state.tool_calls >= int(limits["tool_calls"]):
            breaches["tool_calls"] = {"used": self.state.tool_calls, "limit": int(limits["tool_calls"])}
        if "rework_iterations" in limits and self.state.rework_iterations >= int(limits["rework_iterations"]):
            breaches["rework_iterations"] = {
                "used": self.state.rework_iterations,
                "limit": int(limits["rework_iterations"]),
            }

        action = self.policy.on_breach
        pending = False
        if breaches:
            self._breach_count += 1
            if self.policy.on_breach == "downgrade_deferred":
                if self._deferred_downgrade_pending:
                    action = "downgrade"
                    self._deferred_downgrade_pending = False
                else:
                    action = "defer_downgrade"
                    pending = True
                    self._deferred_downgrade_pending = True

            if self.audit_logger:
                self.audit_logger.log(
                    actor={"type": "system", "id": "budget_enforcer"},
                    subject_type="Task",
                    subject_id=subject_id,
                    event="budget_breached",
                    previous_state="running",
                    new_state=action,
                    payload={
                        "breaches": breaches,
                        "on_breach": self.policy.on_breach,
                        "resolved_action": action,
                        "deferred_downgrade_pending": self._deferred_downgrade_pending,
                        "breach_count": self._breach_count,
                        "state": self.state.to_dict(),
                    },
                )

        return {
            "breached": bool(breaches),
            "breaches": breaches,
            "on_breach": self.policy.on_breach,
            "resolved_action": action,
            "deferred_downgrade_pending": pending,
            "breach_count": self._breach_count,
        }
