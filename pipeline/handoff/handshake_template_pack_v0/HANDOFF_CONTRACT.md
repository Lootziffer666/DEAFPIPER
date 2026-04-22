# Handoff Contract (MD + JSON)

## Deliverables every stage must produce
1) `...__handoff.json` (conforms to `schemas/handoff_schema_v0.json`)
2) one or more artifacts referenced by `output.artifacts_out[]`

## Minimal quality requirements
- **No missing file references**: every artifact listed must exist
- **Explicit assumptions**: list them under `stage.assumptions`
- **Explicit constraints**: list them under `stage.constraints`
- **Explicit next request**: next bot receives a single actionable request string referencing artifacts

## Recommended artifact types
- Specs: `.md` or `.json`
- Data models/contracts: `.json`
- Copy blocks: `.md`
- Design tokens/components: `.json` / `.md`
- Build plan/task breakdown: `.md` / `.json`
