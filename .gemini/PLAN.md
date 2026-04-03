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
