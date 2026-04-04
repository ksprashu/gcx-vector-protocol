# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Resolve the persistent "it still keeps wanting to install the skill" prompt in the Gemini CLI by auditing extension/skill registration and cleaning up stale artifacts.

## 2. Strategic Analysis
- **Problem:** The CLI repeatedly prompts to install skills even if they are defined in the manifest. This often happens due to version mismatches, duplicate registrations, or the presence of both binary `.skill` files and source `SKILL.md` directories.
- **Approach:** 
  1. Audit current CLI registration state.
  2. Identify and remove redundant binary files (`vector-plan.skill`).
  3. Ensure the manifest `gemini-extension.json` points to valid directory-based skills.
  4. Force-refresh the extension registration.

## 3. Implementation Roadmap
- [x] **Task 0: Update Protocol** - Synchronized PLAN.md and STATE.md.
- [x] **Task 1: Audit Registration** - Check `gemini extensions list` and `gemini skills list` for duplicates or stale entries.
- [x] **Task 2: Clean Stale Artifacts** - Identify and remove binary `.skill` files that conflict with the source directories.
- [x] **Task 3: Validate Manifest** - Ensure `gemini-extension.json` version and paths are consistent with the latest 1.12.0 unify.
- [x] **Task 4: Verification** - Re-load the extension and verify the prompt is resolved.

## 4. Review
- (Draft) Investigating the "install skill" loop.
