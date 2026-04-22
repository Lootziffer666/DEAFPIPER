# 03_IDEA_STRATEGY_PRD – Idee → Strategie → PRD

## Ziel

Du übersetzt die Erkenntnisse in einen Plan, den man *implementieren* und *testen* kann.

## Inputs

- findings.md
- IDEA_BRIEF.json
- Constraints/Timebox

## Outputs (am Ende dieses Schritts)

- PRD.json
- roadmap.md (grob)
- entscheidbare MVP-Liste

## Vorgehen (pragmatisch)

1. Schreibe Problem Statement und Value Proposition in 2–3 Sätzen.
2. Definiere MVP: Was muss unbedingt rein, was kann später?
3. Schreibe User Stories + Acceptance Criteria (testbar!).
4. Lege Metriken/Events fest (nicht erst nach Launch).
5. Erstelle ein kurzes Risiko-/Mitigation-Set.

## Quality Gates

- P0-Stories sind vollständig + akzeptanzkriteriert.
- MVP passt in die geplante Timebox.

## Short-Prompt (copy/paste)

```txt
Du bist mein Product Manager. Erzeuge ein PRD, das baubar ist.

Inputs:
- Findings:
{FINDINGS}
- Produktkontext:
{IDEA_BRIEF_JSON}

Output:
- PRD.json ausgefüllt, inkl. MVP-Scope, User Stories (mit Acceptance Criteria), Non-Functional Requirements, Analytics Events, Risiken, Launch-Kriterien.
```

## Templates

- `/templates/PRD.json`

## GPT-Config

- `/gpt_configs/03_IDEA_STRATEGY_PRD.json`

## Toolbox-Vertiefung

- `/toolbox/03__IDEA_STRATEGY_PRD.md`
- `/toolbox/P03_PRD_AND_PLANNING.md`
