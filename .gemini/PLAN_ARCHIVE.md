# Vector Protocol Plan

## 1. Intent
Implement structural and documentation fixes identified in the `protocol-review/FINAL_REPORT.md` to enhance documentation consistency, eliminate state mutation contradictions, and introduce operational robustness (circuit breakers, deadlocks, rollback).

## 2. Success Criteria & Definition of Done
- `SKILL.md` forbids subagents from directly modifying root state files (`PLAN.md`, `STATE.md`, `EVIDENCE.md`).
- Redundancy between `AGENTS.md` and `GEMINI.md` is eliminated.
- Operational robustness guidelines (circuit breakers like `MAX_ITERATIONS`, deadlock arbitration, rollback) are formally documented.
- All structural updates are grouped into mutually exclusive parallel batches.

## 3. Dependencies
- `.gemini/tasks/protocol-review/FINAL_REPORT.md` (reviewed)

## 4. Side Effects
- Future agent runs will strictly adhere to fractal writes and utilize circuit breakers to prevent infinite loops.

## 5. Unknowns & Hypotheses
- Assuming `GEMINI.md` should serve as a high-level pointer/manifest rather than duplicating the entire `AGENTS.md` ruleset.

## 6. Execution Roadmap

### [PARALLEL BATCH 1]
- [x] Task 1: Fix Shared State Mutation rules in `skills/vector/SKILL.md`. (Task: `protocol-fixes/task-1-shared-state`)
- [x] Task 2: Eliminate redundancy in `GEMINI.md` by referencing `AGENTS.md`. (Task: `protocol-fixes/task-2-gemini-redundancy`)
- [x] Task 3: Add operational robustness principles (rollback, deadlocks, cleanup) to `AGENTS.md`. (Task: `protocol-fixes/task-3-robustness-agents`)
- [x] Task 5: Align manifest in `gemini-extension.json`. (Task: `protocol-fixes/task-5-manifest`)

### [PARALLEL BATCH 2]
- [x] Task 4: Integrate `MAX_ITERATIONS` circuit breakers and align loop terminology in `skills/vector/SKILL.md`. (Task: `protocol-fixes/task-4-robustness-skill`)
