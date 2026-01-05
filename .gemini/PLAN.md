# 🗺️ PLAN

## Current Objective
Enforce strict "Stopping Criteria" and prevent slash command execution in shell.

## Rationale
The agent's "eagerness" to follow its own recommendations breaks the human-in-the-loop protocol. We must explicitly forbid autonomous phase transitions and clarify the nature of slash commands (User Input vs. Shell Command).

## Strategy
1.  **Protocol-Level Constraint:** Update `GEMINI.md` (root) to explicitly ban `run_shell_command("/vector:...")`.
2.  **Prompt-Level Constraint:** Update `scan.toml`, `plan.toml`, and `work.toml` to reinforce "WAIT for user input" and "DO NOT execute recommendation".

## Roadmap
- [x] **Step 1: Update `GEMINI.md` (Protocol Definition)**
    - Target: The root `GEMINI.md` file (not `.gemini/GEMINI.md`).
    - Action: Ensure "6. ANTI-PATTERNS" section includes:
        - "NEVER execute `/vector:*` commands via `run_shell_command`. These are USER INPUTS only."
        - "NEVER autonomously transition phases. WAIT for user input."
- [x] **Step 2: Update `commands/vector/scan.toml`**
    - Action: Add explicit warning to `prompt`: "**CRITICAL:** NEVER use `run_shell_command` to execute `/vector:*` commands. These are for the USER to type."
- [x] **Step 3: Update `commands/vector/plan.toml`**
    - Action: Add the same explicit warning to `prompt`.
- [x] **Step 4: Update `commands/vector/work.toml`**
    - Action: Add the same explicit warning to `prompt`.
    - Action: Reinforce "Stopping Criteria" to prevent auto-looping without instruction.
- [x] **Step 5: Verification**
    - Action: Read all modified files to ensure the constraints are present and syntactically correct (TOML string escaping).

## Active Spec
*Focus on adding the "ANTI-PATTERNS" section and hardening the "Stopping Criteria" in TOML files.*