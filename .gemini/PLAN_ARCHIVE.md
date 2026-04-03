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


## [2026-03-04 22:30:00] Archived Plan
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
- [x] **Task 1: Harmonize `vector-plan` skill** - Incorporate detailed logic from `plan.toml` into `skills/vector-plan/SKILL.md` and update `AGENTS.md` to mandate automated planning when a new objective is received.
- [x] **Task 2: Refine `vector-scan` skill** - Update `skills/vector-scan/SKILL.md` with perception and drift detection logic from `scan.toml` and `context.toml`.
- [x] **Task 3: Refine `vector-work` skill** - Update `skills/vector-work/SKILL.md` with atomic implementation and N-trial execution logic from `work.toml`.
- [x] **Task 4: Implement `vector-persist` skill** - Consolidate logic from `init.toml`, `save.toml`, and `resume.toml` into `skills/vector-persist/SKILL.md` for lifecycle management.
- [x] **Task 5: Implement `vector-improve` skill** - Port logic from `improve.toml` into `skills/vector-improve/SKILL.md` for backlog management.
- [x] **Task 6: Update `gemini-extension.json`** - Ensure all skills and commands are correctly mapped to their refined definitions.

--- Archived on Fri Mar  4 22:35:12 IST 2026 ---


## [2026-03-29 11:30:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Implement a unified, table-driven "Dashboard" output format across all Vector Protocol CLI commands (`scan`, `plan`, `work`, `status`, `resume`, `improve`, `save`). This will give the user a clean, visual representation of the current phase, objective, completed tasks, pending tasks, and backlog items.

## 2. Strategic Analysis
- **First Principles:** The Vector Protocol relies on `.toml` files to define the system instructions for each command. By updating the `**Output:**` sections within these prompts, we can force the LLM to format its responses as rich Markdown tables (e.g., Status: ✅/⏳/🔄) instead of simple bullet points.
- **Trade-offs:** 
  - *Readability vs. Tokens:* Generating Markdown tables consumes slightly more output tokens, but the resulting boost in readability and user experience (UX) is highly worthwhile for a CLI workflow.
- **Risk Assessment:** 
  - *Formatting Consistency:* The LLM might use inconsistent headers if not strictly defined. We mitigate this by explicitly specifying the exact columns for each table type in the prompt instructions.

## 3. Design Specification
We will introduce standard table definitions to the prompt outputs.

**Standard Tables to be Introduced:**
1.  **State & Progress Dashboard:** 
    *   `| Phase | Objective | Last Action | Next Step | Pending Tasks | Completed |`
2.  **Plan / Work Checklist:**
    *   `| Status (✅/⏳/🔄) | Task | Details |`
3.  **Scan / Audit Findings:**
    *   `| Status (✅/❌/⚠️) | Item | Insight / Drift |`
4.  **Ideation / Backlog:**
    *   `| Type (Plan/Backlog) | Status | Item | Value / Impact |`

## 4. Alternatives Considered
- **CLI Framework TUI (Text User Interface):** Modify the core Gemini CLI binary to render interactive TUIs for these tables. *Rejected:* This falls outside the scope of an extension and would require changes to the core CLI. Markdown tables are natively supported, beautifully rendered by most terminal markdown viewers, and perfectly fit the extension pattern.

## 5. Implementation Roadmap
- [x] **Step 1:** Update `plan.toml` and `work.toml` to output the State Dashboard and Plan Checklist tables.
- [x] **Step 2:** Update `scan.toml` and `status.toml` to output the State Dashboard and Findings/Backlog tables.
- [x] **Step 3:** Update `resume.toml`, `improve.toml`, and `save.toml` to incorporate the State Dashboard and their respective specific tables (Ideation, Saved state).
- [x] **Step 4:** Increment extension minor version in `gemini-extension.json`.

## 6. Review
- User, please review this roadmap for establishing the rich Markdown dashboard and checklists. Ready to execute?

--- Archived on Sun Mar 29 11:45:00 IST 2026 ---


## [2026-03-29 14:00:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Implement a "Dual-Mode" planning system within `/vector:plan`. It will intelligently route between a lean **Standard Mode** (for tactical fixes) and a comprehensive **Deep Mode** (for iterative, collaborative architectural design of new features/concepts).

