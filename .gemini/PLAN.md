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
- [x] Task 6: Final Critic review of all updated documentation artifacts for alignment with the Vector Protocol v2 mandate, including the Subagent Isolation audit.