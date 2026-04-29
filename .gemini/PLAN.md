# PLAN: Integrate @cli_help Agent into Vector Protocol

## 1. Intent
Integrate the `@cli_help` agent into the Vector Protocol as the authoritative source for Gemini CLI capabilities. This establishes a strict "Reuse First" principle, ensuring the swarm leverages out-of-the-box Gemini agents (like `codebase_investigator` or `browser_agent`) instead of reinventing wheels.

## 2. Success Criteria & Definition of Done
- `AGENTS.md` explicitly mandates consulting `@cli_help` before proposing any new tool, script, or subagent.
- `skills/vector/SKILL.md` integrates `@cli_help` into the grounding and capability discovery phase of dynamic loops.
- A "Reuse First" principle is established to favor existing tools.
- `scripts/grounding_validator.py` (or equivalent protocol verification) includes a check to ensure `@cli_help` or existing documentation was consulted before adding new capabilities.

## 3. Dependencies
- Target files exist and are writable: `AGENTS.md`, `skills/vector/SKILL.md`, and `scripts/grounding_validator.py`.

## 4. Side Effects
- Planning and implementation loops will now inherently block on a capability discovery phase using `@cli_help`.
- Grounding validator will fail validation if evidence of `@cli_help` consultation is absent when proposing new tools.

## 5. Unknowns & Hypotheses
- **Unknown:** How exactly `scripts/grounding_validator.py` parses evidence of agent consultation.
- **Hypothesis:** By enforcing standard logging of capability checks, we can statically parse logs or `EVIDENCE.json` to verify `@cli_help` was used.

## 6. Execution Roadmap

[PARALLEL BATCH 1]
- [x] **Task 1: Update AGENTS.md**
  - Add the "Reuse First" mandate.
  - Require consultation with `@cli_help` before proposing new tools, scripts, or subagents.
- [x] **Task 2: Update skills/vector/SKILL.md**
  - Include `@cli_help` in the capability discovery/grounding phase of the dynamic loop workflow.
- [x] **Task 3: Update Verification System**
  - Define a standard evidence schema for capability checks: `{"type": "capability_check", "agent": "@cli_help", "query": "...", "result": "..."}`.
  - Mandate that this schema must be present in the evidence ledger if a new capability is introduced.
  - Update `scripts/grounding_validator.py` to enforce that evidence of `@cli_help` consultation exists using this schema when introducing new subagents or tools.