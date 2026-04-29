# SPEC: Add Operational Robustness to AGENTS.md

## Objective
Update `AGENTS.md` to include missing operational robustness guidelines identified in the FINAL_REPORT.md.

## Requirements
- Define ownership for non-code tasks (e.g., documentation or review) given the deprecation of the generalist subagent.
- Add clear arbitration mechanisms for deadlocks (e.g., between tester and implementer).
- Explicitly detail concurrency safety guidelines (mutually exclusive workspaces) to prevent race conditions.
- Define a process for rollback and cleanup of stale state from aborted runs.
