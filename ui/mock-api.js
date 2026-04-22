const tasks = [
  {
    id: "task-01",
    title: "Implement validation and decision flow",
    status: "running",
    owner: "agent",
    risk: "medium",
    objective: "Make candidate evaluation deterministic.",
    scope: {
      includes: ["src/deafpiper/"],
      excludes: ["infra/"],
    },
    constraints: ["no_schema_break"],
    budget: { tokens: 10000, tool_calls: 120, wall_time_s: 7200 },
    steps: [
      { id: "s-1", kind: "plan", status: "decided" },
      { id: "s-2", kind: "execute", status: "running" },
      { id: "s-3", kind: "validate", status: "pending" },
    ],
    audit: [
      { ts: "2026-04-22T08:10:00Z", event: "created", actor: "agent" },
      { ts: "2026-04-22T08:12:00Z", event: "transitioned", actor: "agent" },
      { ts: "2026-04-22T08:19:00Z", event: "produced", actor: "agent" },
    ],
  },
  {
    id: "task-02",
    title: "UI skeleton MVP",
    status: "blocked",
    owner: "operator",
    risk: "high",
    objective: "Create dashboard and task detail read-only views.",
    scope: {
      includes: ["ui/"],
      excludes: ["src/deafpiper/"],
    },
    constraints: ["read_only"],
    budget: { tokens: 3000, tool_calls: 20, wall_time_s: 1800 },
    steps: [
      { id: "s-1", kind: "plan", status: "decided" },
      { id: "s-2", kind: "execute", status: "blocked" },
    ],
    audit: [
      { ts: "2026-04-22T07:30:00Z", event: "created", actor: "agent" },
      { ts: "2026-04-22T07:45:00Z", event: "dead_end", actor: "system" },
    ],
  },
  {
    id: "task-03",
    title: "Merge pipeline prototype",
    status: "done",
    owner: "agent",
    risk: "low",
    objective: "Move pipeline assets to root.",
    scope: {
      includes: ["playbook/", "toolbox/"],
      excludes: ["pipeline/"],
    },
    constraints: ["docs_only"],
    budget: { tokens: 5000, tool_calls: 40, wall_time_s: 3600 },
    steps: [
      { id: "s-1", kind: "execute", status: "decided" },
      { id: "s-2", kind: "document", status: "decided" },
    ],
    audit: [{ ts: "2026-04-21T18:00:00Z", event: "decided", actor: "agent" }],
  },
];

const knownIssues = [
  { id: "ISSUE_001", section: "Pre-existing", text: "No persistent storage backend for audit/content stores." },
  { id: "ISSUE_DEFERRED_001", section: "Deferred", text: "Budget downgrade_model behavior not implemented." },
];

const candidateReviews = {
  "task-01": {
    candidateId: "cand-01",
    validation: [
      { rule: "structural", severity: "blocker", outcome: "pass" },
      { rule: "test_suite", severity: "blocker", outcome: "pass" },
      { rule: "lint", severity: "warning", outcome: "warning" },
    ],
    comparison: {
      classification: "improvement",
      dimensions: { coverage: "+5%", lint_warnings: "-1", performance_score: "+2%" },
    },
  },
};

const deadEnds = [
  {
    taskId: "task-02",
    stepId: "s-2",
    category: "unresolvable_ambiguity",
    priority: "high",
    at: "2026-04-22T07:45:00Z",
  },
];

const budgetProvider = {
  "task-01": {
    budget: { tokens_used: 2500, tokens_limit: 10000, tool_calls_used: 30, tool_calls_limit: 120 },
    provider: { provider_id: "openai", model_id: "gpt-5.3-codex", supports_tool_use: true },
  },
};

export async function getTasks() {
  return tasks;
}

export async function getTask(taskId) {
  return tasks.find((task) => task.id === taskId) || null;
}

export async function getKnownIssues() {
  return knownIssues;
}

export async function getCandidateReview(taskId) {
  return candidateReviews[taskId] || null;
}

export async function getDeadEnds() {
  return deadEnds;
}

export async function getBudgetProvider(taskId) {
  return budgetProvider[taskId] || null;
}
