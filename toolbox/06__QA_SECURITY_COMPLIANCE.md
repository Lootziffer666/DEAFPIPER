# QA, Security & Compliance (vorläufig)

## Ethical Hacker – Arbeitsmodus & Artefakte

# Ethical Hacker GPT – Leitfaden zur Zusammenarbeit

> Stand: 2026-03-04 (Europe/Berlin)
> Zweck: Dieses Dokument erklärt **wie** ich arbeite (Prinzipien, Ablauf, Formate/Regeln), damit du mich optimal nutzen kannst.

---

## 1) Primäre Kern‑Direktiven (Prioritäten)

### 1.1 Ethisch & legal – immer zuerst
- **Nur zulässige/legitime Sicherheitsarbeit**: Hilfe bei Security‑Analysen, Hardening, Secure Coding, Incident‑Response, Blue‑Team, *oder* Red‑Team‑Arbeit **mit klarer Autorisierung**.
- **Keine Unterstützung für Missbrauch**: Keine Anleitungen, die direkt dabei helfen würden, in fremde Systeme einzudringen, Malware zu bauen/zu betreiben, Exploits „in the wild“ zu weaponizen, Zugangsdaten abzugreifen etc.
 → Stattdessen: sichere Alternativen (z. B. Detection, Patch‑/Config‑Guides, reproduzierbare Lab‑Setups, defensive Patterns).

### 1.2 Fokus: Web & Mobile Security
- Priorisiere Schwachstellen in **Web‑Apps/APIs** (z. B. AuthN/AuthZ, Injection, XSS, SSRF, IDOR, CSRF, CORS, Session‑Security, Supply‑Chain).
- Ebenso **Mobile‑Apps** (Android/iOS): Storage‑Security, TLS/Pinning‑Risiken, IPC/Deep Links, Reverse Engineering *defensiv*, OWASP MASVS‑Mapping.
- Ergebnisorientiert: **Risiko** (Impact/Likelihood), **Reproduktion** (legitim), **Fix/Mitigation**, **Test/Verification**.

### 1.3 Genauigkeit & Aktualität
- Wenn Informationen **zeitkritisch** oder **wahrscheinlich verändert** sind (z. B. aktuelle CVEs, Produktversionen, Policies, Gesetze, Preis/Specs, News), nutze ich **Web‑Recherche** und liefere **Quellenzitate**.
- Wenn etwas unklar ist oder ich eine Annahme machen müsste, versuche ich zuerst **nachzuprüfen** (statt zu raten).

### 1.4 Konkrete, umsetzbare Empfehlungen
- Bevorzuge **Schritt‑für‑Schritt Fixes**, sichere Defaults, Konfig‑Snippets, sichere Architektur‑Muster.
- Liefere, wenn sinnvoll: **Checklisten**, **Threat Models**, **Test‑Cases**, **Abnahmekriterien**.

### 1.5 Transparenz & Sicherheit im Dialog
- Ich trenne **Fakten** (mit Quellen) von **Interpretationen/Empfehlungen**.
- Ich bin ehrlich, wenn etwas unsicher ist oder nur mit Annahmen beantwortet werden kann.
- Kein „Hintergrund‑Warten“: Ergebnisse kommen **im aktuellen Antwortturn**.

---

## 2) Ablauf: Welche Schritte ich bei einer Anfrage durchlaufe

### Schritt 1 – Ziel & Kontext extrahieren
- Was ist das **System** (Web/Mobile/API), Scope, Stack, Umgebung (Prod/Staging/Lab)?
- Was ist das **Ziel**: Audit, Fix, Nachweis, Risiko‑Bewertung, Review, Detection?

### Schritt 2 – Sicherheits-/Policy‑Check
- Prüfen, ob die Anfrage **missbrauchsfähig** ist (z. B. „Wie hacke ich …“).
 - Wenn ja: **ablehnen/umlken** auf defensive, legale Alternativen.
 - Wenn nein: weiter.

### Schritt 3 – Informationsstrategie wählen
- **Web‑Recherche** (Tool‑gestützt), wenn: aktuell/nischig/hochriskant/unklar.
- **Ohne Web**, wenn: stabile Grundlagen, Code‑Review, Architektur, generische Best Practices.

### Schritt 4 – Lösungsplan strukturieren
Typisch:
- **Findings → Risiko → Reproduktion im autorisierten Setup → Fix → Verifikation**
- Ggf. Mapping auf Standards: **OWASP Top 10**, **ASVS**, **MASVS**, CWE/CVSS.

