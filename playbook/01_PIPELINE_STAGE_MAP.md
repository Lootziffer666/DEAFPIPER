# Pipeline Stage Map (mit Inputs/Outputs)

Diese Map ist die „richtige“ Sortierung: Welche Stufe kommt wann – und was muss dabei entstehen.

## 01. Setup & Prompting-Standards

Inputs: Projektziel/Produktidee (grob); Constraints (Plattform, Budget/Timebox, Datenschutz); Definition: was ist „fertig“?

Outputs: Prompting-Standard (Format + Regeln); Projekt-Glossar (Begriffe); Handoff-Datei: IDEA_BRIEF.json (Rohfassung)

Quality Gates: Ein Output-Format ist festgelegt (z.B. JSON+Markdown).; Jeder Prompt fordert „vollständige“ Artefakte (Code, Tests, Schritte).

Templates: `/templates/IDEA_BRIEF.json`

Toolbox-Vertiefung: `/toolbox/01__PROMPTING_SYSTEM.md`, `/toolbox/P01_PROMPTING_PLAYBOOK.md`

## 02. Research & Validierung

Inputs: IDEA_BRIEF.json; Hypothesen/Annahmen; Zielgruppen-Skizze

Outputs: Research Brief + Findings; Risiko-/Annahmen-Log aktualisiert; Go/Pivot/Stop-Entscheid

Quality Gates: Mindestens 3 belastbare Quellen / oder 5 Nutzerstimmen.; Top 5 Risiken sind benannt + Gegenmaßnahmen.

Templates: `/templates/RESEARCH_BRIEF.json`

Toolbox-Vertiefung: `/toolbox/02__RESEARCH_DOCS.md`, `/toolbox/P02_RESEARCH_SYSTEMS.md`

## 03. Idee → Strategie → PRD

Inputs: Research Findings; Zielgruppe/Problem klar; Constraints

Outputs: PRD (MVP-Scope, Stories, ACs); Metriken/Events; Roadmap grob

Quality Gates: MVP passt in Timebox.; Akzeptanzkriterien sind testbar.; North Star Metric ist definiert.

Templates: `/templates/PRD.json`

Toolbox-Vertiefung: `/toolbox/03__IDEA_STRATEGY_PRD.md`, `/toolbox/P03_PRD_AND_PLANNING.md`

## 04. UX/UI, Flows & UX-Writing

Inputs: PRD.json; Brand/Tone grob; Kontext der Nutzer

Outputs: User Flows + IA; UX Writing/Microcopy; Design System Starter

Quality Gates: Hauptflow ist klick-/testbar (auch als Wireframe).; Accessibility-Grundregeln sind berücksichtigt.

Templates: `/templates/UX_SPEC.json`

Toolbox-Vertiefung: `/toolbox/04__UX_UI_DESIGN.md`, `/toolbox/P08_BRAND_AND_VISUAL_DESIGN.md`, `/toolbox/P12_REWRITE_AND_TONE.md`

## 05. Architektur, Diagramme & Spezifikation

Inputs: PRD.json; UX_SPEC.json; Constraints (Tech/DSGVO)

Outputs: Architektur-Spezifikation (C4/Sequenzen, API, Datenmodell); ADR-Entscheidungen; Operability (Logs/Metrics/Alerts)

Quality Gates: Jede API hat Schema + Fehlerfälle.; Datenflüsse sind DSGVO-bewusst dokumentiert.

Templates: `/templates/ARCHITECTURE_SPEC.json`

Toolbox-Vertiefung: `/toolbox/P04_DIAGRAMS_AND_ARCHITECTURE.md`, `/toolbox/P05_COMPUTATION_WOLFRAM.md`

## 06. Build / Vibe Coding

Inputs: ARCHITECTURE_SPEC.json; UX_SPEC.json; MVP Scope

Outputs: Repo + lauffähiger Build; Tests + CI; Run Instructions

Quality Gates: „Clone → run → works“ ohne Magie.; Tests für P0-Features.; Monitoring-Hooks vorbereitet.

Templates: `/templates/BUILD_PLAN.json`, `/templates/DEPLOY_PACKET.json`

Toolbox-Vertiefung: `/toolbox/05__BUILD_VIBE_CODING.md`, `/toolbox/P06_BUILD_DEBUG_R.md`

## 07. QA, Security & Compliance

Inputs: Build Artefakte; Threat Model Rohfassung; Privacy Notes

Outputs: Testplan + Regression; Threat Model + Controls; DSGVO-Light DPIA + Policies/Impressum-Bausteine

