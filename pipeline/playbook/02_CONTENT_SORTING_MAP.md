# Content Sorting Map – Wo steckt welches Wissen?

Dieses Dokument beantwortet: **„Welche Datei muss ich wann lesen?"**

Grundregel: **Playbook zuerst**, Toolbox nur bei Bedarf. GPT-Configs definieren, wie die CustomGPTs gebaut werden.

## Primäre Reihenfolge (Playbook)

1. `/playbook/00_START_HERE.md`
2. `/playbook/01_PIPELINE_STAGE_MAP.md`
3. `/playbook/03_PROJECT_REPO_SCAFFOLD.md`
4. `/playbook/stages/01_SETUP_PROMPTING.md` → … → `/playbook/stages/10_HANDOFF_LEGAL.md`

## CustomGPT-Konfiguration

Jede Stage hat eine zugehörige GPT-Config in `/gpt_configs/`. Diese definiert Name, System-Prompt-Bausteine, Knowledge-Files, Tools, Input/Output-Formate und Quality Gates.

Zusätzlich gibt es drei Querschnittsmodule in `/gpt_configs/cross_cutting/`: Translation, Slides/Presentations und Brand Guardian.

## Drei Wissensquellen pro Stage

**Schicht 1 – Playbook** (`/playbook/stages/`): Was tun, Reihenfolge, Quality Gates, Short-Prompt.

**Schicht 2 – Toolbox** (`/toolbox/`): Bereinigtes Detailwissen. `0x__`-Dateien = kompakte Summaries, `Pxx`-Dateien = ausführliche Deep-Dives. Ab v2 von Boilerplate und fehlplatzierten GPT-Profilen bereinigt.

**Schicht 3 – MD_Sammlung** (`/mapping/03_MD_SAMMLUNG_INTEGRATION.md`): GPT-Leitfäden als System-Prompt-Bausteine für die GPT-Configs.

## Toolbox (bereinigt) – nach Stages

### 01. Setup & Prompting
Toolbox: `01__PROMPTING_SYSTEM.md`, `P01_PROMPTING_PLAYBOOK.md`
MD_Sammlung: Prompt-Vorlage (S. 4–5), Cheat Sheet (S. 10–12), How to Use GPT (S. 19–21)

### 02. Research & Validierung
Toolbox: `02__RESEARCH_DOCS.md`, `P02_RESEARCH_SYSTEMS.md`
MD_Sammlung: Forschungsassistent (S. 17–18)

### 03. Idee → Strategie → PRD
Toolbox: `03__IDEA_STRATEGY_PRD.md`, `P03_PRD_AND_PLANNING.md`
MD_Sammlung: Insight Companion (S. 22–25)

### 04. UX/UI
Toolbox: `04__UX_UI_DESIGN.md`, `P08 (clean)`, `P12 (clean)`
Querschnitt: Brand Guardian

### 05. Architektur & Diagramme
Toolbox: `P04_DIAGRAMS_AND_ARCHITECTURE.md`, `P05_COMPUTATION_WOLFRAM.md`
MD_Sammlung: Architektur-Prompts (S. 7)

### 06. Build / Vibe Coding
Toolbox: `05__BUILD_VIBE_CODING.md`, `P06_BUILD_DEBUG_R.md`
MD_Sammlung: Prompt-Bibliothek (S. 6–9), Cheat Sheet (S. 10–12), How to Use GPT (S. 19–21)

### 07. QA, Security & Compliance
Toolbox: `06__QA_SECURITY_COMPLIANCE.md`, `P07_LEGAL_AND_CONTRACTS.md`
MD_Sammlung: Ethical Hacker GPT (S. 13–16), Security/DevOps (S. 8–9)

### 08. Marketing, GTM & Launch
Toolbox: `07__MARKETING_GTM_CONTENT.md`, `P09`, `P10`, `P11`, `P08 (clean)`
MD_Sammlung: MARKETING GPT (S. 26–29), Insight Companion (S. 22–25)
Querschnitt: Brand Guardian, Presentation Builder

### 09. Execution & Iteration
Toolbox: `08__EXECUTION_ANALYTICS_ITERATION.md`, `P11`
MD_Sammlung: Math Solver (S. 30–33)

### 10. Handoff & Legal
Toolbox: `09__HANDOFF_CONTRACTS.md`, `P07`
Querschnitt: Translation

## Querschnittsmodule (in `/gpt_configs/cross_cutting/`)

**Translation & Lokalisierung**: DE↔EN Übersetzung mit Glossar-Konsistenz. Stages 01, 03, 04, 08, 10.

**Presentation Builder**: Slide Decks aus Artefakten. Stages 03, 05, 08, 10.

**Brand Guardian**: Markenkonsistenz ab Stage 04 bis Stage 10.

## Meta
- `P99_SOURCE_MAP.md` → welche PDF-Seiten in welche P-Datei einflossen
- `/toolbox/profiles/PROFILE_REGISTRY.json` → alle extrahierten GPT-Profile mit Stage-Zuordnung
