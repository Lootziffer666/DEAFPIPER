# MD_Sammlung → Pipeline Integration

> Diese Datei ordnet die Kapitel der `MD_Sammlung.pdf` den Pipeline-Stages und CustomGPT-Konfigurationen zu.
> Sie ist die fehlende Brücke zwischen den GPT-Leitfäden (System-Prompt-Bausteine) und der Pipeline-Struktur.

## Zuordnung nach Pipeline-Stage

### Stage 01 – Setup & Prompting

**Prompt-Vorlage (Entwickler) – universell** (S. 4–5): Kurzformat und Langformat als universelle Eingabe-Templates. Wird als System-Prompt-Baustein in den Pipeline Coach geladen. Das Kurzformat eignet sich für schnelle Feature-Requests, das Langformat (Nutzerstory + funktionale/nicht-funktionale Anforderungen + Datenmodell + Akzeptanzkriterien) für größere Features ab Stage 03.

**Cheat Sheet – Coding mit GPT** (S. 10–12): Goldene Regeln, Prompt-Muster, Stolperfallen. Wird als Schnellreferenz sowohl in Stage 01 (Prompting-Standard definieren) als auch in Stage 06 (Build) verwendet.

**How to Use This GPT Effectively** (S. 19–21): Englischsprachiges Pendant zu den deutschen Leitfäden. Beschreibt den generischen Verarbeitungszyklus (Intent → Context → Decompose → Generate → Check → Format), der als Basislogik für alle GPT-Configs dient.

### Stage 02 – Research & Validierung

**Forschungs-/Dokumentenassistent** (S. 17–18): Kernfunktionen – Recherche, Zitationshilfe, Dokumentanalyse, Zusammenfassungen. Definiert die Arbeitsweise des Research Agent: Analyse → Kontextprüfung → Werkzeugauswahl → Informationsverarbeitung → Antwortgenerierung.

### Stage 03 – Idee → Strategie → PRD

**Insight Companion – Funktionsübersicht** (S. 22–25): Strategische Unterstützung mit analytischen Frameworks (SWOT, Five Forces, Funnel). Liefert die methodische Basis für den Strategy & PRD Planner: Intent-Erkennung → Kontextbewertung → Analytische Struktur wählen → Insights generieren → Handlungsempfehlungen.

### Stage 06 – Build / Vibe Coding

**Prompt-Bibliothek – Programmierung** (S. 6–9): Acht fertige Prompt-Templates für Debugging, Feature-Implementierung, Architektur, Refactoring, Tests, Performance, Security und DevOps. Wird als primärer System-Prompt-Baustein in den Vibe Coder geladen.

### Stage 07 – QA, Security & Compliance

**Ethical Hacker GPT – Leitfaden** (S. 13–16): Kern-Direktiven (ethisch/legal), Schwerpunkt Web/Mobile Security, OWASP-Mapping, 6-Schritte-Ablauf (Ziel → Policy-Check → Informationsstrategie → Lösungsplan → Antwort → QA). Definiert die Arbeitsweise des Security & QA Auditor.

### Stage 08 – Marketing, GTM & Launch Assets

**MARKETING GPT – So nutzt du mich am effektivsten** (S. 26–29): Kern-Direktiven (KPI-getrieben, plattformgerecht), 6 Arbeitsschritte (A–F), Prompt-Struktur [TASK/CONTEXT/FORMAT/CONSTRAINTS/SUCCESS]. Definiert die Arbeitsweise des Marketing Strategist.

### Stage 09 – Execution, Analytics & Iteration

**Math Solver – Leitfaden** (S. 30–33): Tutor-Format (Solution By Steps → Final Answer → Key Concept). Wird zweckentfremdet als strukturierte Problemlösungs-Methode für KPI-Analyse und Datenvalidierung im Growth & Analytics Lead.

## Kapitel ohne direkte Stage-Zuordnung (Querschnitt)

**Prompt-Bibliothek §3 Architektur & Design** (S. 7): Wird sowohl in Stage 05 (Architecture) als auch in Stage 06 (Build) referenziert.

**Prompt-Bibliothek §7 Security + §8 DevOps** (S. 8–9): Wird sowohl in Stage 06 (Build/CI-CD) als auch in Stage 07 (QA/Security) referenziert.

## Nicht abgedeckte Inhalte aus der PDF

Die Kapitel zu `ai-pdf-drive-gpt_leitfaden_de.md` und `diagram_prompt_cheatsheet.md` (aus dem MANIFEST als Quellen referenziert) sind nur dünn in die Pipeline eingeflossen. Sie sollten bei der nächsten Iteration explizit Stage 02 (PDF-Analyse im Research-Kontext) und Stage 05 (Diagramm-Erzeugung) zugeordnet werden.
