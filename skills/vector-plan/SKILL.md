---
name: vector-plan
description: Develop a rigorous implementation roadmap with analysis, design, and atomic steps. Use during the STRATEGY phase to define how an objective will be achieved before writing code.
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

# 🗺️ Strategy Phase (Plan)

## Plan Generation
1. **Explicit Understanding:** Explain your understanding of the user request and the chosen approach.
2. **Rich Structure:** Plans must be comprehensive Design Documents including:
   - **Analysis (Why):** First Principles, Trade-offs, and Risks.
   - **Design (How):** Technical details, signatures, and API citations.
   - **Roadmap (What):** Numbered list of Atomic, Verifiable steps.
3. **Backlog Integration:** Promote items from `BACKLOG.md` to the active Plan if requested.
4. **Plan Archival:** Append the old `PLAN.md` to `PLAN_ARCHIVE.md` before overwriting.
5. **N-Trial Synthesis:** When N trial synthesis is requested, generate parallel proposals and synthesize the optimal path.

## Verification
- Every step in the roadmap must have a clear verification criteria (test, build, or visual check).
