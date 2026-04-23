# Vector Protocol Strategy: Explicit Custom Subagents

## 1. Intent
Fix the bug where the Vector Protocol keeps spinning off instances of the `generalist` agent. We will explicitly define the custom subagents (`planner`, `implementer`, `tester`, `critic`) following the Gemini CLI spec (Markdown with YAML frontmatter) and bundle them correctly into the `gcx-vector-protocol` extension.

## 2. Success Criteria
- The custom subagents (`planner`, `implementer`, `tester`, `critic`) are defined as individual `.md` files containing YAML frontmatter (`name`, `description`, `kind`, `model`, etc.).
- These definition files are placed within the `agents/` directory of the `gcx-vector-protocol` extension repository.
- The `gemini-extension.json` manifest is updated to remove the inline `subagents` array, as the CLI will automatically discover bundled subagents in the `agents/` directory (similar to `skills/`).
- The `AGENTS.md` documentation is updated if necessary to reflect the explicit agent setup.

## 3. Dependencies
- The Gemini CLI extension documentation regarding custom subagents and bundling (`agents/` directory).

## 4. Side Effects
- The `.gemini/PLAN.md` file will no longer be executed by a fallback `generalist` agent but instead directly routed to the `planner`, `implementer`, `tester`, and `critic` MCP tools/subagents.
- Any manual overrides for the `generalist` agent in user setups related to this extension might break or become obsolete.

## 5. Unknowns & Hypotheses
- **Unknown:** Does the extension spec strictly require the directory to be `agents/` or `.gemini/agents/` inside the extension root?
- **Hypothesis:** Following the pattern of `skills/` and the extension documentation fetched, the folder should be `agents/` in the extension root. If required by a local project, it would be `.gemini/agents/`. We will bundle them in the extension's root `agents/` directory.

---

## 6. Execution Roadmap

### [PARALLEL BATCH: Create Subagent Definitions]
- [x] Task 1: Create `planner` Subagent
- [x] Task 2: Create `implementer` Subagent
- [x] Task 3: Create `tester` Subagent
- [x] Task 4: Create `critic` Subagent

### [PHASE 2: Clean up Manifest & Documentation]
- [x] Task 5: Update `gemini-extension.json`
- [x] Task 6: Update Documentation