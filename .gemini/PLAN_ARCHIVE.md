# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `APPROVED`
- **Goal:** Upgrade Vector Protocol to a 2-command autonomous harness (`/vector:plan` and `/vector:work`) operating as a "Zero-Context Orchestrator", leveraging a fractal file system, subagent swarms via "Ralph Wiggum" verification loops, deep dissection, and legacy tenets.

## 2. Problem Breakdown
- **Functional:** 
    - The main agent session (CLI) suffers from context rot if it performs heavy lifting or receives verbose outputs.
    - True autonomy requires deep task breakdown (tasks -> subtasks -> sub-subtasks) without hitting context limits.
    - High-quality output requires iterative "Plan -> Critique -> Review" loops (Ralph Wiggum protocol).
    - Long-running execution requires seamless handoff between planning and implementation loops.
- **Technical Constraints & Resolution:**
    - *Constraint:* Gemini CLI subagents cannot recursively call other subagents (`geminicli.com/docs/core/subagents`).
    - *Resolution (The Zero-Context Orchestrator):* The main agent does NOT nest subagents. Instead, it acts as a flat orchestrator. It calls `planner`, which writes a task plan to disk. The main agent reads the disk, then calls `worker` for task 1. `worker` writes sub-tasks to disk. The main agent reads the disk, and calls `worker` for sub-task 1. 
    - *State Ledger:* The filesystem is the absolute truth. Subagents must return ONLY minimal status flags or file paths.

## 3. Design Discussion: The Fractal Architecture & Deep Dissection
- **Fractal File System:** To support infinitely deep task breakdown without context bloat, we will expand the 5-File System into a hierarchy:
    - `.gemini/PLAN.md` (Master Roadmap)
    - `.gemini/tasks/task-001/PLAN.md` (Subtask Roadmap)
    - `.gemini/tasks/task-001/subtask-A/STATE.md` (Execution State)
- **Deep Dissection Schema:** All `PLAN.md` files (master or fractal) MUST adhere to this strict dissection schema to ensure goals are thoroughly understood:
    1. **Intent:** What the user wants.
    2. **Success Criteria & Definition of Done:** Measurable completion metrics.
    3. **Dependencies:** What must exist before starting.
    4. **Side Effects:** What else this touches.
    5. **Unknowns & Hypotheses:** Risks and assumptions.
    6. **Execution Roadmap:** Atomic steps.
- **The "Ralph Wiggum" Loop (Plan/Critique/Implement):**
    - The `plan` command will instruct the main agent to orchestrate this sequence:
        1. Call `planner` subagent -> generates draft plan file.
        2. Call `critic` subagent -> reads draft, appends feedback file.
        3. Call `planner` subagent -> reads feedback, updates draft.
        4. (Repeat 2x). Main agent prompts user for final signoff.
    - The `work` command will orchestrate a similar loop for execution, looping autonomously until success criteria are met.

## 4. Proposed Solution: Components
1. **Consolidated Command Definition:**
    - **`/vector:plan`**: The Orchestrator for Strategy. Auto-bootstraps, delegates to `planner` and `critic` in a loop. Waits for human approval.
    - **`/vector:work`**: The Orchestrator for Execution. Auto-resumes from `PLAN.md`. Delegates to `implementer`, `tester`, and `critic`. Auto-commits on success. Loops continuously.
2. **Subagent Swarm (`.gemini/agents/`):**
    - `planner`: Specialized in breaking down goals into fractal `.gemini/tasks/` files using the Deep Dissection schema. Enforces Spec-Driven Development.
    - `implementer`: Specialized in atomic code changes. Enforces Thin Stack and pure functional paradigms.
    - `tester`: Specialized in running verification commands.
    - `critic`: Specialized in finding flaws in plans or code. Enforces Strict External Grounding.
3. **Legacy Tenets Integration:** The overarching `vector-protocol` skill and agent personas will strictly enforce the rules from `GEMINI.md` and `AGENTS.md` (Constraint-Driven Development, Truth Hierarchy, Evidence Citation).
4. **The "Zero-Context" Rule:** Every subagent's `output_format` must strictly dictate returning ONLY strings like `[SUCCESS] Wrote plan to .gemini/tasks/task-1.md` or `[FAILED] See error log in .gemini/tasks/task-1/STATE.md`.

## 5. Alternatives Considered
- *Recursive Subagents:* Rejected due to strict platform limitations. The Flat Orchestrator pattern achieves the same logical depth by using the filesystem as the call stack.

## 6. Revision History
- **2026-04-20 (Iteration 1):** Initial draft for 2-command architecture.
- **2026-04-20 (Iteration 2):** User feedback incorporated. Shifted from "nested" subagents to a "Zero-Context Orchestrator" model with a Fractal File System to respect CLI limitations while achieving infinite depth.
- **2026-04-20 (Iteration 3):** User feedback incorporated. Added Deep Dissection schema for plans, explicitly integrated legacy tenets (Spec-Driven, First Principles, Evidence), and defined the autonomous loop. Plan approved.

## 7. Implementation Roadmap
- [x] **Task 1: Architect the Subagent Personas** - Create `.gemini/agents/planner.md`, `implementer.md`, `tester.md`, and `critic.md` injecting Legacy Tenets and Zero-Context return rules.
- [x] **Task 2: Define the `vector-protocol` Skill** - Create `.gemini/skills/vector-protocol/SKILL.md` to centralize overarching architectural constraints.
- [x] **Task 3: Implement Fractal State System** - Define the directory structure protocol for `.gemini/tasks/`.
- [x] **Task 4: Refactor `plan.toml`** - Implement the Orchestrator loop (Plan -> Critique -> Review -> Repeat 2x -> Human Signoff).
- [x] **Task 5: Refactor `work.toml`** - Implement the Orchestrator loop (Do -> Review -> Test -> Critique -> Repeat) and continuous long-running logic.
- [x] **Task 6: Deprecate Redundant Commands** - Remove `scan`, `save`, `lint`, etc., from manifest and filesystem.
- [x] **Task 7: Documentation Update** - Rewrite `README.md` and `AGENTS.md`.

## 8. Review
Plan COMPLETED. Vector Protocol v2.0.0 is live.

--- Archived on 2026-04-20 ---
