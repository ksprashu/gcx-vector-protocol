# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Current Objective
- Upgrade the Planning Phase to support Design Reviews and detailed Technical Specifications.

## 2. Roadmap
- [ ] Modify `commands/vector/plan.toml` to enforce a Rich Plan Template.
- [ ] Add instructions for the "Review Protocol" in the Plan command.

## 3. Specification
- **Rich Plan Template:**
    - **1. Objective:** Clear goal.
    - **2. Strategic Analysis:** Deconstruction, Trade-offs, Risks.
    - **3. Design Specification:** Technical details (signatures, logic, data).
    - **4. Roadmap:** Atomic implementation steps.
- **Review Protocol:**
    - Agent must ask user to read `.gemini/PLAN.md`.
    - User encourages to edit/comment on the file.
    - Iteration via `/vector:plan <feedback>`.
