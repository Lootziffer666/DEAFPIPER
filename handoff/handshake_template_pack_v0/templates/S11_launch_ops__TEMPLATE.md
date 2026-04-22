# Stage 11: launch_ops
**Producing bot role:** Launch Operator  
**Stage goal:** Launch plan, QA, tracking, release notes, support macros.

## OUTPUT (you must produce)
- `S11_launch_ops__handoff.json`
- `S11_launch_ops__artifact_01_main.md`

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
    "stage_id": "11",
    "stage_slug": "launch_ops",
    "bot_role": "Launch Operator",
    "goal": "Launch plan, QA, tracking, release notes, support macros.",
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
        "name": "S11_launch_ops__artifact_01_main.md",
        "type": "md",
        "description": "Main deliverable for this stage",
        "produced_by_stage": "11",
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

## Artifact skeleton: `S11_launch_ops__artifact_01_main.md`
```md
# Launch Operator — Main Output

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
