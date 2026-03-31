# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective (Status: APPROVED)
- **Goal:** Conduct a comprehensive codebase audit of all 10 Vector Protocol commands (`init`, `scan`, `plan`, `work`, `save`, `resume`, `status`, `improve`, `reset`, `context`) to eradicate UX inconsistencies, standardize the new Dashboard output formats, and address functional redundancies.

## 2. Problem Breakdown
- **Functional (UX) Breakdown:** 
  - Recent updates (v1.8.0) introduced rich Markdown tables and the `State Dashboard Table`. However, commands like `init.toml`, `reset.toml`, and `context.toml` were not updated and still use legacy bulleted lists. This breaks the user's mental model of a unified dashboard.
  - The `COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` aims to reduce cognitive load. Having commands that do the exact same thing (like `/vector:resume` vs the auto-resume built into `/vector:plan`) creates friction.
- **Technical Breakdown:**
  - `init.toml`: Missing the Dashboard Table output. The prompt mentions `.gemini/EVIDENCE.md` but lacks the formal "5-File System" nomenclature.
  - `reset.toml`: Missing the Dashboard Table output. Extremely barebones output.
  - `context.toml`: Uses legacy `Output (Proposal Stage)` and `Output (After Approval & Apply)` blocks with bullet points instead of a structured `Context Audit Table`.
  - `resume.toml`: Functionally redundant since `plan`, `work`, and `scan` now all contain "Auto-Recovery + Fast Scan" logic that implicitly resumes.

## 3. Design Discussion & Trade-offs
- **Addressing Redundancy (The `resume` problem):** We could delete `resume.toml`. However, our `COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` explicitly mandates: *"Do not remove existing commands in this proposal."* (Phase 1). 
  - *Trade-off Solution:* Instead of deleting it, we prefix its description in `resume.toml` with `(Deprecated)` or `(Legacy)` and update its documentation, adhering to the safety constraints while signaling to users that they don't need it.
- **Standardizing Output Profiles:** Every command, regardless of function, should begin its `**Output:**` section with the exact same `State Dashboard Table` structure. This ensures that no matter what command a user types, they immediately understand their current context.

## 4. Proposed Solution
We will surgically update the outlier commands to bring them up to the v1.9.0 protocol standards:
1.  **`context.toml`:** 
    - Add `State Dashboard Table`.
    - Convert change proposals into a `Context Audit Table` with columns: `| Status (ADD/UPD/REM) | Item | Diff / Detail |`.
2.  **`init.toml`:**
    - Add `State Dashboard Table`.
    - Update prompt verbiage to explicitly reference establishing the "5-File System".
3.  **`reset.toml`:**
    - Add `State Dashboard Table` to confirm the reset to `[IDLE]`.
4.  **`resume.toml`:**
    - Update the `description` field to: `"♻️ RESUME: (Deprecated) Recovery Phase. Auto-handled by plan/work."`

## 5. Alternatives Considered
- **Aggressive Pruning:** Delete `resume.toml` and `init.toml` entirely, relying solely on auto-bootstrap. *Rejected:* `init --force` is still required for hard-resetting a project, and the Simplification Plan strictly forbids command deletion in the current phase to protect advanced user workflows.

## 6. Revision History
- **v1 (2026-03-29):** Initial DRAFT. Proposed standardizing `init`, `reset`, `context` outputs, and deprecating `resume`.

## 7. Implementation Roadmap
- [x] **Step 1:** Update `commands/vector/context.toml` to output the `State Dashboard Table` and `Context Audit Table`.
- [x] **Step 2:** Update `commands/vector/init.toml` and `commands/vector/reset.toml` to output the `State Dashboard Table`.
- [x] **Step 3:** Deprecate `resume.toml` by updating its description field.
- [x] **Step 4:** Increment extension minor version in `gemini-extension.json` to 1.10.0 (Consistency Pass).

## 8. Review (Awaiting User APPROVAL)
- User, please review this Concept Document. Should we proceed with standardizing these outlier commands and formally deprecating `resume` via its description? Provide feedback or reply with "APPROVED" to proceed.