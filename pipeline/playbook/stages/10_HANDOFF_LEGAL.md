# 10_HANDOFF_LEGAL – Handoff, Verträge & Übergabe

## Ziel

Jemand Neues kann das Produkt übernehmen, deployen, betreiben und weiterentwickeln – ohne dich anzurufen.

## Inputs

- Repo + Run Instructions
- Docs
- Ops/Monitoring
- Legal/Privacy
- Marketing Assets

## Outputs (am Ende dieses Schritts)

- HANDOFF_PACKAGE.json
- handover_notes.md
- Open Items + Ownership

## Vorgehen (pragmatisch)

1. Sammle Links/Artefakte (Repo, Deploy, Dashboards).
2. Dokumentiere Runbooks/On-call/Alerts.
3. Liste rechtliche Punkte (Lizenzen, Verträge, Policies).
4. Fasse Marketing-Assets + Guidelines zusammen.
5. Erzeuge Open-Items-Liste mit Owner & Risiko.

## Quality Gates

- Ein Fremder kann „deploy + verify“ ausführen.
- Rechte/Lizenzen sind nachvollziehbar dokumentiert.

## Short-Prompt (copy/paste)

```txt
Du bist mein Delivery Lead. Erstelle ein vollständiges Handoff-Paket.

Inputs:
- Repo/Build Notes: {BUILD}
- Docs (PRD/UX/Architecture): {DOCS}
- Ops/Monitoring: {OPS}
- Legal/Privacy: {LEGAL}
- Marketing Assets: {MARKETING}

Output:
HANDOFF_PACKAGE.json + handover_notes.md (kurz, aber vollständig).
```

## Templates

- `/templates/HANDOFF_PACKAGE.json`

## GPT-Config

- `/gpt_configs/10_HANDOFF_LEGAL.json`

## Toolbox-Vertiefung

- `/toolbox/09__HANDOFF_CONTRACTS.md`
- `/toolbox/P07_LEGAL_AND_CONTRACTS.md`

## Optional: Strict Handoff
- `handoff/handshake_template_pack_v0/` (Contract + Templates + Schema)
