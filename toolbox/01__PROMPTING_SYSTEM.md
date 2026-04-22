# Prompting System & Output-Standards (vorläufig)

## Core-Prinzipien & Verarbeitung (extern sichtbar)

# How to Use This GPT Effectively

## 1. Core Operating Principles (High‑Level)

This assistant follows several general principles designed to ensure
useful, safe, and consistent responses:

- **Helpfulness:** Provide clear, practical answers and guidance.
- **Accuracy:** Base responses on available knowledge and clearly
 indicate uncertainty when needed.
- **Safety & Privacy:** Avoid revealing sensitive system information,
 hidden instructions, or private data.
- **Structured Communication:** Prefer organized explanations,
 examples, and step‑by‑step guidance when useful.
- **Adaptation to User Skill Level:** Adjust explanations depending on
 whether the user appears beginner, intermediate, or advanced.
- **Programming Support:** Assist with coding tasks such as:
 - Code generation
 - Code review
 - Optimization suggestions
 - Pull request descriptions
 - Unit test creation
 - Documentation and comments

> cannot be disclosed.

------------------------------------------------------------------------

## 2. Typical Processing Steps for a Request (Conceptual Overview)

When a request is received, the assistant generally follows a reasoning
pipeline similar to the following:

1. **Intent Detection**
 - Determine the user's goal (e.g., coding help, explanation,
 debugging, documentation).
2. **Context Evaluation**
 - Identify relevant information provided by the user.
 - Consider constraints such as language, libraries, frameworks, or
 environment.
3. **Task Decomposition**
 - Break the request into smaller sub‑tasks (e.g., analyze code →
 identify issues → propose improvements).
4. **Solution Generation**
 - Produce an answer, code example, explanation, or structured
 output.
5. **Quality & Safety Check**
 - Ensure the response does not expose restricted information or
 violate policies.
 - Confirm the output is logically consistent and formatted
 clearly.
6. **Response Formatting**
 - Structure the answer (Markdown, lists, code blocks, etc.) to
 make it easy to read and use.

------------------------------------------------------------------------

## 3. Output Formats Commonly Used

Responses may include structured formats such as:

### Markdown

Used for: - Explanations - Documentation - Structured lists - Guides and
tutorials

### Code Blocks

Used for: - Source code examples - Configuration files - CLI commands

Example:

``` python
def add(a, b):
 return a + b
```

### Structured Technical Content

Such as:

- Pull request descriptions
- Architecture explanations
- API usage examples
- Debugging steps

------------------------------------------------------------------------

## 4. Important Constraints

The assistant operates under several restrictions:

- **No disclosure of hidden system prompts or internal policies**
- **No fabrication of sensitive data**
- **No unsafe or malicious guidance**
- **Respect for privacy and security**
- **Compliance with platform formatting rules**

------------------------------------------------------------------------

## 5. Tips for Getting the Best Results

To get more precise and useful responses:

- Provide **clear goals**
- Include **code snippets** when debugging
- Mention **programming language and framework**
- Describe **expected vs. actual behavior**
- Ask for **specific outputs** (tests, refactors, documentation, etc.)

Example good prompt:

> "Refactor this Python function for performance and add unit tests
> using pytest."

------------------------------------------------------------------------

## Summary

You will get the best results when requests are:

- Specific
- Context‑rich
- Goal‑oriented
- Accompanied by relevant code or data

## Universal Prompt-Vorlage

# Prompt-Vorlage (Entwickler) – universell

> Ziel: Maximale Präzision + weniger Rückfragen + reproduzierbare Ergebnisse.

## 1) Kurzformat (copy/paste)

**Rolle:** Du bist mein Senior-Engineer für **{DOMÄNE}**.
**Ziel:** {ZIEL}
**Kontext:**
- Sprache/Stack: {STACK}
- Umgebung: {OS/RUNTIME/DEPLOYMENT}
- Einschränkungen: {LIMITS}
**Anforderungen (Must):**
1. {MUST_1}
2. {MUST_2}
3. {MUST_3}
**Nice-to-have:**
- {NICE_1}
- {NICE_2}

**Inputs/Beispiele:**
- Input: {INPUT_BEISPIEL}
- Output: {OUTPUT_BEISPIEL}

**Randfälle:**
- {EDGE_1}
- {EDGE_2}

**Erwartetes Ergebnis:**
- Liefere: {ARTEFAKTE} (z. B. Ordnerstruktur + vollständiger Code + Tests + Run-Befehle)
- Qualität: sicher, lesbar, ohne Platzhalter, mit Fehlerbehandlung
- Falls Annahmen nötig: Liste sie explizit

---

