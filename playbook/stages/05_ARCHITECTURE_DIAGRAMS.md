# 05_ARCHITECTURE_DIAGRAMS – Architektur, Diagramme & Spezifikation

## Ziel

Du legst fest, wie das System gebaut wird, ohne später in „Spaghetti by Surprise“ zu enden.

## Inputs

- PRD.json
- UX_SPEC.json
- Security/Privacy Constraints

## Outputs (am Ende dieses Schritts)

- ARCHITECTURE_SPEC.json
- ADR.md
- Diagramm-Prompts/Skizzen

## Vorgehen (pragmatisch)

1. Wähle Stack/Komponenten minimalistisch (MVP first).
2. Skizziere Datenflüsse (besonders personenbezogene Daten).
3. Definiere API + Schemas + Fehlerfälle.
4. Lege Observability fest: Logs/Metrics/Alerts/Tracing.
5. Dokumentiere Tradeoffs im ADR.

## Quality Gates

- Jedes P0-Feature ist technisch abbildbar (kein Wunschdenken).
- Privacy-by-Design: Minimierung, Zweckbindung, Retention sind dokumentiert.

## Short-Prompt (copy/paste)

```txt
Du bist mein Software-Architekt. Aus PRD.json + UX_SPEC.json erstelle eine technische Spezifikation:
- C4 (Context/Container/Component) als Textbeschreibung + Diagramm-Prompts
- API-Design (Method, Path, Schemas, Errors)
- Datenmodell (Entities)
- ADRs (Entscheidungen)
- Operability (Logs/Metrics/Alerts)
- DSGVO-Datenflüsse (woher, wohin, warum, retention)

Inputs:
{PRD_JSON}
{UX_SPEC_JSON}

Output:
ARCHITECTURE_SPEC.json
```

## Templates

- `/templates/ARCHITECTURE_SPEC.json`

## GPT-Config

- `/gpt_configs/05_ARCHITECTURE_DIAGRAMS.json`

## Toolbox-Vertiefung

- `/toolbox/P04_DIAGRAMS_AND_ARCHITECTURE.md`
- `/toolbox/P05_COMPUTATION_WOLFRAM.md`

## Toolbox (SSOT)
- `toolbox/P04_DIAGRAMS_AND_ARCHITECTURE.md`
