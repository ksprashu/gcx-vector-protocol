# 💾 STATE

**Phase:** [EXECUTION]
**Objective:** Implement "Next Step Recommendation" logic.

## 📝 Scratchpad
- **User Request:** Add "intelligent prompting for the next step" and "recommend the next command" to the Vector Protocol.
- **Findings:**
    - The protocol is defined by TOML prompts and a central `GEMINI.md` context.
    - Current prompts have static closing questions.
    - Need to inject logic to analyze the current state (Phase + Plan Status) and output a specific command recommendation.
- **Target Files:**
    - `.gemini/GEMINI.md`: Add global "Recommendation Logic".
    - `commands/vector/init.toml`: Recommend `/vector:scan`.
    - `commands/vector/scan.toml`: Recommend `/vector:plan`.
    - `commands/vector/plan.toml`: Recommend `/vector:work`.
    - `commands/vector/work.toml`: Recommend `/vector:work` (loop) or `/vector:save`/`/vector:scan`.
    - `commands/vector/status.toml`: Recommend based on state.
    - `commands/vector/resume.toml`: Recommend based on state.
- **Execution Log:**
    - Updated `GEMINI.md` with "5. NAVIGATION LOGIC".
    - Updated `commands/vector/init.toml`.
    - Updated `commands/vector/scan.toml`.
    - Updated `commands/vector/plan.toml`.
    - Updated `commands/vector/work.toml`.
    - Updated `commands/vector/status.toml` and `commands/vector/resume.toml`.
    - Verified `GEMINI.md` content.
