# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Provide a new objective.

## 2. Strategic Analysis
- **Problem:** The backlog is currently empty.
- **Solution:** The user needs to provide a new feature request, bug report, or directive to continue development.
- **Risk Assessment:** N/A.

## 3. Implementation Roadmap
- [ ] **Task 1: Await user input** - Provide a new objective via `/vector:plan <objective>`.

## 4. Review
Plan established. Ready to Execute?# Deep Dissection: Documentation Sync for Vector Protocol v2.0.0

## Intent
The objective is to verify and ensure that all user-facing and internal documentation accurately reflects the "newly designed vector protocol" (Vector v2.0.0). This includes the Zero-Context Orchestrator model, the Ralph Wiggum loops for planning and execution, the fractal file system structure in `.gemini/tasks/`, and the **Tiered command model** (Core loop: `/vector:plan`, `/vector:work`, `/vector:save`).

## Success Criteria & Definition of Done
- [ ] **Alignment Check:** Every mention of the protocol in documentation matches the logic defined in `.gemini/tasks/PROTOCOL.md`, `skills/vector-protocol/SKILL.md`, and `commands/vector/`.
- [ ] **README.md Accuracy:** The "🚀 Core Loop Workflow" and "🧠 Core Architecture" sections are technically correct, up-to-date, and promote the Tiered command model.
- [ ] **AGENTS.md Consistency:** The mission statement and mandates for subagents align with the Zero-Context mandate and the Ralph Wiggum loops.
- [ ] **GEMINI.md Synchronization:** The top-level `GEMINI.md` and `.gemini/GEMINI.md` contain consistent instructions regarding the protocol version and major/minor versioning rules.
- [ ] **Extension Manifest Audit:** `gemini-extension.json` correctly describes the extension, its version, and the exposed tiered commands.
- [ ] **Documentation Completion:** All core components (Zero-Context, Ralph Wiggum, Fractal FS, Subagent Swarm) are documented with their latest specifications.

## Dependencies
- `docs/COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` (Authoritative source for tiered command model)
- `.gemini/tasks/PROTOCOL.md` (Source of Truth for directory structure and schema)
- `skills/vector-protocol/SKILL.md` (Source of Truth for orchestrator logic)
- `commands/vector/plan.toml`, `work.toml`, etc. (Source of Truth for command implementation)
- `README.md`, `AGENTS.md`, `GEMINI.md`, `gemini-extension.json` (Target documentation files)

## Side Effects
- Minor documentation updates will change the repository state but should not affect functional code.
- Updating `GEMINI.md` might affect agent behavior if system instructions are derived from it.

## Unknowns & Hypotheses
- **Hypothesis:** Some legacy documentation might still refer to older command names or complex workflows that were simplified in v2 (e.g., legacy "2-Command" terminology).
- **Hypothesis:** The fractal file system structure described in `PROTOCOL.md` might need verification to ensure it aligns with the actual v2.0.0 implementation before serving as a baseline.

## Execution Roadmap
1. **Verify Source of Truth:** Audit `.gemini/tasks/PROTOCOL.md` against current implementation to ensure it is up-to-date as a baseline for other docs. [E-000]
2. **Audit README.md:** Verify the "Core Loop Workflow" (plan, work, save) and "Core Architecture" against the `.toml` files, `SKILL.md`, and `COMMAND_SURFACE_SIMPLIFICATION_PLAN.md`. [E-001]
3. **Audit AGENTS.md:** Ensure the mission statement matches the Zero-Context Mandate in `SKILL.md`. [E-002]
4. **Audit GEMINI.md Files:** Check that versioning rules and protocol mentions are consistent. [E-003]
5. **Audit gemini-extension.json:** Verify that command descriptions and versioning are correct. [E-004]
6. **Cross-Reference Documentation:** Ensure the fractal file system and Deep Dissection schema are accurately described in all relevant docs. [E-005]
7. **Update Discrepancies:** Apply surgical fixes to any documentation that lags behind the current implementation or uses legacy terminology.
8. **Final Validation:** Conduct a final pass to ensure all success criteria are met.
