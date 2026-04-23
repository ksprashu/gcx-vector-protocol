# Vector Protocol Agent Renaming Roadmap

## 1. Intent
Rename all subagents (`planner`, `implementer`, `tester`, `critic`) to include a `vector-` prefix (`vector-planner`, `vector-implementer`, `vector-tester`, `vector-critic`) across the entire `gcx-vector-protocol` extension, and update all references to ensure consistency.

## 2. Success Criteria & Definition of Done
- All files in `agents/` are renamed to `vector-<agent>.md`.
- The `name:` YAML frontmatter in all agent files is updated.
- All references in `AGENTS.md`, `GEMINI.md`, `README.md`, `skills/vector-protocol/SKILL.md`, and `commands/vector/*.toml` are correctly updated.
- All references in `.gemini/` state and log files are correctly updated.
- `gemini-extension.json` version is incremented (e.g., from 2.3.0 to 2.4.0) per `.gemini/gemini.md` instructions.
- The extension runs correctly and the CLI recognizes the renamed subagents without errors.

## 3. Dependencies
- Existing `agents/*.md` files.
- `gemini-extension.json` manifest.
- Documentation and configuration files.

## 4. Side Effects
- Any external workflows or scripts depending on the old agent names may break, but this is scoped to the Vector Protocol extension usage.
- Updates to `.gemini/` archive files will rewrite historical context.

## 5. Unknowns & Hypotheses
- **Hypothesis:** Updating the references in the `plan.toml` and `work.toml` command files is sufficient for the Vector Protocol to dispatch the newly named agents.
- **Risk:** Case-sensitivity in logs (e.g., `[Planner]` vs `[Vector-Planner]`). The renaming must account for Title Case and lowercase occurrences.

## 6. Execution Roadmap
1. **Manifest Update**
   - [x] Update `version` in `gemini-extension.json` to 2.4.0.

[PARALLEL BATCH]
2. **Rename Subagent Files and Update Metadata**
   - [x] Rename `agents/planner.md` to `agents/vector-planner.md` and update `name: planner` to `name: vector-planner`.
   - [x] Rename `agents/implementer.md` to `agents/vector-implementer.md` and update `name: implementer` to `name: vector-implementer`.
   - [x] Rename `agents/tester.md` to `agents/vector-tester.md` and update `name: tester` to `name: vector-tester`.
   - [x] Rename `agents/critic.md` to `agents/vector-critic.md` and update `name: critic` to `name: vector-critic`.

3. **Update Core Documentation and Configuration**
   - [x] Update references in `AGENTS.md`.
   - [x] Update references in `README.md`.
   - [x] Update references in `GEMINI.md`.
   - [x] Update references in `commands/vector/work.toml` and `commands/vector/plan.toml`.
   - [x] Update references in `skills/vector-protocol/SKILL.md`.

4. **Update Internal `.gemini/` Context and History**
   - [x] Update references in `.gemini/PLAN_ARCHIVE.md`.
   - [x] Update references in `.gemini/tasks/PROTOCOL.md`, `tasks/PARALLEL-FEEDBACK.md`, `tasks/PLAN-FEEDBACK.md`.
   - [x] Update references in `.gemini/tasks/task-*/SPEC.md`, `LOG.md`, and `CRITIQUE.md`.

5. **Verification**
   - [x] Verify that the CLI successfully parses the new agent files and that `/vector:plan` and `/vector:work` correctly route to `vector-planner` and others.
