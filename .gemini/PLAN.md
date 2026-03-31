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