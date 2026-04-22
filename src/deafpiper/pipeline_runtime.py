from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from .models import Step, Task


@dataclass(frozen=True)
class PipelineStageArtifact:
    stage_id: str
    stage_title: str
    source_path: str


class PipelineRuntimeMapper:
    """Maps playbook and template artifacts into runtime Task/Step objects."""

    def __init__(self, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)

    def discover_stages(self) -> List[PipelineStageArtifact]:
        stages_dir = self.repo_root / "playbook" / "stages"
        artifacts: List[PipelineStageArtifact] = []
        for path in sorted(stages_dir.glob("*.md")):
            parts = path.stem.split("_", 1)
            stage_id = parts[0]
            title = parts[1] if len(parts) > 1 else path.stem
            artifacts.append(PipelineStageArtifact(stage_id=stage_id, stage_title=title, source_path=str(path)))
        return artifacts

    def build_task(self, task_id: str, title: str, objective: str) -> Task:
        includes = ["src/", "docs/", "playbook/", "templates/"]
        excludes = ["infra/"]
        return Task(
            id=task_id,
            title=title,
            objective=objective,
            scope={"includes": includes, "excludes": excludes},
            acceptance_criteria=["All stage artifacts are mappable to runtime execution objects."],
            constraints=["c-paths"],
            budget_policy_id="budget-default",
        )

    def build_steps(self, task: Task) -> List[Step]:
        steps: List[Step] = []
        for idx, stage in enumerate(self.discover_stages(), start=1):
            steps.append(
                Step(
                    id=f"step-{stage.stage_id.lower()}",
                    task_id=task.id,
                    index=idx,
                    kind="pipeline_stage",
                    objective=f"Execute playbook stage {stage.stage_id}: {stage.stage_title}",
                    inputs=[stage.source_path],
                    expected_outputs=[f"artifact://stage/{stage.stage_id}"],
                    constraints=["c-paths"],
                )
            )
        return steps

    def load_template(self, template_name: str) -> Dict[str, object]:
        template_path = self.repo_root / "templates" / template_name
        return json.loads(template_path.read_text(encoding="utf-8"))
