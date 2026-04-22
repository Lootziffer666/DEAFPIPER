# Project Repo Scaffold (empfohlene Ordnerstruktur)

Ziel: Du kannst dieses Gerüst 1:1 in dein Projekt kopieren. Jede Stage schreibt in „ihren“ Ordner. Keine Artefakte verschwinden mehr.

```
/work
  /01_setup_prompting
    IDEA_BRIEF.json
    prompting_standard.md
    glossary.md
  /02_research_validation
    RESEARCH_BRIEF.json
    findings.md
    assumptions_log.md
  /03_prd_planning
    PRD.json
    roadmap.md
  /04_ux_ui
    UX_SPEC.json
    wireframes/
    copy.md
    design_tokens.md
  /05_architecture
    ARCHITECTURE_SPEC.json
    diagrams/
    ADR.md
  /06_build
    BUILD_PLAN.json
    DEPLOY_PACKET.json
    repo_link.md
    run_instructions.md
  /07_quality_security_compliance
    TEST_PLAN.json
    THREAT_MODEL.json
    PRIVACY_DPIA_LITE.json
    QA_REPORT.json
    qa_report.md
  /08_marketing_gtm
    GTM_PLAN.json
    LAUNCH_CHECKLIST.json
    landing_page_copy.md
    creatives/
    press_kit/
  /09_analytics_iteration
    ANALYTICS_PLAN.json
    EXPERIMENTS/
      2026-03-04_experiment_x.json
    ITERATION_BRIEF.json
    POSTMORTEM_LESSONS.json
  /10_handoff
    HANDOFF_PACKAGE.json
    handover_notes.md
```

## Konventionen, die dir später Zeit sparen

- **Ein „Source of Truth“ pro Thema:** PRD = PRD.json, nicht 5 halbe Docs.
- **Decision Log (ADR):** Jede harte Tech-Entscheidung bekommt 5 Zeilen (Warum/Alternativen/Tradeoffs).
- **P0/P1/P2 überall:** Priorität in PRD, Tests, Bugs, Marketing-Experimente – gleiche Sprache, weniger Chaos.

