import {
  getBudgetProvider,
  getCandidateReview,
  getDeadEnds,
  getKnownIssues,
  getTask,
  getTasks,
} from "./mock-api.js";

const dashboardEl = document.getElementById("dashboard");
const tasksEl = document.getElementById("tasks");
const taskDetailEl = document.getElementById("task-detail");
const candidateReviewEl = document.getElementById("candidate-review");
const deadEndCenterEl = document.getElementById("dead-end-center");
const budgetProviderEl = document.getElementById("budget-provider");
const knownIssuesEl = document.getElementById("known-issues");

function statusBadge(status) {
  const cls = status === "done" ? "done" : status === "blocked" ? "blocked" : "running";
  return `<span class="badge ${cls}">${status}</span>`;
}

function renderDashboard(tasks) {
  const running = tasks.filter((t) => t.status === "running").length;
  const blocked = tasks.filter((t) => t.status === "blocked").length;
  const done = tasks.filter((t) => t.status === "done").length;

  dashboardEl.innerHTML = `
    <h2>Dashboard</h2>
    <div class="grid">
      <article class="card"><h3>Running Tasks</h3><div class="metric">${running}</div></article>
      <article class="card"><h3>Blocked Tasks</h3><div class="metric">${blocked}</div></article>
      <article class="card"><h3>Done Tasks</h3><div class="metric">${done}</div></article>
      <article class="card"><h3>Total</h3><div class="metric">${tasks.length}</div></article>
    </div>
  `;
}

function renderTasks(tasks) {
  const rows = tasks
    .map(
      (task) => `
      <tr>
        <td><button class="open-task" data-task-id="${task.id}">${task.id}</button></td>
        <td>${task.title}</td>
        <td>${statusBadge(task.status)}</td>
        <td>${task.owner}</td>
        <td>${task.risk}</td>
      </tr>
    `
    )
    .join("");

  tasksEl.innerHTML = `
    <h2>Tasks</h2>
    <div class="card">
      <table>
        <thead>
          <tr><th>ID</th><th>Title</th><th>Status</th><th>Owner</th><th>Risk</th></tr>
        </thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
  `;

  tasksEl.querySelectorAll(".open-task").forEach((button) => {
    button.addEventListener("click", async () => {
      const task = await getTask(button.dataset.taskId);
      renderTaskDetail(task);
      switchView("task-detail");
    });
  });
}

function renderTaskDetail(task) {
  if (!task) {
    taskDetailEl.innerHTML = `<h2>Task Detail</h2><p>Task nicht gefunden.</p>`;
    return;
  }

  const stepItems = task.steps
    .map((step) => `<li><strong>${step.id}</strong> · ${step.kind} · ${statusBadge(step.status)}</li>`)
    .join("");

  const auditRows = task.audit
    .map((entry) => `<tr><td>${entry.ts}</td><td>${entry.event}</td><td>${entry.actor}</td></tr>`)
    .join("");

  taskDetailEl.innerHTML = `
    <h2>Task Detail: ${task.id}</h2>
    <div class="grid">
      <article class="card">
        <h3>Objective</h3>
        <p>${task.objective}</p>
      </article>
      <article class="card">
        <h3>Scope</h3>
        <p><strong>includes:</strong> ${task.scope.includes.join(", ")}</p>
        <p><strong>excludes:</strong> ${task.scope.excludes.join(", ")}</p>
      </article>
      <article class="card">
        <h3>Budget</h3>
        <p>tokens: ${task.budget.tokens}</p>
        <p>tool_calls: ${task.budget.tool_calls}</p>
        <p>wall_time_s: ${task.budget.wall_time_s}</p>
      </article>
    </div>

    <div class="card">
      <h3>Step Timeline</h3>
      <ul class="timeline">${stepItems}</ul>
    </div>

    <div class="card">
      <h3>Audit Stream</h3>
      <table>
        <thead><tr><th>Timestamp</th><th>Event</th><th>Actor</th></tr></thead>
        <tbody>${auditRows}</tbody>
      </table>
    </div>
  `;
}

