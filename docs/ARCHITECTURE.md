# DEAFPIPER Pipeline Architecture

## 1. Executive Summary

This document formalizes a shared, project-agnostic development execution pipeline. Its purpose is to impose structure on AI-assisted software development: reducing regression, preventing scope drift, making each development step auditable, reproducible, and comparable over time.

The pipeline governs the sequence: **Planning → Tests → Execution → Validation → Comparison → Decision**. It is an orchestration and control layer, not a product.

---

## 2. Architectural Goals

- Enforce a test-first, validation-gated development loop
- Make every execution step traceable and auditable
- Provide explicit comparison between candidate outputs and baselines
- Prevent fake completion and hidden scope creep
- Support controlled agent-mode execution with explicit stop conditions
- Keep documentation and implementation state synchronized
- Support future routing of tasks to different AI providers, models, or tools
- Enable reproducible decisions: same inputs must produce same decision logic

---

## 3. Non-Goals

- Not a monolithic all-in-one application
- Not an end-user product or UI
- Not a prompt collection or prompt library
- Not a CI/CD replacement (no deployment, no environment management)
- Not domain logic for any specific project
- Not an autonomous agent with open-ended goals
- Not a conversation interface

---

## 4. Core Concepts

**Pipeline**: An ordered sequence of Steps belonging to a Task, governed by Constraints, producing ArtifactCandidates, evaluated by ValidationRules, compared against baselines, and decided upon by a PromotionDecision.

**Validation-First**: No step output is accepted until it passes its ValidationRules. Passing tests is necessary but not sufficient — comparison against baseline is also required.

**Baseline**: The last known-good ArtifactCandidate against which new candidates are compared. Promotion replaces the baseline. Rejection preserves it.

**Dead End**: A formal state in which the pipeline cannot proceed without human input or architectural change. Dead ends are logged, not papered over.

**Maintenance Discipline**: Known bugs, deferred work, and documentation drift are first-class artifacts managed within the pipeline, not afterthoughts in commit history.

---

## 5. Core Object Model

| Object | Responsibility |
|---|---|
| **Task** | Top-level unit of work with defined scope and acceptance criteria |
| **Step** | Single executable action within a Task |
| **Constraint** | Rule that bounds what a Step or Task may touch or change |
| **ArtifactCandidate** | Output produced by a Step, awaiting validation and comparison |
| **ValidationRule** | Formal check that an ArtifactCandidate must satisfy |
| **TestResult** | Outcome of executing a ValidationRule against an ArtifactCandidate |
| **ComparisonResult** | Structured diff between a candidate and the current baseline |
| **PromotionDecision** | Formal record of promote / reject / rework with rationale |
| **AuditEntry** | Immutable log record of any state transition or decision |
| **BudgetPolicy** | Rules governing token, cost, time, and tool-call limits |
| **AgentInstructionSet** | Complete, bounded specification for one agent execution run |

---

## 6. Object Relationships

```
Task
 ├── has many → Step
 ├── has many → Constraint
 ├── has one  → AgentInstructionSet (optional, per agent run)
 └── has one  → BudgetPolicy

Step
 ├── belongs to → Task
 ├── produces   → ArtifactCandidate (0..n)
 ├── governed by → Constraint (inherited + local)
 └── emits      → AuditEntry (n)

ArtifactCandidate
 ├── evaluated by → ValidationRule (n)
 ├── produces     → TestResult (n, one per ValidationRule)
 ├── compared via → ComparisonResult (vs. baseline)
 └── resolved by  → PromotionDecision (exactly one)

PromotionDecision
 ├── references → ArtifactCandidate (the subject)
 ├── references → ComparisonResult
 ├── references → TestResult[]
 └── emits      → AuditEntry

AuditEntry
 └── immutable, append-only; references any object by ID
```

**Key invariants:**
- An ArtifactCandidate without a PromotionDecision is `pending`, never `done`.
- A PromotionDecision without a complete set of TestResults is invalid.
- A Step cannot produce an ArtifactCandidate outside its declared Constraints.
- A Task is not closed until every Step has a terminal state.

---

## 7. Required Fields per Object

### Task
- `id` (stable identifier)
- `title`
- `objective` (single sentence, outcome-focused)
- `scope` (explicit in/out list)
- `acceptance_criteria` (list of testable statements)
- `constraints` (list of Constraint IDs)
- `budget_policy_id`
- `status` (`draft | ready | running | blocked | done | abandoned`)
- `created_at`, `updated_at`
- `parent_task_id` (nullable)

**Invariants**: `scope` must enumerate explicit exclusions. `acceptance_criteria` must be mechanically checkable.
**Failure risks**: vague objectives, unbounded scope, acceptance criteria that only humans can judge.

### Step
- `id`
- `task_id`
- `index` (ordering within task)
- `kind` (`plan | test | execute | validate | compare | decide | document`)
- `objective`
- `inputs` (list of artifact or data references)
- `expected_outputs` (declared artifact types)
- `constraints` (local, merged with Task constraints)
- `status` (`pending | running | produced | validated | compared | decided | blocked | skipped`)
- `started_at`, `finished_at`

**Invariants**: every Step must declare `expected_outputs`. A Step cannot transition to `decided` without a PromotionDecision referencing its artifact.
**Failure risks**: steps producing undeclared outputs, steps that silently skip validation.

### Constraint
- `id`
- `scope` (`task | step | global`)
- `kind` (`path_allow | path_deny | action_allow | action_deny | resource_limit | policy`)
- `predicate` (machine-readable rule or reference)
- `rationale` (why this constraint exists)
- `source` (`user | policy | inherited`)

**Invariants**: deny rules override allow rules. Constraints must be evaluable without human interpretation.
**Failure risks**: constraints written as prose only, conflicting constraints with no precedence.