Quality Gates: Keine P0-Bugs offen.; Top Threats mitigiert.; Privacy/Legal Minimum erfüllt.

Templates: `/templates/TEST_PLAN.json`, `/templates/THREAT_MODEL.json`, `/templates/PRIVACY_DPIA_LITE.json`, `/templates/QA_REPORT.json`

Toolbox-Vertiefung: `/toolbox/06__QA_SECURITY_COMPLIANCE.md`, `/toolbox/P07_LEGAL_AND_CONTRACTS.md`

## 08. Marketing, GTM & Launch Assets

Inputs: PRD + Proof/Findings; Brand/Tone; Produktdemo/Build

Outputs: Positioning + Messaging; Landing Page + Copy; Launch Plan + Content Seeds

Quality Gates: Ein klarer Satz: „für wen, welches Problem, warum wir?“; Tracking/Attribution steht.; Launch Checklist erfüllt.

Templates: `/templates/GTM_PLAN.json`, `/templates/LAUNCH_CHECKLIST.json`

Toolbox-Vertiefung: `/toolbox/07__MARKETING_GTM_CONTENT.md`, `/toolbox/P09_WEBSITE_BUILD.md`, `/toolbox/P10_COPYWRITING_MESSAGING.md`, `/toolbox/P11_CONTENT_GROWTH_SYSTEMS.md`, `/toolbox/P08_BRAND_AND_VISUAL_DESIGN.md`

## 09. Execution, Analytics & Iteration

Inputs: Launch Daten; Support/Feedback; Analytics Setup

Outputs: Dashboard + Review Cadence; Experiment Backlog; Iteration Plan (4 Wochen)

Quality Gates: Weekly KPI Review läuft.; Mindestens 2 Experimente vorbereitet.; Feedback wird in PRD/UX zurückgespielt.

Templates: `/templates/ANALYTICS_PLAN.json`, `/templates/EXPERIMENT_BRIEF.json`, `/templates/POSTMORTEM_LESSONS.json`, `/templates/ITERATION_BRIEF.json`

Toolbox-Vertiefung: `/toolbox/08__EXECUTION_ANALYTICS_ITERATION.md`, `/toolbox/P11_CONTENT_GROWTH_SYSTEMS.md`

## 10. Handoff, Verträge & Übergabe

Inputs: Alles oben + Stakeholder-Needs

Outputs: Handoff Package (Docs, Repo, Ops, Legal, Marketing); Offene Punkte + Ownership

Quality Gates: Neue Person kann das Produkt deployen + betreiben.; Rechte/Lizenzen sind geklärt.

Templates: `/templates/HANDOFF_PACKAGE.json`

Toolbox-Vertiefung: `/toolbox/09__HANDOFF_CONTRACTS.md`, `/toolbox/P07_LEGAL_AND_CONTRACTS.md`

## Querschnittsmodule (an mehreren Stages einsetzbar)

**Translation & Lokalisierung**: DE↔EN Übersetzung mit Glossar-Konsistenz. Konfig: `/gpt_configs/cross_cutting/CROSS_TRANSLATION.json`

**Presentation Builder**: Slide Decks aus Artefakten (PRD-Review, Pitch, Architecture). Konfig: `/gpt_configs/cross_cutting/CROSS_SLIDES.json`

**Brand Guardian**: Markenkonsistenz ab Stage 04 (Design Tokens) bis Stage 10 (Brand Kit). Konfig: `/gpt_configs/cross_cutting/CROSS_BRAND.json`

## CustomGPT-Konfigurationen

Jede Stage hat eine zugehörige GPT-Config in `/gpt_configs/`. Diese definiert: Name, System-Prompt-Bausteine (inkl. MD_Sammlung-Referenzen), Knowledge-Files, Tools, Handoff-Formate und Quality Gates.

Siehe auch: `/mapping/03_MD_SAMMLUNG_INTEGRATION.md` für die Zuordnung der GPT-Leitfäden aus der PDF.

## SSOT Notes
- Research SSOT: `toolbox/P02_RESEARCH_SYSTEMS.md`
- Brand SSOT: `toolbox/P08_BRAND_AND_VISUAL_DESIGN.md`
- Marketing/Growth SSOT: `toolbox/P11_CONTENT_GROWTH_SYSTEMS.md` + `toolbox/P12_REWRITE_AND_TONE.md`
- Diagrams SSOT: `toolbox/P04_DIAGRAMS_AND_ARCHITECTURE.md`
- Optional strict handoff: `handoff/handshake_template_pack_v0/`
