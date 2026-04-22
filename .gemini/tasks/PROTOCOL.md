# Fractal State System Protocol

This protocol defines the hierarchical directory structure and file naming conventions for the Vector Protocol's "Zero-Context Orchestrator" and "Fractal File System".

## 1. Directory Hierarchy
All task-specific state is stored in `.gemini/tasks/`.
The structure is flat relative to the `tasks/` directory to prevent deep nesting issues, but logically fractal:

- `.gemini/tasks/task-[ID]/`
    - `PLAN.md`: Localized roadmap for this specific task.
    - `STATE.md`: Localized execution log, phase, and scratchpad.
    - `EVIDENCE.md`: Localized factual findings.
    - `FEEDBACK.md`: Critique entries from the `critic` subagent.
    - `CODE_REVIEV.md` (Optional): Formal code review logs.

## 2. The Deep Dissection Schema
Every `PLAN.md` (master or fractal) MUST include the following sections to ensure thorough goal decomposition:

1. **Intent:** A clear narrative of what the user wants to achieve.
2. **Success Criteria & Definition of Done:** Measurable metrics and a final checklist.
3. **Dependencies:** List of files, tools, or other tasks required.
4. **Side Effects:** Potential impact on other modules or the project state.
5. **Unknowns & Hypotheses:** Assumptions that need verification.
6. **Execution Roadmap:** Atomic, numbered implementation steps.

## 3. Communication Protocol
Subagents MUST NOT return large payloads to the Main Orchestrator. 
They must:
1. Write their findings/work to the task-specific files.
2. Return a status string in the format: `[STATUS] <Short Description>. Path: <File Path>`

Example: `[SUCCESS] Wrote subtask roadmap to .gemini/tasks/task-001/subtask-A/PLAN.md`

## 4. State Persistence
The `STATE.md` in each task folder is the authoritative record for that task. 
- **Phase:** Current phase of the sub-task (e.g., `[DRAFTING]`, `[CRITIQUE]`, `[IMPLEMENTING]`, `[VERIFYING]`).
- **Last Action:** The most recent tool call or logical step completed.
- **Scratchpad:** A chronological append-only log of findings.
