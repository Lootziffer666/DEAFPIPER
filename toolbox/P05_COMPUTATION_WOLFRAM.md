# P05 – Computation & Data (Wolfram)

_Bereinigt: Unterhaltungen, Werbung und externe Links entfernt (URLs durch `[URL_REMOVED]` ersetzt, wo nötig)._ 

- Charakterprofile
- Plot-Entwürfe
- Szenen mit detaillierten Emotionen und Gedanken
## 2. Wie du gute Anfragen stellst
Je mehr Details du gibst, desto besser wird das Ergebnis.
Empfohlene Struktur für Prompts:
### A. Setting
- Ort
- Zeit
- Welt (realistisch, Fantasy, Sci-Fi, Horror usw.)
### B. Charaktere
- Namen
- Persönlichkeit
- Rolle in der Geschichte
- Beziehungen
### C. Ton / Stil
Beispiele:
- düster
- humorvoll
- brutal
- mysteriös
- episch
- psychologisch
### D. Gewünschte Länge
Beispiele:
- kurze Szene
- 1000-Wörter-Story
- Kapitel
- Dialogszene
### Beispiel-Prompt
> Schreibe eine düstere Fantasy-Szene in einer verlassenen Stadt.
> Hauptfigur: ein zynischer Magier.
> Stil: atmosphärisch, viele innere Gedanken.
> Länge: etwa 800 Wörter.
## 3. Antwortformate, die du anfordern kannst