### ArtifactCandidate
- `id`
- `step_id`
- `type` (`code_diff | test_file | doc | config | plan | report`)
- `content_ref` (hash or path to content)
- `produced_at`
- `producer` (agent id, model id, version)
- `baseline_ref` (nullable; what baseline this candidate aims to replace)
- `status` (`produced | validating | validated | compared | decided`)

**Invariants**: `content_ref` must be content-addressable. Two identical candidates must have identical refs.
**Failure risks**: non-deterministic content, candidates that mutate after creation.

### ValidationRule
- `id`
- `applies_to` (artifact type or tag)
- `kind` (`test_suite | static_check | schema | policy | human_gate`)
- `executor` (how to run it)
- `pass_criteria` (machine-readable)
- `severity` (`blocker | warning | info`)

**Invariants**: every rule must declare pass criteria that do not depend on wall-clock or randomness (unless explicitly seeded).
**Failure risks**: rules that pass because no test was run, rules stored only as prose.

### TestResult
- `id`
- `artifact_candidate_id`
- `validation_rule_id`
- `outcome` (`pass | fail | error | skipped`)
- `detail` (structured, including logs/diff)
- `duration_ms`
- `executed_at`
- `environment_ref` (reproducibility hash)

**Invariants**: `skipped` requires an explicit reason. `error` is distinct from `fail`.
**Failure risks**: conflating error with fail, missing environment hash.

### ComparisonResult
- `id`
- `artifact_candidate_id`
- `baseline_ref`
- `dimensions` (map of metric → delta; e.g. `tests_passing`, `coverage`, `complexity`, `lint_warnings`, `performance_score`)
- `classification` (`improvement | regression | neutral | mixed`)
- `blocking_regressions` (list of dimension keys)

**Invariants**: `mixed` requires explicit listing of both gains and regressions. Missing baseline means classification `no_baseline`, not `improvement`.
**Failure risks**: comparing against the wrong baseline, hiding regressions under net-positive framing.

### PromotionDecision
- `id`
- `artifact_candidate_id`
- `decision` (`promote | reject | rework | defer`)
- `rationale`
- `test_results` (references)
- `comparison_result_id`
- `deferred_issues` (list of KnownIssue IDs if decision = defer)
- `decided_by` (agent or human id)
- `decided_at`

**Invariants**: `promote` requires all blocker ValidationRules passing and no `regression` classification without override. `defer` requires at least one KnownIssue entry.
**Failure risks**: promote decisions without rationale, silent overrides.

### AuditEntry
- `id` (monotonic)
- `timestamp`
- `actor` (agent, model, user)
- `subject_type`, `subject_id`
- `event` (`created | transitioned | produced | validated | compared | decided | overridden | escalated`)
- `previous_state`, `new_state`
- `payload_ref` (content-addressable blob)

**Invariants**: append-only, never mutated. No gaps in sequence per subject.
**Failure risks**: incomplete logging, log entries without subject references.

### BudgetPolicy
- `id`
- `limits` (map: `tokens`, `cost_usd`, `wall_time_s`, `tool_calls`, `steps`)
- `on_breach` (`stop | escalate | downgrade_model`)
- `scope` (`task | step | run`)

**Invariants**: at least one limit must be set. `on_breach` must be declared.
**Failure risks**: uncapped runs, silent breaches.

### AgentInstructionSet
See Section 13 for full schema.

---

## 8. State Transitions and Execution Lifecycle

### Task lifecycle

```
draft → ready → running → { done | blocked | abandoned }
                    ↓
                 (blocked) → ready   (after resolution)
```

Transition rules:
- `draft → ready`: requires non-empty `objective`, `scope`, `acceptance_criteria`, `constraints`, `budget_policy_id`
- `ready → running`: first Step transitions to `running`
- `running → done`: every Step has terminal state AND every acceptance_criterion has a passing ValidationRule
- `running → blocked`: any Step hits a dead end with `escalation_path = human`
- `running → abandoned`: explicit user action, requires rationale

### Step lifecycle

```
pending → running → produced → validated → compared → decided
                                   ↓           ↓         ↓
                                 blocked     blocked   blocked
                                   ↓
                                skipped (requires justification)
```

### ArtifactCandidate lifecycle

```
produced → validating → validated → compared → decided
                 ↓
            invalid (terminal; triggers rework Step)
```

### Full execution path (happy)

```
Task(ready)
  → Step[plan].produced Plan artifact
  → Step[test].produced TestSuite artifact
  → Step[execute].produced CodeDiff artifact
  → Step[validate] runs ValidationRules → TestResults
  → Step[compare] produces ComparisonResult vs baseline
  → Step[decide] produces PromotionDecision
  → AuditEntry emitted at every transition
Task(done) iff all acceptance_criteria satisfied
```

### Full execution path (rework)

```
...Step[decide] → PromotionDecision(reject | rework)
  → new Step created with kind=execute, inputs including prior ComparisonResult
  → loop bounded by BudgetPolicy (max rework iterations)
```

---

## 9. Validation Model

Validation is layered. A candidate must pass all applicable layers before comparison.

### Layers (in evaluation order)

1. **Structural** — artifact is well-formed (parses, lints, matches schema)
2. **Constraint** — artifact respects declared Constraints (no forbidden paths, no forbidden actions)
3. **Test** — declared test suites pass (unit, integration, property)
4. **Policy** — security, licensing, style policies pass
5. **Human gate** (optional, only where declared) — explicit sign-off required

### Rules

- A `blocker`-severity failure at any layer halts the candidate at `invalid`.
- A `warning`-severity failure is recorded but does not halt.
- Skipped rules require a recorded reason; they do not count as passing.
- Every rule must produce exactly one TestResult per candidate run.
- Validation environment hash must be recorded; divergent environments invalidate the result.

### Anti-patterns this model forbids

