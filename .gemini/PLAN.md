# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Verify the protocol's ideation-to-planning flow by promoting the "Verify File System Logic" backlog item, and address the architectural drift in `.gemini/CONTEXT.md` by officially migrating the documentation from the "4-File System" to the "5-File System" (incorporating `EVIDENCE.md`).

## 2. Strategic Analysis
- **First Principles:** The `.gemini/CONTEXT.md` file serves as the strict, invariant rulebook for the agent. If it contains outdated structural definitions (e.g., claiming a 4-file system when 5 files are actively required), it creates cognitive dissonance and potential hallucination risks during the auto-recovery (`resume`, `scan`) and persistence phases. 
- **Trade-offs:** 
  - *Complexity vs. Clarity:* Adding a 5th core file (`EVIDENCE.md`) slightly increases state management overhead but drastically improves auditability and traceability, which is a core tenet of the Vector Protocol.
- **Risk Assessment:** 
  - *Documentation Misses:* We must ensure *all* references to "4-File System" within `CONTEXT.md` are updated.

## 3. Design Specification
The `CONTEXT.md` file needs to be updated in two places:
1.  **Section 4. Architecture:** Update "Uses the **4-File System**..." to "**5-File System**".
2.  **Section 5. The 4-File System (State Persistence):** 
    - Rename header to "The 5-File System".
    - Append the `EVIDENCE.md` specification to the list:
      ```markdown
      5.  **`.gemini/EVIDENCE.md` (Ledger / Traceability):**
          *   **Role:** Factual evidence, reference URLs, and source traceability (`E-001` IDs).
          *   **Access:** Append-Only during validation passes.
      ```

## 4. Alternatives Considered
- **Deprecating `EVIDENCE.md`:** We could remove the 5th file and revert to a pure 4-file system to match the docs. *Rejected:* The `EVIDENCE.md` ledger is critical for the "strictly externally grounded" mandate defined in the project's `AGENTS.md`. Updating the `CONTEXT.md` is the correct path.

## 5. Implementation Roadmap
- [x] **Step 1:** Update `CONTEXT.md` Section 4 and Section 5 to officially define the "5-File System" architecture and document the role of `EVIDENCE.md`.
- [x] **Step 2:** Empty the `.gemini/BACKLOG.md` (as the dummy verification item has now been successfully promoted and processed).

## 6. Review
- User, please review this roadmap for verifying the flow and fixing the context drift. Ready to execute?