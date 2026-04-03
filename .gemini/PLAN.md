# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Resolve git pull conflicts, merge the Skill-Based Refactor (v1.10.0 local) with the Command Surface Simplification (v1.11.0 remote), and finalize the extension as version 1.12.0.

## 2. Strategic Analysis
- **Context:** The repository has undergone two parallel evolutions. HEAD implemented a conversion of TOML commands into automated agent skills. The remote implemented a "Command Surface Simplification" (Tiered commands, removing `resume`).
- **Collision Resolution:** A name collision with a sibling repository `skills-vector-protocol` was identified and resolved locally by renaming the other extension.
- **Merge Strategy:** 
  - **Skills vs. TOML:** Adopt the Skill-based architecture. Commands like `plan` are now automated skills.
  - **UX & Docs:** Retain the remote's Tiered Command Model and README improvements, updated for skills.
  - **Versioning:** Finalize as v1.12.0.
- **Risk Assessment:** Ensure automated planning mandate in `AGENTS.md` is correct.

## 3. Implementation Roadmap
- [x] **Task 1: Resolve `gemini-extension.json`** - Merge skills list, update version to 1.12.0, remove `plan.toml` and `resume.toml`.
- [x] **Task 2: Resolve `plan.toml`** - Formally remove the file as it's replaced by the `vector-plan` skill.
- [x] **Task 3: Merge `.gemini/` protocol files** - Consolidate Evidence, Plan, State, and Archives.
- [ ] **Task 4: Update Documentation** - Sync `README.md` and `AGENTS.md` to reflect the final 1.12.0 state (Automated Planning + Tiered Commands).
- [ ] **Task 5: Final Verification** - Verify extension manifest and skill registration.

## 4. Review
- (In-Progress) Resolving conflicts and unifying the two divergent branches.
