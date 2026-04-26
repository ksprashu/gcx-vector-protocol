# Instruction Consistency Audit: AGENTS.md vs skills/vector/SKILL.md

## Overview
An audit was conducted to compare `AGENTS.md` and `skills/vector/SKILL.md` to identify contradictions, redundancies, and terminology inconsistencies in the Vector Protocol instructions.

## 1. Contradictions

### Shared State Mutation
*   **`AGENTS.md` (Section 5):** Enforces a strict "Lock-Free Filesystem Persistence Mandate," stating explicitly: *"Subagents MUST NEVER write directly to shared root files like `STATE.md` or `PLAN.md`."*
*   **`SKILL.md` (Section 2, Step 1):** Instructs the orchestrator to *"Call the `vector-planner` subagent to generate or update the plan in `.gemini/PLAN.md` (or the specific fractal path)."*
*   **`SKILL.md` (Section 3, Step 2):** Instructs the `vector-tester` to *"log evidence to STATE.md or EVIDENCE.md".*
*   **Conflict:** `SKILL.md` suggests the planner might write directly to `.gemini/PLAN.md` and the tester might write directly to `STATE.md` or `EVIDENCE.md`. These instructions directly violate the strict anti-mutation rule for root state files established in `AGENTS.md`. The orchestrator (or a sync script) should be the only entity writing to root files after aggregating from fractal paths.

## 2. Redundancies

Several core concepts are duplicated almost verbatim across both documents. While reinforcement is sometimes helpful for LLMs, these redundancies increase token usage:
*   **Truth Hierarchy:** Both documents list the exact same 4-tier hierarchy (Direct Input -> Repository Truth -> Executed Evidence -> External References).
*   **Citation Hygiene:** Both emphasize using Evidence IDs (`[E-XYZ]`) linked to `EVIDENCE.json`.
*   **Zero-Context Mandate:** Both heavily emphasize avoiding direct implementation, delegating to subagents, and relying on filesystem state.

## 3. Terminology Inconsistencies

### Loop Naming
*   **`AGENTS.md`:** Refers broadly to the execution cycle as the **"Dynamic Multi-Angle Loop (Implement -> Test -> Critique)"**. (Note: Older project context also refers to it as the "Ralph Wiggum Loop").
*   **`SKILL.md`:** Codifies this into two specific, distinct loops: the **"Dynamic Planning Loop"** (Draft -> Critique -> Evaluate) and the **"Dynamic Execution Loop"** (Implement -> Test -> Critique -> Loop/Exit). 
*   **Recommendation:** Align the terminology so `AGENTS.md` reflects the distinct planning and execution loops defined in `SKILL.md`.

## Conclusion
The most critical issue is the contradiction regarding who is permitted to write to root state files. `SKILL.md` needs to be updated to strictly forbid both the `vector-planner` and `vector-tester` from writing to root state files (`PLAN.md`, `STATE.md`, `EVIDENCE.md`), enforcing that they only write to their fractal paths (e.g., `.gemini/tasks/task-ID/PLAN.md`), which are then aggregated.
