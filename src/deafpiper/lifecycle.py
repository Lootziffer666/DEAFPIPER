from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Set

from .models import ArtifactCandidate, Step, Task


@dataclass(frozen=True)
class TransitionError(Exception):
    entity: str
    current: str
    target: str

    def __str__(self) -> str:
        return f"Invalid transition for {self.entity}: {self.current} -> {self.target}"


class _Lifecycle:
    allowed_transitions: Dict[str, Set[str]] = {}

    @classmethod
    def can_transition(cls, current: str, target: str) -> bool:
        return target in cls.allowed_transitions.get(current, set())

    @classmethod
    def validate_transition(cls, entity: str, current: str, target: str) -> None:
        if not cls.can_transition(current, target):
            raise TransitionError(entity=entity, current=current, target=target)


class TaskLifecycle(_Lifecycle):
    allowed_transitions: Dict[str, Set[str]] = {
        "draft": {"ready"},
        "ready": {"running"},
        "running": {"done", "blocked", "abandoned"},
        "blocked": {"ready"},
        "done": set(),
        "abandoned": set(),
    }

    @classmethod
    def transition(cls, task: Task, target: str) -> Task:
        cls.validate_transition("Task", task.status, target)
        task.status = target
        return task


class StepLifecycle(_Lifecycle):
    allowed_transitions: Dict[str, Set[str]] = {
        "pending": {"running"},
        "running": {"produced", "blocked", "skipped"},
        "produced": {"validated", "blocked"},
        "validated": {"compared", "blocked"},
        "compared": {"decided", "blocked"},
        "decided": {"blocked"},
        "blocked": {"skipped"},
        "skipped": set(),
    }

    @classmethod
    def transition(cls, step: Step, target: str) -> Step:
        cls.validate_transition("Step", step.status, target)
        step.status = target
        return step


class ArtifactLifecycle(_Lifecycle):
    allowed_transitions: Dict[str, Set[str]] = {
        "produced": {"validating"},
        "validating": {"validated", "invalid"},
        "validated": {"compared"},
        "compared": {"decided"},
        "decided": set(),
        "invalid": set(),
    }

    @classmethod
    def transition(cls, artifact: ArtifactCandidate, target: str) -> ArtifactCandidate:
        cls.validate_transition("ArtifactCandidate", artifact.status, target)
        artifact.status = target
        return artifact
