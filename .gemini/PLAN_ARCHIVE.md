# Vector Protocol Plan: Clarify Commands vs Skill and Rename Skill

## 1. Intent
Address user confusion regarding the "3 things" (2 commands + 1 skill) in the Vector Protocol extension by clarifying their distinct roles (Commands as triggers, Skill as procedural knowledge/rules engine) and renaming the skill from `vector-protocol` to `vector` for simplicity.

## 2. Success Criteria & Definition of Done
- `gemini-extension.json` correctly references the skill as `vector` and points to `skills/vector/SKILL.md`.
- The `skills/vector-protocol` directory is moved to `skills/vector`.
- `README.md`, `AGENTS.md`, and `SKILL.md` are updated to explicitly explain the functional difference and synergy between the commands (`/vector:plan`, `/vector:work`) and the skill (`vector`).

## 3. Dependencies
- Current workspace with `gemini-extension.json`, `README.md`, `AGENTS.md`, and `skills/vector-protocol` directory.

## 4. Side Effects
- Documentation changes will require users to read the updated definitions.
- The CLI needs to load the extension with the renamed skill.

## 5. Unknowns & Hypotheses
- Will users still be confused by having a skill and commands with similar names? Hypothesis: Explicit documentation of their synergy (Trigger vs Engine) will resolve the confusion.

## 6. Execution Roadmap

### [PARALLEL BATCH] Rename Skill & Update Manifest
-[x] Rename the directory `skills/vector-protocol` to `skills/vector`.
-[x] Update `gemini-extension.json` to change the skill name from `vector-protocol` to `vector` and update the `location` path.
-[x] Update `commands/vector/plan.toml` and `commands/vector/work.toml` to change the instruction `activate_skill("vector-protocol")` to `activate_skill("vector")`.

### [PARALLEL BATCH] Update Documentation
-[x] Update `README.md` to include a section explaining the synergy between the "3 things": the two orchestrator commands (the triggers) and the `vector` skill (the procedural knowledge base).
-[x] Update `AGENTS.md` to clarify how the commands and the skill interact in the Zero-Context Mandate.
-[x] Update `skills/vector/SKILL.md` to reflect the name change to `vector` and add a brief description of its role as the procedural engine for the commands.