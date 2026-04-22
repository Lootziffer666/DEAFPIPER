from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, Iterable, Mapping, Sequence

from .models import ComparisonResult


class Comparator:
    def compare(
        self,
        artifact_candidate_id: str,
        baseline_ref: str | None,
        candidate_metrics: Mapping[str, float],
        baseline_metrics: Mapping[str, float] | None,
        directions: Mapping[str, str],
        blocking_dimensions: Sequence[str],
    ) -> ComparisonResult:
        if baseline_ref is None or baseline_metrics is None:
            return ComparisonResult(
                id=f"cmp-{artifact_candidate_id}",
                artifact_candidate_id=artifact_candidate_id,
                baseline_ref=baseline_ref,
                dimensions=dict(candidate_metrics),
                classification="no_baseline",
                blocking_regressions=[],
            )

        deltas: Dict[str, float] = {}
        improvements = set()
        regressions = set()

        for metric, candidate_value in candidate_metrics.items():
            baseline_value = baseline_metrics.get(metric, 0.0)
            delta = float(candidate_value) - float(baseline_value)
            deltas[metric] = delta

            direction = directions.get(metric)
            if direction == "higher_is_better":
                if delta > 0:
                    improvements.add(metric)
                elif delta < 0:
                    regressions.add(metric)
            elif direction == "lower_is_better":
                if delta < 0:
                    improvements.add(metric)
                elif delta > 0:
                    regressions.add(metric)

        blocking = sorted(list(regressions.intersection(set(blocking_dimensions))))

        if blocking:
            classification = "regression"
        elif improvements and regressions:
            classification = "mixed"
        elif improvements:
            classification = "improvement"
        else:
            classification = "neutral"

        return ComparisonResult(
            id=f"cmp-{artifact_candidate_id}",
            artifact_candidate_id=artifact_candidate_id,
            baseline_ref=baseline_ref,
            dimensions=deltas,
            classification=classification,
            blocking_regressions=blocking,
        )
