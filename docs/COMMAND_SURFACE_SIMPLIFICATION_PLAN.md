# Command Surface Simplification Plan

## Goal
Make Vector Protocol feel concise for daily usage while preserving advanced flexibility and grounded guarantees.

## Recommendation
Adopt a **simplified 2-command entry model** that abstracts situational tools into the core autonomous loops.

- **Core loop (default):** `/vector:plan` → `/vector:work`
- **Supporting capabilities (internalized):** Scanning, context management, and improvement are now part of the internal Ralph Wiggum loops within the core commands.
- **Recovery and maintenance (rare):** `/vector:status`, `/vector:init`, `/vector:resume`, `/vector:reset`

This keeps all existing power but lowers cognitive load for new users.

## Why documentation-first (now)
Current command prompts already include auto-bootstrap/auto-resume behavior in core flow:

- `/vector:plan` handles missing protocol files and implicit resume behavior.
- `/vector:work` performs auto-recovery and a fast reconciliation before coding.

Because this behavior already exists, we simplified the user experience immediately through docs and onboarding guidance without changing command implementations (other than consolidating the core loop to two primary entry points).

## Subagent Isolation (Integration Notes)
A critical component of this simplification is **Subagent Isolation**, which ensures that the autonomous swarm remains deterministic even as the command surface shrinks.

- **Fractal Task Directories:** All subagent work is isolated within `.gemini/tasks/task-XYZ/` to prevent state pollution and enable parallel swarm execution.
- **State Isolation:** Subagents are strictly prohibited from reading/writing outside their assigned fractal directory (except for targeted code files), as enforced in their system prompts in `gemini-extension.json`.
- **Zero-Context Rule:** Main thread context is preserved by requiring subagents to return only status codes and file paths, forcing all verbose logic into the isolated filesystem.

## Proposed Rollout

### Phase 1 — Documentation (Complete)
1. Promote the "2-Command Workflow" as the default in README.
2. Reframe all other commands as situational tools or internal mechanisms.
3. Add clear decision guidance: "Which command should I run now?" (Answer: `/vector:plan` for strategy, `/vector:work` for execution).
4. Deprecated `generalist` subagent in favor of isolated specialists.

### Phase 2 — Optional UX polish (low risk)
1. Add concise aliases in extension UX (if host platform supports aliases).
   - Example: `start -> /vector:plan`, `do -> /vector:work`.
2. Add an optional routing helper command (for example, `/vector:next`) that reads state and suggests the next action.

### Phase 3 — Telemetry-informed cleanup (only if desired)
1. Observe usage patterns in real projects.
2. If certain legacy commands are consistently unused, de-emphasize further in docs.
3. Keep advanced commands available for deterministic recovery and audits.

## Non-Goals
- Do not remove existing commands in this proposal (unless they are truly redundant).
- Do not change protocol state file semantics.
- Do not weaken evidence-first behavior.

## Success Criteria
- New users can complete common sessions by learning only 2 commands.
- Subagent Isolation prevents context rot and race conditions in the swarm.
- Existing users retain full control and compatibility.
- No loss of deterministic recovery workflows.

## Risks and Mitigations
- **Risk:** Advanced users fear reduced control.
  - **Mitigation:** Explicitly preserve all advanced commands and document when to use each.
- **Risk:** Confusion from two "views" of commands.
  - **Mitigation:** Keep one canonical command list, but present it in grouped tiers.

## Recommended Next Step
Validation: Ensure all subagent system prompts in `gemini-extension.json` strictly enforce the isolation boundaries documented here.
