# 07_QA_SECURITY_COMPLIANCE – QA, Security & Compliance

## Ziel

Du machst das Produkt stabil, sicher und (minimal) compliance-fähig – bevor Marketing Traffic drauf kippt.

## Inputs

- Build/Repo
- PRD.json
- ARCHITECTURE_SPEC.json
- Datenschutz-Anforderungen

## Outputs (am Ende dieses Schritts)

- TEST_PLAN.json
- THREAT_MODEL.json
- PRIVACY_DPIA_LITE.json
- QA_REPORT.json (Go/No-Go-Entscheidung)
- qa_report.md (Details)

## Vorgehen (pragmatisch)

1. Erstelle Testmatrix nach P0/P1/P2.
2. Baue Release Checks (Smoke, Regression, Rollback).
3. Modelliere Threats (STRIDE/Abuse Cases light) und mappe Controls.
4. Dokumentiere Datenflüsse + Rechtsgrundlagen + Retention.
5. Erzeuge Fix-Backlog priorisiert nach Risiko.

## Quality Gates

- Keine offenen P0 Bugs.
- Top Threats mitigiert oder bewusst akzeptiert (mit Begründung).
- Privacy Minimum (Transparenz + Minimierung + Rechte) ist vorbereitet.

## Short-Prompt (copy/paste)

```txt
Du bist mein QA + Security Lead.

Inputs:
- PRD.json: {PRD_JSON}
- ARCHITECTURE_SPEC.json: {ARCHITECTURE_SPEC_JSON}
- Build/Repo-Notizen: {BUILD_NOTES}

Tasks:
1) Erzeuge TEST_PLAN.json (Testmatrix, Release Checks, Regression).
2) Erzeuge THREAT_MODEL.json (Assets, Threats, Mitigations).
3) Erzeuge PRIVACY_DPIA_LITE.json (Datenkategorien, Rechtsgrundlage, Retention, Risiken).
4) Gib eine priorisierte Liste: Top 10 Fixes vor Launch (P0).
```

## Templates

- `/templates/TEST_PLAN.json`
- `/templates/THREAT_MODEL.json`
- `/templates/PRIVACY_DPIA_LITE.json`
- `/templates/QA_REPORT.json` (NEU in v2: Go/No-Go-Entscheidung, aggregiert Test/Security/Compliance)

## GPT-Config

- `/gpt_configs/07_QA_SECURITY_COMPLIANCE.json`

## Toolbox-Vertiefung

- `/toolbox/06__QA_SECURITY_COMPLIANCE.md`
- `/toolbox/P07_LEGAL_AND_CONTRACTS.md`
