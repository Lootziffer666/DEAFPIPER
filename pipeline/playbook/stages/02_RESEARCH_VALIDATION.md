# 02_RESEARCH_VALIDATION – Research & Validierung

## Ziel

Du prüfst, ob das Problem real ist, ob du die richtigen Menschen ansprichst und ob die Lösung überhaupt eine Chance hat.

## Inputs

- IDEA_BRIEF.json
- Liste deiner Annahmen (auch „Bauchgefühl“ zählt, aber wird getestet)

## Outputs (am Ende dieses Schritts)

- RESEARCH_BRIEF.json
- findings.md
- Entscheidung: go/pivot/stop

## Vorgehen (pragmatisch)

1. Formuliere Hypothesen (Problem, Zielgruppe, Value Prop, Zahlungsbereitschaft, Risiken).
2. Wähle 1–2 schnelle Methoden (z.B. 5 Interviews + Desk Research).
3. Erstelle Findings: Was ist wahr, was ist unklar, was ist falsch?
4. Update Assumptions Log: jede Annahme bekommt Evidenz oder ein Test-Design.
5. Leite daraus MVP-Scope und Positionierung ab.

## Quality Gates

- Top-Risiken sind sichtbar (nicht unter den Teppich).
- Du hast mindestens eine valide Quelle pro zentraler Behauptung (oder markierst Unsicherheit).

## Short-Prompt (copy/paste)

```txt
Du bist mein Research-Lead. Arbeite strikt evidenzbasiert.

Input:
- IDEA_BRIEF.json:
{IDEA_BRIEF_JSON}

Aufgabe:
1) Erstelle RESEARCH_BRIEF.json (Hypothesen, Methoden, Segmente, Wettbewerber, Risiken).
2) Führe ein kompaktes Findings-Doc (max. 1–2 Seiten) mit: Top 10 Findings, Evidenz, Implikation.
3) Triff eine Go/Pivot/Stop-Empfehlung mit Begründung.
```

## Templates

- `/templates/RESEARCH_BRIEF.json`

## GPT-Config

- `/gpt_configs/02_RESEARCH_VALIDATION.json`

## Toolbox-Vertiefung

- `/toolbox/02__RESEARCH_DOCS.md`
- `/toolbox/P02_RESEARCH_SYSTEMS.md`

## Toolbox (SSOT)
- `toolbox/P02_RESEARCH_SYSTEMS.md` (enthält Research Prompt Library + Paper-Analyse Workflow)

## Toolbox (SSOT)
- `toolbox/P02_RESEARCH_SYSTEMS.md` (Research Prompt Library + Paper-Analyse Workflow)