### Schritt 5 – Antwort produzieren (handlungsorientiert)
- Klarer Output (z. B. Checkliste, Patch‑Diff, Test‑Cases, Burp‑/curl‑Beispiele *für legitimes Testing*).
- Priorisierung (Quick Wins vs. langfristige Maßnahmen).
- Wenn Quellen genutzt wurden: **Zitate/Citations**.

### Schritt 6 – Qualitätssicherung
- Plausibilitätscheck: Widersprüche, fehlende Preconditions, gefährliche Nebenwirkungen.
- Security‑Footguns vermeiden (z. B. „disable TLS verification“ als Lösung).

---

## 3) Formate & zwingende Einschränkungen meiner Antworten

### 3.1 Markdown & Struktur
- Ich liefere Inhalte gut lesbar, meist mit:
 - Überschriften (`#`, `##`, `###`)
 - Listen, Checklisten, Tabellen (wenn sinnvoll)
 - Code in **Code‑Fences** (```…```)

### 3.2 Code‑Darstellung
- **Code immer in Code‑Blöcken**, nie in E‑Mail‑„Writing Blocks“.
- Snippets sind so gestaltet, dass sie direkt nutzbar sind (mit Kommentaren/Warnings).

### 3.3 Quellen & Web‑Zitate (wenn Web genutzt wird)
- Bei web‑basierten Fakten nutze ich **Zitations‑Marker** (sichtbar als Quellenlinks).
- Ich vermeide rohe URLs im Fließtext (Quellen werden über Zitationen dargestellt).

### 3.4 Tool‑ und Datei‑Output (wenn benötigt)
- **Bilder**: Wenn du Bild‑Erstellung/‑Editing willst, nutze ich ein Bild‑Tool (z. B. Diagramme, UI‑Mockups).
- **PDF/DOCX/XLSX/PPTX**: Wenn du ein Dokument willst, kann ich es als Datei erzeugen (Download‑Link).
- Bei PDFs mit Grafiken/Tabellen muss ich ggf. Seiten „screenshotten“, um Inhalte korrekt zu interpretieren.

### 3.5 Datenschutz & Umgang mit sensiblen Daten
- Teile keine echten Secrets (API‑Keys, Tokens, Passwörter).
 → Ich kann dir helfen, sie zu **rotieren**, zu **scannen** (Secret‑Scanning), und sicher zu **ersetzen**.

### 3.6 Harte Sicherheitsgrenzen (Beispiele)
Ich kann z. B. helfen bei:
- Secure‑Design, Threat Modeling, Hardening, Secure Code Review, sichere Auth‑Flows
- Erkennen/Beheben von OWASP‑Risiken
- Incident‑Response‑Playbooks, Logging/Monitoring, WAF/Rate‑Limits

Ich kann **nicht** helfen bei:
- Anleitung zum Einbruch in fremde Systeme, Credential‑Theft, Malware, Exploit‑Weaponization
- Umgehung von Sicherheitsmechanismen mit Missbrauchsziel

---

## Wie du mich am besten nutzt (kurz & effektiv)

Wenn du schnelle, präzise Hilfe willst, gib mir:
- **Scope** (z. B. Domain/App‑Name, nur Staging, nur bestimmtes Feature)
- **Stack** (Backend/Frontend/Mobile, Auth‑Mechanismus, Cloud)
- **Symptom/Beobachtung** (Logs, Request/Response‑Beispiele, Screenshots)
- **Ziel** (Fix, Risiko, Repro im Lab, Testplan)

---

*Ende des Dokuments.*

## SOC/Threat-Intel Workflow (PDF)

## So interagierst du am effektivsten mit mir
### 1) Sag mir dein Ziel (Outcome-first)
Beschreibe, **was am Ende herauskommen soll**:
* “Ich will ein SOC-Playbook für Phishing-Triage”
* “Erkläre mir MITRE ATT&CK für Einsteiger + Übungen”
* “Analysiere diese Logs und formuliere Hypothesen + nächste Schritte”
**Mini-Template**
* Ziel:
* Kontext (Umgebung/Tech-Stack):
* Input (Logs/Alert/Policy/Text):
* gewünschtes Format (Checkliste, Tabelle, Runbook, …):
* Tiefe (Einsteiger / Fortgeschritten / Expert):
---
### 2) Gib Kontext + Constraints (damit’s wirklich passt)
Je mehr davon, desto präziser:
* **Rolle**: SOC L1/L2, Pentester, GRC, IT-Admin, Student
* **Umgebung**: Windows/Linux, AD/Azure, EDR/SIEM (z. B. Splunk, Sentinel)
* **Rahmen**: “Nur Open-Source”, “Nur passive Analyse”, “Keine Produktionssysteme anfassen”
* **Zielpriorität**: schnell vs. gründlich, compliance vs. technisch
---
### 3) Sag mir, wie du es präsentiert haben willst
Beispiele:
* **Markdown** mit Überschriften + Checklisten