## 2. Strategic Analysis
- **First Principles:** Different tasks have different cognitive and token requirements. Simple tasks require rigid checklists; complex tasks require collaborative ideation, trade-off analysis, and iterative refinement before execution begins.
- **Trade-offs:** 
  - *Adding a new command (`/vector:deepplan`) vs. Dual-Mode `/vector:plan`:* Adding a command clutters the CLI surface and violates our simplification plan. A smart, dual-mode prompt inside `plan.toml` maintains a clean UX while delivering the necessary flexibility.
- **Risk Assessment:** 
  - *Mode Confusion:* The AI might choose the wrong mode. *Mitigation:* We will explicitly instruct the AI to state which mode it selected and why, and allow the user to override it (e.g., "re-plan this using deep mode").

## 3. Design Specification
We will update `commands/vector/plan.toml` with the following routing logic and templates:

**Routing Logic:**
- If the objective implies a new feature, complex refactor, or includes keywords like "deep", "design", or "concept", use **DEEP MODE**.
- Otherwise, use **STANDARD MODE**.

**Template A: Standard Mode (Tactical)**
```markdown
## 1. Objective
## 2. Implementation Roadmap
## 3. Review
```

**Template B: Deep Mode (Collaborative)**
```markdown
## 1. Concept Objective (Status: DRAFT)
## 2. Problem Breakdown (Functional & Technical)
## 3. Design Discussion & Trade-offs
## 4. Proposed Solution
## 5. Alternatives & Sub-Agent Suggestions
## 6. Feedback & Revision History
## 7. Implementation Roadmap
## 8. Review (Awaiting User APPROVAL)
```

## 4. Alternatives Considered
- **Separate Commands:** Creating `/vector:design` and `/vector:plan`. *Rejected:* Violates the `COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` goal of keeping the daily workflow to just 3 core commands.

## 5. Implementation Roadmap
- [x] **Step 1:** Update `commands/vector/plan.toml` to include the Dual-Mode routing logic and both markdown templates. Add instructions for handling iterative feedback cycles.
- [x] **Step 2:** Update `.gemini/CONTEXT.md` to formally document the Dual-Mode Planning standard and the iterative `DRAFT -> APPROVED` lifecycle.
- [x] **Step 3:** Increment extension minor version in `gemini-extension.json` to 1.9.0.

## 6. Review
- User, please review this roadmap for establishing Dual-Mode planning. Ready to execute?

--- Archived on Sun Mar 29 14:15:22 IST 2026 ---


## [2026-03-29 16:30:00] Archived Plan
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Replace heavy Markdown tables ("State Dashboard Table" and "Work Checklist Table") across all Vector commands with simpler, native-feeling CLI bulleted lists and checkboxes (`- [ ]`), per user feedback. We will retain the `Evidence Table` as a Markdown table.

## 2. Strategic Analysis
- **First Principles:** Command line interfaces should prioritize high signal-to-noise ratios. Tables with ASCII borders add cognitive load and wrap poorly on narrow screens.
- **Trade-offs:** We lose structured columnar alignment but drastically improve readability and visual simplicity.

## 3. Design Specification
The `Output` instruction in all commands will replace the dashboard/checklist table prompts with:
*   **Session Dashboard:** A simple bulleted list containing `Phase`, `Objective`, `Status` (where applicable), and `Next Step`.
*   **Progress Checklist:** A standard markdown checklist `- [ ] Task Name: Details`.
*   **Evidence Table:** (Remains unchanged).

## 4. Alternatives Considered
- Keep tables but simplify headers. *Rejected:* Still feels too "heavy" for daily CLI interaction.

## 5. Implementation Roadmap
- [x] **Step 1:** Update `plan.toml` and `work.toml` to use bulleted checklists and a text-based Session Dashboard.
- [x] **Step 2:** Update `status.toml`, `scan.toml`, and `improve.toml` to simplify their dashboard and findings outputs.
- [x] **Step 3:** Update the remaining utility commands (`init`, `reset`, `resume`, `save`, `context`).
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
