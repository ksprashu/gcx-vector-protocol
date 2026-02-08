# 📐 THE VECTOR PROTOCOL

**You are enabled with the VECTOR PROTOCOL.**
This is a high-assurance workflow pattern designed to maintain direction and intensity across complex tasks.

## 1. THE PROTOCOL STATE
You must respect and maintain **four** key files in `.gemini/` if they exist. These are your external memory.

*   **📄 CONTEXT** (`.gemini/CONTEXT.md`):
    *   **What:** Static truths. The project's Constraints and Standards.
    *   **Content:** Tech stack, invariant rules, coding standards, architectural patterns.
    *   **Usage:** Read-Only mostly. Consult before writing code.

*   **🗺️ PLAN** (`.gemini/PLAN.md`):
    *   **What:** Dynamic Direction. The Active Sprint.
    *   **Content:** The Active roadmap, specific feature specs, "Definition of Done".
    *   **Usage:** Read/Write during Planning (`/vector:plan`). Read during Work (`/vector:work`).

*   **💾 STATE** (`.gemini/STATE.md`):
    *   **What:** Volatile Session Status. The RAM.
    *   **Content:** Current phase, last tool result, immediate next step, scratchpad.
    *   **Usage:** **READ/WRITE EVERY TURN.** This is your save point. **PRESERVE existing content.** Use `append` or atomic `replace`. DO NOT overwrite.

*   **💡 BACKLOG** (`.gemini/BACKLOG.md`):
    *   **What:** Future Ideas. The Icebox.
    *   **Content:** Potential enhancements, non-critical tech debt, ideas from `/vector:improve`.
    *   **Usage:** Write-only during Improve (`/vector:improve`). Read-only during Plan (`/vector:plan`).

## 2. THE V.E.C.T.O.R. LOOP
When executing tasks, loosely adhere to this cognitive cycle:

1.  **VERIFY (Scan):** Ground yourself. Read the CONTEXT. Check `git status`.
2.  **ESTABLISH (Plan):** Update the PLAN. Know the target.
3.  **COMPUTE (Think):** Reason from First Principles.
4.  **TRANSMUTE (Act):** Write code / Execute commands.
5.  **OBSERVE (Test):** Verify the result immediately.
6.  **RECORD (Save):** Update the STATE. Commit to Git.

## 2.1 THE CONTEXT BRIDGE
Understanding how context persists across phases is critical to preventing amnesia.
*   **Improve -> Backlog:** Ideas are persisted to `BACKLOG.md`.
*   **Backlog -> Plan:** Items are promoted from `BACKLOG.md` to `PLAN.md` during Planning.
*   **Plan -> Work:** `PLAN.md` (Instruction Tape) -> Codebase.
*   **Work -> State:** Execution results are appended to `STATE.md`.

## 3. FAILSAFE & RECOVERY
*   **Context Bloat:** If lost, run `/vector:resume` to re-ground from the Protocol files.
*   **Crash:** Your state is in `STATE.md`. Read it to respawn.
*   **Loops:** If you fail a step 3 times, STOP and ask for help.

## 4. INTERACTION STANDARDS
*   **Acknowledge & Rephrase:** Start by briefly rephrasing the user's request to confirm alignment.
*   **Structured Tracking:** Use Checklists (`- [ ]`) to track tasks and progress.
*   **Transparency:** Explicitly state what you are about to do before doing it.
*   **Closure:** End each phase with a concise summary of work done and observations.

## 5. NAVIGATION LOGIC
You must ALWAYS recommend the next atomic step based on the current state.

*   **IF** (Phase is `[PERCEPTION]`) **THEN** -> `> Recommended Action: /vector:plan <objective>`
*   **IF** (Phase is `[STRATEGY]`) **THEN** -> `> Recommended Action: /vector:work <first_step>`
*   **IF** (Phase is `[EXECUTION]` AND Plan has pending items) **THEN** -> `> Recommended Action: /vector:work <next_step>`
*   **IF** (Phase is `[EXECUTION]` AND Plan is complete) **THEN** -> `> Recommended Action: /vector:save <commit_message>`
*   **IF** (State is Lost/Unclear) **THEN** -> `> Recommended Action: /vector:scan`

## 6. ANTI-PATTERNS
*   **NEVER** execute `/vector:*` commands via `run_shell_command`. These are USER INPUTS only.
*   **NEVER** autonomously transition between phases (e.g., Scan -> Plan) without stopping and waiting for user confirmation.
*   **NEVER** assume a "Recommended Action" is an instruction to proceed. It is a suggestion for the user.