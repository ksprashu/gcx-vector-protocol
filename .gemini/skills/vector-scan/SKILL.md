---
name: vector-scan
description: Audit project state, detect drift in protocol files, and sync context. Use during the PERCEPTION phase to ensure the agent's mental model matches the repository truth.
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

# 🔍 Perception Phase (Scan & Context)

## Environment Analysis
1. **Auto-Bootstrap:** If protocol files are missing, create minimal templates for `CONTEXT.md`, `PLAN.md`, `STATE.md`, `BACKLOG.md`, and `EVIDENCE.md`.
2. **State Audit:** Read all protocol files to understand the current objective and status.
3. **Investigation:** Use `glob`, `list_directory`, or `search_file_content` to locate relevant files.
4. **Drift Detection:** Flag discrepancies between the current `PLAN.md`, `STATE.md`, and the actual codebase state.
5. **Evidence Table:** Record Topic, Source, and Last-checked status for all findings.

## Context Maintenance
1. **Drift Audit:** Scan configuration files (e.g., `package.json`, `go.mod`) to detect staleness in `CONTEXT.md`.
2. **Discrepancy Classification:**
   - **[MISSING]:** Real item exists but is absent from `CONTEXT.md`.
   - **[STALE]:** Documentation no longer matches reality.
   - **[OBSOLETE]:** Refers to removed patterns or dependencies.
3. **Surgical Proposals:** Present `ADD`, `UPDATE`, or `REMOVE` diffs.
4. **Wait for Approval:** Do NOT modify `CONTEXT.md` without explicit user confirmation.
