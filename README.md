# Vibecoding Pipeline – Sorted v2

Öffne als erstes: `/playbook/00_START_HERE.md`

## Was ist neu in v2?

**Toolbox bereinigt:** P-Dateien sind von Boilerplate und fehlplatzierten GPT-Profilen befreit. P06 enthält jetzt nur noch R Wizard statt 27 verschiedene GPT-Profile.

**CustomGPT-Konfigurationen:** `/gpt_configs/` definiert pro Stage: Name, System-Prompt-Bausteine, Knowledge-Files, Tools, Input/Output-Formate und Quality Gates.

**Querschnittsmodule:** Translation, Slides/Presentations und Brand Guardian als wiederverwendbare Module in `/gpt_configs/cross_cutting/`.

**Fehlende Templates ergänzt:** QA_REPORT.json (Go/No-Go), DEPLOY_PACKET.json (Infrastruktur), ITERATION_BRIEF.json (Feedback-Loop).

**MD_Sammlung integriert:** `/mapping/03_MD_SAMMLUNG_INTEGRATION.md` ordnet die GPT-Leitfäden aus der PDF den Pipeline-Stages zu.

## Ordner

- `/playbook/` – die sortierte Pipeline + Stage-Guides
- `/templates/` – JSON-Handoffs (18 Templates)
- `/gpt_configs/` – CustomGPT-Konfigurationen (10 Stages + 3 Querschnitt)
- `/toolbox/` – bereinigtes Originalmaterial
- `/mapping/` – Orientierung, File-Map, MD_Sammlung-Integration
