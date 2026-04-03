---
name: vector-protocol
description: A rigorous, state-aware development workflow extension for Gemini CLI. Implements the Research -> Strategy -> Execution lifecycle with strict grounding and persistent state management.
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

## 🔄 Workflow Lifecycle
The protocol is organized into five specialized phases:
- **[PERCEPTION]**: Audit state and detect drift. See [perception.md](references/perception.md).
- **[STRATEGY]**: Develop a rigorous implementation roadmap. See [strategy.md](references/strategy.md).
- **[EXECUTION]**: Implement and verify atomic changes. See [execution.md](references/execution.md).
- **[PERSISTENCE]**: Commit state and recover context. See [persistence.md](references/persistence.md).
- **[IDEATION]**: Analyze codebase for enhancements. See [ideation.md](references/ideation.md).

### 🚀 Getting Started
To bootstrap a project with the Vector Protocol, run the initialization routine described in [persistence.md](references/persistence.md#initialization).
