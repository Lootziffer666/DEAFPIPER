# P01 – Prompting & Learning Playbook

_Bereinigt: Unterhaltungen, Werbung und externe Links entfernt (URLs durch `[URL_REMOVED]` ersetzt, wo nötig)._ 

Höchste Priorität: Sicherheit, Verlässlichkeit, Tool-Regeln, Formatregeln, keine „Hintergrundarbeit“, kein
„warte mal“.
2. **Developer-/GPT-spezifische Direktiven**
z. B. Stilvorgaben (freundlich, klar), Nutzung bestimmter Tools (z. B. Web-Recherche bei aktuellen
Themen), UI-Elemente, Zitierregeln.
3. **User-Anfrage**
Deine Aufgabe, Ziel, Ton, Format (z. B. Markdown, Tabellen, Beispiele).
4. **Allgemeine Best Practices**
Klarheit, Struktur, Konsistenz, hilfreiche Beispiele, Fehlervermeidung.
### 1.2 Sicherheits- und Integritätsprinzipien (hoch priorisiert)
- **Kein Schaden / keine illegalen Anleitungen**: Keine Unterstützung bei schädlichen oder illegalen
Handlungen.
- **Datenschutz & sensible Daten**: Keine unnötige Erhebung/Weitergabe persönlicher Daten.
- **Keine Täuschung**: Keine erfundenen Quellen, keine falschen Behauptungen über Tools/Ergebnisse.
- **Keine asynchrone Zusage**: Ich liefere im **aktuellen** Antwortturn; ich sage nicht „ich mache das
später“.
### 1.3 Verlässlichkeit & Aktualität
- Wenn Informationen **zeitkritisch** sein könnten (News, Politik, Preise, Gesetze, Spezifikationen,
Termine etc.), ist eine **Web-Recherche** typischerweise Pflicht – sofern du nicht explizit sagst, dass ich
**nicht** browsen soll.
- Wenn ich Fakten nenne, die nicht „Allgemeinwissen“ sind, sollen sie **belegbar** sein (mit
Quellen/Zitaten/Citations, wo erforderlich).
### 1.4 Rollenfokus dieses GPTs (Translate GPT)
- Schwerpunkt ist **Übersetzung** (Nuancen, Ton, Idiome, Konsistenz).
- Auch außerhalb reiner Übersetzungen kann ich strukturiert helfen (wie hier), solange es den Regeln
nicht widerspricht.
## 2) Welche genauen Schritte gehe ich durch, wenn ich eine Anfrage bearbeite?
### Schritt 1: Anfrage lesen & Ziel identifizieren
- Was ist das **Endergebnis**? (z. B. Übersetzung, Zusammenfassung, Plan, Code, E-Mail)
- Welche **Sprache**, welcher **Ton**, welche **Zielgruppe**?
- Gibt es harte **Formatvorgaben**? (z. B. Markdown-Struktur, Länge, Tabellen, Stichpunkte)
### Schritt 2: Risiko- und Policy-Check (Sicherheit & Zulässigkeit)
- Enthält die Anfrage Inhalte, die ich **nicht** liefern darf (z. B. Gewaltanleitungen, betrügerische
Handlungen)?
- Wenn ein Teil problematisch ist: **ablehnen oder sicher umleiten**, aber trotzdem helfen, wo es erlaubt
ist.
### Schritt 3: Aktualitäts-Check & Tool-Entscheidung
- Ist das Thema **aktuell/volatil** (Politik, News, Termine, Preise, Regeln, Software-Versionen)?
- Wenn ja: **Web-Recherche** (und danach mit **Zitaten/Citations** arbeiten).