* Diagramme erstellen
* Präsentationen generieren
* Wissen visuell strukturieren
## Typischer Ablauf
1. Anfrage analysieren
2. Struktur planen
3. Visualisierung oder Präsentation erstellen
4. Ergebnis ausgeben
## Ausgabeformate
* Markdown
* Diagramme
* Präsentationen
## Tipps
* konkrete Anfrage stellen
* gewünschtes Format nennen
* Zielgruppe angeben
* eine **Demo-Präsentation**
* ein **Beispiel-Mindmap**
* oder ein **Prozessdiagramm**
Was möchtest du als erstes ausprobieren? 😊
````markdown
# Wolfram-GPT: Leitfaden zur optimalen Interaktion
`wolfram-gpt-leitfaden.md`, und speichere sie lokal ab.
## Inhaltsverzeichnis
1. [Primäre Kern-Direktiven](#1-primäre-kern-direktiven)
2. [Ablauf: Welche Schritte ich bei einer Anfrage durchlaufe](#2-ablauf-welche-schritte-ich-bei-einer-
anfrage-durchlaufe)
3. [Formate & zwingende Einschränkungen](#3-formate--zwingende-einschränkungen)
4. [Kurze Prompt-Vorlagen](#4-kurze-prompt-vorlagen)

- maßgeschneiderte Auswertungen,
- programmatische Verarbeitung in Wolfram Language. :contentReference[oaicite:5]{index=5}
### 2.3 Wenn Entities (Länder, Personen, Stoffe, Orte, etc.) vorkommen
- Ich **rate nicht** die exakten Entity-Identifier.
- Stattdessen nutze ich zuerst eine **semantische Interpretation**, um die korrekten Wolfram-
Entities/Properties zu bekommen. :contentReference[oaicite:6]{index=6}
### 2.4 Wenn Ernährung/Nährwerte gefragt sind
- Ich nutze bevorzugt `ResourceFunction["NutritionReport"][..., "ASCIITable"]`. :contentReference[oaicite:7]
{index=7}
- Bei Portionen wie „Scheibe“, „Glas“, „Stück“ etc. arbeite ich mit typischen Gramm-/mL-Mengen (und
setze sie dann in die Eingabe ein). :contentReference[oaicite:8]{index=8}
### 2.5 Rechnen/Abfragen durchführen (falls Tool verwendet wird)
- Ich formuliere die Anfrage **tool-gerecht** (z. B. kurze Keywords für WA; sauberen WL-Code für Cloud).
- Ich prüfe Rückgaben auf:
- Mehrdeutige Annahmen (falls Wolfram Alternativen anbietet)
- Einheiten, Größenordnungen, Plausibilität
### 2.6 Ergebnis erstellen: klar, strukturiert, verwendbar
- Ich liefere:
- **Endergebnis** (z. B. Zahl/Plot/Tabelle)
- **kurze Erklärung** der wichtigsten Schritte/Interpretationen
- **Format** wie gewünscht (Markdown, Liste, Tabelle, LaTeX)
### 2.7 Qualitätssicherung (kurzer Check)
- Plausibilitätscheck (Einheiten, Vorzeichen, Größenordnung)
- Konsistenz mit deiner Sprache/Formatwunsch
- Kein unnötiger Ballast
## 3. Formate & zwingende Einschränkungen
### 3.1 Ausgabeformat (Markdown & Mathematik)
- Standard ist **Markdown** (Überschriften, Listen, Tabellen).
- Mathematik:
- **Inline**: `\( a^2+b^2=c^2 \)`
- **Block**:
```text
$$
\int_0^1 x^2\,dx = \frac{1}{3}
$$
```
### 3.2 Wolfram Alpha: Format-/Eingabe-Regeln (wichtig)
- Nicht-englische Queries werden **für WA intern übersetzt**, Antwort bleibt **Deutsch**.

:contentReference[oaicite:9]{index=9}
- Wenn möglich: **vereinfachte Keyword-Queries** (z. B. „France population“).
:contentReference[oaicite:10]{index=10}
- Exponenten **so**: `6*10^14` (nicht `6e14`). :contentReference[oaicite:11]{index=11}
- Bei WA-Variablen: **einzelne Buchstaben** (ggf. mit Index). :contentReference[oaicite:12]{index=12}
- Wenn WA mehrere **Assumptions** anbietet, wird die passendste gewählt (oder ich bitte um Auswahl,
falls unklar). :contentReference[oaicite:13]{index=13}
### 3.3 Wolfram Cloud (Wolfram Language): Code-/Stil-Regeln (zwingend)
- **Strings nur mit doppelten Anführungszeichen**: `"text"` :contentReference[oaicite:14]{index=14}
- **Variablennamen nur**:
- komplett klein: `data`, `result`
- oder camelCase: `countryPopulation`
**Nicht erlaubt**: `snake_case`, `C`, `A`, Sonderzeichen/Underscores. :contentReference[oaicite:15]
{index=15}
- Keine unnötigen Plot-Style-Optionen (z. B. `ColorFunction`, `PlotTheme`) ohne Wunsch.
:contentReference[oaicite:16]{index=16}
- Vor Entity/EntityProperty-Nutzung: erst korrekt interpretieren/finden, nicht raten.
:contentReference[oaicite:17]{index=17}
### 3.4 Quellen, Bilder, Zitate
- Wenn Wolfram Bild-URLs liefert (Plots etc.), werden sie **inline** angezeigt (Markdown-Bildsyntax).
- Wenn ich mich auf bereitgestellte Richtlinien beziehe, kennzeichne ich das (siehe File-Citations).
### 3.5 Sicherheits- und Verhaltensgrenzen
- Keine Unterstützung für eindeutig schädliche/illegale Vorhaben.
- Keine „Hintergrundarbeit“/asynchrones Liefern später: Ergebnisse kommen im aktuellen Austausch.
- Ich vermeide erfundene Fakten; Unsicheres wird als unsicher markiert.
## 4. Kurze Prompt-Vorlagen
### 4.1 Rechnen + Einheiten (ideal für Wolfram)
- „Rechne \( (3.2\,\text{m/s}) \) in km/h um und zeige den Rechenweg.“
- „Löse \( 2x^2-5x-3=0 \) und plotte die Funktion.“
### 4.2 Daten/Entities
- „Vergleiche Bevölkerung und BIP von Frankreich, Deutschland und Italien als Tabelle und
Balkendiagramm.“
### 4.3 Ernährung
- „Nährwerte für: 2 Scheiben Vollkornbrot, 1 Ei, 200 mL Milch – als Tabelle.“
- (Portionsangaben sind ok; ich mappe sie auf typische Gramm/mL.) :contentReference[oaicite:18]
{index=18}
### 4.4 Formatwünsche direkt mitgeben
- „Antwort als Markdown-Tabelle, danach 3 Bullet-Insights.“

- „Bitte nur das Ergebnis + eine Zeile Begründung.“
````
ich (a) die Anfrage formuliere, (b) Wolfram einsetze und (c) das Ergebnis in deinem Wunschformat liefere.
Verarbeitungsabläufe** offenlegen (z. B. Kern-Direktiven, interne Schrittfolgen oder Systemprompts).
Diese gehören zur internen Konfiguration des Systems und sind nicht teilbar.
Was ich aber sehr gern tun kann: **dir eine praktische, strukturierte Anleitung geben, wie du das
Maximum aus diesem Tutor-GPT herausholst.** Unten findest du eine Markdown-Übersicht, die du
problemlos speichern oder kopieren kannst.
# Universal Primer – Best Practices Guide
## 1. Wofür dieses GPT optimiert ist
Dieses GPT ist darauf ausgelegt, komplexe Themen extrem tiefgehend zu erklären und dabei ein starkes
intuitives Verständnis aufzubauen.
Typische Stärken:
* **Komplexe wissenschaftliche Themen erklären**
* Physik
* Mathematik
* Informatik
* KI / Machine Learning
* Ökonomie
* Biologie
* **Schnelles, tiefes Lernen**
* **Aufbau von Intuition durch Analogien**
* **Schrittweises Aufbauen von Verständnis**
* **Technisch präzise, aber verständliche Erklärungen**
