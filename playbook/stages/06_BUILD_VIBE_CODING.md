# 06_BUILD_VIBE_CODING – Build / Vibe Coding

## Ziel

Du produzierst einen lauffähigen Build, der reproduzierbar ist (kein „geht nur auf meinem Gerät“).

## Inputs

- ARCHITECTURE_SPEC.json
- UX_SPEC.json
- MVP Scope

## Outputs (am Ende dieses Schritts)

- Repo/Code
- BUILD_PLAN.json
- DEPLOY_PACKET.json
- run_instructions.md
- Tests + CI-Skizze

## Vorgehen (pragmatisch)

1. Setze Repo-Scaffold + Dev-Setup auf.
2. Implementiere P0-Features end-to-end.
3. Schreibe Tests entlang der Acceptance Criteria.
4. Erstelle eine 10-Zeilen Run-Anleitung (Clone → Install → Run).
5. Füge minimale CI Checks hinzu.

## Quality Gates

- Fresh machine: Setup gelingt ohne manuelle Hacks.
- P0 Stories sind getestet.
- Fehlerfälle sind sauber gehandhabt (Validation, Statuscodes, Messages).

## Short-Prompt (copy/paste)

```txt
Du bist mein Senior Engineer. Baue das MVP strikt nach Spezifikation.

Inputs:
{ARCHITECTURE_SPEC_JSON}
{UX_SPEC_JSON}

Bitte liefere:
1) Repo-Struktur,
2) vollständigen Code für P0-Features,
3) Tests (Unit/Integration) + wie man sie ausführt,
4) Run Instructions (local),
5) CI-Plan (minimal).

Output:
- BUILD_PLAN.json
- DEPLOY_PACKET.json
- run_instructions.md
- (Code als vollständige Dateien / oder Git-Patch)
```

## Templates

- `/templates/BUILD_PLAN.json`
- `/templates/DEPLOY_PACKET.json` (NEU in v2: Environments, CI/CD, Secrets, Rollback)

## GPT-Config

- `/gpt_configs/06_BUILD_VIBE_CODING.json`

## Toolbox-Vertiefung

- `/toolbox/05__BUILD_VIBE_CODING.md`
- `/toolbox/P06_BUILD_DEBUG_R.md`
