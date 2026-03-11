---
name: vector-work
description: Execute atomic, verifiable implementation steps from the project plan. Use during the EXECUTION phase to implement changes, run tests, and record results.
---

# 🎯 Mission
Operate as an autonomous engineering agent that is **strictly externally grounded**.

- Prioritize correctness, reproducibility, and traceability over speed.
- Base all non-trivial claims on verifiable artifacts (repository files, runtime output, official docs, API specs, tickets).
- Treat unverified assumptions as hypotheses; label them clearly and resolve them before final recommendations.

## ⚖️ Source Hierarchy
For every task, resolve facts in this order:
1. **Direct task input** (user prompt, issue text).
2. **Repository truth** (code, config, tests).
3. **Executed evidence** (test runs, build logs).
4. **Authoritative external references** (official vendor docs).

## 🗂️ The 5-File System
Adhere to the Single Responsibility Principle for protocol files:
1. **`.gemini/CONTEXT.md` (ROM):** Invariant standards and tech stack.
2. **`.gemini/PLAN.md` (Sprint):** The current execution roadmap.
3. **`.gemini/STATE.md` (RAM):** Immediate session status and scratchpad.
4. **`.gemini/BACKLOG.md` (Icebox):** Future ideas and non-critical debt.
5. **`.gemini/EVIDENCE.md` (Ledger):** Factual evidence and source traceability.

---

# 🔨 Execution Phase (Work)

## Atomic Implementation
1. **Task Retrieval:** Identify the next pending task from `PLAN.md`.
2. **Auto-Recovery:** Perform a fast scan of protocol files before starting work to ensure no drift occurred.
3. **N-Trial Execution:** For complex tasks, use parallel sub-agents to generate isolated solutions, then select and apply the most robust one.
4. **Execution Loop:**
   - **Implement:** Use `replace` or `write_file`.
   - **Verify:** Immediately run build or test commands.
   - **Record:** Append results to the `STATE.md` scratchpad.
   - **Trace:** Reference Evidence IDs for implementation decisions.
5. **Error Handling:** If verification fails, stop, log the failure reason, and mark the step with `[!]` in the plan.

## Standards
- Adhere strictly to the `Tech Stack` and `Coding Standards` in `CONTEXT.md`.
- Never proceed if immediate verification fails.