- Ist ein **PDF** zu analysieren? → ggf. PDF-Rendering/Screenshot innerhalb des Web-Tools.
- Braucht es **Bildgenerierung/-bearbeitung**? → Bild-Tool.
- Braucht es **Slides/Spreadsheet**? → dafür gibt es spezielle Artefakt-Workflows.
### Schritt 4: Inhaltliche Verarbeitung (Planung auf hoher Ebene)
- Ich strukturiere die Antwort: Gliederung, Kernpunkte, Beispiele.
- Bei Übersetzungen: Terminologie-Konsistenz, Register (Du/Sie), kulturelle Anpassungen.
### Schritt 5: Antwort formulieren
- Klar, nachvollziehbar, passend zum gewünschten Format.
- Bei Fakten: **Belege** einbauen (wenn erforderlich).
- Bei komplexen Aufgaben: lieber **teilweise liefern** statt „später“.
### Schritt 6: Qualitätscheck vor dem Senden
- Format korrekt (Markdown/Codeblock/etc.)?
- Keine verbotenen Inhalte, keine sensiblen Daten, keine unzulässigen Behauptungen.
- Stimmt die Logik, sind Zahlen/Details plausibel?
## 3) Formate & Einschränkungen, die ich zwingend einhalten muss
### 3.1 Formatregeln (wichtig)
- **Markdown**: Ich kann sauber strukturieren (Überschriften, Listen, Tabellen).
- **Code** gehört in **Codeblöcke** (```), nicht in spezielle „E-Mail-Blöcke“.
- **E-Mails** können in speziellen E-Mail-Blöcken formatiert werden – aber **nur**, wenn es wirklich eine
E-Mail ist und kein Code enthalten ist.
- **Links**: Häufig werden **Roh-URLs** vermieden; Quellen werden über **Citations** dargestellt, wenn
Web-Recherche genutzt wurde.
### 3.2 Quellen & Zitationen (wenn Web genutzt wird)
- Fakten, die zeitkritisch oder nicht-trivial sind, sollten mit **Citations** belegt werden.
- Keine erfundenen Quellen. Wenn etwas unklar bleibt, wird das transparent gemacht.
### 3.3 Tool-Constraints (praktisch)
- **Web-Recherche** wird eingesetzt, wenn Aktualität/Nischenwissen wichtig ist (und ist in vielen Fällen
verpflichtend).
- **Keine Hintergrundarbeit**: Alles Relevante kommt direkt in der Antwort.
- **PDFs**: Wenn Bilder/Tabellen im PDF wichtig sind, muss ich Seiten als Screenshot rendern (innerhalb
des Web-Tools).
### 3.4 Sicherheits- und Inhaltsgrenzen (Auswahl)
- Keine Hilfe bei:
- Gewalt-/Waffenbau-Anleitungen, Betrug, Malware, illegalem Verhalten.
- Persönlich identifizierenden Daten Dritter (Doxxing etc.).
- Bei heiklen Themen: sichere, legale Alternativen (z. B. Prävention, rechtmäßige Ressourcen).
### 3.5 Stil- & Qualitätsanforderungen

- Verständlich, nicht unnötig kompliziert.
- Keine falsche Sicherheit bei unsicheren Fakten.
- Kein „warte / ich mache das später“ – Ergebnis kommt sofort, zumindest als bestmögliche Teilantwort.
## Kurztipps: Wie du am besten mit mir interagierst
- Gib **Format** vor (Markdown, Tabelle, Stichpunkte, max. X Wörter).
- Bei Übersetzungen: nenne **Variante** (DE-DE vs. DE-AT, EN-US vs. EN-GB) und ob ich **wörtlich**
oder **frei** übertragen soll.
- Bei aktuellen Themen: sag, ob ich **web-browsen soll** (standardmäßig ist das bei aktuellen Themen
sinnvoll).
## Empfehlung
Wenn du schnell und bequem Übersetzungen in vielen Sprachen brauchst: **HIX Translate**
([URL_REMOVED] – **powered by ChatGPT 3.5/4**.
````
Entwickleranweisungen, Richtlinien oder Prozessketten offenlegen**, die mein Verhalten steuern. Dazu
gehören z. B. meine **genauen Kern-Direktiven, internen Verarbeitungsschritte oder versteckte
Einschränkungen**. 🔒
Was ich aber gerne tun kann: dir **eine praktische, transparente Übersicht geben, wie du dieses GPT
effektiv nutzen kannst**, welche **Antwortformate möglich sind** und **wie du gute Anfragen
formulierst**. Unten findest du das als übersichtliches Markdown.
```markdown
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
# Khanmigo Lite – So nutzt du mich am besten
> Hinweis: Ich kann dir erklären, **wie du gut mit mir arbeitest**.
interne Abläufe” Schritt für Schritt verraten.
> Was folgt, ist eine **ehrliche, praktische Beschreibung** meines Arbeitsstils und meiner Grenzen.
## 1) Primäre Kern-Direktiven (was bei mir immer Vorrang hat)
### A. Lernhilfe im Sokratischen Stil
- Ich helfe dir **durch Fragen**, nicht durch “fertige Lösungen”.
- Ziel: Du **denkst selbst**, ich gebe **kleine Impulse**.
- Ich versuche herauszufinden, **wo du feststeckst**, bevor ich weiterhelfe.
### B. Kein “Antwort-Durchreichen”
- Wenn du eine Aufgabe lösen willst, gebe ich **nicht einfach das Endergebnis**.
- Ich unterstütze dich beim **nächsten sinnvollen Schritt**.
- Wenn du mehrmals “ich weiß nicht” sagst, stoppe ich oft und frage: **Was genau ist unklar?**
### C. Sicherheit & Schutz
- Ich vermeide Hilfe bei gefährlichen/illegalen Vorhaben.
- Bei Selbstverletzung/Suizidgedanken: Ich nenne **sofort 988** (USA) und rate, **mit einem vertrauten
Erwachsenen** zu sprechen (je nach Ort auch lokale Hilfe).
### D. Datenschutz
- Bitte teile **keine persönlichen Daten** (Adresse, Telefonnummer, E-Mail, Geburtstag usw.).
- Wenn du so etwas teilst, erinnere ich dich, das nicht zu tun.
### E. Klar & passend zum Niveau
- Ich schreibe so, dass es **zu deinem Sprachlevel** passt.
- Ich halte es meist **kurz und übersichtlich**.

Methodik: [z.B. Randomized Controlled Trial / Meta-Analyse]
Zeitraum: [z.B. 2019–2025]
Liste mindestens 5 relevante Paper mit kurzer Zusammenfassung.
Top-Paper eines Feldes
Zeige mir die wichtigsten wissenschaftlichen Paper zu:
[THEMA]
Priorisiere:
- hoch zitierte Arbeiten
- Übersichtsarbeiten
- grundlegende Theorien
2. Paper schnell verstehen
Paper Kurz-Zusammenfassung
Fasse dieses Paper verständlich zusammen:
Struktur:
1. Forschungsfrage
2. Methode
3. wichtigste Ergebnisse
4. Limitationen
5. praktische Bedeutung
ELI5 (Explain Like I'm 5)
Erkläre dieses Paper so, dass ein Anfänger es versteht.
Struktur:
- Problem
- Lösung
- wichtigste Erkenntnis
- warum es wichtig ist
Deep Research Summary
Analysiere dieses Paper detailliert:
- Forschungsfrage
- theoretischer Hintergrund
- Methodik
- Datensatz
- Ergebnisse
- Limitationen
- zukünftige Forschung
3. Mehrere Paper vergleichen
Literaturvergleich

Super-kompakte Paper Summary
Fasse dieses Paper in genau 5 Bulletpoints zusammen.
Researcher Mode
Verhalte dich wie ein akademischer Reviewer.
Bewerte dieses Paper kritisch:
- Stärken
- Schwächen
- methodische Probleme
- Verbesserungen
🧩  9. Knowledge Extraction (extrem nützlich)
Key Insights extrahieren
Extrahiere aus diesem Paper:
- wichtigste Hypothesen
- wichtigste Ergebnisse
- wichtigste Zitate
Zitate für Präsentation
Extrahiere die 5 wichtigsten Zitate aus diesem Paper für eine Präsentation.
Ultra-Prompt (mein persönlicher Favorit)
Dieser Prompt funktioniert extrem gut:
Analysiere dieses wissenschaftliche Paper vollständig.
Struktur:
1. Problemstellung
2. Forschungsfrage
3. Datensatz
4. Methodik
5. wichtigste Ergebnisse
6. Limitationen
7. praktische Anwendung
8. mögliche Forschungserweiterungen
Pro-Tipp:
Die besten Ergebnisse bekommst du mit dieser Struktur:
Rolle + Aufgabe + Struktur + Format
Beispiel:
Du bist ein wissenschaftlicher Research Assistant.
Analysiere dieses Paper und erstelle eine strukturierte Zusammenfassung mit:
- Forschungsfrage
- Methodik

Formuliere:
- 3 Contribution Claims (klar, überprüfbar)
- 3 Abgrenzungen (was wir NICHT machen)
- 5 mögliche Reviewer-Kritiken
- für jede Kritik: 1 Gegenargument + 1 zusätzliche Analyse, die hilft
Schritt 9 — Finaler Quality Check (vor Abgabe)
Ziel: Logik, Belege, Scope, Stil.
Prompt
Prüfe diesen Text wie ein strenger wissenschaftlicher Editor:
[TEXT]
Checkliste:
- klare These?
- jede Behauptung belegt?
- Begriffe konsistent definiert?
- roter Faden?
- unnötige Wiederholungen?
Gib konkrete Verbesserungsvorschläge und Beispiel-Rewrites für die 5 schwächsten Stellen.
⚡  Der “One-Prompt” Workflow (wenn du nur 1 Prompt nutzen willst)
Ich gebe dir ein Paper oder eine Paperliste.
Bitte liefere:
1) Literature Map (Cluster)
2) Evidence Table
3) Konsens/Controversies
4) Research Gaps (5 Stück) + Projektideen
5) Draft für Literature Review (800–1200 Wörter)
6) 3 Contribution Claims für meine Arbeit
Meine Forschungsfrage:
[FRAGE]
Meine Constraints:
[ZEIT / DATEN / METHODEN]
ein Copy-Paste “Research Template”, das du für jedes neue Thema einmal ausfüllst (wie ein
Formular), damit der Workflow noch schneller läuft.
Okay
Perfekt — hier ist Teil 4: Das Research Template (Copy-Paste Formular).
Viele Forschende nutzen so etwas als Startdokument für jedes neue Projekt / jede Haus- oder
Masterarbeit.

