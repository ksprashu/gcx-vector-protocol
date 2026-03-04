# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Convert `gcx-vector-protocol` extension into a single, comprehensive agent skill named `vector-protocol`.

## 2. Strategic Analysis
- **First Principles:** The Vector Protocol is a procedural onboarding guide for an agent to work on a specific project. This is exactly what Skills are designed for.
- **Trade-offs:** 
  - *Slash Commands:* Explicit user control, less agentic autonomy.
  - *Skills:* High agentic autonomy, proactive triggering, context-efficient via Progressive Disclosure.
  - *Decision:* Convert to a single skill with sub-references for each phase to maintain protocol integrity while improving usability.
- **Risk Assessment:**
  - *Context Bloat:* Managed by reference files.
  - *Triggering Reliability:* Handled by a clear description in `SKILL.md` frontmatter.

## 3. Design Specification
- **Skill Name:** `vector-protocol`
- **Trigger Description:** "A rigorous, state-aware development workflow extension for Gemini CLI. Implements the Research -> Strategy -> Execution lifecycle with strict grounding and persistent state management. Use when starting a new task, managing project state via the 5-file system, or requiring high-signal engineering workflows."
- **Structure:**
  - `skills/vector-protocol/SKILL.md`: Protocol overview, Mission (from `AGENTS.md`), Hierarchy of Truth, 5-File System rules.
  - `skills/vector-protocol/references/perception.md`: `scan.toml` + `context.toml` instructions.
  - `skills/vector-protocol/references/strategy.md`: `plan.toml` instructions.
  - `skills/vector-protocol/references/execution.md`: `work.toml` instructions.
  - `skills/vector-protocol/references/persistence.md`: `save.toml`, `resume.toml`, `status.toml`, `reset.toml`.
  - `skills/vector-protocol/references/ideation.md`: `improve.toml` instructions.
- **API Citations:** `skill-creator` (Core Principle: Concise is Key, Progressive Disclosure).

## 4. Alternatives Considered
- **Multiple Skills:** Create a skill for each command (e.g., `vector-scan`, `vector-plan`). *Rejected:* This fragments the protocol and makes it harder for the agent to maintain the overall lifecycle context. A single skill with references is more cohesive.
- **Keep Commands:** Retain the TOML commands. *Decision:* Move logic to the skill as the primary interface, potentially deprecating commands once the skill is verified.

## 5. Implementation Roadmap
- [x] **Step 1: Initialization** - Run `init_skill.cjs` to bootstrap `skills/vector-protocol/`.
- [x] **Step 2: Logic Drafting (Parallel)** - Use $N=3$ `generalist` sub-agents to draft Markdown from TOML logic.
- [x] **Step 3: Content Implementation** - Finalize `SKILL.md` and reference files.
- [x] **Step 4: Validation & Packaging** - Run `package_skill.cjs` to create the `.skill` bundle.
- [x] **Step 5: Manifest Update** - Prepare `gemini-extension.json` for the new skill.
- [x] **Step 6: Installation & Handoff** - Install the skill and provide reload instructions.

## 6. Review
User, please review the conversion plan. Ready to execute?
*(Recommendation: We should decide whether to deprecate the TOML commands after the skill is fully functional.)*
