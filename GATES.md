# 🚪 GATES — DEAFPIPER

---

## 🔜 Nächste Gates

### Gate DP-011: Pipeline Runner CLI
- **Branch:** `gate/dp-011-runner-cli`
- **To-Dos:**
  - [ ] CLI zum Starten einer Pipeline-Stage
  - [ ] Input/Output-Validation pro Stage
  - [ ] Stage-Chaining (auto-continue)
  - [ ] Error-Recovery mit Checkpoint
- **Akzeptanz:** Stage per CLI startbar mit Validation
- **Kill:** Stage ohne Input-Check

### Gate DP-012: Quality Gate Automation
- **Branch:** `gate/dp-012-quality-gates`
- **To-Dos:**
  - [ ] Automatische Quality-Gate-Checks
  - [ ] Go/No-Go Report pro Stage
  - [ ] Threshold-Konfiguration
  - [ ] Blockierung bei Failed Gate
- **Akzeptanz:** Quality Gates blockieren fehlerhafte Stages
- **Kill:** Quality Gates nur informativ

### Gate DP-013: Template Engine v2
- **Branch:** `gate/dp-013-template-v2`
- **To-Dos:**
  - [ ] Jinja2-basierte Templates
  - [ ] Variablen-Injection aus Pipeline-Context
  - [ ] Template-Vererbung
  - [ ] Preview-Mode
- **Akzeptanz:** Templates mit Variablen renderbar
- **Kill:** Hardcoded Templates

### Gate DP-014: Multi-Provider Support
- **Branch:** `gate/dp-014-multi-provider`
- **To-Dos:**
  - [ ] OpenAI, Anthropic, Google als Provider
  - [ ] Fallback-Chain bei Provider-Ausfall
  - [ ] Cost-Tracking pro Provider
  - [ ] Provider-spezifische Prompt-Anpassung
- **Akzeptanz:** Pipeline läuft mit ≥2 Providern
- **Kill:** Single-Provider-Lock-In
