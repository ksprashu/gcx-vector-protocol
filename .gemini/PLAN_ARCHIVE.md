# Vector Protocol Execution Plan

## 1. Intent
The user reported a concurrency bug where subagents are running the same task in parallel threads, instead of picking up different isolated work. The intent is to update the Vector Protocol orchestrator prompts (`work.toml`, `plan.toml`, `SKILL.md`, and `README.md`) to completely remove the "multi-angle parallel implementations" logic. This will enforce a strict 1:1 mapping of distinct, independent tasks to parallel subagent threads.

## 2. Success Criteria & Definition of Done
- `commands/vector/work.toml` is updated to remove instructions for "multi-angle parallel implementations" and explicitly mandates assigning exactly one distinct task per parallel thread.
- `commands/vector/plan.toml` is updated to remove "Multi-Angle Strategies" from the planning instructions.
- `skills/vector/SKILL.md` is updated to remove the "Multi-Angle Implementations" rule and reinforce independent task dispatching.
- `README.md` is updated to remove references to the "multi-angle iteration loop".
- The orchestrator reliably dispatches different tasks to different subagents during parallel execution.

## 3. Dependencies
- Access to the `gcx-vector-protocol` codebase.
- The `gemini-cli` framework must correctly handle concurrent subagent tool calls with different arguments.

## 4. Side Effects
- Removing the multi-angle capability simplifies the Orchestrator's execution loop.
- The protocol will rely on a single implementation attempt per task per cycle, reducing token usage and overlapping execution traces.

## 5. Unknowns & Hypotheses
- **Hypothesis:** The orchestrator's behavior of repeating the same task in parallel threads is directly caused by the "multi-angle" instructions in the prompt, which tells the LLM to spawn multiple parallel subagents for the *same* task to find the best solution. 
- **Risk:** If the bug persists after prompt adjustments, there may be a deeper closure or mapping bug in the `gemini-cli` core's handling of parallel tool calls, which would require investigating `useGeminiStream` or the `SubagentGroupDisplay`.

## 6. Execution Roadmap

### [PARALLEL BATCH 1]
- [x] Task 1: Update `commands/vector/work.toml` to remove "multi-angle parallel implementations" and strictly mandate mapping distinct tasks to separate threads. Use `.gemini/tasks/task-update-work/` for isolation.
- [x] Task 2: Update `skills/vector/SKILL.md` to replace "Multi-Angle Implementations" with strict independent task parallelization. Use `.gemini/tasks/task-update-skill/` for isolation.
- [x] Task 3: Update `commands/vector/plan.toml` to remove "Multi-Angle Strategies" from the planning phase. Use `.gemini/tasks/task-update-plan/` for isolation.
- [x] Task 4: Update `README.md` to remove references to "multi-angle iteration loop". Use `.gemini/tasks/task-update-readme/` for isolation.

### [PARALLEL BATCH 2]
- [x] Task 5: Run integration tests (`scripts/e2e_test.py`) to verify that independent tasks are now correctly executed concurrently by different subagents without duplication. Use `.gemini/tasks/task-verify-e2e/` for isolation.
