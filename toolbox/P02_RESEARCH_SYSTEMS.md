# P02 – Research Systems (SSOT)

Ziel: Stage 02 (Research & Validierung) maximal schnell und reproduzierbar machen.

## Output-Contracts (Pipeline)
- Ergebnis in `templates/RESEARCH_BRIEF.json` überführen
- Claims mit Evidenz + Confidence markieren
- Entscheidung: Go / Pivot / Stop

---

## 50 Ultra-Power Prompts für Research (Copy/Paste)
1/3: 50 Ultra-Power-Prompts für Research (Copy-Paste)
(Platzhalter in [Klammern] ersetzen.)
A) Literaturrecherche & Paper-Finden (1–10)
Finde 10 peer-reviewed Paper zu [THEMA] (2019–heute). Gib Titel, Autoren, Jahr, Link, 2–3 Zeilen
Summary und warum relevant.
2. ```text
Finde die 5 meistzitierten Grundlagenarbeiten zu [THEMA] + 5 neueste Arbeiten. Erkläre die
Entwicklung des Feldes in 8 Sätzen.
Suche nach systematischen Reviews/Meta-Analysen zu [THEMA]. Liste die wichtigsten Ergebnisse +
Limitationen.
4. ```text
Finde Paper zu [THEMA] mit Methode [METHODE]. Filter: Datensatzgröße > [N], offene Daten
bevorzugt.
Finde konträre Positionen zu [THEMA]. Je 3 Paper pro Seite, mit Kernargumenten und Evidenz.
6. ```text
Finde Paper, die [BEGRIFF] definieren. Vergleiche Definitionen und schlage eine präzise
Arbeitsdefinition vor.
Finde “state of the art” Benchmarks zu [THEMA]. Welche Metriken und Datensätze sind Standard?
8. ```text
Finde 8 Paper zu [THEMA], aber nur aus Top-Venues/Journals: [LISTE]. Gib Begründung der Auswahl.
Erstelle eine Suchstrategie (Keywords + Synonyme + Boolean Strings) für [THEMA] für Google
Scholar/Scopus.
10. ```text
Identifiziere 10 zentrale Autor:innen/Labs zu [THEMA] und liste ihre 2 wichtigsten Arbeiten +
Themenfokus.
B) Paper schnell verstehen (11–20)
Fasse dieses Paper in 7 Bulletpoints zusammen: Problem, Ansatz, Daten, Methode, Ergebnis, Limitation,
Takeaway.
12. ```text
Gib mir eine 200-Wörter-Zusammenfassung + 5 “Key Claims” + 3 “Open Questions”.
Erkläre das Paper als: (a) Tweet-Thread mit 8 Tweets, (b) 1-Minuten Elevator Pitch, (c) Fachsummary.