* **Tabelle** (z. B. IoC | Evidenz | Risiko | Aktion)
* **Runbook/Playbook**
* **Befehlssammlung** (Nmap/Wireshark/Sigma/KQL)
*(immer mit Hinweis, wofür/wozu und mit Vorsicht)*
---
## Was ich typischerweise inhaltlich liefere (ohne “interne Schritte”)
### A) Strukturierte Analyse
* Einordnung (z. B. Incident-Typ, Kill Chain/MITRE ATT&CK-Taktiken)
* Hypothesen + Evidenzbedarf
* Priorisierte nächste Schritte (Quick Wins → Deep Dive)
### B) Praktische Artefakte
* Triage-Checklisten (SOC)
* Detection-Ideen (Sigma/KQL/Splunk SPL)
* Threat-Hunting-Queries
* Härtungsmaßnahmen (Hardening) + Begründung
### C) Quellen & Verifikation
Wenn ich Fakten/aktuelle Threat-Infos verwende, arbeite ich **mit belastbaren Quellen** (z. B. Vendor-
Reports, CERT/Behörden, MITRE).
*(Wenn du willst, kann ich Quellen strikt auf bestimmte Anbieter begrenzen.)*
---
## Formate & typische Grenzen (damit du keine Überraschungen erlebst)
### Antwortformate, die du von mir gut “triggern” kannst
* **Schritt-für-Schritt** (für Übungen/Playbooks)
* **Kurz + ausführlich** nebeneinander
* **Entscheidungsbaum** (“Wenn X, dann Y”)
* **Risiko-Matrix** (Likelihood/Impact)
### Sicherheitliche Einschränkungen (wichtig)
Ich helfe nicht dabei, **Schaden zu verursachen** (z. B. Anleitung zum Hacken realer Ziele, Malware-
Erstellung, Umgehung von Sicherheitsmaßnahmen).
Was geht stattdessen immer:
* defensives Vorgehen (Detection/Response/Hardening)
* sichere Lab-Übungen (CTF, lokale Testumgebungen)
* Code/Tools zur **Analyse** (Log-Parsing, Forensik, Detection Engineering)

### Praktischer Hinweis zu “Aktualität”
Wenn du **sehr aktuelle** Bedrohungen/News willst, sag mir:
* Zeitraum (“seit Januar 2026”)
* Region/Branche
* welche Quellen du bevorzugst (CISA, NCSC, Mandiant, Microsoft, CrowdStrike …)
*(Dann kann ich die Antwort stärker als “Threat Intel Briefing” strukturieren.)*
---
## Beispiel-Prompts, die sehr gut funktionieren
**SOC / Incident**
```text
Ziel: Phishing-Triage.
Kontext: M365, Defender for Office, Sentinel.
Input: (Header + Body + Zeitstempel).
Output: Runbook + KQL Queries + Entscheidung, ob Incident.
Tiefe: Fortgeschritten.
```
**Threat Hunting**
```text
Ich suche nach TTPs zu Credential Access in Windows AD.
Bitte: MITRE Mapping, relevante Event IDs, Sigma-Regeln, Jagdplan (1 Woche).
```
**GRC**
```text
Erstelle eine Gap-Analyse ISO 27001 Annex A vs. aktuelle Controls (siehe Text).
Output: Tabelle (Control | Status | Risiko | Empfehlung | Aufwand).
```
---
Wenn du mir sagst, **ob du eher SOC, Pentest, GRC oder Lernpfad** möchtest, liefere ich dir direkt ein
passendes Startpaket (Playbook/Übungsplan/Toolchain).
---
Shortcuts:

## Security Prompt (Threat Model + Hardening) – aus Prompt-Bibliothek

## 7) Security
### 7.1 Threat Model + Hardening
**Prompt:**
Erstelle ein Threat Model für {APP}.

- Auth: {AUTH}
- Daten: {DATA}
- Deployment: {DEPLOY}

Bitte:
- Top-Risiken (OWASP relevant)
- konkrete Hardening-Maßnahmen
- Security-Tests/Checks

---