- "Tests passed locally" without recorded TestResults
- Treating absence of test as evidence of correctness
- Conflating lint warnings with passing tests
- Silent skipping when a test harness is unavailable

---

## 10. Comparison Model

Comparison is mandatory, not optional. A candidate without a ComparisonResult cannot be promoted.

### What is compared

- **Functional**: which ValidationRules pass on candidate vs. baseline
- **Quality**: coverage, complexity, duplication, lint warnings
- **Performance**: declared benchmarks (where applicable)
- **Surface**: public API, schema, config shape (for breaking-change detection)
- **Size**: diff size, file churn (signal for scope creep)

### Against what baseline

- **Primary baseline**: the last `promoted` ArtifactCandidate for the same scope
- **Origin baseline**: the state at Task creation (to detect net regression across multiple iterations)
- **Sibling baseline** (optional, reserved): parallel candidates from alternative agent runs

### Rules

- Comparison metrics must be declared up front per Task (in acceptance_criteria or Constraints)
- A metric without a declared direction (`higher_is_better` / `lower_is_better`) cannot contribute to classification
- `mixed` classification requires explicit enumeration of both gains and losses
- `no_baseline` is a distinct classification; it does not count as `improvement`
- A regression in any declared blocking dimension produces `regression` regardless of gains elsewhere

### Result classes

| Class | Meaning | Default next action |
|---|---|---|
| `improvement` | Strict improvement in at least one dimension, no regressions | eligible for `promote` |
| `neutral` | No meaningful change in any dimension | eligible for `reject` or `promote` with rationale |
| `mixed` | Both gains and non-blocking regressions | requires explicit rationale to promote |
| `regression` | At least one blocking regression | `reject` or `rework` |
| `no_baseline` | No prior baseline exists | eligible for `promote` as initial baseline |

---

## 11. Promotion / Reject / Rework Decision Model

A PromotionDecision is the formal resolution of an ArtifactCandidate. It is never implicit.

### Decision classes

| Decision | Meaning | Required conditions |
|---|---|---|
| `promote` | Candidate replaces the baseline | All blocker ValidationRules pass; ComparisonResult is `improvement`, `neutral`, or `no_baseline`; or `mixed`/`regression` with explicit override |
| `reject` | Candidate is discarded | Any blocker ValidationRule fails, OR `regression` without override; no rework will be attempted |
| `rework` | Candidate is discarded, a new Step is created to produce a new candidate | Rework iterations below budget limit; failure is understood well enough to retry |
| `defer` | Candidate is set aside; issue logged for future | Explicit out-of-scope finding; requires KnownIssue entry |

### Decision logic (deterministic)

```
Inputs: TestResults[], ComparisonResult, BudgetPolicy, overrides[]

IF any TestResult.outcome == error:
    decision = rework IF rework_budget_remaining ELSE reject
    reason = "execution error, not logical failure"

ELSE IF any blocker TestResult.outcome == fail:
    IF failure_is_diagnosable AND rework_budget_remaining:
        decision = rework
    ELSE:
        decision = reject

ELSE IF ComparisonResult.classification == regression:
    IF override{actor=human, scope=this_decision} exists:
        decision = promote (flagged)
    ELSE:
        decision = reject OR rework

ELSE IF ComparisonResult.classification == mixed:
    IF rationale_explains_tradeoff AND override exists:
        decision = promote
    ELSE:
        decision = rework OR defer

ELSE IF classification in [improvement, neutral, no_baseline]:
    decision = promote

ELSE:
    decision = reject (unclassifiable)
```

### Traceability requirements

Every PromotionDecision must record:
- The exact set of TestResult IDs examined
- The exact ComparisonResult ID examined
- The rationale (non-empty string; template-filled rationale is not acceptable for regression overrides)
- The actor (agent ID + model ID + version, OR human user ID)
- Any override references with explicit scope
- The BudgetPolicy state at decision time (how much budget remains)

### Anti-patterns forbidden

- Promoting without reviewing ComparisonResult
- Rejecting without emitting an AuditEntry that says why
- Rework loops without iteration counter
- `defer` without a KnownIssue entry
- Silent acceptance of regressions as "acceptable for now"
- Promotion by inaction (timeout-based acceptance)

### Override discipline

Overrides exist to handle legitimate edge cases (e.g. deliberate performance tradeoff). They must:
- Be scoped to a specific PromotionDecision (never blanket)
- Carry an explicit human actor
- Carry rationale that names the specific regression being accepted
- Emit a distinct AuditEntry kind: `override_applied`
- Be reviewable via audit query: "show all overrides in last N days"

---

## 12. Audit and Traceability Model

The audit trail is the ground truth of the pipeline. Without it, decisions are not reproducible.

### Core principles

- **Append-only**: AuditEntry records are never modified or deleted
- **Complete**: Every state transition emits an AuditEntry
- **Content-addressable**: Large payloads referenced by hash, stored separately
- **Monotonic**: AuditEntry IDs are strictly increasing per subject
- **Queryable**: State at any past point must be reconstructible

### What generates an AuditEntry

Any of the following events:
- Object created (Task, Step, ArtifactCandidate, etc.)
- State transition (any lifecycle transition)
- Artifact produced
- ValidationRule executed (one AuditEntry per TestResult)
- ComparisonResult produced
- PromotionDecision recorded
- Override applied
- Budget breach detected
- Dead end triggered
- Escalation raised

### AuditEntry payload

```
{
  id: monotonic_sequence_id,
  timestamp: iso8601_utc,
  actor: { type: agent|human|system, id: string, model_id?: string, version?: string },
  subject: { type: Task|Step|ArtifactCandidate|..., id: string },
  event: created|transitioned|produced|validated|compared|decided|overridden|escalated|budget_breached|dead_end,
  previous_state: string | null,
  new_state: string | null,
  payload_ref: content_hash,
  context_refs: [related_subject_ids]
}
```