function renderKnownIssues(issues) {
  knownIssuesEl.innerHTML = `
    <h2>Known Issues</h2>
    <div class="card">
      <ul>
        ${issues.map((issue) => `<li><strong>${issue.id}</strong> [${issue.section}] — ${issue.text}</li>`).join("")}
      </ul>
    </div>
  `;
}

function renderCandidateReview(review) {
  if (!review) {
    candidateReviewEl.innerHTML = `<h2>Candidate Review</h2><p>Keine Candidate-Daten vorhanden.</p>`;
    return;
  }
  const validationRows = review.validation
    .map((row) => `<tr><td>${row.rule}</td><td>${row.severity}</td><td>${row.outcome}</td></tr>`)
    .join("");
  const comparisonRows = Object.entries(review.comparison.dimensions)
    .map(([key, value]) => `<tr><td>${key}</td><td>${value}</td></tr>`)
    .join("");

  candidateReviewEl.innerHTML = `
    <h2>Candidate Review (${review.candidateId})</h2>
    <div class="grid">
      <article class="card">
        <h3>Validation</h3>
        <table>
          <thead><tr><th>Rule</th><th>Severity</th><th>Outcome</th></tr></thead>
          <tbody>${validationRows}</tbody>
        </table>
      </article>
      <article class="card">
        <h3>Comparison (${review.comparison.classification})</h3>
        <table>
          <thead><tr><th>Dimension</th><th>Delta</th></tr></thead>
          <tbody>${comparisonRows}</tbody>
        </table>
      </article>
    </div>
  `;
}

function renderDeadEndCenter(deadEnds) {
  const rows = deadEnds
    .map(
      (event) => `<tr><td>${event.taskId}</td><td>${event.stepId}</td><td>${event.category}</td><td>${event.priority}</td><td>${event.at}</td></tr>`
    )
    .join("");
  deadEndCenterEl.innerHTML = `
    <h2>Dead-End Center</h2>
    <div class="card">
      <table>
        <thead><tr><th>Task</th><th>Step</th><th>Category</th><th>Priority</th><th>Timestamp</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
  `;
}

function renderBudgetProvider(payload) {
  if (!payload) {
    budgetProviderEl.innerHTML = `<h2>Budget & Provider</h2><p>Keine Daten vorhanden.</p>`;
    return;
  }

  budgetProviderEl.innerHTML = `
    <h2>Budget & Provider</h2>
    <div class="grid">
      <article class="card">
        <h3>Budget</h3>
        <p>Tokens: ${payload.budget.tokens_used} / ${payload.budget.tokens_limit}</p>
        <p>Tool calls: ${payload.budget.tool_calls_used} / ${payload.budget.tool_calls_limit}</p>
      </article>
      <article class="card">
        <h3>Provider</h3>
        <p>Provider: ${payload.provider.provider_id}</p>
        <p>Model: ${payload.provider.model_id}</p>
        <p>Tool use: ${payload.provider.supports_tool_use ? "yes" : "no"}</p>
      </article>
    </div>
  `;
}

function switchView(viewId) {
  document.querySelectorAll(".view").forEach((view) => view.classList.add("hidden"));
  document.getElementById(viewId).classList.remove("hidden");

  document.querySelectorAll(".nav-btn").forEach((button) => {
    button.classList.toggle("active", button.dataset.view === viewId);
  });
}

async function main() {
  const tasks = await getTasks();
  const issues = await getKnownIssues();
  const review = await getCandidateReview("task-01");
  const deadEnds = await getDeadEnds();
  const budgetProvider = await getBudgetProvider("task-01");

  renderDashboard(tasks);
  renderTasks(tasks);
  renderTaskDetail(tasks[0]);
  renderCandidateReview(review);
  renderDeadEndCenter(deadEnds);
  renderBudgetProvider(budgetProvider);
  renderKnownIssues(issues);

  document.querySelectorAll(".nav-btn").forEach((button) => {
    button.addEventListener("click", () => switchView(button.dataset.view));
  });
}

main();
