# Vector Protocol Documentation Verification Plan

## 1. Intent
Verify that the current documentation comprehensively and consistently reflects the newly designed Vector Protocol updates (Tiered Command Model, Parallel Swarm Execution, removal of `generalist` subagent, early short-circuiting in loops, and Subagent Isolation via fractal task directories and state isolation). Make any necessary corrections to align all documentation artifacts.

## 2. Success Criteria & Definition of Done
- `AGENTS.md`, `README.md`, `gemini-extension.json`, `docs/`, and `skills/vector-protocol/SKILL.md` accurately describe the Tiered Command Model (Core loop vs. Supporting tools).
- Parallel Swarm Execution is clearly documented as a core feature.
- The `generalist` subagent is explicitly marked as deprecated or removed in all agent definitions.
- Early short-circuiting in the Ralph Wiggum loops is documented correctly.
- Subagent Isolation principles, including the use of fractal task directories and state isolation, are clearly defined and enforced in the documentation.
- No contradictory or outdated instructions exist regarding these features.

## 3. Dependencies
- Read access to all repository documentation files.

## 4. Side Effects
- Minor documentation formatting and content updates. No code logic changes expected.

## 5. Unknowns & Hypotheses
- Older documentation files (e.g. in `docs/` or `scripts/`) might still reference deprecated behaviors or command workflows without classifying them into the new Tiered Command Model.
- There may be missed references to the `generalist` agent in deep context files or extension manifests.
- Subagent isolation might be described inconsistently across different files, especially regarding the structure of the `.gemini/tasks/` directory.

## 6. Execution Roadmap

[PARALLEL BATCH]
- [x] Task 1: Audit `AGENTS.md` and `README.md` for consistent references to Parallel Swarm, `generalist` deprecation, Tiered Command Model, and Subagent Isolation via fractal task directories.
- [x] Task 2: Audit `gemini-extension.json` to ensure `generalist` is completely removed from subagents array and Subagent Isolation is reflected in command descriptions.
- [x] Task 3: Audit `skills/vector-protocol/SKILL.md` to confirm early short-circuiting and subagent state isolation (e.g., zero-context mandate) are explicitly instructed.
- [x] Task 4: Audit `docs/COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` to ensure the planned documentation changes, including Subagent Isolation, have been fully integrated into the primary docs (README, AGENTS).

- [x] Task 5: Consolidate findings from the parallel audit and implement necessary text replacements to fix inconsistencies, specifically ensuring Subagent Isolation principles are applied.
- [x] Task 6: Final Critic review of all updated documentation artifacts for alignment with the Vector Protocol v2 mandate, including the Subagent Isolation audit.# Vector Protocol Strategy: Filesystem as the Persistence of State

## 1. Intent
To transform the `.gemini/` directory into a deterministic, immutable record of truth for the Vector Protocol. This ensures that tracking, transparency, and trust are built into the filesystem, allowing for complete state recovery and auditability independent of the session context.

## 2. Success Criteria
- **Traceability:** Every action taken by any subagent is recorded in a specific fractal task directory (`.gemini/tasks/task-ID/`).
- **Observability:** A high-level state file (`.gemini/STATE.md`) provides a clear overview of the project's progress, including a DAG of tasks.
- **Citation Hygiene:** All claims, decisions, and outcomes are backed by Evidence IDs (`[E-XXX]`) stored in `EVIDENCE.json`.
- **Lock-Free State:** Subagents operate and log within their own isolated state boundaries, completely eliminating race conditions for root state files.
- **Durability:** The system can be resumed or audited at any time by reading the aggregated filesystem state.

## 3. Dependencies
- Subagents (`planner`, `implementer`, `tester`, `critic`) must adhere to the local logging protocols.
- Python execution environment for sync scripts.

## 4. Side Effects
- **Storage Growth:** The `.gemini/` directory will grow in size as detailed logs and artifacts are persisted.
- **Context Compression:** The main session history will be significantly leaner, as technical details are offloaded to the filesystem.

## 5. Unknowns
- **Archiving Logic:** At what point should old tasks be moved to `STATE_ARCHIVE.md` to maintain performance?
- **Sync Trigger Frequency:** How often should `scripts/sync_state.py` be executed during autonomous swarm operation to maintain accurate observability?

---

## 6. Execution Roadmap

### [PHASE 1: Foundational Theory]
- **Task 1: Define Evidence & Citation Schema (Theory)**
  - Define the strict format for Evidence IDs (`[E-XXX]`).
  - Mandate Citation Hygiene in all protocol logs and outputs.
  - Enhance `.gemini/EVIDENCE.json` schema to include source task mapping, timestamps, and deep links.

### [PHASE 2: Structural Implementation]
- **Task 2: Define Fractal Task Structure (Structure)**
  - *Dependency: Task 1 (Must incorporate citation schema into log templates)*.
  - Establish mandatory files for each task directory (`.gemini/tasks/TASK-ID/`):
    - `SPEC.md`: Intent, Success Criteria, and specific sub-plan.
    - `LOG.md`: Detailed transcript of tool calls and citations.
    - `CRITIQUE.md`: Independent verification by the `critic` subagent.
    - `STATUS.json`: Localized state for Lock-Free Aggregation.

### [PHASE 3: Enforcing & Tooling (PARALLEL BATCH)]
- **Task 3: Update Agent Mandates**
  - Update `AGENTS.md` and `skills/vector-protocol/SKILL.md` with the "Lock-Free Filesystem Persistence Mandate" and Citation Hygiene rules.
- **Task 4: State Synchronization Tooling (scripts/)**
  - Explicitly modify `scripts/sync_state.py`.
  - Implement a **Lock-Free State Aggregation** strategy: 
    - Subagents **never** write directly to `.gemini/STATE.md`.
    - Subagents write their status strictly to `.gemini/tasks/TASK-ID/STATUS.json`.
    - `scripts/sync_state.py` sweeps all fractal `STATUS.json` files and dynamically aggregates/re-renders `.gemini/STATE.md`.

### [FINAL REVIEW]
- **Task 5: Critic Audit of Strategy**
  - The `critic` subagent verifies the implementation of the Lock-Free strategy, confirms no circular dependencies between Phase 1 and 2, and validates the `scripts/sync_state.py` functionality.---
