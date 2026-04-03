# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Resolve git pull conflicts, merge the Skill-Based Refactor (v1.10.0 local) with the Command Surface Simplification (v1.11.0 remote), and finalize the extension as version 1.12.0.

## 2. Strategic Analysis
- **Merge Strategy:** 
  - **Skills vs. TOML:** Accept the local refactor which moves planning and other logic to skills. Remove `plan.toml` and `resume.toml`.
  - **UX & Docs:** Retain the remote's Tiered Command Model and README improvements, but update them to explain the automated planning skill.
  - **Versioning:** Bump to v1.12.0.
- **Risk Assessment:** Ensure automated planning mandate in `AGENTS.md` is correct and consistent with `README.md`.

## 3. Implementation Roadmap
- [x] **Task 1: Resolve `gemini-extension.json`** - Merge skills list, update version to 1.12.0, remove `plan.toml` and `resume.toml`.
- [x] **Task 2: Resolve `plan.toml`** - formally remove the file as it's replaced by the `vector-plan` skill.
- [x] **Task 3: Merge `.gemini/` protocol files** - Consolidate Evidence, Plan, State, and Archives.
- [ ] **Task 4: Update Documentation** - Sync `README.md` and `AGENTS.md` to reflect the final 1.12.0 state (Automated Planning + Tiered Commands).
- [ ] **Task 5: Final Verification** - Verify extension manifest and skill registration.

## 4. Review
- (In-Progress) Resolving conflicts and unifying the two divergent branches.
