# Vector Protocol Plan: Auto-Commit Authorization Fix

## 1. Intent
Ensure the `/vector:work` cycle successfully performs the final commit after completing all tasks, satisfying the "Working tree is clean" requirement of the Merge-Readiness Checklist.

## 2. Success Criteria & Definition of Done
- The conflict between the global anti-commit mandate and the `/vector:work` final commit step is resolved.
- `commands/vector/work.toml` explicitly instructs the orchestrator to perform `git add` and `git commit` at the end of the execution loop.
- `AGENTS.md` and `GEMINI.md` explicitly override the global anti-commit rule for the final step of the `/vector:work` command.
- The working tree is left clean upon successful completion of the work cycle.

## 3. Dependencies
- `commands/vector/work.toml`
- `AGENTS.md`
- `GEMINI.md`

## 4. Side Effects
- The agent will now automatically commit changes to the local repository history at the end of a successful `/vector:work` run.
- Unintended changes could be committed if the `vector-critic` validation is flawed, placing higher importance on test coverage.

## 5. Unknowns & Hypotheses
- **Hypothesis**: The global context mandate "Do not stage or commit changes unless specifically requested by the user" is currently preventing the agent from executing the final commit step in `commands/vector/work.toml`. By adding explicit authorization and clear CLI instructions to the project-level context (`AGENTS.md`, `GEMINI.md`) and the command prompt, the orchestrator will safely perform the commit.

## 6. Execution Roadmap

[PARALLEL BATCH]
- [x] Task 1: Update Command Prompt (.gemini/tasks/task-7/)
  - Modify `commands/vector/work.toml` under "State Synchronization & Handoff".
- [x] Task 2: Update Protocol Mandates (.gemini/tasks/task-8/)
  - Modify `AGENTS.md` section 7 (Merge-Readiness Checklist).
- [x] Task 3: Update Local GEMINI.md (.gemini/tasks/task-9/)
  - Apply the same updates to `GEMINI.md` and `.gemini/GEMINI.md` to ensure context parity.

[SEQUENTIAL]
- [x] Task 4: Verify and Commit (.gemini/tasks/task-10/)
  - Validate that the updated markdown and TOML files are syntactically correct.
  - Run the commit to apply these protocol updates.
