# Vector Protocol Update Plan: Parallelization & Subagent Scoping

## 1. Intent
Enhance the Vector Protocol to massively parallelize independent tasks, reduce reliance on the `generalist` subagent in favor of narrowly scoped specialists (`planner`, `implementer`, `tester`, `critic`), and optimize the Ralph Wiggum loop to short-circuit immediately upon `[APPROVED]` feedback without forcing unnecessary iterations.

## 2. Success Criteria & Definition of Done
- **Full-Loop Parallelization:** The orchestrator can dispatch the entire Ralph Wiggum loop (Implement -> Test -> Critic) concurrently for multiple independent tasks.
- **Consolidated Orchestration Logic:** Swarm management and state merging logic are centralized in `skills/vector-protocol/SKILL.md`. Legacy sequential instructions are stripped from `commands/vector/work.toml`.
- **Dynamic Loop Termination:** All hardcoded "retry limits" or "iteration counts" are removed from `work.toml` and `plan.toml`. The protocol terminates early on `[APPROVED]` and continues only if drift is detected.
- **Subagent Scoping:** `generalist` usage is explicitly deprecated for standard protocol tasks. `SKILL.md` and `work.toml`/`plan.toml` enforce routing to specialists.
- **DoD:** All documentation, TOML command files, and SKILL files are updated, and the extension manifests reflect the changes.

## 3. Dependencies
- Current `gemini-extension.json` (defines the 4 specific subagents).
- `commands/vector/plan.toml` and `commands/vector/work.toml`.
- `skills/vector-protocol/SKILL.md`.

## 4. Side Effects
- Concurrent execution of full Ralph Wiggum loops requires absolute isolation in fractal directories (`.gemini/tasks/task-[ID]/`) to prevent state corruption.
- Removing retry limits allows for faster success but requires the `critic` to be highly rigorous to maintain quality.

## 5. Unknowns & Hypotheses
- *Hypothesis:* Centralizing orchestration logic in `SKILL.md` will reduce instruction conflict and improve the consistency of parallel swarm behavior.
- *Unknown:* The optimal way to consolidate large amounts of concurrent feedback without overwhelming the orchestrator's context window.

## 6. Execution Roadmap

- [x] **Task 1: Update Core Documentation (`AGENTS.md` & `README.md`)**
   - Define the "Parallel Swarm" execution model where the full Ralph Wiggum loop is executed concurrently for independent tasks.
   - Explicitly define the specialist roles and the deprecation of the `generalist`.

- [x] **Task 2: Consolidate Swarm Logic & Refine Loop (`skills/vector-protocol/SKILL.md`)**
   - **Centralization:** Move all complex orchestration, swarm management, and state merging instructions into `SKILL.md`.
   - **Short-circuiting:** Rewrite instructions to eliminate "exactly 3 times" or retry limits. Mandate immediate short-circuit on `[APPROVED]`.

- [x] **Task 3: Refactor Planning Command (`commands/vector/plan.toml`)**
   - Instruct the `planner` to identify independent tasks and group them into `[PARALLEL BATCH]` sections in `.gemini/PLAN.md`.
   - Remove any hardcoded loop constraints or iteration counts from the TOML prompt.

- [x] **Task 4: Refactor Work Command (`commands/vector/work.toml`)**
   - **Strip Legacy Logic:** Remove hardcoded sequential loop instructions and retry limits ("Limit retries to 3").
   - **Delegate Orchestration:** Redirect the orchestrator to follow the swarm logic defined in `SKILL.md`.
   - **Full-Loop Concurrency:** Update the orchestrator to dispatch independent tasks as complete parallel Ralph Wiggum loops (Implement -> Test -> Critic).

- [x] **Task 5: Update Subagent Prompts (`gemini-extension.json`)**
   - Ensure `implementer`, `tester`, and `critic` are constrained to their localized fractal directories to ensure thread-safety and state isolation during parallel execution.
