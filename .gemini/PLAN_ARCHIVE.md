# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Set dynamic default values for `N` in the "Best-of-N" evaluation loop based on the model class (N=3 for Flash, N=1 for Pro, N=5 for Flash-Lite) when the user requests multiple options but does not specify an exact number.

## 2. Strategic Analysis
- **First Principles:** The Vector Protocol commands (`plan` and `work`) instruct the main agent on how to behave. By modifying the prompt instructions in these `.toml` files, we can explicitly define the heuristic the agent should use to infer `N` based on its own model capabilities.
- **Trade-offs:** 
  - *Pro Models:* N=1 minimizes token cost and latency since Pro models are highly capable and expensive.
  - *Flash Models:* N=3 provides a balanced, fast synthesis.
  - *Flash-Lite Models:* N=5 leverages the extreme speed and low cost of lite models to overcome their lower individual accuracy through volume synthesis.
- **Risk Assessment:** 
  - *Model Awareness:* The LLM might not explicitly know its own tier. However, the system instructions or the user's prompt generally provide context, or the agent can deduce it based on the capabilities. The instruction will direct the agent to infer its model class and apply the corresponding `N`.

## 3. Design Specification
We will update the `N-Trial Synthesis` step in `plan.toml` and the `N-Trial Execution` step in `work.toml`.

**Updated Instruction snippet:**
```text
(If `trials=N` or multiple options requested. If N is unspecified, default to: N=3 for Flash models, N=1 for Pro models, N=5 for Flash-Lite models):
```

## 4. Alternatives Considered
- **CLI Framework Argument:** We could parse the model flag in the CLI framework itself and pass `N` as an argument. *Rejected:* This extension focuses on the protocol via prompt engineering (`.toml` files) rather than modifying the core CLI source code. Using prompt-based heuristics is simpler and adheres to the extension boundaries.

## 5. Implementation Roadmap
- [x] **Step 1:** Update the `N-Trial Synthesis` instruction in `commands/vector/plan.toml` to include the dynamic default N heuristic.
- [x] **Step 2:** Update the `N-Trial Execution` instruction in `commands/vector/work.toml` to include the same heuristic.
- [x] **Step 3:** Increment extension minor version in `gemini-extension.json`.

## 6. Review
- User, please review this roadmap for establishing the default `N` heuristics. Ready to proceed?
--- Archived on Wed Mar  4 21:38:22 IST 2026 ---


## [2026-03-04 21:51:24] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Convert `gcx-vector-protocol` extension into a single, comprehensive agent skill named `vector-protocol`.

## 2. Strategic Analysis
- **First Principles:** The Vector Protocol is a procedural onboarding guide for an agent to work on a specific project. This is exactly what Skills are designed for.
...
- [x] **Step 5: Manifest Update** - Prepare `gemini-extension.json` for the new skill.
- [x] **Step 6: Installation & Handoff** - Install the skill and provide reload instructions.

## 6. Review
User, please review the conversion plan. Ready to execute?
*(Recommendation: We should decide whether to deprecate the TOML commands after the skill is fully functional.)*


## [2026-03-04 22:30:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Convert Vector Protocol slash commands to skills with automated planning.
...
- [x] **Task 6: Update `gemini-extension.json`** - Ensure all skills and commands are correctly mapped to their refined definitions.

--- Archived on Fri Mar  4 22:35:12 IST 2026 ---


## [2026-03-29 11:30:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Implement a unified, table-driven "Dashboard" output format across all Vector Protocol CLI commands (`scan`, `plan`, `work`, `status`, `resume`, `improve`, `save`).
...
- [x] **Step 4: Increment extension minor version in `gemini-extension.json`.**

## 6. Review
- User, please review this roadmap for establishing the rich Markdown dashboard and checklists. Ready to execute?

--- Archived on Sun Mar 29 11:45:00 IST 2026 ---


## [2026-03-29 14:00:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Implement a "Dual-Mode" planning system within `/vector:plan`. 
...
- [x] **Step 3:** Increment extension minor version in `gemini-extension.json` to 1.9.0.

## 6. Review
- User, please review this roadmap for establishing Dual-Mode planning. Ready to execute?

--- Archived on Sun Mar 29 14:15:22 IST 2026 ---


## [2026-03-29 16:30:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Replace heavy Markdown tables ("State Dashboard Table" and "Work Checklist Table") across all Vector commands with simpler, native-feeling CLI bulleted lists and checkboxes (`- [ ]`), per user feedback.
...
- [x] **Step 4:** Increment extension version to `1.10.1` (UX Polish).

## 6. Review
- (Auto-Approved) User explicitly requested simple text checklists/bullet lists rather than a table.

--- Archived on Sun Mar 29 16:45:10 IST 2026 ---


## [2026-04-03 14:56:39] Archived Plan
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

--- Archived on Fri Apr  3 14:56:39 IST 2026 ---
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Streamline the Vector Protocol command surface by removing redundant and deprecated commands (`init`, `resume`, `status`, `reset`).

## 2. Strategic Analysis
- **Problem:** The command surface has grown to 10 commands, several of which overlap with the "auto-bootstrap" and "auto-resume" logic now embedded in the core loop (`plan`, `work`, `scan`, `save`).
- **Approach:** 
  1. Audit cross-command dependencies to ensure no critical recovery logic is lost.
  2. Remove redundant TOML files and update the extension manifest.
  3. Synchronize documentation (`README.md`, `AGENTS.md`, `GEMINI.md`) to reflect the new 6-command surface.
  4. Perform a version bump to `1.14.0`.

## 3. Implementation Roadmap
- [x] **Task 1: Code Audit & Final Verification** - Verify no remaining logic depends on `init`, `resume`, `status`, or `reset`.
- [x] **Task 2: Command Removal** - Delete `init.toml`, `resume.toml`, `status.toml`, `reset.toml` and update `gemini-extension.json`.
- [x] **Task 3: Documentation Sync** - Update `README.md`, `AGENTS.md`, and `GEMINI.md`.
- [x] **Task 4: Version Update** - Increment version to `1.14.0` in `gemini-extension.json`.

## 4. Review
- (Approved) Command surface streamlined to 6 core commands.
\n\n---\n\n
