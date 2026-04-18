# 09_EXECUTION_ANALYTICS_ITERATION – Execution, Analytics & Iteration

## Ziel

Du baust den Feedback-Loop: Messen → Lernen → Verbessern, ohne dich zu verlieren.

## Inputs

- Nutzungsdaten
- Feedback/Support
- GTM Assets
- PRD/UX Baseline

## Outputs (am Ende dieses Schritts)

- ANALYTICS_PLAN.json
- Experiment Backlog
- Review Cadence
- Iteration Plan

## Vorgehen (pragmatisch)

1. Definiere North Star + 1–2 Funnels.
2. Instrumentiere Events (Name/Properties/Trigger).
3. Baue ein Dashboard für wöchentliche Entscheidungen.
4. Plane Experimente (Hypothese → Metric → Decision Rule).
5. Spiele Learnings formal zurück via ITERATION_BRIEF.json → PRD/UX/Build.

## Quality Gates

- Wöchentlicher Review ist kalendarisch/operativ möglich (Owner, Ritual).
- Experimente haben Guardrails (nicht nur Vanity Metrics).

## Short-Prompt (copy/paste)

```txt
Du bist mein Growth + Analytics Lead.

Inputs:
- Launch Daten/Feedback: {DATA}
- GTM_PLAN.json: {GTM_PLAN_JSON}

Tasks:
1) ANALYTICS_PLAN.json (North Star, Funnels, Events, Dashboards, Cadence).
2) Lege 5 Experimente an (jeweils EXPERIMENT_BRIEF.json).
3) Schreibe ein Weekly Review Template (was schauen wir, was entscheiden wir).
4) POSTMORTEM_LESSONS.json (falls Launch Probleme hatte) oder „Lessons so far“.
```

## Templates

- `/templates/ANALYTICS_PLAN.json`
- `/templates/EXPERIMENT_BRIEF.json`
- `/templates/POSTMORTEM_LESSONS.json`
- `/templates/ITERATION_BRIEF.json` (NEU in v2: formaler Feedback-Loop zurück zu PRD/Build)

## GPT-Config

- `/gpt_configs/09_EXECUTION_ANALYTICS_ITERATION.json`

## Toolbox-Vertiefung

- `/toolbox/08__EXECUTION_ANALYTICS_ITERATION.md`
- `/toolbox/P11_CONTENT_GROWTH_SYSTEMS.md`
