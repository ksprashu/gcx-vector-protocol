# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Allow the `/vector:work` command to intelligently resume or pick up the next task in the sequence without requiring the user to provide an explicit task name or number as an argument.

## 2. Strategic Analysis
- **Current Behavior:** `commands/vector/work.toml` strictly halts execution in "Protocol 0. Argument Check" if `{{args}}` is empty, demanding the user provide an argument. 
- **Proposed Change:** The logic to auto-identify the next pending task (`- [ ]`) or a failing task (`- [!]`) is already partially present in "Protocol 2. Task Retrieval". By removing the strict argument check and clarifying the auto-retrieval fallback, `/vector:work` will act dynamically: if an argument is provided, it prioritizes it; if empty, it picks up where the plan left off.
- **Risk:** The agent might pick the wrong task if the plan isn't perfectly structured. We mitigate this by instructing the agent to explicitly state *which* task it auto-selected.

## 3. Implementation Roadmap
- [x] **Task 1: Update Argument Check** - Edit `commands/vector/work.toml` (Protocol 0) to remove the hard stop. Allow `{{args}}` to be optional.
- [x] **Task 2: Refine Task Retrieval** - Edit `commands/vector/work.toml` (Protocol 2) to clearly instruct the agent to parse `.gemini/PLAN.md` for the first incomplete (`- [ ]`) or failing (`- [!]`) task when `{{args}}` is missing.

## 4. Review
Plan established. Ready to Execute?
