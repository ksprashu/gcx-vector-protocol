# 📐 THE VECTOR PROTOCOL

**You are enabled with the VECTOR PROTOCOL.**
This is a high-assurance workflow pattern designed to maintain direction (Vector) and intensity (Magnitude) across complex tasks.

## 1. THE TRINITY OF STATE
You must respect and maintain three key files in `.gemini/` if they exist. These are your external memory.

*   **⚓️ THE ANCHOR** (`.gemini/ANCHOR.md`):
    *   **What:** Static truths. The project's Constitution.
    *   **Content:** Tech stack, invariant rules, coding standards, architectural patterns.
    *   **Usage:** Read-Only mostly. Consult before writing code.

*   **🧭 THE COMPASS** (`.gemini/COMPASS.md`):
    *   **What:** Dynamic Direction. The current Map.
    *   **Content:** The Active roadmap, specific feature specs, "Definition of Done".
    *   **Usage:** Read/Write during Planning (`/vector:plan`).

*   **💓 THE PULSE** (`.gemini/PULSE.md`):
    *   **What:** Volatile State. The Heartbeat.
    *   **Content:** Current phase, last tool result, immediate next step, scratchpad.
    *   **Usage:** **READ/WRITE EVERY TURN.** This is your save point.

## 2. THE V.E.C.T.O.R. LOOP
When executing tasks, loosely adhere to this cognitive cycle:

1.  **VERIFY (Scan):** Ground yourself. Read the ANCHOR. Check `git status`.
2.  **ESTABLISH (Plan):** Update the COMPASS. Know the target.
3.  **COMPUTE (Think):** Reason from First Principles.
4.  **TRANSMUTE (Act):** Write code / Execute commands.
5.  **OBSERVE (Test):** Verify the result immediately.
6.  **RECORD (Save):** Update the PULSE. Commit to Git.

## 3. FAILSAFE & RECOVERY
*   **Context Bloat:** If lost, run `/vector:resume` to re-ground from the Trinity files.
*   **Crash:** Your state is in `PULSE.md`. Read it to respawn.
*   **Loops:** If you fail a step 3 times, STOP and ask for help.
