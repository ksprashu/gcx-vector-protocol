# SPEC: Fix Shared State Mutation in SKILL.md

## Objective
Update `skills/vector/SKILL.md` to strictly forbid subagents (like `vector-planner` and `vector-tester`) from directly modifying root state files (`.gemini/PLAN.md`, `STATE.md`, `EVIDENCE.md`).

## Requirements
- Identify instructions in `SKILL.md` that tell subagents to write to root files.
- Replace them with instructions to write exclusively to their specific fractal paths (e.g., `.gemini/tasks/task-ID/PLAN.md`).
- Emphasize that root aggregation is handled by the orchestrator or synchronization scripts.
