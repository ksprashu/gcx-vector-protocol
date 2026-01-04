# 📐 GCX Vector Protocol

**The Vector Protocol** is a high-assurance, state-aware development workflow extension for the Gemini CLI. It is designed to provide **Direction** (Vector) and **Magnitude** (Intensity) to your development process.

## Installation

Install the Vector Protocol extension by running the following command from your terminal:

```bash
gemini extensions install https://github.com/ksprashu/gcx-vector-protocol --auto-update
```

The `--auto-update` is optional: if specified, it will update to new versions as they are released.

This extension implements the **Vector Protocol** for the Gemini CLI.

It creates the **Protocol State** files: `CONTEXT.md`, `PLAN.md`, and `STATE.md`.

## The Files

1.  **📄 CONTEXT (`.gemini/CONTEXT.md`)**
    *   Static project rules, tech stack, and constraints.
    *   *The "Constitution".*

2.  **🗺️ PLAN (`.gemini/PLAN.md`)**
    *   The active roadmap and implementation strategy.
    *   *The "Map".*

3.  **💾 STATE (`.gemini/STATE.md`)**
    *   Volatile session state, last action, and scratchpad.
    *   *The "Save Point".*

## 🔄 The Workflow (V.E.C.T.O.R.)

The extension provides specific commands for each phase of the loop:

*   **V - VERIFY (`/vector:scan`)**
    *   Grounding phase. The agent reads the Anchor and Compass, checks the codebase, and maps the territory.
*   **E - ESTABLISH (`/vector:plan`)**
    *   Strategy phase. The agent drafts the plan in the Compass.
*   **C - COMPUTE** (Internal)
    *   The agent uses First Principles thinking during the Plan/Work phases.
*   **T - TRANSMUTE (`/vector:work`)**
    *   Execution phase. The agent writes code based on the Compass.
*   **O - OBSERVE** (Internal)
    *   The agent verifies code immediately after writing it (part of `/vector:work`).
*   **R - RECORD (`/vector:save`)**
    *   Persistence phase. The agent commits changes and saves the Pulse.

## 🛠 Commands

*   `/vector:init` - Bootstrap the Trinity files.
*   `/vector:scan` - Analyze the codebase and current state.
*   `/vector:plan` - Create or update the implementation plan.
*   `/vector:work` - Execute the plan (write code + verify).
*   `/vector:status` - Show the current Pulse dashboard.
*   `/vector:save` - Commit changes to git and save state.
*   `/vector:resume` - Reload context after a restart.
*   `/vector:reset` - Clear the Pulse (failsafe).
