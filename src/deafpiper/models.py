from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Mapping, Optional


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class Constraint:
    id: str
    scope: str
    kind: str
    predicate: Any
    rationale: str
    source: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class BudgetPolicy:
    id: str
    limits: Dict[str, Any]
    on_breach: str
    scope: str

    def __post_init__(self) -> None:
        if not self.limits:
            raise ValueError("BudgetPolicy.limits must not be empty")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Task:
    id: str
    title: str
    objective: str
    scope: Dict[str, List[str]]
    acceptance_criteria: List[str]
    constraints: List[str]
    budget_policy_id: str
    status: str = "draft"
    created_at: str = field(default_factory=_now_iso)
    updated_at: str = field(default_factory=_now_iso)
    parent_task_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Step:
    id: str
    task_id: str
    index: int
    kind: str
    objective: str
    inputs: List[str]
    expected_outputs: List[str]
    constraints: List[str]
    status: str = "pending"
    started_at: Optional[str] = None
    finished_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ArtifactCandidate:
    id: str
    step_id: str
    type: str
    content_ref: str
    produced_at: str
    producer: str
    baseline_ref: Optional[str]
    status: str = "produced"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationRule:
    id: str
    applies_to: str
    kind: str
    executor: str
    pass_criteria: Dict[str, Any]
    severity: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TestResult:
    id: str
    artifact_candidate_id: str
    validation_rule_id: str
    outcome: str
    detail: Dict[str, Any]
    duration_ms: int
    executed_at: str
    environment_ref: str

    def __post_init__(self) -> None:
        if self.outcome == "skipped" and not self.detail.get("reason"):
            raise ValueError("Skipped TestResult requires detail.reason")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ComparisonResult:
    id: str
    artifact_candidate_id: str
    baseline_ref: Optional[str]
    dimensions: Dict[str, float]
    classification: str
    blocking_regressions: List[str]

    def __post_init__(self) -> None:
        if self.classification == "mixed":
            gains = [metric for metric, delta in self.dimensions.items() if delta > 0]
            losses = [metric for metric, delta in self.dimensions.items() if delta < 0]
            if not gains or not losses:
                raise ValueError("mixed classification requires explicit gains and losses")
        if self.baseline_ref is None and self.classification != "no_baseline":
            raise ValueError("Missing baseline must be classified as no_baseline")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PromotionDecision:
    id: str
    artifact_candidate_id: str
    decision: str
    rationale: str
    test_results: List[str]
    comparison_result_id: str
    deferred_issues: List[str]
    decided_by: str
    decided_at: str
    budget_state: Dict[str, Any]

    def __post_init__(self) -> None:
        if not self.test_results:
            raise ValueError("PromotionDecision requires at least one test_result reference")
        if self.decision == "defer" and not self.deferred_issues:
            raise ValueError("defer decision requires deferred issues")
        if not self.rationale.strip():
            raise ValueError("PromotionDecision rationale must not be empty")

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AuditEntry:
    id: int
    timestamp: str
    actor: Dict[str, Any]
    subject_type: str
    subject_id: str
    event: str
    previous_state: Optional[str]
    new_state: Optional[str]
    payload_ref: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class AuditEntryStore:
    """Append-only in-memory audit store with monotonic IDs."""

    def __init__(self) -> None:
        self._entries: List[AuditEntry] = []

    def append(self, entry: AuditEntry) -> None:
        expected_id = len(self._entries) + 1
        if entry.id != expected_id:
            raise ValueError(f"AuditEntry.id must be monotonic, expected {expected_id}")
        self._entries.append(entry)

    def list_entries(self) -> List[AuditEntry]:
        return list(self._entries)

    def snapshot(self) -> List[Dict[str, Any]]:
        return [entry.to_dict() for entry in self._entries]

    def restore(self, entries: List[Mapping[str, Any]]) -> None:
        restored: List[AuditEntry] = []
        for raw in entries:
            restored.append(AuditEntry(**dict(raw)))
        self._entries = []
        for entry in restored:
            self.append(entry)
