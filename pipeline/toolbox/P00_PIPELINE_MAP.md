# Pipeline for Vibe Coding: Idea → Product → Build → Launch → Growth

> **NEU (Pipeline Glue):** Diese Datei ist eine **neue** Orchestrierung aus den bereinigten Prompt-Systemen dieses PDFs.  
> Ziel: Jeder Schritt erzeugt **standardisierte Outputs**, die ohne Reibungsverlust in den nächsten Schritt übergehen.

## Vorläufige Stufen (nummeriert, kann später umsortiert werden)

1. **Prompting & Learning Playbook** → `P01_PROMPTING_PLAYBOOK.md`  
2. **Research & Validation** → `P02_RESEARCH_SYSTEMS.md`  
3. **PRD & Planning** → `P03_PRD_AND_PLANNING.md`  
4. **Diagrams & Architecture** → `P04_DIAGRAMS_AND_ARCHITECTURE.md`  
5. **Computation & Data (Wolfram)** → `P05_COMPUTATION_WOLFRAM.md`  
6. **Build & Debug (R / DS workflows)** → `P06_BUILD_DEBUG_R.md`  
7. **Legal & Contracts** → `P07_LEGAL_AND_CONTRACTS.md`  
8. **Brand & Visual Design** → `P08_BRAND_AND_VISUAL_DESIGN.md`  
9. **Website & Landing Page Build** → `P09_WEBSITE_BUILD.md`  
10. **Copywriting & Messaging** → `P10_COPYWRITING_MESSAGING.md`  
11. **Content & Growth Systems** → `P11_CONTENT_GROWTH_SYSTEMS.md`  
12. **Rewrite & Tone Polish** → `P12_REWRITE_AND_TONE.md`

## Standardisierte Handoff-Formate (NEU)

### A) IDEA_BRIEF (von „Ideation“ → „Research/PRD“)
```json
{
  "product_name": "",
  "one_liner": "",
  "target_users": "",
  "primary_pain": "",
  "desired_outcome": "",
  "context_constraints": {
    "platforms": ["Windows", "Android"],
    "time_budget": "",
    "team": "",
    "no_gos": []
  },
  "success_definition": {
    "north_star_metric": "",
    "guardrails": []
  }
}
```

### B) RESEARCH_PACKET (von „Research“ → „PRD“)
```json
{
  "topic_map": [],
  "clusters": [],
  "reading_list": [
    {"title": "", "why_relevant": "", "type": "influential|recent|review"}
  ],
  "evidence_table": [
    {"paper": "", "theory": "", "method": "", "data": "", "finding": "", "limitation": ""}
  ],
  "consensus_vs_conflicts": {
    "consensus": [],
    "conflicts": []
  },
  "gaps": [
    {"gap": "", "why_matters": "", "rq": "", "hypothesis": "", "method_min_data": ""}
  ]
}
```

### C) PRD_PACKET (von „PRD“ → „Build/Design“)
```json
{
  "problem_statement": "",
  "goals": [],
  "non_goals": [],
  "target_users": [],
  "user_stories": [
    {"id": "US-001", "story": "", "acceptance_criteria": [], "priority": "P0|P1|P2"}
  ],
  "ux_flow": {"happy_path": [], "edge_cases": []},
  "metrics_instrumentation": {
    "events": [],
    "funnels": []
  },
  "milestones": [
    {"name": "", "scope": "", "exit_criteria": []}
  ],
  "risks_dependencies": []
}
```

### D) BRAND_PACKET (von „Brand/Design“ → „Website/Copy“)
```json
{
  "brand_name": "",
  "positioning": "",
  "voice": {"adjectives": [], "dos": [], "donts": []},
  "logo_directions": [],
  "palette": [],
  "typography": [],
  "design_tokens": {"spacing": "", "radius": "", "components": []}
}
```

### E) LAUNCH_PACKET (von „Copy/Website“ → „Marketing/Growth“)
```json
{
  "messaging_house": {
    "core_promise": "",
    "target_audience": "",
    "problem": "",
    "desired_outcome": "",
    "proof": "",
    "unique_mechanism": "",
    "key_messages": [],
    "objections": [],
    "rebuttals": [],
    "cta": ""
  },
  "landing_page": {"sections": [], "copy": {}},
  "ads": {"hooks": [], "variants": []},
  "emails": {"sequence": []},
  "content_system": {"pillars": [], "templates": [], "automation_prompts": []}
}
```

## Nutzung
- Verwende die Dateien `P01`–`P12` als **Bibliothek** pro Stage.  
- Handoff-JSONs oben sind die **„Stecker/Buchsen“** zwischen Bots.

