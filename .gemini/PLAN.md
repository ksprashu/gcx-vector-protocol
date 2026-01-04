# 🗺️ PLAN

## Current Objective
Fix `STATE.md` data loss by enforcing "Append/Preserve" semantics in Protocol Prompts.

## Rationale
User identification of "context overwrites" reveals a critical flaw. Agents default to destructive `write_file` unless explicitly instructed to `append` or `preserve`. We must code this safeguard into the prompts.

## Roadmap
- [ ] **Step 1: Update `GEMINI.md` (Protocol Definition)**
    - Redefine `STATE.md` usage: "You must PRESERVE existing content. Use APPEND or atomic REPLACEMENTS."
- [ ] **Step 2: Update `scan.toml`**
    - Instruction: "Write findings... PRESERVING any existing session history if relevant."
- [ ] **Step 3: Update `plan.toml`**
    - Instruction: "Update Phase... DO NOT overwrite the Scratchpad/Findings."
- [ ] **Step 4: Update `work.toml`**
    - Instruction: "APPEND execution logs to `STATE.md`. DO NOT overwrite previous entries."
- [ ] **Step 5: Verification**
    - Run a simulation: Scan -> Plan -> Work. Check if `STATE.md` grows or resets.

## Active Spec
*Focus on adding explicit "Preservation" constraints to the TOML prompts.*
