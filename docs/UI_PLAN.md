# DeafPiper UI Plan

## 1) Ziele des Interfaces

Das UI soll den Pipeline-Lebenszyklus sichtbar und steuerbar machen:
- Task- und Step-Status in Echtzeit.
- Validation/Comparison/Decision nachvollziehbar mit Audit-Bezug.
- Dead-End und Budget-Breaches klar priorisiert.
- Rework-Ketten verständlich visualisiert.
- Operator:innen sollen Entscheidungen treffen können (promote/reject/rework/defer, override).

## 2) Zielgruppen

1. **Operator / Maintainer**
   - Startet Tasks, beobachtet Steps, untersucht Fehler.
2. **Reviewer / Architect**
   - Bewertet Vergleichsergebnisse, genehmigt Overrides.
3. **Team Lead / PM**
   - Sieht Fortschritt, Risiken, Budgetverbrauch.

## 3) Informationsarchitektur (Screens)

## A. Dashboard
- Karten: Running Tasks, Blocked Tasks, Dead Ends (24h), Budget Breaches (24h).
- Timeline: letzte Audit-Ereignisse.
- Quick Actions: "Open blocked task", "Show recent overrides".

## B. Task Detail
- Header: Objective, Scope (includes/excludes), Constraints, BudgetPolicy.
- Step-Liste inkl. State-Machine-Badge.
- Artifacts je Step + PromotionDecision.
- Rework-Chain Graph.
- Audit-Tab (filterbar nach Eventtyp).

## C. Candidate Review
- Validation-Ergebnisse (blocker/warning/info).
- Comparison-Dimensionen mit Delta.
- Baseline-Referenz + Klassifikation.
- Decision Panel mit strukturiertem Rationale-Formular.

## D. Dead-End / Escalation Center
- Liste aller Dead-End-Events mit Kategorie.
- Detailpanel mit detector_output, rework_chain, budget_state.
- Empfohlene Human Actions als Checkliste.

## E. Budget & Provider
- Budget-Verbrauch pro Task/Step (tokens/cost/time/tool_calls/rework).
- ProviderBinding + Modellfähigkeiten.
- Tool-Calls aus ToolBroker mit allow/deny.

## F. Known Issues
- Anzeige von `docs/KNOWN_ISSUES.md`.
- Markierung pre-existing vs newly introduced.
- Verlinkung auf PromotionDecision IDs.

## 4) Kern-User-Flows

1. **Task Monitoring**
   Dashboard → Task Detail → Audit Tab → Entscheidung (weiterlaufen/escalate).
2. **Candidate Decision**
   Task Detail → Candidate Review → promote/rework/reject/defer.
3. **Dead-End Handling**
   Dead-End Center → Escalation Payload prüfen → neue InstructionSet-Version auslösen.
4. **Budget Incident**
   Budget & Provider → Breach verstehen → on_breach-Aktion + Anpassung BudgetPolicy.

## 5) Datenmodell-Mapping (UI ↔ Backend)

- Dashboard:
  - `AuditEntry` (events: dead_end, escalated, budget_breached)
  - `Task.status`
- Task Detail:
  - `Task`, `Step`, `ArtifactCandidate`, `PromotionDecision`
- Candidate Review:
  - `TestResult`, `ComparisonResult`, `PromotionDecision`
- Dead-End Center:
  - Escalation payload aus `EscalationHandler`
- Budget & Provider:
  - `BudgetState`, `BudgetPolicy`, `ProviderBinding`, ToolBroker-Events

## 6) Komponentenstruktur (Frontend)

- `AppShell`
- `DashboardPage`
- `TaskDetailPage`
  - `TaskHeaderCard`
  - `StepTimeline`
  - `ArtifactTable`
  - `ReworkChainGraph`
  - `AuditEventList`
- `CandidateReviewPage`
  - `ValidationPanel`
  - `ComparisonPanel`
  - `DecisionForm`
- `DeadEndPage`
  - `DeadEndTable`
  - `EscalationPayloadViewer`
- `BudgetProviderPage`
  - `BudgetUsageCharts`
  - `ProviderBindingCard`
  - `ToolCallLogTable`

## 7) API-Contract Vorschlag

- `GET /tasks`
- `GET /tasks/{id}`
- `GET /tasks/{id}/history`
- `GET /tasks/{id}/rework-chains`
- `GET /candidates/{id}/validation-results`
- `GET /candidates/{id}/comparison`
- `POST /candidates/{id}/decision`
- `GET /dead-ends?since=&until=`
- `GET /overrides?since=&until=`
- `GET /budget/{task_id}`
- `GET /providers/{task_id}`
- `GET /known-issues`

## 8) UX/Visual Design Leitlinien

- Ampel-Status: blocker=rot, warning=gelb, pass=grün.
- State machine sichtbar und klickbar (mit erlaubten Übergängen).
- Jede Entscheidung muss eine Rationale erzwingen.
- Diff/Delta-Ansichten side-by-side für Vergleich.
- Kritische Events (dead_end, budget_breach) sticky oben in Task Detail.

## 9) Security & Governance

- Rollenmodell:
  - Viewer: read-only.
  - Operator: execute/rework.
  - Reviewer: promote/reject/defer.
  - Architect/Admin: overrides und Policy-Änderungen.
- Audit-Sicht unveränderlich anzeigen (append-only Prinzip).
- Override-Dialog mit Pflichtfeldern (actor + rationale + scope).

## 10) Umsetzung in Iterationen

### Iteration 1 (MVP, 2 Wochen)
- Dashboard, Task Detail, Audit-Liste, Known Issues Viewer.
- Read-only API-Endpunkte.

### Iteration 2 (2 Wochen)
- Candidate Review inkl. DecisionForm.
- Dead-End Center inkl. Escalation Payload.

### Iteration 3 (2 Wochen)
- Budget & Provider Seite.
- ToolBroker-Call-Log und Breach-Warnungen.

### Iteration 4 (1–2 Wochen)
- Rollen/Rechte, Override-Workflows, Exportfunktionen.

## 11) Erfolgskriterien

- MTTR bei Dead-End-Fällen sinkt.
- Keine Promotion ohne sichtbare ComparisonResult + TestResult.
- Budget-Breaches werden innerhalb von 1 Stunde triagiert.
- 100% der Overrides mit vollständiger Begründung dokumentiert.