### Reconstruction contract

Given the audit log and the content store, the system must be able to:
- Reconstruct the full state of any Task at any past timestamp
- List all ArtifactCandidates produced for a Task
- Show the exact TestResults a PromotionDecision considered
- Trace the chain of rework iterations
- Identify all overrides applied in a date range
- Identify all dead ends and their escalations

### Storage model (implementation guidance, not mandate)

Two tiers:
- **Index tier**: structured records (AuditEntry metadata), queryable by subject and time
- **Content tier**: content-addressable blob store for large payloads (diffs, logs, reports)

Either tier can be file-based, database-based, or object-store-based; the abstraction is a seam.

### Traceability queries (required)

The audit system must support at minimum:
- `get_history(subject_id)` — full AuditEntry chain for one object
- `reconstruct_state(subject_id, at_timestamp)` — state at a past moment
- `list_overrides(since, until)` — all override events in a window
- `list_dead_ends(since, until)` — all dead-end events in a window
- `list_rework_chains(task_id)` — full rework iteration chain for a Task

### Failure risks

- Missing AuditEntry for a state transition (breaks reconstruction)
- Payload stored inline with index (bloats storage, degrades query)
- Non-monotonic IDs (makes ordering ambiguous)
- Content store diverging from index (broken refs)

---

## 13. AgentInstructionSet Schema

An AgentInstructionSet is the complete, bounded specification handed to an agent for exactly one execution. It replaces free-form prompt crafting with a structured contract.

### Schema (concrete, translatable to JSON/YAML/DB)

```yaml
instruction_set:
  id: string
  version: semver
  task_ref: string
  step_ref: string
  created_at: iso8601

  objective:
    statement: string
    success_signal: string

  scope:
    includes:
      - path: string
        rationale: string
    excludes:
      - path: string
        rationale: string
    touch_limit:
      max_files_changed: integer
      max_lines_changed: integer

  constraints:
    - id: string
      kind: path_allow|path_deny|action_allow|action_deny|resource_limit|policy
      predicate: string | object
      severity: blocker|warning

  inputs:
    - ref: artifact_id | data_ref
      kind: plan|test|prior_diff|spec|doc|comparison_result
      required: boolean

  required_artifacts:
    - kind: plan|test_file|code_diff|doc|report
      schema_ref: string
      min_count: integer
      max_count: integer

  validation:
    applicable_rules:
      - id: string
        severity: blocker|warning
    pre_execution_checks:
      - id: string

  dead_end:
    max_iterations: integer
    max_tool_calls: integer
    max_wall_time_s: integer
    on_repeated_identical_output: stop|escalate
    on_ambiguous_requirement: stop|escalate
    on_constraint_violation_attempt: stop

  escalation_path:
    trigger: dead_end|budget_breach|unresolvable_ambiguity
    destination: human_review|parent_task|policy_arbiter
    payload_template: string

  budget:
    tokens: integer
    cost_usd: decimal
    wall_time_s: integer
    tool_calls: integer
    on_breach: stop|escalate|downgrade_model

  allowed_tools:
    - tool_id: string
      scope: { paths?: [string], actions?: [string] }

  context_refs:
    - ref: string
      kind: doc|audit_entry|prior_decision
      inclusion_reason: string
```

### Validation rules for the InstructionSet itself

Before handing to an agent, the InstructionSet must pass:
- `objective.statement` is non-empty and single-sentence
- `scope.includes` is non-empty OR scope explicitly declared global
- `scope.excludes` names all paths that must not be touched
- `required_artifacts` is non-empty (agent must produce something)
- `validation.applicable_rules` is non-empty (output will be judged)
- `dead_end` has at least `max_iterations` set
- `escalation_path` has a valid destination
- `budget` inherits from BudgetPolicy without exceeding it
- `allowed_tools` is an explicit allow-list (default-deny)

### Instantiation

An AgentInstructionSet is built by an `InstructionBuilder` at Step start time:
- Inherits Task-level constraints, scope, budget
- Adds Step-level specifics (inputs, expected outputs)
- Validates completeness before execution
- Stored as an artifact itself; referenced by AuditEntry

### Invariants

- An agent execution without a valid InstructionSet is forbidden
- An InstructionSet is immutable once execution starts
- Changes require a new InstructionSet ID (new execution)
- The InstructionSet is archivable and replayable

### Why this matters

- Eliminates the category of "what was the agent actually told?"
- Makes execution comparable across runs (same instruction, different model)
- Enables deterministic replay for debugging
- Forms the basis for provider/model routing (same instruction, different provider)

---

## 14. Dead-End and Stop-Rule Design

Dead ends are not failures of the pipeline. They are correct outputs when the work cannot proceed under current constraints.

### Categories of dead end

1. **Budget exhaustion** — tokens, cost, wall time, or tool calls exceeded
2. **Repeated identical output** — agent produced the same artifact hash N times in a row
3. **Unresolvable ambiguity** — requirement cannot be interpreted deterministically
4. **Constraint conflict** — declared constraints contradict each other
5. **Missing input** — required input artifact is unavailable
6. **Validation loop** — rework iterations exceeded without progress
7. **Scope breach attempt** — agent repeatedly attempts excluded paths
8. **External dependency unavailable** — required tool/service not reachable

### Detection rules

```
budget_exhaustion:
  trigger: cumulative_tokens >= budget.tokens OR
           cumulative_cost >= budget.cost_usd OR
           elapsed_time_s >= budget.wall_time_s OR
           tool_call_count >= budget.tool_calls

repeated_identical_output:
  trigger: last_N_artifact_hashes all equal, where N = 2

unresolvable_ambiguity:
  trigger: agent emits ambiguity_marker OR
           same question asked twice without new information

constraint_conflict:
  trigger: constraint_evaluator returns CONFLICT for the current scope

missing_input:
  trigger: required input ref resolves to null OR invalid

validation_loop:
  trigger: rework_iteration_count >= budget.rework_iterations AND
           no progress delta (same failing rules)

scope_breach_attempt:
  trigger: attempted_path matches scope.excludes, N times in run

external_dependency_unavailable:
  trigger: tool_broker returns UNAVAILABLE for required tool
```

