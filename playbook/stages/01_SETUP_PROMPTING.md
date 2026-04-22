# 01_SETUP_PROMPTING – Setup & Prompting-Standards

## Ziel

Du legst fest, **wie** du mit KI arbeitest, bevor du sie inhaltlich loslässt. Das verhindert 80% der späteren Reibung.

## Inputs

- Grobe Produktidee (2–5 Sätze)
- Plattform/Stack-Vorlieben (falls vorhanden)
- Timebox/Budget grob
- DSGVO/Privacy-Anspruch (z.B. „privacy first“)

## Outputs (am Ende dieses Schritts)

- Prompting-Standard (Format + Regeln)
- Glossar
- IDEA_BRIEF.json (Rohfassung)

## Vorgehen (pragmatisch)

1. Lege ein Output-Format fest (ich empfehle: **JSON für strukturierte Artefakte + Markdown für Erklärung**).
2. Definiere Quality Gates: vollständiger Code, Tests, Run Steps, Annahmen explizit, Unsicherheiten markieren.
3. Erzeuge ein Glossar (damit Begriffe später konsistent bleiben).
4. Fülle IDEA_BRIEF.json als Start-Artefakt.

## Quality Gates

- Jeder Prompt fordert *konkrete* Deliverables (keine vagen Essays).
- Du hast eine Definition von „fertig“ (DoD) für Artefakte (PRD, UX, Code, Marketing).

## Short-Prompt (copy/paste)

```txt
Du bist mein Pipeline-Orchestrator. Erzeuge mir:
1) einen klaren Prompting-Standard (Output-Format, Regeln, Qualitätsschwellen),
2) ein kurzes Projekt-Glossar (10–30 Begriffe),
3) eine ausgefüllte Rohfassung von IDEA_BRIEF.json.

Kontext (Produktidee, Constraints):
{HIER_EINFÜGEN}

Output:
- prompting_standard.md
- glossary.md
- IDEA_BRIEF.json
```

## Templates

- `/templates/IDEA_BRIEF.json`

## GPT-Config

- `/gpt_configs/01_SETUP_PROMPTING.json`

## Toolbox-Vertiefung

- `/toolbox/01__PROMPTING_SYSTEM.md`
- `/toolbox/P01_PROMPTING_PLAYBOOK.md`
