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
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Phase 3: Validation & Reliability. Implement an automated test suite and state linter to ensure protocol integrity and state consistency.

## 2. Problem Breakdown
- **Functional:** As the Vector Protocol prompts grow more complex (XML, CoT, etc.), manual verification is insufficient. A single typo in a `.toml` file or a hallucinated markdown tag in `PLAN.md` can break the entire state machine. Users need a "trust but verify" layer.
- **Technical:**
  - *Manifest/TOML Sync:* We need a script to ensure every command in `gemini-extension.json` exists as a valid `.toml` file with all required sections.
  - *State Invariants:* We need a script (`vector-lint`) that checks if `.gemini/*.md` files follow their respective schemas (e.g., `PLAN.md` has an "Objective", `STATE.md` has a "Phase").
  - *Continuous Integration:* These checks should run on every commit via GitHub Actions.

## 3. Design Discussion
- **Trade-offs:** Adding a linter script adds maintenance overhead, but it is necessary for a "high-assurance" protocol.
- **First Principles:** "Deterministic State". If the protocol state is intended to be machine-readable by subsequent agent turns, it MUST be validated against a schema.
- **Tools:** Python (since it's common for CLI scripting) or Node.js. Given this is a Gemini CLI extension (often used with JS/TS), a simple Node.js validation script might be more idiomatic, but Python is often faster for regex-based markdown linting. I'll use Python for the linter as it's excellent for text processing.

## 4. Proposed Solution
1. **`scripts/validate_commands.py`:** Parses `gemini-extension.json`, loads every `.toml`, and verifies it has `<role>`, `<instructions>`, `<goal>`, and `<output_format>`.
2. **`scripts/vector_lint.py`:** Checks `.gemini/` files for structural invariants (headers, mandatory sections).
3. **`.github/workflows/protocol-audit.yml`:** Runs both scripts on push/PR.
4. **Command Argument Guardrails:** Update `.toml` prompts to explicitly handle missing `{{args}}` with a "Help" style output.

## 5. Alternatives Considered
- *Custom extension command (`/vector:lint`):* This would be a great way for users to check their repo state locally. *Recommendation:* We'll start with the CI scripts and then wrap them in a `/vector:lint` command in Phase 4.

## 6. Revision History
- **2026-04-04:** Draft created from Backlog Review ("review backlog").

## 7. Implementation Roadmap
- [ ] **Task 1: Command Validation Script** - Create `scripts/validate_commands.py` to audit TOML prompt structure.
- [ ] **Task 2: Vector State Linter** - Create `scripts/vector_lint.py` to audit `.gemini/` file invariants.
- [ ] **Task 3: GitHub Actions CI** - Implement `.github/workflows/protocol-audit.yml` to automate verification.
- [ ] **Task 4: Argument Guardrails** - Add "If args is empty, show usage" logic to `plan.toml` and `work.toml`.
- [ ] **Task 5: Version Bump (v1.16.0)** - Update manifest and document the new reliability tools.

## 8. Review
- User, does this Phase 3 roadmap (Validation & Reliability) align with your priorities for the Vector Protocol?
\n\n---\n\n
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Author a series of detailed technical blog posts explaining the prompt engineering best practices (XML, CoT, Grounding, Context-First) recently implemented in the Vector Protocol.

## 2. Problem Breakdown
- **Functional:** The user wants to understand the theoretical and practical underpinnings of the recent prompt architecture upgrades. A detailed technical blog series will serve as both educational material and extended documentation for the extension.
- **Technical:**
  - Need to create a new directory (e.g., `docs/blog/`) to store the markdown files.
  - Write 4 separate, deep-dive articles based on the evidence gathered previously (`E-008`, `E-009`, `E-010`, `E-011`).
  - Each post must balance theory (referencing DeepMind/Anthropic guidelines) with practical implementation examples from the Vector Protocol's `.toml` files.

## 3. Design Discussion
- **Content Strategy:** 
  Each blog post should follow a clear narrative arc:
  1. **The Problem:** Why legacy prompt design fails (e.g., instruction drift, hallucination).
  2. **The Research/Best Practice:** What Google and Anthropic recommend.
  3. **The Implementation:** How we applied it to the Gemini CLI Vector Protocol.
  4. **The Impact:** The resulting improvements in deterministic agent behavior.
- **Format:** Markdown with standard YAML frontmatter for compatibility with static site generators (like Hugo, Docusaurus, or Next.js blogs).
- **Alternatives:** We could write one massive article, but breaking it down into a 4-part series makes the technical density more digestible and better suited for publishing.

## 4. Proposed Solution (The Blog Series)
- **Post 1:** *XML as the Native Language of LLMs* - Transitioning away from Markdown headers for semantic prompt boundaries.
- **Post 2:** *Enforcing Determinism with Mandatory `<thinking>` Blocks* - The power of forced Chain-of-Thought (CoT) before action.
- **Post 3:** *High-Assurance Perception:* - Utilizing Strict Grounding constraints to eliminate hallucination during RAG and repository scans.
- **Post 4:** *The "Context-First" Architecture* - Defeating the "Lost in the Middle" phenomenon by optimizing the sequence of data and instructions.

## 5. Revision History
- **2026-04-04:** Draft created based on user request to document recent prompt engineering improvements.

## 6. Implementation Roadmap
- [x] **Task 1: Setup Blog Directory** - Create `docs/blog/` and initialize an index or series introduction.
- [x] **Task 2: Author Blog 1 (XML Tagging)** - Write the technical deep dive on XML semantic boundaries [E-008].
- [x] **Task 3: Author Blog 2 (Chain of Thought)** - Write the deep dive on `<thinking>` blocks and planning [E-009].
- [x] **Task 4: Author Blog 3 (Strict Grounding)** - Write the deep dive on anti-hallucination constraints [E-010].
- [x] **Task 5: Author Blog 4 (Context-First)** - Write the deep dive on long-context sequence optimization [E-011].

## 7. Review
- Please review this Deep Mode draft plan for the technical blog series. Do these topics and the proposed structure align with what you are looking for?
\n\n---\n\n
