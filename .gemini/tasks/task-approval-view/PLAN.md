# Deep Dissection: Plan Approval View Implementation

## 1. Intent
Design and implement a formal "Plan Approval" HTML view (`APPROVAL.html`) for the Vector Protocol. This view must be distinct from the execution dashboard (`VIEW.html`) and act as a formal design document highlighting Intent, Scope, Risks, Side Effects, Trade-offs, Verification Gates, and a prominent Approval interface.

## 2. Success Criteria & Definition of Done
- [ ] `mockups/proposal_template.html` is created with a clean, formal document aesthetic (typography, whitespace, clear sections).
- [ ] `scripts/sync_state.py` is updated to generate an `APPROVAL.html` file alongside or integrated with `VIEW.html`.
- [ ] `APPROVAL.html` correctly extracts and renders "Intent", "Scope", "Risks/Unknowns", "Side Effects", "Trade-offs", and "Verification Gates" from `.gemini/PLAN.md`.
- [ ] `APPROVAL.html` includes a clear "Approval" section for user sign-off.
- [ ] The generation of `APPROVAL.html` does not break the existing generation of `VIEW.html`.

## 3. Dependencies
- Existing `.gemini/PLAN.md` structure.
- Existing `scripts/sync_state.py` script.
- Python environment for testing the sync script.

## 4. Side Effects
- Modifying `scripts/sync_state.py` introduces risk to the existing state synchronization and timeline view generation.
- Adds a new artifact (`APPROVAL.html`) to the `.gemini/` directory.

## 5. Unknowns & Hypotheses
- **Unknown:** The current structure and consistency of sections within `.gemini/PLAN.md`. If it varies, parsing regex/logic might be brittle.
- **Hypothesis:** We can use simple markdown parsing (e.g., matching headers like `## Unknowns & Hypotheses`) to extract the necessary blocks for the approval template.
- **Hypothesis:** `proposal_template.html` can be rendered using standard Python string formatting or a lightweight templating engine if one is already in use.

## 6. Execution Roadmap

### Batch 1: Independent Setup (Parallel Execution)

**task-approval-view-1: Design the Proposal Mockup**
- **Goal:** Create `mockups/proposal_template.html`.
- **Implementation:** Draft HTML/CSS for a formal document. Include placeholders (e.g., `{{intent}}`, `{{side_effects}}`) for data injection. Focus on clean typography, readability, and a clear "Approve" call-to-action area.

**task-approval-view-parse: Enhance Plan Parsing Logic**
- **Goal:** Ensure `PLAN.md` can be reliably parsed into structured sections.
- **Implementation:** Create or update parsing utilities (potentially inside `scripts/sync_state.py` or a helper module) to extract headers: Intent, Success Criteria (Verification Gates), Dependencies, Side Effects, Unknowns (Risks), and Trade-offs (if present). Write tests to verify extraction against a sample `PLAN.md`.

### Batch 2: Integration (Sequential)

**task-approval-view-2: Implement Dual View Generation**
- **Goal:** Update `scripts/sync_state.py` to generate `APPROVAL.html`.
- **Dependencies:** Requires `task-approval-view-1` and `task-approval-view-parse`.
- **Implementation:**
  - Modify `sync_state.py` to load `proposal_template.html`.
  - Read and parse `.gemini/PLAN.md`.
  - Inject the parsed markdown sections into the template.
  - Write the output to `.gemini/APPROVAL.html`.
  - Ensure existing `VIEW.html` logic remains intact.