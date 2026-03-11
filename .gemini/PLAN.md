# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Decompose the single `vector-protocol` mega-skill into granular, phase-specific skills for better intent-based selection.

## 2. Strategic Analysis
- **First Principles:** The Gemini CLI agent selects tools (skills) based on their name and description in the manifest. A single mega-skill forces the agent to load irrelevant instructions for every task. Decomposing into `vector-scan`, `vector-plan`, etc., allows for "Just-in-Time" context loading.
- **Trade-offs:** 
  - *Granular Skills:* Improved triggering accuracy, lower context bloat per turn, clearer intent.
  - *Single Skill:* Easier to maintain, all context available at once.
  - *Decision:* Proceed with decomposition to align with the agent's internal tool-selection heuristics.
- **Risk Assessment:**
  - *Context Fragmentation:* Solved by including "Core Rules" (5-File System, Grounding) in every skill's `SKILL.md`.
  - *Registry Bloat:* Managed by clear naming conventions (`vector-*`).

## 3. Design Specification
- **Skill 1: `vector-scan` (Perception)**
  - Description: "Audit project state, detect drift in protocol files, and sync context. Use during the PERCEPTION phase to ensure the agent's mental model matches the repository truth."
- **Skill 2: `vector-plan` (Strategy)**
  - Description: "Develop a rigorous implementation roadmap with analysis, design, and atomic steps. Use during the STRATEGY phase to define how an objective will be achieved before writing code."
- **Skill 3: `vector-work` (Execution)**
  - Description: "Execute atomic, verifiable implementation steps from the project plan. Use during the EXECUTION phase to implement changes, run tests, and record results."
- **Skill 4: `vector-persist` (Persistence)**
  - Description: "Persist progress, sync state, rotate scratchpads, and commit changes. Use during the PERSISTENCE phase or when a meaningful milestone is reached."
- **Skill 5: `vector-improve` (Ideation)**
  - Description: "Analyze the codebase to find and log backlog-worthy improvements. Use during the IDEATION phase to capture technical debt or future features."
- **Shared logic:** Every skill will include the "Mission" and "5-File System" rules to ensure consistent behavior.

## 4. Alternatives Considered
- **Keep Mega-Skill + References:** *Rejected.* While references are loaded "as needed", the agent still has to *know* which reference to load. Having separate skills makes the phase-specific instructions the *primary* content for that specific intent.
- **Namespace by Phase (`scan-vector`, `plan-vector`):** *Rejected.* `vector-*` prefix is more standard for extension-specific grouping.

## 5. Implementation Roadmap
- [x] **Step 1: Initialization** - Use `init_skill.cjs` to create directories for `vector-scan`, `vector-plan`, `vector-work`, `vector-persist`, and `vector-improve`.
- [x] **Step 2: Logic Transfer** - Port content from `skills/vector-protocol/references/*.md` into the new `SKILL.md` files.
- [x] **Step 3: Core Rule Integration** - Add Mission and 5-File System rules to each `SKILL.md`.
- [x] **Step 4: Packaging** - Run `package_skill.cjs` on all 5 new skill directories.
- [x] **Step 5: Manifest Update** - Update `gemini-extension.json` to version 1.9.0, register new skills, and remove the old `vector-protocol` skill registration.
- [x] **Step 6: Local Installation** - Install the 5 `.skill` files using `gemini skills install --scope workspace`.
- [x] **Step 7: Verification** - Verify installation via `gemini skills list`.

## 6. Review
User, please review the decomposition plan. Ready to execute?
*(Note: This will significantly improve my ability to trigger the correct protocol phase autonomously.)*