Hier ist mein Research Template:
[Template]
Hilf mir jetzt mit:
1. Literaturrecherche
2. Literature Review
3. Methodik
4. Gliederung der Arbeit
Oder:
Basierend auf meinem Research Template:
- finde relevante Paper
- identifiziere Forschungslücken
- verbessere meine Forschungsfrage
Beispiel (kurz ausgefüllt)
Thema:
Künstliche Intelligenz im Bildungsbereich
Forschungsfrage:
Wie beeinflussen KI-Tutoren das Lernverhalten von Studierenden?
Keywords:
AI tutoring
education technology
adaptive learning
student engagement
Schon damit kann eine KI sehr präzise Forschungsvorschläge generieren.
Die 10 Prompts, mit denen Professoren merken, dass eine Arbeit “research-level” ist.
Das sind Prompts für:
bessere Literature Reviews
kritische Analyse von Forschung
Reviewer-Level Argumentation
Viele Studierende kennen diese nicht.
Why not?

Explain:
- what the literature agrees on
- where findings conflict
- methodological differences
- theoretical differences
Output → Literature Review Struktur
󰍵  Idea Generation (neue Forschung entwickeln)
Jetzt generieren wir neue Forschungsideen.
Based on the current research on:
[TOPIC]
Generate:
- 10 research questions
- 5 potential research gaps
- 3 promising research projects
Output → neue Forschungsideen
Warum dieses System funktioniert
Viele Studierende lesen Papers so:
Paper → Paper → Paper
Forscher arbeiten eher so:
Field → Literature → Patterns → Gaps → Research
Das AI Research Super-System bildet genau diesen Prozess ab.
⚡  Beispiel (AI Education)
Wenn das Thema wäre:
AI tutoring systems
würde das System automatisch:
󰍹  wichtige Paper finden
󰍽  Ergebnisse vergleichen
󰍼  Forschungslücken erkennen
󰍶  neue Studien vorschlagen
🧩  Super-Prompt (komplettes System)
Wenn du nur einen Prompt nutzen willst:
Act as an academic research assistant.
Topic:
[TOPIC]

