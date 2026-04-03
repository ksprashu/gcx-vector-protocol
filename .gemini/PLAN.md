# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Update the README.md and documentation to reflect the new tiered command model (Phase 1 Simplification), remove the deprecated `resume` command, update the manifest, and analyze the system state for backlog improvements.

## 2. Strategic Analysis
- **Context:** The `resume` command is deprecated as `plan` and `work` now handle implicit state recovery. Users have requested a simpler command surface.
- **Approach:** Standard Mode (Tactical). Remove deprecated code, update manifest, refactor docs into tiers, and update backlog.

## 3. Implementation Roadmap
- [x] **Step 1:** Delete `commands/vector/resume.toml`.
- [x] **Step 2:** Update `gemini-extension.json` (remove `resume`, bump version to `1.11.0`).
- [x] **Step 3:** Refactor `README.md` (Commands tiering, remove `/vector:resume`).
- [x] **Step 4:** System state review and Backlog update.
- [x] **Step 5:** Final verification and version check.

## 4. Review
- (Auto-Approved) Follows explicit user instructions to remove deprecated commands and implement the simplification docs.
