# Command Surface Simplification Plan

## Goal
Make Vector Protocol feel concise for daily usage while preserving advanced flexibility and grounded guarantees.

## Recommendation
Adopt a **tiered command model** instead of removing capabilities.

- **Core loop (default):** `/vector:plan` → `/vector:work` → `/vector:save`
- **Supporting tools (situational):** `/vector:scan`, `/vector:improve`, `/vector:context`
- **Recovery and maintenance (rare):** `/vector:status`, `/vector:init`, `/vector:resume`, `/vector:reset`

This keeps all existing power but lowers cognitive load for new users.

## Why documentation-first (now)
Current command prompts already include auto-bootstrap/auto-resume behavior in core flow:

- `/vector:plan` handles missing protocol files and implicit resume behavior.
- `/vector:work` performs auto-recovery and a fast reconciliation before coding.

Because this behavior already exists, we can simplify user experience immediately through docs and onboarding guidance without changing command implementations.

## Proposed Rollout

### Phase 1 — Documentation (no behavior change)
1. Promote "Core loop" as the default in README.
2. Reframe all other commands as situational tools.
3. Add clear decision guidance: "Which command should I run now?"
4. Keep compatibility intact (no command removal or rename).

### Phase 2 — Optional UX polish (low risk)
1. Add concise aliases in extension UX (if host platform supports aliases).
   - Example: `start -> /vector:plan`, `do -> /vector:work`, `done -> /vector:save`.
2. Add an optional routing helper command (for example, `/vector:next`) that reads state and suggests the next action.

### Phase 3 — Telemetry-informed cleanup (only if desired)
1. Observe usage patterns in real projects.
2. If certain commands are consistently unused, de-emphasize further in docs.
3. Keep advanced commands available for deterministic recovery and audits.

## Non-Goals
- Do not remove existing commands in this proposal.
- Do not change protocol state file semantics.
- Do not weaken evidence-first behavior.

## Success Criteria
- New users can complete common sessions by learning only 3 commands.
- Existing users retain full control and compatibility.
- No loss of deterministic recovery workflows.

## Risks and Mitigations
- **Risk:** Advanced users fear reduced control.
  - **Mitigation:** Explicitly preserve all advanced commands and document when to use each.
- **Risk:** Confusion from two "views" of commands.
  - **Mitigation:** Keep one canonical command list, but present it in grouped tiers.

## Recommended Next Step
Implement Phase 1 immediately (documentation-only), then validate adoption before any command-level changes.
