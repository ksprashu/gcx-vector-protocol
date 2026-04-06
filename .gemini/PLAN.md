# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Harden `/vector:work` for empty plans and implement the DORA Metrics Dashboard Output from the backlog.

## 2. Strategic Analysis
- **Harden `/vector:work`:** The agent currently hallucinates or fails ungracefully when no arguments are provided and all tasks in `.gemini/PLAN.md` are marked complete. We must update `commands/vector/work.toml` (Protocol 2: Task Retrieval) to explicitly check for the "All tasks complete" state and halt cleanly with a helpful message recommending `/vector:plan`.
- **DORA Metrics Dashboard:** A backlog item requests a visual representation of `METRICS.json`. We will implement a new command (`commands/vector/metrics.toml`) that reads the metrics file and outputs a clean Markdown dashboard. We must also register this command in `gemini-extension.json`.
- **Risk:** Low. Modifications to `work.toml` are text-based prompt adjustments. Creating a new command follows the established extension pattern.

## 3. Implementation Roadmap
- [x] **Task 1: Harden `/vector:work` Task Retrieval** - Edit `commands/vector/work.toml` to explicitly instruct the agent to halt cleanly if `{{args}}` is empty AND there are no pending (`- [ ]`) or failing (`- [!]`) tasks.
- [x] **Task 2: Create `/vector:metrics` Command** - Implement `commands/vector/metrics.toml` with instructions to read `.gemini/METRICS.json` and format it as a markdown table/dashboard.
- [x] **Task 3: Register `/vector:metrics`** - Update `gemini-extension.json` to include the new command and increment the minor version.

## 4. Review
Plan established. Ready to Execute?
