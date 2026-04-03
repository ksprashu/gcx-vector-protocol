---
name: vector-persist
description: Persist progress, sync state, rotate scratchpads, initialize protocol files, and commit changes. Use during the PERSISTENCE phase or when a meaningful milestone is reached.
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

# 💾 Persistence Phase (Persist / Save / Init)

You are entering the **PERSISTENCE (Save / Init)** phase.

**User Message/Arguments:** The specific arguments or commit message provided by the user. If the user invokes an initialization command, use Mode 1. Otherwise, use Mode 2.

## Mode 1: Initialization (Bootstrap)
**Goal:** Establish the persistent context and state tracking files.

### Protocol:
0.  **Pre-flight Check:**
    *   Check if the 5 protocol files exist.
    *   **IF** files exist AND the user did not specify `--force`:
        *   Read `.gemini/PLAN.md` (if available) to identify current objective.
        *   Report: "⚠️ **Vector Protocol is already initialized.**"
        *   STOP. Do not overwrite.
    *   **ELSE:** Proceed.
1.  **Context Discovery:**
    *   Read key configuration files (`package.json`, `Cargo.toml`, etc.) to identify the Tech Stack.
2.  **State Initialization:**
    *   Create `.gemini/CONTEXT.md` (pre-fill tech stack).
    *   Create `.gemini/PLAN.md` (empty roadmap template).
    *   Create `.gemini/STATE.md` (timestamp and "Initialized" status).
    *   Create `.gemini/BACKLOG.md` (header: `# 💡 BACKLOG`).
    *   Create `.gemini/EVIDENCE.md` (evidence ledger template).
3.  **Output:**
    *   **Session Dashboard:** Bulleted list.
    *   **Confirmation:** List the files created.
    *   **Navigation:** `> Recommended Action: /vector:scan`

---

## Mode 2: Save & Commit
**Goal:** Persist execution state to disk, manage scratchpad growth, and commit to version control.

### Protocol:
1.  **Context Loading:** Read `.gemini/STATE.md`, `.gemini/PLAN.md`, and `.gemini/BACKLOG.md`.
2.  **State Sync:** Ensure `.gemini/STATE.md` reflects the latest outcome.
3.  **Scratchpad Rotation:**
    *   **IF** the `## 3. Scratchpad` section in `.gemini/STATE.md` has more than 20 entries:
        *   Append the full Scratchpad content to `.gemini/STATE_ARCHIVE.md`.
        *   Replace the active Scratchpad with a single "Previous Session Summary" line.
    *   **ELSE:** Leave the Scratchpad as-is.
4.  **Phase Update:** Update `**Phase:**` in `.gemini/STATE.md` to `[IDLE]`.
5.  **Git Check:** Run `git status`.
6.  **Commit:**
    *   Stage relevant files (including `.gemini/`).
    *   Commit with the **User Message**. If empty, derive a concise message from the Last Action in State.
7.  **Output:**
    *   **Session Dashboard:** Bulleted list.
    *   **Save Summary:** Actions and commit hash.
    *   **Navigation:** `> Recommended Action: /vector:scan` or `/vector:improve`
    *   **Stopping Criteria:** STOP after committing. WAIT for user instruction. DO NOT execute recommended command.