### Stop action per category

| Category | Action | Escalation destination |
|---|---|---|
| Budget exhaustion | `stop` | Per `on_breach` policy |
| Repeated output | `stop` | Human review |
| Unresolvable ambiguity | `stop` | Human review |
| Constraint conflict | `stop` | Task owner |
| Missing input | `stop` | Parent Task or Task owner |
| Validation loop | `stop` | Human review with full rework chain |
| Scope breach | `stop` | Human review; flag as policy issue |
| External dependency | `stop` (retryable) | System operator |

### Escalation payload

When a dead end is triggered, the EscalationHandler produces a structured payload:

```
{
  task_ref, step_ref, instruction_set_ref,
  dead_end_category,
  detector_output: {...},
  full_rework_chain: [artifact_ids],
  last_validation_results: [test_result_ids],
  last_comparison_result: comparison_result_id,
  budget_state: {...},
  recommended_human_actions: [string],
  audit_ref: audit_entry_id
}
```

This payload is:
- Emitted as an AuditEntry (`event: escalated`)
- Routed to the declared `escalation_path.destination`
- Stored for reconstruction

### Anti-patterns forbidden

- Silent retry after dead end (retries require new InstructionSet)
- Marking Task `done` while a dead end is unresolved
- Burying dead-end output in logs without AuditEntry
- Inventing work to continue past a dead end ("scope creep via desperation")
- Empty escalation payloads

### The stop-rule principle

**"Work until the next real dead end, then stop."**

This means:
- Agents run to the first unresolvable obstacle, not to a time or token ceiling (though those exist as backstops)
- A clean stop with a structured escalation is a successful outcome
- Detection is proactive, not post-hoc
- The pipeline prefers visible incompletion over invisible completion

---

## 15. Budget / Provider / Tool Abstraction Seams

These are seams — interfaces designed now, implementations deferred. They exist to prevent hard-coded assumptions that will need to be ripped out later.

### Required now

**BudgetPolicy object** (Section 7) is fully specified. BudgetEnforcer must:
- Track cumulative consumption per Task and per Step
- Evaluate `on_breach` before every Step execution and artifact production
- Emit AuditEntry on breach
- Support at minimum: tokens, cost_usd, wall_time_s, tool_calls, rework_iterations

### Reserved for later

**ProviderResolver** — decides which model/provider executes a given Step.

Seam shape:
```
ProviderResolver.resolve(instruction_set, policy) -> ProviderBinding
```
Where `ProviderBinding` includes:
- provider_id (anthropic, openai, local, etc.)
- model_id (claude-opus-4-7, etc.)
- endpoint_ref
- cost_profile
- capabilities

The seam is an interface; implementation can be trivial (single provider) initially.

**ModelCapabilityRegistry** — declares what each model can do.

Seam shape:
```
ModelCapabilityRegistry.query(model_id) -> Capabilities
```
Where `Capabilities` includes:
- supports_tool_use: bool
- max_context_tokens: int
- typical_cost_per_million_in: decimal
- typical_cost_per_million_out: decimal
- known_limitations: [string]

Used by ProviderResolver to match InstructionSet requirements to capable models.

**ToolBroker** — gateway for all tool access from agents.

Seam shape:
```
ToolBroker.invoke(tool_id, params, context) -> Result
```
Enforcement responsibilities:
- Check `allowed_tools` in active InstructionSet
- Apply Constraint predicates to tool invocation
- Emit AuditEntry for every tool call
- Return structured errors, not raw exceptions
- Respect budget (`tool_calls` counter)

Required policies:
- Default-deny: tools not in `allowed_tools` are rejected
- Path-scoped: file tools receive path predicates
- Action-scoped: network tools receive action predicates
- No fallback: a denied tool call is logged and surfaced, not silently bypassed

**CostAccountant** — normalizes cost across providers.

Seam shape:
```
CostAccountant.record(execution_ref, tokens, duration, provider_binding) -> void
CostAccountant.summarize(task_ref) -> CostSummary
```

Used by BudgetEnforcer to convert provider-specific metrics into the unified budget dimensions.

### Explicitly out of scope (for now)

- Automatic model downgrade on budget pressure (seam exists via `on_breach: downgrade_model`, but no logic)
- Cross-provider response quality comparison
- Dynamic pricing optimization
- Parallel provider races for same InstructionSet
- Tool marketplace or plugin registry

### Why the seams matter now

If these seams are not designed up front:
- BudgetEnforcer will assume a single cost model, breaking multi-provider later
- Tool access will be scattered across the codebase, preventing auditability
- Provider selection will be hard-coded, preventing A/B testing
- Cost tracking will be inconsistent, preventing reliable budget enforcement

Designing the seams costs little now. Retrofitting them later is expensive and error-prone.

### Integration points with other sections

- **AgentInstructionSet** (Section 13) references `allowed_tools` — consumed by ToolBroker
- **BudgetPolicy** (Section 7) limits — enforced by BudgetEnforcer via CostAccountant
- **AuditEntry** (Section 12) — every tool call, every breach, every provider binding logged
- **Dead-End detection** (Section 14) — `budget_exhaustion` and `external_dependency_unavailable` detectors plug into these seams

---

## 16. Repository Hygiene and Maintenance Model

Maintenance discipline is a structural requirement, not a post-hoc cleanup activity.

### Known Issues Registry

Every project repository must maintain a `KNOWN_ISSUES.md` file at the root level. This is not a bug tracker; it is a first-class artifact.

