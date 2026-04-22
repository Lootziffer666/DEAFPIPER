# Stage 05: build_plan
**Producing bot role:** Build Director  
**Stage goal:** Turn architecture into milestone plan + task breakdown + dev prompts.

## OUTPUT (you must produce)
- `S05_build_plan__handoff.json`
- `S05_build_plan__artifact_01_main.md`

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
    "stage_id": "05",
    "stage_slug": "build_plan",
    "bot_role": "Build Director",
    "goal": "Turn architecture into milestone plan + task breakdown + dev prompts.",
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
        "name": "S05_build_plan__artifact_01_main.md",
        "type": "md",
        "description": "Main deliverable for this stage",
        "produced_by_stage": "05",
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

## Artifact skeleton: `S05_build_plan__artifact_01_main.md`
```md
# Build Director — Main Output

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
