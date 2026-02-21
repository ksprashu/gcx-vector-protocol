# 📐 GCX Vector Protocol

**The Vector Protocol** is a high-assurance, state-aware development workflow extension for the Gemini CLI. It is designed to provide **Direction** (Vector) and **Magnitude** (Intensity) to your development process.

## Installation

Install the Vector Protocol extension by running the following command from your terminal:

```bash
gemini extensions install https://github.com/ksprashu/gcx-vector-protocol --auto-update
```

The `--auto-update` is optional: if specified, it will update to new versions as they are released.

This extension implements the **Vector Protocol** for the Gemini CLI.

It creates the **5-File Protocol State**: `CONTEXT.md`, `PLAN.md`, `STATE.md`, `BACKLOG.md`, and `EVIDENCE.md` (or `SOURCES.md` as a compatible alias).

## The Files

1.  **📄 CONTEXT (`.gemini/CONTEXT.md`)**
    *   Static project rules, tech stack, and constraints.
    *   *The "Constitution".*

2.  **🗺️ PLAN (`.gemini/PLAN.md`)**
    *   The active roadmap and implementation strategy. Includes **Design Specifications**.
    *   *The "Map".*

3.  **💾 STATE (`.gemini/STATE.md`)**
    *   Volatile session state, last action, and scratchpad.
    *   *The "Save Point".*

4.  **💡 BACKLOG (`.gemini/BACKLOG.md`)**
    *   Future ideas, enhancements, and non-critical tech debt.
    *   *The "Icebox".*

5.  **🔎 EVIDENCE (`.gemini/EVIDENCE.md` or `.gemini/SOURCES.md`)**
    *   Source-backed claims, findings, and traceability records.
    *   Lightweight schema per entry:
        *   **Claim/Question**
        *   **Source URL (or identifier)**
        *   **Source type** (`official doc` / `spec` / `release` / `paper` / `article`)
        *   **Retrieved date/time**
        *   **Key extracted facts**
        *   **Confidence/conflict notes**
    *   *The "Evidence Ledger".*

## 🔄 The Workflow (V.E.C.T.O.R.)

The extension provides specific commands for each phase of the loop:

*   **V - VERIFY (`/vector:scan`)**
    *   Grounding phase. The agent reads the Context and Plan, checks the codebase, and maps the territory.
*   **E - ESTABLISH (`/vector:plan`)**
    *   Strategy phase. The agent drafts a **Rich Design Document** in the Plan for your review.
*   **C - COMPUTE** (`/vector:improve`)
    *   Ideation phase. The agent brainstorms enhancements and persists them to the Backlog.
*   **T - TRANSMUTE (`/vector:work`)**
    *   Execution phase. The agent writes code based on the Plan with explicit **Transparency**.
*   **O - OBSERVE** (Internal)
    *   The agent verifies code immediately after writing it (part of `/vector:work`).
*   **R - RECORD (`/vector:save`)**
    *   Persistence phase. The agent commits changes and saves the State.

## 🛠 Commands

*   `/vector:init` - Bootstrap the Protocol State files (Safe mode included).
*   `/vector:scan` - Analyze the codebase and current state.
*   `/vector:improve` - Ideation & Brainstorming. Suggests enhancements and persists them to the Backlog.
*   `/vector:plan` - Create or update the implementation plan (Design Document).
*   `/vector:work` - Execute the plan (write code + verify) with step-by-step confirmation.
*   `/vector:status` - Show the current State dashboard.
*   `/vector:save` - Commit changes to git and save state.
*   `/vector:resume` - Reload context after a restart.
*   `/vector:reset` - Clear the State (failsafe).
*   `/vector:context` - Audit and update the project Context (CONTEXT.md) with guided, approval-gated changes.

## 💡 Best Practices

1.  **Start with Scan:** Always run `/vector:scan` when starting a session to ground the agent.
2.  **Ideate First:** Use `/vector:improve` to generate ideas before committing to a plan.
3.  **Review the Plan:** `/vector:plan` now generates a detailed Design Document in `.gemini/PLAN.md`. **Read it.** Edit it. It is your blueprint.
4.  **Iterate:** If the plan isn't right, run `/vector:plan "<feedback>"` to refine it.
5.  **Atomic Work:** `/vector:work` is designed to be atomic. It will explain what it's doing. Verify each step.
6.  **Save Often:** Use `/vector:save` after every successful logical unit of work.
7.  **Keep Context Fresh:** When you add a dependency, change architecture, or update standards, run `/vector:context` to keep CONTEXT.md in sync.
8.  **Cite Evidence IDs:** For scan/plan/work outputs, reference relevant evidence entries (for example `E-003`) so claims are traceable.