**Purpose**: Make undocumented major issues invalidate "done" claims.

**Content**:
```markdown
# Known Issues

## Pre-existing (before Task X)
- [ISSUE_001] Description. Impact: {low|medium|high}. Workaround: {none|user-facing|internal}.

## Introduced in Task X (Date)
- [ISSUE_NEW_001] Description. Root cause: {brief}. Remediation: {defer to Task Y | fix by date | blocked on {external dependency}}.

## Deferred by decision
- [ISSUE_DEFERRED_001] (from Task Y) Rationale: {why it was not fixed}. Decision record: {PromotionDecision ID}.

## Fixed
- ~~[ISSUE_002]~~ Fixed in Task Z, merged {date}.
```

**Rules**:
- Every newly introduced issue identified during validation must be logged with its PromotionDecision ID.
- Deferral requires explicit rationale that explains why it was not in-scope.
- A Task cannot be marked `done` if it introduces unlogged blockers or high-impact deferred issues without explicit override.
- Pre-existing issues must be distinguished from new ones; the prefix captures this.

### README Freshness Contract

The `README.md` file must stay synchronized with implementation state.

**Mandatory sections**:
- Quick start (must run without errors)
- Architecture overview (link to ARCHITECTURE.md)
- Project status (list what is stable / in-progress / planned)
- Known limitations (link to KNOWN_ISSUES.md)
- Setup and test instructions

**Refresh rules**:
- If a Step introduces changes to how the project is set up, or adds/removes a major dependency, README must be updated in the same commit.
- If README quick-start fails, the Task is not done.
- `README.md` mtime must be >= the latest commit time in the default branch (enforcement: CI check).

### Architecture Documentation Drift Prevention

`ARCHITECTURE.md` (this document or its successor) is the source of truth for design decisions.

**Refresh rules**:
- Any architectural decision (new object type, new state transition, new seam) must update ARCHITECTURE.md in the same commit or clearly documented as deferred in KNOWN_ISSUES.md.
- If implementation contradicts ARCHITECTURE.md, the implementation is a bug, not a feature.
- Drift is detected by: code review, CI linting, or periodic manual audit.

### Implementation Status Visibility

A `STATUS.md` file tracks high-level completion per major component.

**Template**:
```markdown
# Implementation Status

| Component | Status | Last Updated | Notes |
|---|---|---|---|
| Task model | complete | 2026-04-15 | All fields implemented |
| Step model | complete | 2026-04-15 | State machine validated |
| Validation model | partial | 2026-04-16 | Structural layer done; policy layer deferred |
| Comparison model | in-progress | 2026-04-18 | Metrics framework implemented |
| Audit model | not-started | - | Reserved for Q2 |
```

**Rules**:
- Updated monthly or after major Tasks.
- Drives visibility into what's blocked, partial, or deferred.
- Feeds into communication and planning.

### Change Log for Architectural Decisions

A `CHANGELOG_ARCHITECTURE.md` documents when significant design shifts occur.

**Entries**:
```
## 2026-04-18
- Added `dead_end` block to AgentInstructionSet (Section 14).
  Rationale: Prevent silent looping and fake completion.
  Affected: Agent execution layer, escalation handling.
```

**Rules**:
- One entry per architectural change.
- Rationale is mandatory.
- Tied to Task IDs or PromotionDecision IDs when applicable.
- Helps future maintainers understand the evolution of the system.

### Pre-existing vs. Newly Introduced Issues

**Pre-existing**: Issues that exist in the baseline before a Task starts.
- Marked in KNOWN_ISSUES.md with a pre-existing tag.
- A Task is not required to fix them unless they are in scope.
- If a Task exacerbates a pre-existing issue, that is a new regression.

**Newly introduced**: Issues created by a Task's output.
- Identified during validation.
- Logged with the PromotionDecision ID that allowed them through.
- Either fixed before promotion or deferred with explicit rationale.

**Never ambiguous**: every issue must be classified as one or the other. Unmarked issues are a hygiene violation.

### Maintenance Checklist (per Task)

Before marking a Task `done`:

- [ ] KNOWN_ISSUES.md updated (new issues logged, pre-existing vs. new distinguished)
- [ ] README.md quickstart tested and updated if changed
- [ ] ARCHITECTURE.md reflects any design changes
- [ ] STATUS.md updated if component completion changed
- [ ] CHANGELOG_ARCHITECTURE.md entry added if applicable
- [ ] All AuditEntries linked and traceable
- [ ] No blocker-severity ValidationRules remain unresolved

---

## 17. Recommended Module / Folder Structure

This is a practical structure for implementing the architecture. Adapt per language / framework; keep the logical separation.

