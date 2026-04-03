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
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Convert Vector Protocol slash commands to skills with automated planning.

## 2. Strategic Analysis
- **First Principles:** The goal is to automate structured planning while maintaining user control over scanning and execution. We will refine the `vector-plan` skill to trigger automatically upon receiving an objective, back `/vector:work` and `/vector:scan` slash commands with skills, and convert other commands into skills like `vector-persist` and `vector-improve`.
- **Trade-offs:** 
  - *Automated Planning:* Reduces manual overhead but requires clear objective setting.
  - *Manual Execution/Scanning:* Keeps the user in control, which is the requested behavior.
- **Risk Assessment:** Ensure `AGENTS.md` clearly dictates the automated planning behavior so the LLM knows to activate the skill.

## 3. Implementation Roadmap
- [ ] **Task 1: Harmonize `vector-plan` skill** - Incorporate detailed logic from `plan.toml` into `skills/vector-plan/SKILL.md` and update `AGENTS.md` to mandate automated planning when a new objective is received.
- [ ] **Task 2: Refine `vector-scan` skill** - Update `skills/vector-scan/SKILL.md` with perception and drift detection logic from `scan.toml` and `context.toml`.
- [ ] **Task 3: Refine `vector-work` skill** - Update `skills/vector-work/SKILL.md` with atomic implementation and N-trial execution logic from `work.toml`.
- [ ] **Task 4: Implement `vector-persist` skill** - Consolidate logic from `init.toml`, `save.toml`, and `resume.toml` into `skills/vector-persist/SKILL.md` for lifecycle management.
- [ ] **Task 5: Implement `vector-improve` skill** - Port logic from `improve.toml` into `skills/vector-improve/SKILL.md` for backlog management.
- [ ] **Task 6: Update `gemini-extension.json`** - Ensure all skills and commands are correctly mapped to their refined definitions.
