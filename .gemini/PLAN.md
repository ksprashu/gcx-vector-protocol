# 🗺️ PLAN

## Current Objective
Enforce strict "Stopping Criteria" and prevent slash command execution in shell.

## Rationale
The agent's "eagerness" to follow its own recommendations breaks the human-in-the-loop protocol. We must explicitly forbid autonomous phase transitions and clarify the nature of slash commands (User Input vs. Shell Command).

## Strategy
1.  **Protocol-Level Constraint:** Update `GEMINI.md` to explicitly ban `run_shell_command("/vector:...")`.
2.  **Prompt-Level Constraint:** Update `scan.toml` and `plan.toml` to reinforce "WAIT for user input" and "DO NOT execute recommendation".

## Roadmap
- [ ] **Step 1: Update `.gemini/GEMINI.md` (Protocol Definition)**
    - Add "6. ANTI-PATTERNS" section.
    - Rule 1: "NEVER execute `/vector:*` commands via `run_shell_command`."
    - Rule 2: "NEVER autonomously transition phases. WAIT for user input."
- [ ] **Step 2: Update `commands/vector/scan.toml`**
    - Update "Stopping Criteria" to be more aggressive: "WAIT for the user. Do NOT execute the recommended command."
- [ ] **Step 3: Update `commands/vector/plan.toml`**
    - Update "Stopping Criteria" similarly.
- [ ] **Step 4: Update `commands/vector/work.toml`**
    - Add constraint: "If recommending next step, STOP. Do not loop automatically unless explicitly instructed."
- [ ] **Step 5: Verification**
    - Check `GEMINI.md` for the new rules.

## Active Spec
*Focus on adding the "ANTI-PATTERNS" section and hardening the "Stopping Criteria" in TOML files.*