```
repository_root/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── KNOWN_ISSUES.md
│   ├── STATUS.md
│   ├── CHANGELOG_ARCHITECTURE.md
│   └── examples/
│       ├── example_task_01.md
│       └── example_promotion_flow.md
│
├── src/
│   ├── pipeline/
│   │   ├── task
│   │   ├── step
│   │   ├── artifact_candidate
│   │   ├── validation_rule
│   │   ├── test_result
│   │   ├── comparison_result
│   │   ├── promotion_decision
│   │   └── audit_entry
│   │
│   ├── lifecycle/
│   │   ├── task_lifecycle
│   │   ├── step_lifecycle
│   │   └── artifact_lifecycle
│   │
│   ├── validation/
│   │   ├── validation_runner
│   │   ├── rule_registry
│   │   └── builtin_rules/
│   │       ├── structural
│   │       ├── test_suite
│   │       ├── lint
│   │       └── policy
│   │
│   ├── comparison/
│   │   ├── comparator
│   │   ├── metrics_registry
│   │   └── baseline_loader
│   │
│   ├── decision/
│   │   ├── decision_engine
│   │   └── override_policy
│   │
│   ├── audit/
│   │   ├── audit_logger
│   │   ├── audit_query
│   │   └── content_store
│   │
│   ├── agent_instruction/
│   │   ├── instruction_set
│   │   ├── instruction_builder
│   │   └── instruction_validator
│   │
│   ├── dead_end/
│   │   ├── stop_detector
│   │   ├── escalation_handler
│   │   └── dead_end_rules
│   │
│   ├── budget/
│   │   ├── budget_policy
│   │   └── budget_enforcer
│   │
│   └── constraints/
│       ├── constraint
│       └── constraint_evaluator
│
├── tests/
│   ├── unit/
│   ├── integration/
│   │   ├── test_end_to_end_flow
│   │   ├── test_rework_loop
│   │   ├── test_dead_end_handling
│   │   └── test_audit_trail
│   └── fixtures/
│
├── tools/
│   ├── inspect_task
│   └── replay_audit
│
├── examples/
│   ├── simple_task.json
│   ├── simple_instruction_set.yaml
│   └── sample_promotion_decision.json
│
├── README.md
├── KNOWN_ISSUES.md
├── STATUS.md
└── CHANGELOG_ARCHITECTURE.md
```

**Key principles**:
- `src/pipeline/` is the core domain model (import first, test heavily).
- `src/lifecycle/` and `src/decision/` contain business logic.
- `src/audit/` is append-only, immutable (enforce at the module level).
- `tests/integration/` exercises end-to-end flows; a single test should cover Task → Step → Artifact → Validation → Comparison → Decision.
- No "utils" folder; logic lives in appropriately named modules.

---

## 18. Example End-to-End Execution Flow

**Scenario**: Implement input validation for a user registration endpoint. Task has max 3 rework iterations and a token budget of 10K tokens.

### Setup phase

```
1. Task created (status: draft)
   - objective: "Add validation to registration endpoint"
   - scope: { includes: [src/api/register/], excludes: [src/db/, infra/] }
   - acceptance_criteria:
       [ "All required fields validated before DB insert",
         "All tests pass (>80% coverage)",
         "No new lint warnings",
         "No backward-incompatible API changes" ]
   - constraints: [no_new_deps, no_schema_breaking_changes]
   - budget: {tokens: 10_000, rework_iterations: 3}

2. Task transitioned to ready

3. AuditEntry emitted: task.transitioned(draft → ready)
```

### Execution phase

```
4. Step[0] created: kind=plan → produces Plan artifact
5. Step[1] created: kind=test → produces TestFile artifact
6. Step[2] created: kind=execute → produces CodeDiff artifact
```

### Validation phase

```
7. Step[3] created: kind=validate
   - applies ValidationRules: unit_tests (blocker), lint (warning),
     type_check (blocker), coverage_min_80 (blocker)
8. All rules pass → TestResult per rule, all status: pass
```

### Comparison phase

```
9. Step[4] created: kind=compare
   - dimensions: tests_passing +100%, coverage +13%, lint_warnings =,
     api_surface unchanged
   - classification: improvement
```

### Decision phase

```
10. Step[5] created: kind=decide
    - All blocker rules pass, no regressions
    - PromotionDecision: promote
    - rationale: "All tests pass, coverage improved to 85%, no regressions"
11. Baseline updated. Task transitioned to done.
```

### Rework scenario (alternative)

If unit_tests had failed:
- ComparisonResult = regression
- PromotionDecision: rework
- New Step[6] created with prior diff + failing TestResult as input
- Budget tracks: 2 rework iterations remaining
- If next candidate passes: promoted, Task done
- If all rework iterations exhausted: Task blocked, escalated

### Audit trail (selected entries)

```
AuditEntry[001]: task_01.created
AuditEntry[002]: task_01.transitioned(draft → ready)
AuditEntry[003]: step_01.produced(plan_01)
...
AuditEntry[014]: pd_01.recorded(promote)
AuditEntry[015]: task_01.transitioned(running → done)
```

---

## 19. Failure Modes and Drift Risks

### Drift: Implementation diverges from ARCHITECTURE.md
**Symptom**: Code implements a state machine that doesn't match Section 8.
**Prevention**: Code review, automated checks, required updates to ARCHITECTURE.md on design changes.
**Remedy**: Fix code to match, or update ARCHITECTURE.md with rationale in CHANGELOG_ARCHITECTURE.md.

### Drift: README quickstart breaks
**Symptom**: Setup instructions no longer work.
**Prevention**: README updates required in the same commit as setup changes; CI runs README quickstart.
**Remedy**: Update README and re-test.

### Drift: Known issues are forgotten
**Symptom**: Deferred issues never surface in planning.
**Prevention**: KNOWN_ISSUES.md high-visibility; STATUS.md tracks deferred items; Task acceptance_criteria must account for known high-impact issues.
**Remedy**: Review KNOWN_ISSUES.md and STATUS.md before starting any Task.

### Failure: Fake completion (silent validation skip)
**Symptom**: An ArtifactCandidate promoted without ValidationRules executed.
**Prevention**: PromotionDecision requires non-empty test_results; status cannot become `decided` without PromotionDecision reference.
**Remedy**: Enforce cardinality; any candidate without TestResults is invalid.

### Failure: Undetected constraint violation
**Symptom**: Agent modifies an excluded path.
**Prevention**: Constraint evaluation runs statically over diffs before artifact acceptance.
**Remedy**: Strengthen constraint detection; fail validation with blocker severity.

### Failure: Rework loop never terminates
**Symptom**: Agent produces candidates failing the same validation repeatedly.
**Prevention**: BudgetPolicy max_rework_iterations; dead_end detector on repeated identical output.
**Remedy**: Escalate instead of looping; mark Task blocked.

