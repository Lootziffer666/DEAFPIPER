# Stage 01: idea_intake
**Producing bot role:** Idea Strategist  
**Stage goal:** Turn a raw idea into a validated problem statement + initial scope.

## OUTPUT (you must produce)
- `S01_idea_intake__handoff.json`
- `S01_idea_intake__artifact_01_main.md`

## Handoff JSON skeleton
```json
{
  "meta": {
    "pipeline_id": "PIPELINE-YYYYMMDD-0001",
    "pipeline_version": "v0",
    "handoff_version": "v0",
    "created_at": "2026-03-04T00:00:00Z",
    "locale": "de-DE",
    "timezone": "Europe/Berlin",
    "owner": ""
  },
  "stage": {
    "stage_id": "01",
    "stage_slug": "idea_intake",
    "bot_role": "Idea Strategist",
    "goal": "Turn a raw idea into a validated problem statement + initial scope.",
    "assumptions": [],
    "constraints": [],
    "quality_bar": []
  },
  "input": {
    "context": {},
    "artifacts": [],
    "decisions_so_far": [],
    "open_questions_in": []
  },
  "output": {
    "summary": "",
    "artifacts_out": [
      {
        "name": "S01_idea_intake__artifact_01_main.md",
        "type": "md",
        "description": "Main deliverable for this stage",
        "produced_by_stage": "01",
        "content_hash": ""
      }
    ],
    "decisions": [],
    "open_questions_out": [],
    "risks": [],
    "metrics": [],
    "acceptance_criteria": []
  },
  "next": {
    "next_stage_id": "",
    "request": "",
    "handoff_checklist": [
      "All referenced artifacts exist",
      "Assumptions and constraints explicitly listed",
      "Open questions clearly stated and minimized",
      "Next-stage request references exact artifact filenames"
    ]
  }
}
```

## Artifact skeleton: `S01_idea_intake__artifact_01_main.md`
```md
# Idea Strategist — Main Output

## Executive summary
- ...

## Details
- ...

## Decisions made
- ...

## Open questions
- ...

## Risks
- ...

## What the next stage must do
- ...
```
