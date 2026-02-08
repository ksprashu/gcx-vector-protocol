# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Current Objective
- Implement `/vector:improve` command for Ideation and Project Enhancement.

## 2. Strategic Analysis
- **Goal:** Enable "Brainstorming/Enhancement" mode.
- **Decision:** Create a dedicated `/vector:improve` command.
- **Rationale:** Separates "Idea Generation" (Creativity) from "Execution Planning" (Logistics).

## 3. Design Specification
- **Command:** `/vector:improve [focus_area]`
- **System Prompt:**
    - Role: Senior Architect / Product Owner.
    - Task: Review project state, identify gaps (Production Readiness, Features, Tech Debt).
    - Output: List of actionable **Enhancement Proposals**.

## 4. Implementation Roadmap
- [ ] Create `commands/vector/improve.toml`.
- [ ] Register command in `gemini-extension.json`.