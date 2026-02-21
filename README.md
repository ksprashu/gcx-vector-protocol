# 📐 GCX Vector Protocol

**The Vector Protocol** is a high-assurance, state-aware development workflow extension for the Gemini CLI. It is designed to provide **Direction** (Vector) and **Magnitude** (Intensity) to your development process.

## Installation

Install the Vector Protocol extension by running the following command from your terminal:

```bash
gemini extensions install https://github.com/ksprashu/gcx-vector-protocol --auto-update
```

The `--auto-update` is optional: if specified, it will update to new versions as they are released.

This extension implements the **Vector Protocol** for the Gemini CLI.

It creates the **4-File Protocol State**: `CONTEXT.md`, `PLAN.md`, `STATE.md`, and `BACKLOG.md`.

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

*   `/vector:init` - Bootstrap the Protocol State files (Safe mode included) and report created/reused artifacts.
*   `/vector:scan` - Analyze the codebase and current state with evidence-first findings (files checked, drift found, next action).
*   `/vector:improve` - Ideation & Brainstorming with evidence-backed rationale; persists proposals to the Backlog plus concise chat summary.
*   `/vector:plan` - Create/update the implementation plan (Design Document) from observed repository evidence and explicit assumptions.
*   `/vector:work` - Execute the plan (write code + verify) in evidence-first mode with immediate verification outputs and state log updates.
*   `/vector:status` - Show the current State dashboard derived from protocol files with explicit source references.
*   `/vector:save` - Commit changes to git and save state, including commit evidence and post-save state snapshot.
*   `/vector:resume` - Reload context after a restart and summarize recovered evidence artifacts.
*   `/vector:reset` - Clear the State (failsafe) with a confirmation summary of what was reset.
*   `/vector:context` - Audit/update project Context (CONTEXT.md) using approval-gated, evidence-backed ADD/UPDATE/REMOVE proposals.


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

1.  **Start with Scan:** Always run `/vector:scan` when starting a session to ground the agent.
2.  **Ideate First:** Use `/vector:improve` to generate ideas before committing to a plan.
3.  **Review the Plan:** `/vector:plan` now generates a detailed Design Document in `.gemini/PLAN.md`. **Read it.** Edit it. It is your blueprint.
4.  **Iterate:** If the plan isn't right, run `/vector:plan "<feedback>"` to refine it.
5.  **Atomic Work:** `/vector:work` is designed to be atomic. It will explain what it's doing. Verify each step.
6.  **Save Often:** Use `/vector:save` after every successful logical unit of work.
7.  **Keep Context Fresh:** When you add a dependency, change architecture, or update standards, run `/vector:context` to keep CONTEXT.md in sync.

## 📝 Release Notes

* **v1.6.0** - Introduced grounded-agent guarantees: binding evidence-first behavior, explicit expected outputs, and documented Grounded Mode evidence artifacts across Vector commands.