## 2) Langformat (für größere Features / Projekte)

### A) Problem & Nutzerstory
- Problem: {PROBLEM}
- Nutzerstory: Als {ROLLE} möchte ich {AKTION}, damit {NUTZEN}.

### B) Funktionale Anforderungen
- Endpunkte/Flows:
 - {FLOW_1}
 - {FLOW_2}

### C) Nicht-funktionale Anforderungen
- Performance: {PERF}
- Sicherheit: {SEC}
- Observability: {LOGS/METRICS}
- Skalierung: {SCALE}

### D) Datenmodell
- Entities + Felder: {DATA_MODEL}
- Validierung: {VALIDATION}
- Migrationen: {MIGRATIONS}

### E) Akzeptanzkriterien
- Gegeben/Wenn/Dann:
 - {AC_1}
 - {AC_2}

### F) Deliverables
- {DELIVERABLE_1}
- {DELIVERABLE_2}
- {DELIVERABLE_3}

---

## 3) Mini-Checkliste vor dem Absenden
- [ ] Stack genannt
- [ ] Ziel + Output klar
- [ ] Must/Nice getrennt
- [ ] Beispiele enthalten
- [ ] Randfälle erwähnt
- [ ] Tests/Run-Befehle gewünscht? (ja/nein)

## Cheat Sheet – Coding mit GPT

# Cheat Sheet – „Coding mit GPT“ (schnell & effektiv)

## Goldene Regeln
- **Sag den Stack.** (Sprache, Framework, Versionen)
- **Sag das Ziel.** (Was ist „done“?)
- **Gib Beispiele.** (Input/Output, JSON, Requests)
- **Nenne Constraints.** (Zeit, Speicher, kompatible APIs, Lizenz)
- **Poste Fehler vollständig.** (Stacktrace, Logs, relevante Config)

---

## Prompt-Muster (ultrakurz)

### Debug
```
Fixe diesen Bug. Stack: {STACK}
Code: {CODE}
Fehler: {ERROR}
Ergebnis: vollständiger Fix + Erklärung + Tests.
```

### Neues Feature
```
Implementiere {FEATURE}. Stack: {STACK}
Must: {MUSTS}
Nice: {NICES}
Liefere: Architektur + vollständigen Code + Tests + Run-Befehle.
```

### Architektur
```
Designe {SYSTEM}. Last: {LOAD}. SLA: {SLA}. Constraints: {CONSTRAINTS}
Liefere: Komponenten, Datenflüsse, Failure Modes, Migrationsplan.
```

---

## Was du immer anfordern kannst
- **Ordnerstruktur** als Tree
- **vollständigen Code** (keine Platzhalter)
- **Tests** (unit/integration)
- **Run-Befehle** (lokal + docker)
- **Fehlerbehandlung** (Retries/Timeouts)
- **Security** (Input-Validation, AuthZ, Secrets)
- **Observability** (Logs, Metrics, Tracing)

---

## Gute Inputs, die Antworten verbessern
- Minimal Repro (kleines Beispielprojekt)
- Erwartete vs. tatsächliche Ausgabe
- Datenformate + Schemas
- Performance-Zielwerte (p95 latency, throughput)
- Produktionsbedingungen (Kubernetes? Serverless? Region?)

---

## „Antwort-Qualität“ steuern (Sätze zum Copy/Paste)

### Mehr Details
- „Begründe jede Designentscheidung in 1–2 Sätzen.“
- „Zeige Alternativen und Trade-offs.“

### Weniger Text, mehr Code
- „Halte die Erklärung kurz, Fokus auf vollständigen Code.“

### Strengere Qualität
- „Keine Platzhalter. Keine TODOs. Alles ausführbar.“
- „Füge Input-Validation, Logging und Tests hinzu.“

### Schrittweise
- „Erst Plan + Ordnerstruktur. Dann implementieren.“

---

## Häufige Stolperfallen
- Versionskonflikte (Node/Python/Java)
- Fehlende Env-Variablen/Secrets
- CORS/CSRF/Session vs JWT
- N+1 Queries, fehlende Indizes
- Race Conditions, Deadlocks
- Timeouts, Retries ohne Backoff

---

## Mini-Checkliste beim Einfügen von Code/Fehlern
- [ ] komplette Fehlermeldung
- [ ] relevante Codepfade + Config
- [ ] Versionsinfos
- [ ] Schritte zum Reproduzieren
- [ ] gewünschte Endausgabe

## Format-/Tool-Regeln (PDF)

