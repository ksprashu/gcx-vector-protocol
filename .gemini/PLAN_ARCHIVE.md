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

**Files to modify:**
- `commands/vector/plan.toml`
- `commands/vector/work.toml`
- `commands/vector/scan.toml`
- `commands/vector/status.toml`
- `commands/vector/resume.toml`
- `commands/vector/improve.toml`
- `commands/vector/save.toml`

## 4. Alternatives Considered
- **CLI Framework TUI (Text User Interface):** Modify the core Gemini CLI binary to render interactive TUIs for these tables. *Rejected:* This falls outside the scope of an extension and would require changes to the core CLI. Markdown tables are natively supported, beautifully rendered by most terminal markdown viewers, and perfectly fit the extension pattern.

## 5. Implementation Roadmap
- [x] **Step 1:** Update `plan.toml` and `work.toml` to output the State Dashboard and Plan Checklist tables.
- [x] **Step 2:** Update `scan.toml` and `status.toml` to output the State Dashboard and Findings/Backlog tables.
- [x] **Step 3:** Update `resume.toml`, `improve.toml`, and `save.toml` to incorporate the State Dashboard and their respective specific tables (Ideation, Saved state).
- [x] **Step 4:** Increment extension minor version in `gemini-extension.json`.

## 6. Review
- User, please review this roadmap for establishing the rich Markdown dashboard and checklists. Ready to execute?# 🗺️ PLAN
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
- User, please review this roadmap for establishing Dual-Mode planning. Ready to execute?# 🗺️ PLAN
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
- [ ] **Step 1:** Update `plan.toml` and `work.toml` to use bulleted checklists and a text-based Session Dashboard.
- [ ] **Step 2:** Update `status.toml`, `scan.toml`, and `improve.toml` to simplify their dashboard and findings outputs.
- [ ] **Step 3:** Update the remaining utility commands (`init`, `reset`, `resume`, `save`, `context`).
- [ ] **Step 4:** Increment extension version to `1.10.1` (UX Polish).

## 6. Review
- (Auto-Approved) User explicitly requested simple text checklists/bullet lists rather than a table.