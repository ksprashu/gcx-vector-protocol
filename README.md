# 📐 GCX Vector Protocol

**The Vector Protocol** is a high-assurance, state-aware development workflow extension for the Gemini CLI. It is designed to provide **Direction** (Vector) and **Magnitude** (Intensity) to your development process.

## Installation

Install the Vector Protocol extension by running the following command from your terminal:

```bash
gemini extensions install https://github.com/ksprashu/gcx-vector-protocol --auto-update
```

The `--auto-update` is optional: if specified, it will update to new versions as they are released.

## 🚀 Getting Started

1.  **Initialize:** Run `/vector:init` in your project root.
    *   This creates the `.gemini/` directory.
    *   It creates the **Trinity of State** files: `ANCHOR.md`, `COMPASS.md`, and `PULSE.md`.

## 🧠 The Trinity of State

The protocol relies on three files to maintain context, so you don't have to keep repeating yourself.

1.  **⚓️ ANCHOR (`.gemini/ANCHOR.md`)**
    *   **The "Why" and "How".**
    *   Static truths: Tech stack, coding conventions, architectural invariants.
    *   *Edit this once at the start of the project.*

2.  **🧭 COMPASS (`.gemini/COMPASS.md`)**
    *   **The "Where".**
    *   Dynamic roadmap: Current active feature specs, user stories, TODOs.
    *   *Update this before starting a new feature (Strategy Phase).*

3.  **💓 PULSE (`.gemini/PULSE.md`)**
    *   **The "Now".**
    *   Volatile state: Current phase, last tool output, immediate next step, scratchpad.
    *   *The agent updates this automatically after every turn.*

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
