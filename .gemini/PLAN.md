# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Phase 4: Structured Intelligence & Workflow Integration. Transition to a machine-readable Evidence schema, implement state-sync Git hooks, and deliver a dynamic workflow router (`/vector:next`).

## 2. Problem Breakdown
- **Functional:** 
    - *Evidence Retrieval:* As projects grow, searching a flat `EVIDENCE.md` for specific facts becomes inefficient for the LLM. 
    - *State Drift:* Users committing manually bypassing `/vector:save` leaves `STATE.md` in a stale phase (e.g., `[EXECUTION]`).
    - *Workflow Friction:* New users often hesitate on which command to run next.
- **Technical:**
    - *Evidence Schema:* Need to transition from a Markdown table to a block-based schema with YAML frontmatter or a companion JSON store.
    - *Git Hooks:* Need a script to install and manage a `.git/hooks/pre-commit` script that resets the phase to `[IDLE]` or warns the user.
    - *Routing Logic:* `/vector:next` needs a heuristic parser for `STATE.md` and `PLAN.md` to output the next logical command.

## 3. Design Discussion
- **Evidence Structure:** I propose keeping `EVIDENCE.md` but wrapping each entry in a structured block (e.g., `<!-- { "id": "E-001", ... } -->`) or using a dedicated `EVIDENCE.json`. A JSON file is best for high-assurance retrieval (RAG optimization).
- **Git Hook Strategy:** The hook should be a simple shell script that calls a Python utility to update the `STATE.md` phase. This ensures protocol integrity even with external git clients.
- **Router Logic:** `/vector:next` will be a new TOML command that uses a simple state-machine logic:
    - If Phase is `[IDLE]` and Plan is empty -> `/vector:scan`.
    - If Phase is `[IDLE]` and Plan has unchecked tasks -> `/vector:work <task>`.
    - If Phase is `[EXECUTION]` -> `/vector:save`.

## 4. Proposed Solution
1. **Automated Evidence Schema:** Implement a migration script to move existing entries to `EVIDENCE.json` and update the `save` command to write to both.
2. **Protocol State Git Hooks:** Create `scripts/install_hooks.sh` and a Python helper to auto-sync state on commit.
3. **`/vector:next` Routing Helper:** Create `commands/vector/next.toml` with the routing logic.

## 5. Revision History
- **2026-04-04:** Draft created from Backlog Review.

## 6. Implementation Roadmap
- [x] **Task 1: Structured Evidence Migration** - Transition `EVIDENCE.md` data to a machine-readable `EVIDENCE.json` and update `save.toml`.
- [x] **Task 2: Protocol Git Hooks** - Implement `pre-commit` hook to ensure `STATE.md` sync during manual commits.
- [x] **Task 3: Implement `/vector:next`** - Create the dynamic routing command to guide the developer workflow.
- [x] **Task 4: Documentation & Version Bump (v1.17.0)** - Update README and increment manifest.

## 7. Review
- User, please review this Phase 4 roadmap. Does the focus on Structured Evidence and Workflow Integration align with the next evolution of the Vector Protocol?