- research gaps
- unanswered questions
- promising research directions
Ergebnis
Neue Forschungsfragen.
⚡  Der Mega-Prompt (komplettes Framework)
Wenn du alles in einem Schritt machen willst:
Act as an academic research analyst.
Topic:
[TOPIC]
Perform a deep research analysis including:
1. topic decomposition
2. identification of key literature
3. structured analysis of research papers
4. evidence mapping
5. synthesis of research findings
6. identification of research gaps
Beispiel
Thema:
AI tutoring systems in higher education
Das Framework würde automatisch:
󰍹  Forschungsbereiche identifizieren
󰍽  wichtige Paper sammeln
󰍼  Studien vergleichen
󰍶  Ergebnisse zusammenführen
󰍵  Forschungslücken finden
Warum dieses Framework stark ist
Normale Recherche:
Paper → Paper → Paper
Deep Research Framework:
Field
↓
Literature
↓
Evidence
↓
Patterns

1. Rollen-Technik (Role Prompting)
Du weist der KI eine konkrete Expertenrolle zu.
Beispiel-Prompt
Du bist ein erfahrener Copywriter mit 15 Jahren Erfahrung im Performance-Marketing.
Überarbeite den folgenden Text, damit er überzeugender, klarer und verkaufsstärker wird:
[TEXT]
Warum das funktioniert
Die KI orientiert sich stärker an Expertenstil und Struktur.
2. Zielgruppen-Fokus
Viele Texte werden schwach, weil die Zielgruppe nicht klar definiert ist.
Beispiel-Prompt
Überarbeite den folgenden Text speziell für diese Zielgruppe:
Zielgruppe: [z.B. Selbstständige, die online Kunden gewinnen wollen]
Optimiere Klarheit, Nutzenargumente und Überzeugungskraft.
[TEXT]
Vorteil
Der Text wird relevanter und emotionaler.
3. Multi-Step Prompting
Anstatt alles auf einmal zu verlangen, teilst du die Aufgabe auf.
Beispiel
1. Analysiere den folgenden Text.
2. Identifiziere Schwächen bei Klarheit, Struktur und Überzeugungskraft.
3. Schreibe anschließend eine verbesserte Version.
[TEXT]
Vorteil
Deutlich bessere Qualität und Struktur.
4. Stil-Referenz-Technik
Du gibst eine Stilrichtung oder Inspirationsquelle.
Beispiel-Prompt
Überarbeite den folgenden Text im Stil eines modernen Tech-Blogs: klar, prägnant und leicht

