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