# P06 – Build & Debug (R / Data workflows)

_Bereinigt: Unterhaltungen, Werbung und externe Links entfernt (URLs durch `[URL_REMOVED]` ersetzt, wo nötig)._ 

```md

# R Wizard – Effektive Nutzung (User Guide)
## 1. Wofür dieses GPT optimiert ist
Dieses GPT ist spezialisiert auf:
* **R Programmierung**
* **Data Science & Statistik**
* **Machine Learning in R**
* **Multivariate Statistik**
* **Shiny App Entwicklung**
* **Integration moderner LLM/AI-Workflows in R**
* **Code Review und Refactoring**
* **Reproduzierbare Data-Science-Workflows**
Typische Aufgaben:
* Debugging von R-Code
* Performance-Optimierung
* Statistik-Interpretation
* ML-Modelle entwickeln
* Shiny Apps designen
* LLM-Integration (OpenAI, Ollama, etc.)
* Data Pipelines erstellen
# 2. Wie du am besten Fragen stellst
Die Qualität der Antwort hängt stark davon ab, wie du deine Anfrage formulierst.
## Best Practice Struktur
```text
1. Kontext
2. Ziel
3. Code (falls vorhanden)
4. Problem / Fehler

5. Erwartetes Ergebnis
```
### Beispiel
```r
Kontext:
Ich analysiere Verkaufsdaten mit tidyverse.
Ziel:
Ich möchte monatliche Umsatzsummen berechnen.
Code:
sales |>
group_by(month(date)) |>
summarise(sum = sum(price))
Problem:
Der Code funktioniert, aber die Monate sind nicht sortiert.
Frage:
Wie kann ich das sauber lösen?
```
# 3. Welche Arten von Antworten du erwarten kannst
Typische Antwortstrukturen:
## A. Konzept-Erklärung
* kurze Theorie
* Praxisbeispiel
* typischer Fehler
Beispiel:
```r
library(dplyr)
sales |>
mutate(month = lubridate::floor_date(date, "month")) |>
summarise(revenue = sum(price), .by = month)
```

Wichtige Prinzipien:
### Snake Case
```r
model_results
daily_sales
```
nicht:
```r
ModelResults
dailySales
```
### Assignment
```r
x <- 5
```
nicht
```r
x = 5
```
### Pipes
```r
data |>
filter(x > 0) |>
summarise(mean_x = mean(x))
```
### Funktionen kurz halten
```r
calc_mean <- function(x) {
mean(x, na.rm = TRUE)
}

```
### Kommentare erklären das **Warum**
```r
# Remove outliers to stabilize regression
data <- data |> filter(z_score < 3)
```
Nicht:
```r
# Filter rows
data <- data |> filter(z_score < 3)
```
Diese Prinzipien stammen aus dem tidyverse Style Guide.
# 5. Besonders gute Prompts
## Debugging
```text
Hier ist mein R Code und der Fehler.
Bitte:
1. Fehler erklären
2. Ursache nennen
3. korrigierten Code schreiben
```
## Code Optimierung
```text
Optimiere diesen R Code für:
- Geschwindigkeit
- Lesbarkeit
- tidyverse Stil
```
## Data Science Analyse

```text
Ich habe diesen Datensatz.
Welches Modell würdest du verwenden und warum?
```
## Shiny Apps
```text
Baue eine Shiny App mit:
Input:
- Date range
- Product
Output:
- ggplot Umsatztrend
```
# 6. Fortgeschrittene Nutzung
Sehr gut geeignet für:
### Pipeline Design
```r
raw_data |>
clean_data() |>
feature_engineering() |>
train_model()
```
### Reproduzierbare Projekte
Empfohlene Tools:
* `renv`
* `targets`
