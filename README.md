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
    *   Grounding phase. The agent reads Context, Plan, and Evidence, checks the codebase, and maps the territory. Also auto-bootstraps protocol files if they are missing.
*   **E - ESTABLISH (`/vector:plan`)**
    *   Strategy phase. Also handles implicit init/resume so you can jump straight into planning.
*   **C - COMPUTE** (`/vector:improve`)
    *   Ideation phase. The agent brainstorms enhancements and persists them to the Backlog.
*   **T - TRANSMUTE (`/vector:work`)**
    *   Execution phase. Also performs a lightweight resume + drift check before making changes.
*   **O - OBSERVE** (Internal)
    *   The agent verifies code immediately after writing it (part of `/vector:work`).
*   **R - RECORD (`/vector:save`)**
    *   Persistence phase. The agent commits changes and saves the State.

## 🛠 Commands

The Vector Protocol uses a **tiered command model** to balance daily efficiency with advanced control.

### Tier 1: Core Loop (Daily Use)
The standard development cycle. These commands handle state recovery automatically.

*   **`/vector:plan`** - Create or update the implementation plan.
*   **`/vector:work`** - Execute the plan (includes atomic verification).
*   **`/vector:save`** - Commit changes to git and persist protocol state.

### Tier 2: Supporting Tools (Situational)
Use these for deep analysis, brainstorming, or infrastructure maintenance.

*   **`/vector:scan`** - Deep perception pass and drift analysis. Safe as a first command.
*   **`/vector:improve`** - Ideation & Brainstorming. Persists ideas to the Backlog.
*   **`/vector:context`** - Audit and update the project CONTEXT.md.

### Tier 3: Maintenance & Recovery (Rare)
Advanced tools for manual state management and troubleshooting.

*   **`/vector:status`** - Show the current State dashboard.
*   **`/vector:init`** - Explicit bootstrap of protocol files.
*   **`/vector:reset`** - Clear the protocol State (failsafe).

## 🧭 Grounded Mode

Grounded Mode is the default behavioral contract for this extension: **evidence first, conclusions second**.

**Example flow**
1. Run `/vector:scan` to gather repository evidence (protocol files, git status, config drift checks).
2. Run `/vector:plan` to create a plan that cites observed constraints and known unknowns.
3. Run `/vector:work` for one atomic step, verify immediately, and record the result in `STATE.md`.
4. Run `/vector:save` to persist a commit plus state checkpoint.

**Evidence artifacts you should expect**
* Checked-file lists and drift notes from scan/context phases.
* Verification outputs (tests/build/lint) from work phase.
* `STATE.md` scratchpad entries reflecting real outcomes, including failures.
* Git commit metadata captured during save.

## 💡 Best Practices

1.  **Default Fast Path:** In most sessions, just run `/vector:plan` → `/vector:work` → `/vector:save`.
2.  **Use Scan Intentionally:** Run `/vector:scan` for deep drift detection, onboarding to unfamiliar repos, or troubleshooting.
3.  **Review the Plan:** `/vector:plan` generates a detailed Design Document in `.gemini/PLAN.md`. **Read it.** Edit it. It is your blueprint.
4.  **Iterate:** If the plan isn't right, run `/vector:plan "<feedback>"` to refine it.
5.  **Atomic Work:** `/vector:work` is designed to be atomic and now includes automatic resume checks.
6.  **Save Often:** Use `/vector:save` after every successful logical unit of work.
7.  **Keep Context Fresh:** When you add a dependency, change architecture, or update standards, run `/vector:context` to keep CONTEXT.md in sync.
8.  **Cite Evidence IDs:** For scan/plan/work outputs, reference relevant evidence entries (for example `E-003`) so claims are traceable.


## 🧩 Ambiguity Resolution & Handoff Contract

To keep the protocol deterministic across restarts and multi-agent handoffs:

* **Objective precedence:** user instruction overrides stale plan text; update `PLAN.md` immediately to match.
* **Phase precedence:** `STATE.md` is the active phase source of truth; corrections must be appended (not silently rewritten).
* **Evidence gating:** non-trivial factual decisions should be logged in `EVIDENCE.md` (or `SOURCES.md`) before final recommendations.
* **Handoff minimum:** before stopping, append to `STATE.md` what changed, what was verified, what failed, and the exact next action.

## 📝 Release Notes

* **v1.11.0** - Command Surface Simplification Phase 1: Removed deprecated `/vector:resume` and introduced a Tiered Command Model (Core, Supporting, Maintenance) in documentation.
* **v1.10.1** - UX Polish: Replaced Markdown tables with native CLI bulleted lists and checkboxes in all command outputs.
* **v1.6.0** - Introduced grounded-agent guarantees: binding evidence-first behavior, explicit expected outputs, and documented Grounded Mode evidence artifacts across Vector commands.