### Failure: Comparison against wrong baseline
**Symptom**: Candidate compared to archived baseline.
**Prevention**: ComparisonResult requires explicit baseline_ref; baseline promotion is atomic.
**Remedy**: Validate baseline_ref matches expected primary before accepting ComparisonResult.

### Failure: Override policy bypassed
**Symptom**: Regression-classified candidate promoted without override.
**Prevention**: Decision logic checks classification; regression promotion requires override + human actor.
**Remedy**: Enforce in decision engine; reject any promote that violates override policy.

### Failure: Budget exhaustion unnoticed
**Symptom**: Agent runs over budget without halt.
**Prevention**: BudgetEnforcer tracks cumulative; on_breach action triggers; AuditEntry logs breach.
**Remedy**: Enforce budget checks before every Step; fail fast.

---

## 20. Definition of Done

A Task is `done` if and only if:

1. Every Step is in a terminal state.
2. Every acceptance criterion is satisfied by a passing ValidationRule (or explicitly waived with recorded rationale).
3. Every ArtifactCandidate has a PromotionDecision.
4. Every PromotionDecision is traceable: complete TestResults, ComparisonResult, AuditEntry chain.
5. Newly introduced issues are logged in KNOWN_ISSUES.md with pre-existing vs. new distinction.
6. Deferred work has KnownIssue entries with rationale and remediation plan.
7. No blocker validations remain unresolved (unless explicitly overridden with recorded rationale).
8. README.md quickstart runs end-to-end without error; significant changes reflected.
9. ARCHITECTURE.md reflects design changes made, or the deltas are logged as deferred in CHANGELOG_ARCHITECTURE.md.
10. Budget within policy; any breach has `on_breach` action recorded.
11. AuditEntry chain is unbroken from Task creation to closure.
12. No validation rule skipped without recorded reason.

---

## 21. Suggested Implementation Order

Strict dependency order. Each phase depends on prior phases.

### Phase 1: Core objects (no state machine yet)
**Goal**: Data model serializable and storable.
1. `Constraint` (value object)
2. `BudgetPolicy` (value object)
3. `Task` (all required fields, no state validation yet)
4. `Step`
5. `ArtifactCandidate`
6. `ValidationRule`
7. `TestResult`
8. `AuditEntry` (append-only store)

**Deliverable**: Objects serialize to JSON/YAML cleanly.

### Phase 2: State machines and transitions
**Goal**: Enforce legal state transitions.
1. `TaskLifecycle`
2. `StepLifecycle`
3. `ArtifactLifecycle`
4. Transition validators per Section 8

**Deliverable**: Invalid transitions rejected; legal ones succeed.

### Phase 3: Validation framework
**Goal**: Execute ValidationRules and produce TestResults.
1. `ValidationRunner`
2. `RuleRegistry`
3. Builtin rules: structural, test_suite, lint, policy
4. `ConstraintEvaluator`

**Deliverable**: Runner executes 5+ rules against a candidate and produces TestResult per rule.

### Phase 4: Comparison and decision
**Goal**: Compare candidates and make promotion decisions.
1. `Comparator`
2. `MetricsRegistry`
3. `ComparisonResult` generation with classification
4. `DecisionEngine`

**Deliverable**: End-to-end candidate → validation → comparison → decision with full audit trail.

### Phase 5: Audit and traceability
**Goal**: Immutable audit trail.
1. `AuditLogger` (append-only)
2. `AuditQuery` (reconstruction)
3. `ContentStore` (content-addressable)
4. Tests: reconstruct full Task state from audit log.

**Deliverable**: Audit log is immutable, queryable, sufficient to replay any state.

### Phase 6: Agent instruction and execution
**Goal**: Formalize agent boundaries.
1. `AgentInstructionSet` schema and validation
2. `InstructionBuilder`
3. `InstructionValidator`
4. Format: JSON/YAML schema

**Deliverable**: Valid InstructionSet can be given to an agent; output accepted by system.

### Phase 7: Dead-end and escalation
**Goal**: Stop detection and escalation.
1. `StopDetector` (all 8 categories)
2. `EscalationHandler`
3. `DeadEndRules`
4. Integration: StopDetector called before every rework.

**Deliverable**: Rework loop terminates; escalation is traceable.

### Phase 8: Budget enforcement
**Goal**: Hard budget limits.
1. `BudgetEnforcer`
2. Integration before Step execution and at artifact production
3. `on_breach` actions (stop, escalate; downgrade deferred to Phase 10)

**Deliverable**: Breaches logged; execution stops per policy.

### Phase 9: CLI and inspection tools
**Goal**: Operational visibility.
1. `inspect_task`
2. `replay_audit`
3. `list_known_issues`
4. Logging and error messages

**Deliverable**: Operators can inspect and debug a Task run without reading code.

### Phase 10 (Reserved): Provider and tool routing
**Goal**: Multi-provider and tool flexibility.
1. `ProviderResolver`
2. `ModelCapabilityRegistry`
3. `ToolBroker`
4. Cost accounting integration

**Deliverable**: Same Task runs on different models/providers; audit trail includes provider details.

### Testing strategy (throughout all phases)

- **Unit**: Individual objects and state machines.
- **Integration**: Full Task → Step → Artifact → Validation → Comparison → Decision flows.
- **Scenario**: Rework loops, dead-end detection, constraint violations, budget breaches.
- **Audit replay**: Replay Task from audit log; reconstructed state must match live state.

---

## Appendix: Document Governance

This document is the source of truth for the pipeline architecture. Changes require:

1. Update to ARCHITECTURE.md (this file)
2. Rationale entry in CHANGELOG_ARCHITECTURE.md
3. Code implementation (Phase order above)
4. AuditEntry logging for the change

Divergence between code and this document is a bug — in the document or the code.

---

**Document version**: 1.0
**Last updated**: 2026-04-18
**Status**: Foundation release, ready for Phase 1 implementation