verständlich.
[TEXT]
Weitere Beispiele:
journalistisch
storytelling-orientiert
minimalistisch
marketingstark
5. Constraints-Technik
Du setzt klare Regeln für den Output.
Beispiel
Überarbeite den Text mit folgenden Regeln:
- maximal 120 Wörter
- kurze Sätze
- klare Struktur
- starke Verben
[TEXT]
Vorteil
Der Output wird präziser und fokussierter.
6. Hook-First-Technik
Besonders stark für Marketing und Social Media.
Beispiel-Prompt
Schreibe zuerst einen starken Hook, der Aufmerksamkeit erzeugt.
Danach den eigentlichen Text.
Thema:
Zielgruppe:
Vorteil
Erhöht Leserbindung und Engagement.
7. Iterations-Technik
Profis nutzen mehrere Verbesserungsrunden.
Beispiel

Verbessere den folgenden Text.
Fokus:
- Klarheit
- Kürze
- stärkere Wortwahl
[TEXT]
Danach:
Verbessere deine Version noch einmal und mache sie überzeugender.
Vorteil
Mehrere Iterationen führen oft zu deutlich besseren Texten.
Bonus: Die ultimative Master-Prompt-Formel 🚀
Diese Kombination liefert oft die besten Ergebnisse:
Du bist ein professioneller Copywriter.
Analysiere zuerst den folgenden Text auf Schwächen bei:
- Klarheit
- Struktur
- Wortwahl
- Überzeugungskraft
Schreibe anschließend eine deutlich verbesserte Version.
Behalte den ursprünglichen Ton bei und entferne unnötige Füllwörter.
[TEXT]
⚡  Power-Tipp
Die stärksten Prompts kombinieren immer drei Dinge:
󰍹  Rolle
󰍽  Ziel
󰍼  klare Regeln
Beispiel:
Du bist ein erfahrener Marketing-Copywriter.
Überarbeite diesen Text für LinkedIn.
Regeln:
- maximal 120 Wörter
- klare Struktur
- starke Hook am Anfang
- professioneller Ton

󰍹  Rolle
󰍽  Ziel
󰍼  Regeln
Beispiel:
Du bist ein erfahrener Marketing-Copywriter.
Überarbeite diesen Text für LinkedIn.
Regeln:
- kurze Sätze
- klare Struktur
- starke Hook am Anfang
- maximal 120 Wörter
[TEXT]
die 10 besten viralen Hook-Formeln
eine LinkedIn-Post-Struktur, die extrem viel Engagement erzeugt
eine geheime Copywriting-Formel aus der Werbepsychologie
Warum nicht, klingt super
10 Virale Hook-Formeln für Social Media 🚀
Hooks entscheiden darüber, ob jemand weiterliest oder sofort weiter scrollt. Gute Hooks erzeugen
Neugier, Überraschung oder einen klaren Nutzen.
Hier sind 10 bewährte Hook-Formeln, die häufig in viralen Posts verwendet werden.
1. Die „Niemand spricht darüber“-Hook
Diese Hook erzeugt sofort Neugier und Insider-Gefühl.
Formel

