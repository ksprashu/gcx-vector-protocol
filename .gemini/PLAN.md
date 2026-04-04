# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Phase 6: Codebase Hygiene & Final Polish. Clean up remaining tech debt in the backlog, expand integration tests, and finalize the v1.20.0 release of the Vector Protocol.

## 2. Problem Breakdown
- **Functional:** 
    - *Testing Gap:* We have an E2E test stub (`scripts/e2e_test.py`), but the backlog highlights the need for a "Full Integration" test suite that uses the `generalist` sub-agent to simulate complex commands against a dummy repo.
    - *Self-Healing Friction:* The `[New] Protocol Invariant Validator (State Linter Extension)` was already mostly implemented in Phase 5 (`/vector:lint`), but the backlog item remains. We need to verify if the implementation is complete and remove the tech debt.
- **Technical:**
    - *Integration Tests:* Expand `scripts/e2e_test.py` to cover more than just the initialization phase.
    - *Backlog Grooming:* Clear implemented items from `.gemini/BACKLOG.md`.

## 3. Design Discussion
- **Testing Expansion:** We will update `scripts/e2e_test.py` to add a test for the `work` phase, ensuring the agent can successfully pick up a task and execute a file edit. This will increase confidence in the full loop.
- **Backlog Pruning:** The two remaining items in the Backlog have effectively been addressed by our recent sprints (Phase 5 built the `/vector:lint` extension, and Phase 6 will expand the integration tests). We will move these items out of the Icebox.

## 4. Proposed Solution
1. **Expand E2E Tests:** Add a `test_work_execution` function to `scripts/e2e_test.py`.
2. **Prune Backlog:** Remove the resolved tech debt from `.gemini/BACKLOG.md`.
3. **Version 1.20.0:** Prepare the final 1.x minor release.

## 5. Revision History
- **2026-04-04:** Draft created from Backlog Review.

## 6. Implementation Roadmap
- [x] **Task 1: Expand Integration Tests** - Add a test for the `work` command to `scripts/e2e_test.py`.
- [x] **Task 2: Prune Backlog** - Remove the completed tech debt items from `.gemini/BACKLOG.md`.
- [x] **Task 3: Documentation & Version Bump (v1.20.0)** - Update README and increment manifest for the final polish release.

## 7. Review
- User, please review this roadmap for Phase 6. Ready to proceed?
