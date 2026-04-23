# CRITIQUE: Documentation Sync for Vector Protocol v2.0.0

## Flaws Detected in `.gemini/PLAN.md`

1. **Missing Critical Dependency:** 
   The plan fails to list `docs/COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` as a Dependency. This document defines the "newly designed" tiered command model and is the authoritative source for the Phase 1 documentation rollout.

2. **Roadmap Misalignment with Design:** 
   Step 1 of the Execution Roadmap mandates verifying the "2-Command Workflow". However, the simplification plan explicitly defines a "Tiered command model" featuring a "Core loop" (plan, work, save) and other situational commands. The roadmap must audit against the tiered model, not the legacy "2-Command" framing.

3. **Missing Verification Target (`gemini-extension.json`):** 
   The extension manifest is a critical piece of documentation containing the extension's description, version, and exposed commands. It is omitted from the "Success Criteria" and the "Execution Roadmap".

4. **Ambiguous Role of `PROTOCOL.md`:** 
   `.gemini/tasks/PROTOCOL.md` is listed as a dependency, but if the protocol was "newly designed", this file itself might need verification or updates to ensure it matches the actual v2.0.0 design before using it as the sole Source of Truth.

## Required Actions
- Add `docs/COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` to Dependencies.
- Update Step 1 and Success Criteria to reflect the "Tiered command model" and "Core loop" terminology instead of "2-Command Workflow".
- Add an audit step and success criteria for `gemini-extension.json`.
- Ensure `PROTOCOL.md` is verified as up-to-date before being used as the baseline.