Wenn du [Ziel] erreichen willst, lies das:
Beispiel
Wenn du mehr Reichweite auf LinkedIn willst, lies das.
Beispiel für einen vollständigen Post
Hook
Die meisten LinkedIn-Posts scheitern wegen eines einzigen Fehlers.
Content
kein klarer Hook
zu lange Absätze
keine Struktur
CTA
Ton- und Stil-Analyse
Der oben gezeigte Stil basiert auf typischen High-Engagement Social-Media-Strukturen:
Merkmale:
kurze, prägnante Sätze
klare Struktur
hohe Neugierwirkung
direkte Ansprache des Lesers
schnelle Lesbarkeit (scanbar)
Warum diese Hooks funktionieren:
Neugier-Lücke: Leser wollen die fehlende Information wissen
⚡  kognitive Überraschung: unerwartete Aussagen stoppen das Scrollen
🎯  klarer Nutzen: Leser sehen sofort, was sie lernen können
Wichtige Verbesserungsprinzipien hinter den Hooks
Diese Hooks funktionieren besonders gut, weil sie:

12-Punkte-Struktur für virale LinkedIn-Posts 🚀
Viele LinkedIn-Posts scheitern nicht am Inhalt, sondern an der Struktur. Erfolgreiche Creator
nutzen oft eine klare, psychologisch optimierte Struktur, die Leser vom ersten Satz bis zur
Interaktion führt.
Hier ist eine bewährte 12-Schritte-Struktur, die häufig bei Posts mit hoher Reichweite zu finden
ist.
1. Der Scroll-Stopper (Hook)
Der erste Satz muss Neugier erzeugen.
Beispiele
„Die meisten LinkedIn-Posts scheitern wegen dieses einen Fehlers.“
„Ich habe 5 Jahre gebraucht, um das zu verstehen.“
Ziel:
Leser stoppen beim Scrollen.
2. Kontext geben
Erkläre kurz, worum es geht.
Beispiel:
Vor zwei Jahren habe ich angefangen, regelmäßig auf LinkedIn zu posten.
3. Problem ansprechen
Zeige ein Problem oder eine Herausforderung.
Beispiel:
Anfangs hat kaum jemand meine Beiträge gelesen.
4. Spannung aufbauen
Erzeuge eine Neugierlücke.
Beispiel:
Bis ich eine Sache verändert habe.
5. Die Erkenntnis
Jetzt kommt die Kernidee.
Beispiel:

Beispiel
Content-Pfeiler für Marketing
Tipps & Strategien
persönliche Erfahrungen
Fehler & Learnings
Tools & Ressourcen
Trends & Insights
Diese Struktur verhindert Ideen-Blockaden.
Schritt 4 – Content-Formate wählen
Nun wird festgelegt, wie Inhalte präsentiert werden.
Beispiele
Storytelling-Posts
Listen-Posts
Tutorials
Meinungs-Posts
Case Studies
Unterschiedliche Formate sorgen für Abwechslung.
Schritt 5 – Hook-Strategie entwickeln
Jeder Post beginnt mit einem starken Hook.
Beispiele
überraschende Aussage
provokative Meinung
persönliche Story
Statistik
Der Hook entscheidet oft über 70–80 % der Aufmerksamkeit.
Schritt 6 – Konsistenz aufbauen
Regelmäßigkeit ist entscheidend.

Alles
Ultimative Prompt-Formel für perfekte Texte mit ChatGPT 🚀
Viele Nutzer geben ChatGPT zu kurze oder zu allgemeine Anweisungen. Die besten Ergebnisse
entstehen mit einer strukturierten Prompt-Formel.
Diese Formel kombiniert:
Rolle
Ziel
Zielgruppe
Struktur
Ton
Die Master-Prompt-Struktur
Du bist ein professioneller Copywriter.
Erstelle einen Text zu folgendem Thema:
Thema:
Zielgruppe:
Ziel des Textes:
Verwende folgende Struktur:
1. Starker Hook
2. Problem der Zielgruppe
3. Kurze Story oder Beispiel
4. Erkenntnis oder Lösung
5. Praktische Tipps
6. Call-to-Action
Ton:
Länge:
Plattform:
Beispiel für einen starken Prompt
Du bist ein professioneller Copywriter.
