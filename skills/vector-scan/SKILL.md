---
name: vector-scan
description: Audit project state, detect drift in protocol files, and sync context. Use during the PERCEPTION or MAINTENANCE phases to ensure the agent's mental model matches the repository truth.
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

# 🔍 Perception & Maintenance Phase (Scan & Context)

You are entering either the **PERCEPTION (Scan)** or **MAINTENANCE (Context Update)** phase based on the user's request.

**User Focus:** The area to investigate. If empty, perform a general environment analysis. If the user explicitly asks to "audit context" or "update context", switch to Maintenance Mode.

## Mode 1: Perception (Scan)
**Goal:** Rigorously map the relevant codebase context and **Reconcile** the 5-File System State.

### Protocol:
0.  **Auto-Bootstrap Guardrail:**
    *   If protocol files are missing, create ONLY the missing files with minimal templates before continuing: `.gemini/CONTEXT.md`, `.gemini/PLAN.md`, `.gemini/STATE.md`, `.gemini/BACKLOG.md`, `.gemini/EVIDENCE.md`.
1.  **State Audit (The 5-File Check):**
    *   **Read ALL** existing protocol files.
2.  **Investigation:**
    *   **Search & Verify:** Use `glob`, `list_directory`, or `read_file` to locate files relevant to the User Focus. Confirm their actual content.
3.  **External Evidence Pass (Mandatory):**
    *   Collect authoritative references for every major conclusion. Build an Evidence Table (`Topic | Source | Why authoritative | Last-checked`).
4.  **State Update:**
    *   **Write** your raw findings to `.gemini/STATE.md` under the `## 3. Scratchpad` section (APPEND, do not overwrite).
    *   Update `**Phase:**` in `.gemini/STATE.md` to `[PERCEPTION]`.

### Output (Scan):
*   **Session Dashboard:** Bulleted list (Phase, Objective, Last Action, Next Step, Pending Tasks).
*   **Scan Findings:** Bullet points of insights.
*   **Drift Report:** Bullet points of expected vs actual state.
*   **Evidence Table:** Markdown table.
*   **Prompt:** "Analysis complete. Ready to proceed to Planning?"
*   **Navigation:** `> Recommended Action: /vector:plan <objective>` or `/vector:improve`
*   **Stopping Criteria:** STOP and WAIT for user to select next action. DO NOT generate a plan or modify code.

---

## Mode 2: Maintenance (Context Update)
**Goal:** Detect staleness between `.gemini/CONTEXT.md` and project state, then **propose** surgical updates. **DO NOT modify CONTEXT.md without explicit user approval.**

### Protocol:
1.  **Load Current Context:** Read `.gemini/CONTEXT.md`.
2.  **Drift Detection (Audit):**
    *   Scan configuration files (`package.json`, `Cargo.toml`, etc.) and top-level directories.
    *   Classify discrepancies: **[MISSING]**, **[STALE]**, **[OBSOLETE]**.
3.  **External Evidence Pass:** Build an Evidence Table for each major discrepancy.
4.  **Proposal Generation:**
    *   Create labelled proposals: **[ADD #N]**, **[UPDATE #N]**, **[REMOVE #N]**.
    *   If no discrepancies: "Context is up to date." STOP.
5.  **Await Approval:** Present numbered proposals and ask: "Apply all, apply #N, or skip?". STOP.
6.  **Apply Approved Changes:** Apply ONLY what the user approved via surgical edits to `.gemini/CONTEXT.md`.
7.  **State Update:** Update `**Phase:**` to `[MAINTENANCE]` and append summary to `.gemini/STATE.md` scratchpad.

### Output (Context Proposal Stage):
*   **Session Dashboard:** Bulleted list.
*   **Context Audit:** List discrepancies.
*   **Evidence Table:** Markdown table.
*   **Prompt:** "Apply all, apply #N, or skip?"
*   **Stopping Criteria:** STOP. WAIT for user confirmation. DO NOT write to `CONTEXT.md` before approval.
