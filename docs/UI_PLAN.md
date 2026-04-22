# DeafPiper UI Plan (Execution v1)

> Status: **Startdokument** – dieses Dokument ist der Einstiegspunkt für die UI-Umsetzung.

## 0) Ziel dieses Dokuments

Dieses Dokument übersetzt die Architektur (`docs/ARCHITECTURE.md`) in eine umsetzbare UI-Roadmap mit:
- klaren Screens,
- API-Verträgen,
- Rollen/Rechten,
- Metriken,
- Iterationsplan (MVP → v1.0).

---

## 1) Produktziele für das UI

Das UI ist kein Chat und kein Endkundenprodukt. Es ist ein **Operator- und Review-Interface** für die Pipeline.

### Muss-Ziele
1. Jede Entscheidung (`promote/reject/rework/defer`) muss nachvollziehbar sein.
2. Dead Ends und Budget-Breaches müssen sofort sichtbar sein.
3. Rework-Ketten müssen visuell verständlich werden.
4. Kein „done“ ohne sichtbare Validation + Comparison + Decision.

### Nicht-Ziele
- Kein vollwertiges Projektmanagement-Tool (Jira-Ersatz).
- Kein allgemeines BI-System.
- Keine freie Prompting-Oberfläche.

---

## 2) Personas und Verantwortungen

### 2.1 Operator
- Startet Task-Runs, beobachtet Steps, triagiert Fehler.
- Darf Rework auslösen, aber keine Overrides auf Regression.

### 2.2 Reviewer
- Prüft Candidate-Resultate.
- Darf promote/reject/defer.
- Darf Overrides mit Pflichtbegründung setzen.

### 2.3 Architect/Admin
- Verwaltet Policies, Budgets, Constraint-Sets, Rollen.
- Prüft Drift und Governance.

---

## 3) Informationsarchitektur (Navigation)

1. **Dashboard**
2. **Tasks** (Liste)
3. **Task Detail**
4. **Candidate Review**
5. **Dead-End Center**
6. **Budget & Provider**
7. **Known Issues**
8. **Settings (Policies, Roles, Limits)**

---

## 4) Screen-Spezifikation

## 4.1 Dashboard
**Widgets**:
- Running/Blocked/Done Tasks
- Dead Ends letzte 24h
- Budget Breaches letzte 24h
- Recent Overrides
- „Needs Human Action“-Queue

**Aktionen**:
- Zu blockiertem Task springen
- Dead-End-Payload öffnen

## 4.2 Task List
**Spalten**:
- Task ID, Titel, Status, Owner, letzte Änderung, Risiko

**Filter**:
- Status, Label, Budget-Risk, mit/ohne Dead-End

## 4.3 Task Detail
**Bereiche**:
- Header (Objective, Scope, Constraints, Budget)
- Step Timeline (State Machine)
- Artifacts pro Step
- Audit Stream
- Rework-Ketten-Graph

**Kritisch**:
- Sticky Warnbanner bei blocker fail / dead_end / budget_breached

## 4.4 Candidate Review
**Panels**:
- Validation (pro Rule + Severity)
- Comparison (Delta je Dimension + Klassifikation)
- Decision-Panel (promote/rework/reject/defer)

**Regeln im UI**:
- `promote` nur aktiv, wenn Blocker-Pflicht erfüllt.
- Override nur mit Pflichtfeldern (`actor`, `scope`, `rationale`).

## 4.5 Dead-End Center
**Liste**:
- Kategorie, Task, Step, Zeitpunkt, Priorität

**Detail**:
- detector_output
- budget_state
- last_validation_results
- last_comparison_result
- empfohlene nächste Aktionen

## 4.6 Budget & Provider
**Budget**:
- Verbrauch pro Task/Step (`tokens`, `cost_usd`, `wall_time_s`, `tool_calls`, `rework_iterations`)

**Provider**:
- ProviderBinding, ModelCapabilities, letzte ToolBroker-Calls

## 4.7 Known Issues
- Direktanzeige aus `docs/KNOWN_ISSUES.md`
- Filter: pre-existing / introduced / deferred / fixed
- Verlinkung auf Decision IDs

---

## 5) UX-Standards

1. Ampel-System: blocker=rot, warning=gelb, ok=grün.
2. Jede mutierende Aktion öffnet einen Confirm-Dialog mit Auswirkungen.
3. Audit-Events immer timestamp + actor + subject.
4. Diff/Delta side-by-side in Candidate Review.
5. Keyboard-friendly (schnelle Triagierung ohne Maus).

---

## 6) API-Contract (v1 Vorschlag)

### Read
- `GET /tasks`
- `GET /tasks/{id}`
- `GET /tasks/{id}/steps`
- `GET /tasks/{id}/audit`
- `GET /tasks/{id}/rework-chains`
- `GET /candidates/{id}/validation`
- `GET /candidates/{id}/comparison`
- `GET /dead-ends?since=&until=`
- `GET /overrides?since=&until=`
- `GET /budget/{task_id}`
- `GET /provider/{task_id}`
- `GET /known-issues`

### Write
- `POST /candidates/{id}/decision`
- `POST /candidates/{id}/override`
- `POST /tasks/{id}/rework`
- `POST /tasks/{id}/escalate`

---

## 7) Rollen & Berechtigungen

| Aktion | Operator | Reviewer | Architect/Admin |
|---|---:|---:|---:|
| Task ansehen | ✅ | ✅ | ✅ |
| Rework starten | ✅ | ✅ | ✅ |
| Decision setzen | ⚠️ eingeschränkt | ✅ | ✅ |
| Override setzen | ❌ | ✅ | ✅ |
| Policy/Budget ändern | ❌ | ❌ | ✅ |

---

## 8) Umsetzungsplan (Backlog)

## Iteration 1 – MVP Read-Only (1–2 Wochen)
- Dashboard, Task List, Task Detail, Known Issues
- Audit Stream + Rework-Graph (read-only)
- Basis-Rollenmodell (Viewer/Operator)

## Iteration 2 – Review Actions (1–2 Wochen)
- Candidate Review Seite
- Decision-Form (promote/reject/rework/defer)
- Override-Dialog (Reviewer+)

## Iteration 3 – Incident Ops (1–2 Wochen)
- Dead-End Center
- Budget & Provider Seite
- Alerts/Badges bei blocker und budget breach

## Iteration 4 – Governance & Hardening (1–2 Wochen)
- Vollständiges RBAC
- Audit-Exports
- Performance-Optimierung, Accessibility, Telemetrie

---

## 9) Technische Empfehlung (UI-Stack)

- Frontend: React + TypeScript + TanStack Query
- UI-Komponenten: shadcn/ui oder MUI
- Tabellen: AG Grid oder TanStack Table
- Graphen: React Flow (Rework chains), ECharts (Budget)
- State: server-state-first, minimale globale Client-State

---

## 10) Messbare Erfolgskriterien

1. 100% Decision-Events mit verknüpften Validation + Comparison IDs sichtbar.
2. Dead-End-Triage in < 15 Minuten median.
3. Keine Override-Action ohne Pflichtbegründung.
4. 0 „silent promotions“ (promote ohne sichtbare Begründung).

---

## 11) Nächster konkreter Schritt

1. **UI-Skeleton erstellen** (Navigation + leere Seiten).
2. Mock-API für `GET /tasks`, `GET /tasks/{id}`, `GET /tasks/{id}/audit`.
3. Dashboard + TaskDetail read-only zuerst ausliefern.