14. ```text
Extrahiere: Forschungsfrage, Hypothesen, Variablen/Constructs, Operationalisierung, Hauptresultate.
Liste alle Abbildungen/Tabellen und erkläre, was jede beweist und wie sie zum Argument beiträgt.
16. ```text
Erkläre die Methodik wie für eine mündliche Prüfung: Schritte, Annahmen, typische Fehler, Validität.
Fasse die Diskussion zusammen: Claims vs. Evidenz vs. Spekulation. Markiere Unsicherheiten.
18. ```text
Was müsste wahr sein, damit die Schlussfolgerung falsch ist? Nenne 5 plausible Gegen-Erklärungen.
Erstelle ein Glossar mit 15 Fachbegriffen aus dem Paper + kurze Definitionen.
20. ```text
Gib mir 10 Fragen, die ich dem/der Autor:in stellen würde (Methodik, Daten, Robustheit,
Generalisierbarkeit).
C) Kritische Bewertung / Reviewer-Mode (21–30)
Agiere als Peer-Reviewer: Stärken, Schwächen, Major/Minor Revisions, und ein Gesamturteil
(accept/reject) mit Begründung.
22. ```text
Prüfe Kausalität: Identifikation, Confounder, Endogenität, Messfehler. Was fehlt für kausale Aussagen?
Bewerte Replizierbarkeit: Daten/Code verfügbar? Methodendetails? Welche Schritte sind unklar?
24. ```text
Robustness Check Liste: Nenne 10 Robustheitstests, die zu diesem Setup passen.
Validität: interne, externe, Konstrukt-, statistische Schlussvalidität. Gib je 2 konkrete Risiken.
26. ```text
Bias-Check: Auswahlbias, Publikationsbias, Reporting bias. Welche Hinweise gibt es im Paper?
Bewerte Metriken: Sind die Metriken passend? Welche Alternativen wären besser und warum?
28. ```text
Bewerte den Datensatz: Repräsentativität, Leakage, Label-Qualität, Missingness. Welche Risiken?
Schreibe einen “Rebuttal”: Wie würde das Autorenteam die stärksten Kritikpunkte entkräften?
30. ```text
Erstelle eine Fehlerliste: 10 Stellen, an denen Leser:innen das Paper missverstehen könnten +
Klarstellung.
D) Synthese & Vergleich mehrerer Quellen (31–40)
Vergleiche diese Paper: [PAPER A,B,C]. Matrix: Frage, Methode, Daten, Ergebnis, Limitation, Beitrag.
32. ```text
Erstelle eine Taxonomie der Ansätze zu [THEMA] (3–6 Kategorien) mit repräsentativen Papern.
Schreibe einen Literaturüberblick (800–1200 Wörter) zu [THEMA] mit rotem Faden und
Forschungsdebatten.
34. ```text

Identifiziere Forschungslücken aus [PAPERLISTE]. Gib 5 konkrete Gap→Projekt-Ideen.
Konfliktanalyse: Warum widersprechen sich Paper A und B? (Daten, Definitionen, Metriken, Kontext)
36. ```text
Evidence Map: Ordne Studien nach Evidenzstärke (Meta-Analyse, RCT, Beobachtung, Theorie) und
Ergebnisrichtung.
Schlage ein integriertes Modell/Framework vor, das die Erkenntnisse aus [PAPERLISTE] verbindet.
38. ```text
Erstelle eine “Related Work” Sektion (ca. 400–600 Wörter) für ein Paper zu [MEIN THEMA/BEITRAG].
Erstelle 10 Zitier-Sätze (paraphrasiert) aus diesen Papern, die ich in eine Arbeit einbauen kann.
40. ```text
Identifiziere 5 Kernvariablen/Constructs im Feld [THEMA] und wie sie typischerweise gemessen
werden.
E) Forschungsdesign, Thesis-Planung, Umsetzung (41–50)
Formuliere 5 präzise Forschungsfragen zu [THEMA] inkl. Motivation, Scope, erwarteter Beitrag.
42. ```text
Leite Hypothesen aus Theorie [THEORIE] ab und mappe sie auf messbare Variablen + erwartete
Richtung.
Schlage ein Studiendesign vor (Methode, Stichprobe, Messung, Analyseplan) für die Frage: [FRAGE].
44. ```text
Erstelle einen Analyseplan: Datenvorbereitung, Modelle, Metriken, Robustheit, Visualisierung,
Reporting.
Operationalisiere [CONSTRUCT] in 3 Varianten (stark/schwach/alternativ) + Vor-/Nachteile.
46. ```text
Erstelle ein Pre-Registration Outline (Hypothesen, Outcomes, Exklusionskriterien, Power, Analyse).
Power/Effect-Size Denkhilfe: Welche Effektgrößen sind plausibel? Welche Stichprobe wäre grob nötig?
48. ```text
Schreibe eine Gliederung für eine Masterarbeit zu [THEMA] inkl. Kapitelzielen und Deliverables pro
Kapitel.
Erstelle einen 6-Wochen-Arbeitsplan für [PROJEKT] mit Meilensteinen, Risiken und Fallbacks.
50. ```text
Übersetze mein Ergebnis in “Contribution Claims”: 3 klare Beiträge, Abgrenzung, und warum es neu ist.
Wenn du bereit bist: 2/3 wäre die komplette Masterarbeit-Prompt-Library (sehr praxisnah: von Topic →
Exposé → Methodik → Schreiben → Abgabe). Soll ich damit weitermachen?
Bitte
Perfekt — hier ist 2/3: Die komplette Masterarbeit-Prompt-Library.
Diese Prompts decken den gesamten Workflow einer Bachelor-, Master- oder Doktorarbeit ab.

🎓


---

## Paper-Analyse Prompt Engine (Research Workflow)
Paper-Analyse Prompt Engine (Research Workflow)
🧭 Phase 1 — Schnellverständnis (2 Minuten)
Goal: Sofort verstehen, worum es im Paper geht.
Analysiere dieses wissenschaftliche Paper und gib mir eine Ultra-Kurz-Zusammenfassung:
1. Forschungsproblem

2. Hauptidee des Ansatzes
3. wichtigste Ergebnisse
4. warum das Paper wichtig ist
Antwort in maximal 8 Bulletpoints.
📄 Phase 2 — Struktur des Papers verstehen
Extrahiere aus diesem Paper:
- Forschungsfrage
- Hypothesen
- Datensatz
- Methodik
- wichtigste Ergebnisse
- zentrale Schlussfolgerung
🧠 Phase 3 — Methodik verstehen
Erkläre die Methodik dieses Papers verständlich:
Struktur:
- Forschungsdesign
- Datenerhebung
- Analyseverfahren
- wichtige Annahmen
- mögliche Schwächen
📊 Phase 4 — Ergebnisse analysieren
Analysiere die Ergebnisse dieses Papers.
Erkläre:
- wichtigste Resultate
- wie stark die Evidenz ist
- mögliche alternative Erklärungen
⚖ Phase 5 — Kritische Bewertung (Reviewer Mode)
Verhalte dich wie ein Peer-Reviewer.
Bewerte dieses Paper:
- Stärken
- Schwächen
- methodische Probleme
- mögliche Bias
- Verbesserungsvorschläge
🔍 Phase 6 — Forschungslücken finden
Basierend auf diesem Paper:
Identifiziere mögliche Forschungslücken.
Erstelle:
- 5 neue Forschungsfragen
- 3 mögliche Anschlussstudien

🧩 Phase 7 — Wissen extrahieren
Extrahiere aus diesem Paper:
- wichtigste Erkenntnisse
- wichtigste Zitate
- wichtigste Konzepte
📚 Phase 8 — Verbindung zur Literatur
Ordne dieses Paper in die Forschung ein.
Analysiere:
- welche Theorie unterstützt wird
- welche früheren Studien bestätigt werden
- wo das Paper neu ist
🚀 Phase 9 — Anwendung verstehen
Welche praktischen Anwendungen ergeben sich aus diesem Paper?
Analysiere:
- reale Anwendungen
- mögliche Industrien
- gesellschaftliche Auswirkungen
🧪 Phase 10 — Reproduzierbarkeit
Bewerte die Reproduzierbarkeit dieses Papers.
Analysiere:
- Datenverfügbarkeit
- Codeverfügbarkeit
- Methodentransparenz
- mögliche Replikationsprobleme
⚡ Der 10-Minuten-Paper-Workflow
Dieser Prompt kombiniert alles:
Analysiere dieses wissenschaftliche Paper vollständig.
Struktur:
1. Problemstellung
2. Forschungsfrage
3. Datensatz
4. Methodik
5. wichtigste Ergebnisse
6. Limitationen
7. Beitrag zur Forschung
8. praktische Anwendungen
9. Forschungslücken
🧠 Researcher-Level Prompt (extrem stark)
Dieser Prompt ist besonders nützlich für Doktorarbeit, Forschung oder Paper Reviews.
Verhalte dich wie ein erfahrener akademischer Reviewer.

Analysiere dieses Paper kritisch:
1. Beitrag zur Forschung
2. Originalität
3. Methodische Qualität
4. Validität der Ergebnisse
5. Schwächen
6. Verbesserungsvorschläge
📊 Bonus: Paper-Vergleich-Engine
Vergleiche diese wissenschaftlichen Paper:
[PAPER 1]
[PAPER 2]
[PAPER 3]
Analysiere:
- Forschungsfrage
- Methodik
- Ergebnisse
- Unterschiede
- Gemeinsamkeiten
💡 Pro-Tipp (sehr mächtig):
Der beste Workflow ist:
󰍹 Paper hochladen
󰍽 Super-Paper Prompt verwenden
󰍼 Reviewer Prompt verwenden
󰍶 Research Gap Prompt verwenden
Damit verstehst du ein Paper meist besser als nach 2–3 Stunden normalem Lesen.
✅ Wenn du möchtest, kann ich dir noch etwas bauen, das viele Researcher extrem hilfreich finden:
🧠 Die 25 mächtigsten Prompts für KI-Research
📚 Eine komplette Prompt-Bibliothek für wissenschaftliches Schreiben
⚡ Ein „AI Research Workflow“, mit dem man Papers 10× schneller analysiert
Das ist der eigentliche „Hidden Workflow“ vieler KI-Forscher.
Ja, bitte einzeln, damit es nicht gekürzt wird
Perfekt 👍 Dann machen wir es wirklich Schritt für Schritt, damit nichts gekürzt wird.

Hier ist Teil 1: Die 25 mächtigsten Prompts für KI-Research.
🧠 Die 25 mächtigsten Prompts für KI-Research
Diese Prompts sind speziell für wissenschaftliche Forschung, Paper-Recherche und Wissensextraktion
optimiert.
󰍹 Research Landscape Prompt
Verstehen, wie ein Forschungsfeld aufgebaut ist.
Erkläre mir das Forschungsfeld:
[THEMA]
Struktur:
- wichtigste Forschungsbereiche
- zentrale Theorien
- wichtigste Paper
- aktuelle Trends
- offene Probleme
󰍽 State-of-the-Art Prompt
Was ist der aktuelle State of the Art in:
[THEMA]
Analysiere:
- wichtigste Methoden
- wichtigste Modelle
- führende Paper
- aktuelle Benchmarks
󰍼 Research Gap Finder
Basierend auf der aktuellen Forschung zu:
[THEMA]
Identifiziere:
- ungelöste Probleme
- widersprüchliche Ergebnisse
- mögliche Forschungslücken
󰍶 Paper Insight Extractor
Extrahiere aus diesem Paper:
- wichtigste Hypothesen
- wichtigste Erkenntnisse
- wichtigste Methoden
- wichtigste Zitate
󰍵 Literature Map Prompt
Erstelle eine Map der wichtigsten Paper zu:

[THEMA]
Gruppiere sie nach:
- Theorie
- Methodik
- Anwendungen
󰍻 Concept Explainer Prompt
Erkläre dieses Konzept wissenschaftlich und verständlich:
[KONZEPT]
Struktur:
- Definition
- Ursprung
- wichtigste Studien
- Anwendung
󰍺 Theory Builder Prompt
Basierend auf diesen Studien:
[PAPER]
Erstelle ein mögliches theoretisches Modell.
󰍴 Hypothesis Generator
Generiere 10 wissenschaftliche Hypothesen zu:
[THEMA]
󰍷 Study Design Prompt
Schlage ein Studiendesign vor für folgende Forschungsfrage:
[FORSCHUNGSFRAGE]
Enthalten:
- Methodik
- Datenerhebung
- Analyse
🔟 Academic Debate Prompt
Welche wissenschaftlichen Debatten gibt es zu:
[THEMA]
Analysiere:
- verschiedene Positionen
- wichtige Studien
1󰍹 Critical Thinking Prompt
Welche Annahmen liegen der Forschung zu:
[THEMA]

zugrunde?
1󰍽 Evidence Strength Prompt
Bewerte die Evidenz der Forschung zu:
[THEMA]
Kategorisiere Studien nach:
- starke Evidenz
- moderate Evidenz
- schwache Evidenz
1󰍼 Interdisciplinary Research Prompt
Welche Disziplinen beschäftigen sich mit:
[THEMA]
Und wie unterscheiden sich ihre Ansätze?
1󰍶 Research Trend Analysis
Welche Trends haben sich in der Forschung zu:
[THEMA]
in den letzten 10 Jahren entwickelt?
1󰍵 Key Research Questions Prompt
Was sind die wichtigsten offenen Forschungsfragen in:
[THEMA]?
1󰍻 Method Comparison Prompt
Vergleiche diese Forschungsmethoden:
[METHODE A]
[METHODE B]
1󰍺 Knowledge Extraction Prompt
Extrahiere aus diesen Papern:
- wichtigste Erkenntnisse
- zentrale Konzepte
1󰍴 Expert Perspective Prompt
Wenn du ein Experte für:
[THEMA]
wärst – welche Fragen würdest du untersuchen?
1󰍷 Paradigm Shift Prompt
Gab es Paradigmenwechsel in der Forschung zu:
[THEMA]?
2󰑣 Research Critique Prompt

Welche Schwächen hat die aktuelle Forschung zu:
[THEMA]?
2󰍹 Future Research Prompt
Welche Forschung wird in den nächsten 10 Jahren wichtig für:
[THEMA]?
2󰍽 Framework Builder Prompt
Erstelle ein konzeptionelles Framework für:
[THEMA]
2󰍼 Research Strategy Prompt
Wenn du eine Dissertation zu:
[THEMA]
schreiben würdest, welche Forschungsstrategie würdest du wählen?
2󰍶 Academic Reviewer Prompt
Verhalte dich wie ein Reviewer eines Top-Journals.
Bewerte die Forschung zu:
[THEMA]
2󰍵 Research Synthesis Prompt
Fasse den gesamten Forschungsstand zu:
[THEMA]
in einer strukturierten Analyse zusammen.
Wenn du möchtest, kommt als nächstes Teil 2 (sehr spannend):
⚡ Die komplette Prompt-Bibliothek für wissenschaftliches Schreiben
Damit kannst du z.B.:
Paper schreiben
Literature Reviews generieren
Dissertationen strukturieren
Abstracts erstellen
Journals vorbereiten
Soll ich mit Teil 2 weitermachen? 🚀

Ja
Perfekt 👍 Hier ist Teil 2: Die komplette Prompt-Bibliothek für wissenschaftliches Schreiben.
Diese Prompts helfen dir beim Schreiben von Papers, Essays, Literaturreviews, Abstracts und
wissenschaftlichen Kapiteln.
✍ Prompt-Bibliothek für wissenschaftliches Schreiben
󰍹 Abstract schreiben
Schreibe ein wissenschaftliches Abstract zu folgendem Thema:
[THEMA]
Struktur:
- Problem
- Methode
- wichtigste Ergebnisse
- Bedeutung der Ergebnisse
Maximal 200 Wörter.
󰍽 Einleitung schreiben
Schreibe eine wissenschaftliche Einleitung zu:
[THEMA]
Struktur:
- Problemstellung
- Bedeutung des Themas
- kurzer Überblick über Forschung
- Ziel der Arbeit
󰍼 Literature Review schreiben
Schreibe einen Literature Review zu:
[THEMA]
Struktur:
- wichtigste Forschungsrichtungen
- zentrale Studien
- aktuelle Debatten
- Forschungslücken
󰍶 Related Work Section
Schreibe eine Related-Work-Sektion für ein Paper zu:
[THEMA]
Vergleiche verschiedene Forschungsansätze und ihre Ergebnisse.
󰍵 Theorie-Kapitel
Schreibe einen wissenschaftlichen Abschnitt über die Theorie hinter:

[THEMA]
Struktur:
- Definition
- wichtige Modelle
- zentrale Studien
󰍻 Hypothesen formulieren
Formuliere wissenschaftliche Hypothesen zu:
[THEMA]
Erstelle mindestens 5 Hypothesen.
󰍺 Methodenkapitel schreiben
Schreibe ein Methodenkapitel für eine Studie zu:
[THEMA]
Inhalt:
- Forschungsdesign
- Datenerhebung
- Stichprobe
- Analyseverfahren
󰍴 Ergebnisse schreiben
Schreibe einen wissenschaftlichen Abschnitt über die Ergebnisse einer Studie.
Daten:
[ERGEBNISSE]
Struktur:
- wichtigste Ergebnisse
- statistische Interpretation
󰍷 Diskussion schreiben
Schreibe eine wissenschaftliche Diskussion basierend auf:
[ERGEBNISSE]
Struktur:
- Interpretation
- Vergleich mit Literatur
- Limitationen
- praktische Bedeutung
🔟 Fazit schreiben
Schreibe ein wissenschaftliches Fazit zu:
[THEMA]

Struktur:
- wichtigste Erkenntnisse
- Beitrag zur Forschung
- zukünftige Forschung
1󰍹 Argumentationsstruktur verbessern
Verbessere die Argumentationsstruktur dieses wissenschaftlichen Textes:
[TEXT]
1󰍽 Wissenschaftlichen Stil verbessern
Verbessere den akademischen Schreibstil dieses Textes:
[TEXT]
Achte auf:
- Klarheit
- präzise Sprache
- wissenschaftlichen Ton
1󰍼 Text kürzen
Kürze folgenden wissenschaftlichen Text um 40 %, ohne wichtige Informationen zu verlieren:
[TEXT]
1󰍶 Text erweitern
Erweitere diesen wissenschaftlichen Text und füge mehr Kontext und Literatur hinzu:
[TEXT]
1󰍵 Paraphrasieren (Plagiat vermeiden)
Paraphrasiere diesen wissenschaftlichen Text vollständig neu, ohne die Bedeutung zu verändern:
[TEXT]
1󰍻 Struktur verbessern
Verbessere die Struktur dieses wissenschaftlichen Kapitels:
[TEXT]
Erstelle klare Abschnitte und Übergänge.
1󰍺 Titel generieren
Generiere 10 mögliche wissenschaftliche Titel für eine Arbeit zu:
[THEMA]
1󰍴 Keywords generieren
Generiere 10 wissenschaftliche Keywords für ein Paper über:
[THEMA]
1󰍷 Paper-Outline erstellen
Erstelle eine vollständige Outline für ein wissenschaftliches Paper zu:
[THEMA]

Struktur:
- Abstract
- Introduction
- Related Work
- Methodology
- Results
- Discussion
- Conclusion
2󰑣 Reviewer-Feedback simulieren
Verhalte dich wie ein Reviewer eines wissenschaftlichen Journals.
Bewerte diesen Text:
[TEXT]
Analysiere:
- wissenschaftliche Qualität
- Argumentation
- mögliche Verbesserungen
⚡ Super-Prompt für komplette Paper
Dieser Prompt funktioniert extrem gut:
Hilf mir ein wissenschaftliches Paper zu schreiben.
Thema:
[THEMA]
Erstelle:
1. Abstract
2. Introduction
3. Literature Review
4. Methodology
5. Results
6. Discussion
7. Conclusion
✅ Als nächstes kommt Teil 3 (der mächtigste Teil):
🧠 Der AI-Research Workflow
Damit kannst du:
Papers 10× schneller analysieren
Literatur automatisch strukturieren
Masterarbeiten extrem effizient schreiben

Forschungslücken finden
Viele Researcher benutzen genau so einen Workflow.
Wenn du willst, zeige ich dir den kompletten Research-Workflow Schritt für Schritt. 🚀
Aber natürlich
Alles klar — Teil 3: Der AI-Research Workflow (Schritt für Schritt, Copy-Paste-fähig)
Ziel: Von Thema → Literature Map → Paper-Analyse → Synthese → Writing mit einem wiederholbaren
System.
🧠 AI-Research Workflow in 9 Schritten
Schritt 0 — Setup (30 Sekunden)
Was du bereithältst
1 Satz: Was genau willst du wissen?
3–8 Keywords (Synonyme inkl.)
Optional: 1–3 Startpaper (oder ein PDF)
Prompt
Ich arbeite an folgendem Thema/Problem:
[1 SATZ PROBLEM]
Kontext:
- Ziel (z.B. Masterarbeit, Paper, Produktentscheidung): [ZIEL]
- Fokus (was ist IN scope / OUT of scope): [IN/OUT]
- Kriterien (z.B. 2019–heute, peer-reviewed, bestimmte Methoden): [KRITERIEN]
Gib mir:
1) 8–12 präzise Suchbegriffe + Synonyme
2) 3 Beispiel-Boolean-Strings (Scholar/Scopus)
3) 5 Subtopics (Cluster), die ich getrennt recherchieren sollte
Schritt 1 — Literatur finden (die “Startmenge”)
Ziel: 15–30 gute Quellen, nicht 300.
Prompt
Finde 20 relevante wissenschaftliche Quellen zu [THEMA].
Regeln:
- Priorität: Reviews/Meta-Analysen + Top-Venues
- Zeitraum: [JAHR–HEUTE]

- Ausgabe als Liste mit: Titel, Autor:innen, Jahr, Link, 2–3 Zeilen Summary, “Warum wichtig?”
- Sortiere in: (A) Grundlagen, (B) SOTA/neu, (C) Reviews, (D) konträre Positionen
Schritt 2 — Literature Map bauen (Cluster statt Chaos)
Ziel: Deine Quellen werden zu einem System.
Prompt
Erstelle eine Literature Map zu diesen Quellen:
[LISTE ODER LINKS]
Bitte:
- gruppiere in 4–7 Cluster (mit Cluster-Namen)
- ordne jedes Paper einem Cluster zu
- gib pro Cluster: zentrale Idee, typische Methoden, offene Fragen
- liefere am Ende: 5 “Must-read” Papers insgesamt
Schritt 3 — 10-Minuten Paper Pipeline (für jedes Paper gleich)
Ziel: Jedes Paper schnell, aber sauber verstehen.
3A: Schnellsummary
Fasse dieses Paper in maximal 8 Bulletpoints zusammen:
- Problem
- Ansatz
- Daten
- Methode
- Ergebnis
- Limitation
- Takeaway
- 1 Satz: “Wenn ich nur 1 Sache merke, dann …”
3B: Methodik & Validität
Erkläre die Methodik dieses Papers:
- Forschungsdesign
- Annahmen
- Messung/Operationalisierung
- Analyseverfahren
- Validitätsrisiken (intern/extern/konstrukt/statistisch)
3C: Reviewer-Check
Agiere als Peer-Reviewer:
- 3 Stärken
- 3 Schwächen
- 3 Major Revisions (konkret)
- 3 Robustheitstests, die fehlen könnten
- Gesamturteil + Begründung
Schritt 4 — Evidence Table (dein “Master Sheet”)
Ziel: Vergleichbar machen, damit du später schnell schreiben kannst.
Prompt

Erstelle eine Evidence Table aus diesen Papern:
[PAPERLISTE]
Tabelle mit Spalten:
- Citation (Autor, Jahr)
- Forschungsfrage
- Datensatz/Stichprobe
- Methode
- Hauptbefund (1–2 Sätze)
- Effekt/Größe (falls vorhanden)
- Limitationen
- Relevanz für meine Frage: [MEINE FRAGE]
Schritt 5 — Widersprüche erklären (Superkraft)
Ziel: Wenn Studien widersprechen, warum?
Prompt
Diese Studien widersprechen sich / wirken inkonsistent:
[STUDIE A]
[STUDIE B]
(optional [C])
Analysiere:
- Unterschiede in Definitionen
- Unterschiede in Daten/Stichproben
- Unterschiede in Metriken
- Unterschiede in Methodik/Identifikation
- Kontext/Setting
Gib am Ende 3 plausible Erklärungen + wie man sie testen würde.
Schritt 6 — Research Gaps → Projektideen
Ziel: Aus “Lücke” wird “machbares Projekt”.
Prompt
Basierend auf dieser Literature Map/Evidence Table:
[INPUT]
Gib mir:
1) 7 potenzielle Research Gaps (konkret, nicht allgemein)
2) zu jedem Gap: 1 Forschungsfrage + 1 Hypothese
3) zu jedem: mögliche Methode + minimale Datenanforderung
4) priorisiere nach Machbarkeit (hoch/mittel/niedrig)
Schritt 7 — Schreib-Engine (Literature Review / Related Work)
Ziel: Aus Table → fertiger Text (mit rotem Faden).

Prompt (Literature Review)
Schreibe einen Literature Review zu [THEMA], basierend auf diesen Papern:
[PAPERLISTE ODER TABLE]
Anforderungen:
- klare Struktur nach Clustern
- pro Cluster: Konsens + Kontroversen + offene Fragen
- am Ende: klare Forschungslücke, die meine Frage motiviert: [MEINE FRAGE]
Prompt (Related Work für ein Paper)
Schreibe eine Related Work Sektion (400–700 Wörter) für mein Paper.
Mein Beitrag/Angle:
[MEIN BEITRAG]
Nutze diese Quellen:
[QUELLEN]
Struktur:
- 2–4 Absätze nach Themenblöcken
- klare Abgrenzung: “Unterschied zu uns”
Schritt 8 — Argument & Contribution Claims schärfen
Ziel: Deine Arbeit klingt “paper-ready”.
Prompt
Hier ist meine Kernidee:
[IDEA]
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
⚡ Der “One-Prompt” Workflow (wenn du nur 1 Prompt nutzen willst)
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
Wenn du möchtest, machen wir als nächstes Teil 4 (mini, aber extrem nützlich):
ein Copy-Paste “Research Template”, das du für jedes neue Thema einmal ausfüllst (wie ein Formular),
damit der Workflow noch schneller läuft.
Okay
Perfekt — hier ist Teil 4: Das Research Template (Copy-Paste Formular).
Viele Forschende nutzen so etwas als Startdokument für jedes neue Projekt / jede Haus- oder
Masterarbeit.
Du füllst einfach die Felder aus, und danach kann ich oder eine andere KI sehr präzise arbeiten.
📄 Universal Research Template
Kopiere dieses Template und fülle es aus:
RESEARCH PROJECT TEMPLATE
1. Thema / Research Topic
[Beschreibe dein Thema in 1–2 Sätzen]
2. Forschungsproblem
Welches Problem soll untersucht werden?
[Problem beschreiben]
3. Forschungsfrage

Hauptfrage:
[Research Question]
Unterfragen:
4. Motivation
Warum ist dieses Thema wichtig?
- wissenschaftliche Bedeutung
- praktische Bedeutung
5. Kontext / Forschungsfeld
Fachgebiet:
[Disziplin]
Verwandte Themen:
6. Schlüsselbegriffe / Keywords
7. Bekannte Paper / Literatur
8. Vermutete Forschungslücke
Was fehlt bisher in der Forschung?
[Research Gap]

9. Hypothesen (optional)
H1:
H2:
H3:
10. Mögliche Methodik
Methode:
Datenerhebung:
Analyse:
11. Erwarteter Beitrag
Was könnte diese Arbeit neu beitragen?
12. Einschränkungen
- Datenverfügbarkeit
- Zeit
- Methodenkenntnisse
⚡ Wie du dieses Template benutzt
Sobald du das ausgefüllt hast, kannst du z.B. sagen:
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
🧠 Beispiel (kurz ausgefüllt)
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
✅ Wenn du möchtest, kann ich dir noch etwas sehr Wertvolles zeigen:
Die 10 Prompts, mit denen Professoren merken, dass eine Arbeit “research-level” ist.
Das sind Prompts für:
bessere Literature Reviews
kritische Analyse von Forschung
Reviewer-Level Argumentation
Viele Studierende kennen diese nicht.
Why not?
Alright — here are the 10 prompts that make writing sound like real academic research (the kind
supervisors and reviewers usually expect).
These focus on critical analysis, theory integration, and research contribution.
🎓 10 Prompts That Make Work Look “Research-Level”
󰍹 Theoretical Positioning Prompt
Use this when writing a literature review or theory section.
Position this research within the broader theoretical landscape.
Topic:
[TOPIC]
Explain:
- which theoretical frameworks dominate this field
- how different theories explain the phenomenon

- which theory best supports the current research
󰍽 Critical Literature Analysis
Most students summarize literature.
Researchers critically analyze it.
Critically analyze the literature on:
[TOPIC]
Focus on:
- agreements between studies
- contradictions
- methodological limitations
- gaps in the literature
󰍼 Research Contribution Prompt
This is what journals care about most.
Based on the current research on:
[TOPIC]
Explain what a meaningful research contribution would look like.
Identify:
- theoretical contribution
- methodological contribution
- practical contribution
󰍶 Conceptual Framework Builder
Used in many master theses and PhDs.
Build a conceptual framework for the research topic:
[TOPIC]
Include:
- key variables
- relationships between variables
- theoretical justification
󰍵 Assumption Analysis Prompt
Researchers question assumptions.
What assumptions underlie the research on:
[TOPIC]?
Explain:
- theoretical assumptions
- methodological assumptions

- possible biases
󰍻 Competing Explanations Prompt
Very important for high-quality discussion sections.
What alternative explanations could exist for findings related to:
[TOPIC]?
Explain at least 5 competing explanations.
󰍺 Methodological Critique Prompt
Used by peer reviewers.
Critically evaluate the research methods commonly used to study:
[TOPIC]
Discuss:
- strengths
- limitations
- possible improvements
󰍴 Theory Integration Prompt
Advanced academic writing integrates theories.
Integrate the following theories into a coherent explanation:
[THEORY 1]
[THEORY 2]
Explain how they complement or contradict each other.
󰍷 Research Debate Prompt
Good for high-level literature reviews.
What are the major debates in the research on:
[TOPIC]?
Explain the main positions and supporting evidence.
🔟 Future Research Prompt
Used in discussion sections of papers.
Identify promising directions for future research on:
[TOPIC]
Explain:
- unresolved questions
- methodological improvements
- new research opportunities

🧠 Why these prompts work
Weak academic writing usually:
summarizes studies
lists papers
describes findings
Strong academic writing:
compares research
critiques methods
identifies gaps
builds theory
These prompts push the output into that research-level thinking.
✅ If you want, I can also show you something extremely useful:
The “PhD Research Prompt Stack”
(about 15 prompts that replicate the workflow of academic researchers when writing papers).
Many people consider that the most powerful academic prompt system.
Sicher
Super — hier ist der PhD Research Prompt Stack.
Das ist ein Workflow aus 15 Prompts, der ziemlich nah an dem liegt, wie Forschende tatsächlich Papers
entwickeln.
Man kann ihn für:
Masterarbeit
Dissertation
Journal-Paper
Forschungsprojekte
verwenden.
🧠 PhD Research Prompt Stack

󰍹 Research Landscape Mapping
Map the research landscape for the topic:
[TOPIC]
Explain:
- main research streams
- influential theories
- key authors and papers
- emerging trends
󰍽 Core Literature Identification
Identify the 20 most influential academic papers on:
[TOPIC]
Explain briefly why each paper is important.
󰍼 Literature Clustering
Cluster the research on:
[TOPIC]
Group studies into major themes or research traditions.
󰍶 Concept Clarification
Define the key concepts used in research on:
[TOPIC]
Explain how different scholars define them.
󰍵 Theoretical Foundations
Explain the theoretical foundations behind research on:
[TOPIC]
Which theories are most commonly used?
󰍻 Methodological Landscape
Analyze the methods used in research on:
[TOPIC]
Explain:
- common research designs
- common data sources
- methodological strengths and weaknesses
󰍺 Evidence Evaluation
Evaluate the strength of the evidence in research on:
[TOPIC]

Which findings are strongly supported?
Which findings are controversial?
󰍴 Research Gap Detection
Identify research gaps in the literature on:
[TOPIC]
Explain why these gaps exist.
󰍷 Hypothesis Development
Develop testable hypotheses based on research about:
[TOPIC]
🔟 Conceptual Model
Develop a conceptual model explaining:
[TOPIC]
Identify variables and relationships.
1󰍹 Study Design
Propose a study design to test hypotheses about:
[TOPIC]
Include:
- data
- methods
- analysis approach
1󰍽 Expected Contributions
Explain the potential contributions of a study about:
[TOPIC]
Consider:
- theoretical contributions
- empirical contributions
- practical implications
1󰍼 Critical Evaluation
Critically evaluate the current research on:
[TOPIC]
Focus on limitations and biases.
1󰍶 Future Research Agenda
Develop a future research agenda for:
[TOPIC]
Identify promising research directions.

1󰍵 Paper Blueprint
Create a blueprint for a publishable academic paper about:
[TOPIC]
Include:
- introduction
- literature review
- theory
- methods
- results
- discussion
⚡ Why this stack is powerful
Dieser Stack deckt die 3 wichtigsten Ebenen wissenschaftlicher Arbeit ab:
1. Mapping the field
Literature
theories
debates
2. Generating research
hypotheses
frameworks
study designs
3. Publishing research
contributions
arguments
paper structure
💡 Pro Tipp:
Viele Doktoranden nutzen diese Reihenfolge:
1 → 3 → 6 → 8 → 10 → 11 → 15
Das bringt dich von Idee → Paper-Struktur.
Wenn du möchtest, kann ich dir noch etwas sehr Spannendes zeigen:
📚 Das „AI Research Super-System“
Damit kann man:

Papers 20× schneller verstehen
komplette Literaturreviews automatisieren
Forschungslücken finden, die kaum jemand sieht
Viele KI-Forscher nutzen inzwischen genau solche Systeme.
Klar, deinen nächsten Vorschlag direkt mit
Perfekt — hier ist das AI Research Super-System.
Das ist im Grunde ein kompletter Workflow, mit dem viele KI-Forscher heute Literatur schneller
analysieren und Forschung strukturieren.
Die Idee:
Du kombinierst Mapping → Paper-Analyse → Wissensextraktion → Synthese → Forschungsideen.
🚀 AI Research Super-System
Übersicht der 5 Ebenen
1. Field Mapping
2. Paper Mining
3. Knowledge Extraction
4. Research Synthesis
5. Idea Generation
Wenn man diese fünf Ebenen kombiniert, kann man ein Forschungsfeld sehr schnell durchdringen.
󰍹 Field Mapping (Forschungsfeld verstehen)
Zuerst verstehen wir die Struktur des gesamten Feldes.
You are a research analyst.
Map the research field of:
[TOPIC]
Explain:
- main research areas
- major theories
- influential authors
- major research debates
- emerging research trends
Output → Überblick über das gesamte Forschungsgebiet
󰍽 Paper Mining (wichtige Papers finden)
Jetzt finden wir die wichtigsten Studien.
Identify the most influential academic papers on:

[TOPIC]
Group them into:
- foundational papers
- highly cited papers
- recent influential papers
- review papers
Output → Core literature
󰍼 Knowledge Extraction (Wissen extrahieren)
Jetzt analysieren wir jedes Paper systematisch.
Extract the key knowledge from this research paper.
Identify:
- research question
- theoretical framework
- methodology
- main findings
- limitations
- contributions
Output → strukturierte Paperanalyse
󰍶 Research Synthesis (Literatur zusammenführen)
Jetzt verbinden wir die Studien miteinander.
Synthesize the literature on:
[TOPIC]
Explain:
- what the literature agrees on
- where findings conflict
- methodological differences
- theoretical differences
Output → Literature Review Struktur
󰍵 Idea Generation (neue Forschung entwickeln)
Jetzt generieren wir neue Forschungsideen.
Based on the current research on:
[TOPIC]
Generate:
- 10 research questions
- 5 potential research gaps

- 3 promising research projects
Output → neue Forschungsideen
🧠 Warum dieses System funktioniert
Viele Studierende lesen Papers so:
Paper → Paper → Paper
Forscher arbeiten eher so:
Field → Literature → Patterns → Gaps → Research
Das AI Research Super-System bildet genau diesen Prozess ab.
⚡ Beispiel (AI Education)
Wenn das Thema wäre:
AI tutoring systems
würde das System automatisch:
󰍹 wichtige Paper finden
󰍽 Ergebnisse vergleichen
󰍼 Forschungslücken erkennen
󰍶 neue Studien vorschlagen
🧩 Super-Prompt (komplettes System)
Wenn du nur einen Prompt nutzen willst:
Act as an academic research assistant.
Topic:
[TOPIC]
Perform a full research analysis including:
1. research field mapping
2. identification of key papers
3. extraction of key knowledge from studies
4. synthesis of the literature
5. identification of research gaps
6. generation of new research questions
💡 Wenn du möchtest, kann ich dir noch etwas zeigen, das viele Leute extrem überrascht:
Das „Deep Research Prompt Framework“
Damit kann man:
komplette Literature Reviews fast automatisch erstellen
100+ Papers strukturieren

ein Forschungsfeld in wenigen Stunden verstehen
Viele Leute nennen das inzwischen „AI-assisted literature review system“.
Ja
Perfekt — hier ist das Deep Research Prompt Framework.
Das ist ein systematisches System, um große Mengen wissenschaftlicher Literatur (50–200+ Papers) zu
analysieren und daraus eine hochwertige Literature Review zu erstellen.
Viele Researcher nutzen heute eine ähnliche Struktur.
🧠 Deep Research Prompt Framework
Überblick
Das Framework besteht aus 6 Phasen:
1. Topic Decomposition
2. Literature Discovery
3. Paper Structuring
4. Evidence Mapping
5. Literature Synthesis
6. Research Gap Identification
Diese Schritte führen dich von Thema → vollständige Literature Review.
󰍹 Topic Decomposition
Zuerst wird ein Thema in Teilbereiche zerlegt.
Prompt
Act as a research strategist.
Topic:
[TOPIC]
Break this topic into:
1. core research questions
2. subtopics
3. key theoretical perspectives
4. important variables studied in the literature
Ergebnis
Du bekommst:
Forschungscluster
wichtige Variablen

Teilbereiche der Literatur
󰍽 Literature Discovery
Jetzt wird relevante Literatur systematisch gesammelt.
Prompt
Identify the most relevant academic literature on:
[TOPIC]
Organize papers into categories:
- foundational papers
- highly cited papers
- recent research
- review articles
Ergebnis
Eine strukturierte Paperliste.
󰍼 Paper Structuring
Jetzt wird jedes Paper in eine einheitliche Struktur zerlegt.
Prompt
Analyze this research paper and extract:
- research question
- theoretical framework
- research design
- data / sample
- methods
- key findings
- limitations
Ergebnis
Du erhältst eine standardisierte Paperanalyse.
󰍶 Evidence Mapping
Jetzt werden alle Paper vergleichbar gemacht.
Prompt
Create an evidence map based on the following papers:
[PAPER LIST]
Include:
- study
- research question
- methodology

- main findings
- limitations
Ergebnis
Eine Evidence Table, die Forschung vergleichbar macht.
󰍵 Literature Synthesis
Jetzt entsteht die Literature Review.
Prompt
Synthesize the literature on:
[TOPIC]
Explain:
- major research themes
- areas of agreement
- conflicting findings
- methodological differences
Ergebnis
Eine strukturierte Literaturübersicht.
󰍻 Research Gap Identification
Jetzt wird neue Forschung entwickelt.
Prompt
Based on the literature on:
[TOPIC]
Identify:
- research gaps
- unanswered questions
- promising research directions
Ergebnis
Neue Forschungsfragen.
⚡ Der Mega-Prompt (komplettes Framework)
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
📚 Beispiel
Thema:
AI tutoring systems in higher education
Das Framework würde automatisch:
󰍹 Forschungsbereiche identifizieren
󰍽 wichtige Paper sammeln
󰍼 Studien vergleichen
󰍶 Ergebnisse zusammenführen
󰍵 Forschungslücken finden
🧠 Warum dieses Framework stark ist
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
↓
Gaps
↓
New Research
So arbeiten viele wissenschaftliche Reviews.
💡 Wenn du möchtest, kann ich dir noch etwas Extrem-Nützliches zeigen:
📊 Das „100-Paper Reading System“
Damit kannst du:
100 wissenschaftliche Papers in wenigen Stunden strukturieren
automatisch Literature Reviews bauen
schnell Forschungslücken entdecken

Viele Doktoranden nutzen genau so ein System.
Hau raus
Alles klar 😄 Hier kommt das „100-Paper Reading System“ – ein praktischer, wiederholbarer Ablauf, mit
dem du 50–200 Papers schnell strukturierst, ohne dich zu verlieren.
📊 100-Paper Reading System (AI-gestützt)
Grundidee
Du liest nicht 100 Papers linear. Du baust zuerst ein System, dann liest du selektiv:
Triaging (schnell aussortieren)
Standardisierte Extraktion (alles gleich formatieren)
Evidence Table (Vergleichbarkeit)
Synthese (Cluster → Argument)
Gaps → Beitrag (dein eigenes Projekt)
Phase 1 — Triage (1–3 Minuten pro Paper)
Ziel
In 2 Minuten entscheiden:
A) Must-read (voll) • B) Relevant (teilweise) • C) Drop
Prompt: 2-Minuten Triage
Triage dieses Paper in <3 Minuten.
Gib:
1) 1-Satz-These des Papers
2) 5 Bulletpoints: Problem, Methode, Daten, Ergebnis, Limitation
3) Klassifikation: A (Must-read) / B (Relevant) / C (Drop)
4) Warum diese Klassifikation?
Praxisregel (Gold wert)
A (10–15%): Voll lesen + tief extrahieren
B (25–40%): Intro + Method + Results + Discussion selektiv
C (Rest): Nur bibliografisch speichern (evtl. später)
Phase 2 — Standard Extraction (5–8 Minuten pro A-Paper)
Ziel
Jedes Paper bekommt dieselbe Karteikarte (damit du später nicht neu lesen musst).
Prompt: Paper Card (einheitliches Schema)
Erstelle eine Paper Card im folgenden Format:

Citation:
Research question:
Theory / framework:
Data / sample:
Method:
Key findings (max 3):
Effect size / metrics (falls vorhanden):
Limitations (max 3):
What this paper is useful for (1 sentence):
2 keywords for retrieval:
Phase 3 — Evidence Table (das Herzstück)
Ziel
Alle A/B-Paper in eine Tabelle, damit du:
schnell vergleichen
Trends erkennen
Literature Review schreiben kannst
Prompt: Evidence Table Builder
Erstelle eine Evidence Table aus diesen Paper Cards:
[PASTE PAPER CARDS]
Tabelle mit Spalten:
- Autor, Jahr
- Frage
- Setting/Stichprobe
- Methode
- Hauptbefund
- Evidenzstärke (hoch/mittel/niedrig) + warum
- Limitationen
- Relevanz für meine Frage: [MEINE FRAGE]
Evidenzstärke Heuristik (schnell)
Hoch: Meta-Analyse, RCT, starke Identifikation, gute Robustheit
Mittel: saubere Beobachtungsstudie, plausible Controls
Niedrig: kleine Stichprobe, schwache Messung, starke Annahmen
Phase 4 — Cluster & Map (aus Tabelle wird Struktur)
Ziel
Du erzeugst 4–7 Cluster, die später deine Kapitel/Unterabschnitte werden.
Prompt: Cluster Generator

Basierend auf dieser Evidence Table:
[PASTE TABLE]
1) Gruppiere die Paper in 4–7 Cluster mit Namen
2) Pro Cluster: Kernidee + typische Methoden + Konsens + Konflikte
3) Welche 5 Paper sind “Must-cite”?
Phase 5 — Contradiction Resolver (wenn Studien sich widersprechen)
Prompt: Widersprüche erklären
Diese Befunde scheinen sich zu widersprechen:
[STUDIE A: Befund]
[STUDIE B: Befund]
Erkläre 5 plausible Ursachen:
- Definitionen
- Metriken
- Daten/Population
- Methodik/Identifikation
- Kontext/Setting
Und: Wie könnte man jede Ursache testen?
Phase 6 — Synthesis Writing (Literature Review in 1–2 Durchläufen)
Ziel
Nicht „Paper aneinanderreihen“, sondern:
Cluster → Argument → Gap → Beitrag
Prompt: Literature Review Draft
Schreibe einen Literature Review basierend auf diesen Clustern:
[CLUSTER OUTPUT]
Anforderungen:
- Pro Cluster: (a) Konsens, (b) Kontroversen, (c) Limitationen
- Übergänge zwischen Clustern (roter Faden)
- Endet mit: klare Forschungslücke + Motivation für [MEINE FRAGE]
Phase 7 — Gap → Projektideen (das, was Betreuer lieben)
Prompt: Research Gap to Study Design
Basierend auf der Literatur (Cluster + Evidence):
1) Liste 7 konkrete Research Gaps
2) Für die Top 3:
- Forschungsfrage
- Hypothese(n)
- Studiendesign (Daten, Methode, Analyseplan)
- Risiken + Fallbacks
Priorisiere nach Machbarkeit (hoch/mittel/niedrig).
🧰 Das System als “Pipeline” (Copy-Paste Workflow)

Wenn du wirklich schnell sein willst, nutze diese Reihenfolge:
Triage Prompt auf alle Papers
Nur A-Papers → Paper Card Prompt
Alle Cards → Evidence Table Prompt
Evidence Table → Cluster Prompt
Cluster → Literature Review Draft Prompt
Cluster + Table → Gap → Study Design Prompt
⏱ Realistischer Durchsatz (ohne Stress)
Triage: 100 Papers ≈ 2–4 Stunden (je nach Zugang/Format)
A-Paper Deep Extraction: 10–15 Papers ≈ 1–2 Stunden
Synthesis: 30–60 Minuten
→ Du hast danach ein Literature-Review-Gerüst, statt 100 PDFs im Chaos.
🧠 Pro-Tipps (die den Unterschied machen)
Nicht jedes Paper gleich tief lesen.
Immer standardisieren (Paper Cards).
Immer schreiben aus der Evidence Table, nicht aus PDFs.
Konflikte sind Gold: daraus entstehen Beiträge.
Wenn du willst, machen wir’s maximal praktisch:
Nenn mir dein Thema + deine Forschungsfrage (1–2 Sätze), und ich passe die Triage-Kriterien +
Evidence-Table-Spalten + Cluster-Logik exakt darauf an.


---

## Appendix (optional) – Academic / Masterarbeit Prompt Library
Masterarbeit Prompt Library (kompletter Workflow)
󰍹 Thema finden
Themenvorschläge generieren
Schlage 15 mögliche Themen für eine Masterarbeit im Bereich [FACHGEBIET] vor.
Für jedes Thema:
- kurze Beschreibung
- mögliche Forschungsfrage
- mögliche Methode
- geschätzter Schwierigkeitsgrad
Trendbasierte Themen
Welche aktuellen Forschungstrends gibt es im Bereich [FACHGEBIET]?
Schlage daraus 10 mögliche Masterarbeitsthemen ab.
󰍽 Forschungsfrage entwickeln
Forschungsfrage formulieren
Hilf mir eine präzise Forschungsfrage zu formulieren.
Themenbereich: [THEMA]
Erstelle:
- 1 Hauptforschungsfrage
- 3 Unterfragen
- mögliche Hypothesen
Forschungsfragen verbessern
Bewerte diese Forschungsfrage kritisch:
[FORSCHUNGSFRAGE]
Verbessere sie hinsichtlich:
- Klarheit
- Messbarkeit
- wissenschaftliche Relevanz
󰍼 Exposé / Proposal schreiben
Exposé erstellen
Erstelle ein Exposé für eine Masterarbeit zu folgendem Thema:
[THEMA]
Struktur:
- Problemstellung
- Forschungsfrage
- Stand der Forschung

- Methodik
- erwarteter Beitrag
Exposé verbessern
Bewerte dieses Exposé wie ein Betreuer.
[EXPOSÉ]
Analysiere:
- wissenschaftliche Qualität
- Klarheit
- Forschungslücke
- Verbesserungsvorschläge
󰍶 Literaturrecherche
Literaturübersicht
Erstelle eine strukturierte Literaturübersicht zu:
[THEMA]
Struktur:
- wichtigste Theorien
- zentrale Studien
- aktuelle Forschung
- offene Fragen
Literatur systematisch sammeln
Erstelle eine Liste von 20 wichtigen Papern zu:
[THEMA]
Sortiere nach:
- Grundlagenliteratur
- neuere Studien
- wichtige Reviews
󰍵 Theorie-Kapitel schreiben
Theoretischen Hintergrund erstellen
Schreibe einen wissenschaftlichen Abschnitt zum theoretischen Hintergrund über:
[THEMA]
Struktur:
- zentrale Theorien
- wichtige Modelle
- Verbindungen zur Forschungsfrage
Theorien vergleichen

Vergleiche folgende Theorien:
[THEORIE A]
[THEORIE B]
Analysiere:
- Gemeinsamkeiten
- Unterschiede
- Relevanz für meine Forschungsfrage
󰍻 Methodik planen
Methodik entwickeln
Hilf mir eine Forschungsmethodik zu entwickeln.
Forschungsfrage:
[FRAGE]
Erstelle:
- geeignete Methode
- Datenerhebung
- Stichprobe
- Analyseverfahren
Methodenkapitel schreiben
Schreibe ein Methodenkapitel für eine Masterarbeit.
Inhalt:
- Forschungsdesign
- Datenerhebung
- Stichprobe
- Analyseverfahren
󰍺 Datenanalyse verstehen
Statistische Ergebnisse erklären
Erkläre folgende statistische Ergebnisse verständlich:
[ERGEBNISSE]
Struktur:
- Interpretation
- Bedeutung
- mögliche Fehlerquellen
Ergebnisse interpretieren
Hilf mir folgende Ergebnisse zu interpretieren:
[ERGEBNISSE]

Analysiere:
- Bedeutung
- Zusammenhang mit Hypothesen
- mögliche Erklärungen
󰍴 Diskussion schreiben
Diskussionskapitel erstellen
Schreibe eine wissenschaftliche Diskussion basierend auf diesen Ergebnissen:
[ERGEBNISSE]
Struktur:
- Interpretation
- Vergleich mit Literatur
- Limitationen
- praktische Implikationen
󰍷 Fazit und Beitrag
Fazit formulieren
Schreibe ein Fazit für eine Masterarbeit zu folgendem Thema:
[THEMA]
Struktur:
- wichtigste Ergebnisse
- wissenschaftlicher Beitrag
- zukünftige Forschung
🔟 Korrektur & Verbesserung
Akademischen Stil verbessern
Verbessere den akademischen Stil dieses Textes:
[TEXT]
Achte auf:
- Klarheit
- wissenschaftliche Sprache
- Struktur
Logik prüfen
Prüfe diesen Text auf logische Schwächen:
[TEXT]
Analysiere:
- Argumentationsstruktur
- fehlende Belege
- mögliche Verbesserungen

⚡ Super-Prompt für komplette Arbeiten
Dieser Prompt funktioniert extrem gut:
Ich schreibe eine Masterarbeit zum Thema:
[THEMA]
Hilf mir Schritt für Schritt bei:
1. Forschungsfrage
2. Literaturübersicht
3. Methodik
4. Datenanalyse
5. Diskussion
6. Fazit
🧠 Profi-Prompt (für komplette Thesis)
Verhalte dich wie ein akademischer Betreuer.
Hilf mir meine Masterarbeit zu strukturieren.
Thema: [THEMA]
Erstelle:
- komplette Gliederung
- Forschungsfragen
- Methodenvorschläge
- wichtige Literatur
✅ Als nächstes kommt 3/3 — die Paper-Analyse-Prompt-Engine.
Das ist ein extrem starkes Workflow-System, mit dem du jedes wissenschaftliche Paper in 5–10
Minuten komplett analysieren kannst (inkl. Reviewer-Level Analyse).
Soll ich dir die auch zeigen? 🚀
Ja, sehr gerne
Hier ist 3/3: Die Paper-Analyse-Prompt-Engine.
Damit kannst du jedes wissenschaftliche Paper systematisch in 5–10 Minuten analysieren – ähnlich wie
ein Peer-Reviewer oder Researcher.
🔬
