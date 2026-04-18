# Bot-to-Bot Handshake Template Pack (v0)

This pack defines a **single, consistent handoff contract** for a multi-bot pipeline from **idea → build → launch → marketing → iteration**.

## What you get
- A **global JSON schema** for handoffs
- **Stage templates** (Markdown) with embedded JSON skeletons
- **Examples** (filled minimal handoffs) you can copy/paste
- A **file-naming convention** and **versioning** approach

## Core rule
Every bot MUST output:
1) `handoff.json` (conforming to schema)  
2) one or more `artifact_*.md` or `artifact_*.json` files referenced by the handoff  

## Versioning
- This is **v0 (provisional)**. Keep `pipeline_version` and `handoff_version` fields.
- Stage IDs are **provisional** and can be renumbered later without breaking the schema.

## File naming (recommended)
- `S{stage_id}_{slug}__handoff.json`
- `S{stage_id}_{slug}__artifact_{nn}_{name}.md`

Generated: 2026-03-04
