# START HERE – Vibe Coding Pipeline (sortiert v2)

Dieses Paket ordnet das vorhandene Material so, dass du von **Idee → fertiges Produkt → Launch/Marketing → Iteration** ohne „Wo war das nochmal?" durchkommst.

## Was ist was?

- **/playbook/** = die **eigentliche** Pipeline (Schritt-für-Schritt, Inputs/Outputs, Quality Gates, Short-Prompts)
- **/templates/** = standardisierte **Handoff-Dateien** (18 JSON-Skelette), damit jeder Schritt sauber in den nächsten übergeht
- **/gpt_configs/** = **CustomGPT-Konfigurationen** (10 Stages + 3 Querschnitt): Name, System-Prompt-Bausteine, Knowledge-Files, Tools, Handoff-Formate
- **/toolbox/** = deine **Materialsammlung** (bereinigt: Boilerplate und fehlplatzierte GPT-Profile entfernt)
- **/mapping/** = Zuordnung & Orientierung (File-Map, MD_Sammlung-Integration, Rename-Vorschläge)

## Zwei Nutzungsmodi

1) **Fast Track (empfohlen, wenn du bauen willst):**  
   Arbeite die Stage-Files in `/playbook/stages/` der Reihe nach durch und fülle dabei die passenden JSON-Templates.

2) **Deep Dive (wenn du stecken bleibst oder optimieren willst):**  
   Spring aus einem Stage-File gezielt in die verlinkten Toolbox-Dokumente (Pxx = groß & detailreich).

## Minimaler „Happy Path"

1. `/playbook/01_PIPELINE_STAGE_MAP.md` lesen (gesamtes Bild)  
2. `/playbook/03_PROJECT_REPO_SCAFFOLD.md` übernehmen (Ordner/Dateien)  
3. Dann: `/playbook/stages/01_SETUP_PROMPTING.md` → … → `10_HANDOFF_LEGAL.md`  
4. Wenn etwas unklar ist: `/playbook/02_CONTENT_SORTING_MAP.md` (wo steckt das Wissen?)

## CustomGPTs bauen

Wenn du die Pipeline als Kette von CustomGPTs umsetzen willst:
1. Lies `/gpt_configs/01_SETUP_PROMPTING.json` → dort stehen System-Prompt-Bausteine, Knowledge-Files und Tools.
2. Lade die angegebenen Knowledge-Files aus `/toolbox/` als Knowledge-Base in deinen CustomGPT.
3. Verwende die System-Prompt-Bausteine (referenziert auf MD_Sammlung-Seiten) als Basis für die Instructions.
4. Definiere das Input/Output-Format gemäß der Config, damit der Handoff zum nächsten GPT funktioniert.

Querschnittsmodule (Translation, Slides, Brand) können an jeder Stage zusätzlich eingesetzt werden.

## Tipp: Ein Output pro Schritt

Wenn du pro Stage **genau einen** Output-Ordner pflegst (z.B. `work/03_prd/PRD.json`), wird die Pipeline plötzlich… langweilig zuverlässig. Und das ist ein Kompliment.

## Was ist neu in v2?

- **Toolbox bereinigt**: P-Dateien um 37–95% reduziert (Boilerplate, fehlplatzierte GPT-Profile entfernt)
- **GPT-Configs**: 10 Stage-Configs + 3 Querschnittsmodule
- **3 neue Templates**: QA_REPORT, DEPLOY_PACKET, ITERATION_BRIEF
- **MD_Sammlung integriert**: GPT-Leitfäden aus der PDF den Stages zugeordnet
- **Profil-Registry**: `/toolbox/profiles/PROFILE_REGISTRY.json` dokumentiert alle extrahierten GPT-Profile

— erstellt am 2026-03-04