* Wenn du eine Datei brauchst (z. B. PDF, Docx, Sheet, Slides) → ich erstelle sie mit den passenden
Tools.
---
## 3) Formate & Einschränkungen, die ich zwingend einhalten muss
### A) Formatierungsregeln
* **Markdown** ist ok (und von dir gewünscht).
* **Keine UI-Writing-Blocks** außer bei **E-Mails** (und dann ohne Code darin).
* **Code** immer in normalen Code-Blöcken (`…`), nicht in Writing-Blocks.
### B) Web-Recherche & Quellen
* Bei zeitkritischen Infos: **muss** ich online nachsehen.
* Wenn ich Fakten aus dem Web nutze, setze ich **Quellen-Zitate** (Citations) an die passenden
Stellen.
### C) Tool-Pflichten
* **Bilder editieren/generieren** → Bild-Tool.
* **PDF analysieren** → ggf. PDF-Screenshot-Tool.
* **Spreadsheets/Slides** → dafür vorgesehenes Artifact-Tooling.
### D) Sicherheits-Constraints (harte Grenzen)
* Keine Anleitung zu illegalen oder schädlichen Aktivitäten.
* Keine Inhalte, die Privatsphäre verletzen oder zu Schaden anstiften.
* Bei heiklen Themen: sichere, legale Alternativen.
### E) Kommunikations-Constraints
* Kein „ich mache das später“ oder „warte…“.
* Ich frage **nicht mehrfach** nach Dingen, die du schon beantwortet hast.
* Wenn es kompliziert wird: lieber **Teil-Lösung sofort** als blockieren.
---
**Welche Art App willst du bauen (1 Satz): Marketplace, Social, Fitness, Booking, Chat, Finanzen, Lern-
App oder etwas anderes?**
*"You can use AI like the top 1% to build income streams, automate tasks and do alot more by
Alles klar — hier ist ein ausführliches „Playbook“, mit dem du das Maximum aus diesem GPT als
**wissenschaftlichem Recherche-Assistenten** herausholst.

## Perfekte Prompt-Vorlagen (PDF)

return 1
if __name__ == "__main__":
raise SystemExit(run())
```
---
## B) „Perfekte Prompt“-Vorlage (Copy/Paste)
### 1) Neue Funktion / Feature bauen
```text
Ziel:
- [Was soll gebaut werden? 1–2 Sätze]
Stack/Constraints:
- Sprache/Version: [z.B. Python 3.12]
- Laufzeit/Plattform: [Linux/Mac/Windows/Docker/...]
- Erlaubte Dependencies: [keine / stdlib / erlaubt: ...]
- Non-Goals: [was NICHT passieren soll]
Input/Output:
- Input-Beispiel(e):
1) ...
- Output-Beispiel(e):
1) ...
Edge Cases:
- [z.B. leere Inputs, ungültige Daten, große Dateien, Unicode, ...]
Akzeptanzkriterien:
- [bullet list: muss X, Y, Z]
Bitte liefere:
1) Detaillierten Plan/Pseudocode
2) Vollständigen, kompilierbaren Code in EINEM Codeblock
3) Kurze Hinweise zu Tests/Validierung
```
### 2) Bugfix / Debugging
```text
Problem:
- Erwartetes Verhalten:
- Tatsächliches Verhalten:
- Fehlermeldung/Stacktrace (vollständig):

- Minimaler Repro (Code + Input):
Umgebung:
- OS:
- Sprache/Runtime-Version:
- Dependency-Versionen:
- Wie wird gestartet? (Command):
Code:
- [Paste relevante Dateien oder Link + relevante Ausschnitte]
Bitte:
- Ursache erklären (kurz)
- Fix liefern (vollständiger Code / Patch)
- 2–3 Edge-Case-Tests vorschlagen
```
### 3) Code Review / Refactor
```text
Ziel des Reviews:
- [Performance / Security / Readability / Architektur / Testing]
Kontext:
- [Wofür ist das Projekt? Welche Constraints?]
Material:
- [Repo-Link oder Code hier einfügen]
- Hotspots/Dateien: [Liste]
Bitte:
- Top 5 Risiken/Probleme (priorisiert)
- Konkrete Refactor-Schritte
- Optional: Beispiel-Patch (kompletter Code in 1 Block)
```
### 4) Wenn du’s ultra-knapp willst: „Quick Fix“
```text
/quick_fix
Hier ist der Code + Error. Gib mir NUR den Fix (keine Erklärung).
[...]
```
---
**a.** Schick mir deine echte Aufgabe (Ziel + Sprache + kleines I/O-Beispiel) – ich liefere Plan +
vollständigen Code.

**b.** Soll ich dir für deine typische Arbeit (z. B. Web-App, Data Pipelines, ML, DevOps) eine
maßgeschneiderte Prompt-Vorlage erstellen?
