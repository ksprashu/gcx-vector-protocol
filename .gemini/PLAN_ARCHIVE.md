# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Fix extension packaging (Move subagents to manifest and skills to extension root)

## 2. Strategic Analysis
- **Problem:** The V2 architecture relies on `planner`, `implementer`, `tester`, `critic` subagents, and the `vector-protocol` skill. However, they were created in the local `.gemini/` directory of the `gcx-vector-protocol` repository. This means they are acting as project-level assets for developing the extension itself, and will *not* be distributed to end-users when they install the extension.
- **Solution:** The extension manifest (`gemini-extension.json`) must be updated. Subagents must be declared inline under the `subagents` array. The skill must be moved from `.gemini/skills/vector-protocol` to an extension-level directory (e.g., `skills/vector-protocol`) and registered in the `skills` array of the manifest.
- **Risk Assessment:** Low risk functionally, but critical for deployment. Standard Mode applies.

## 3. Implementation Roadmap
- [x] **Task 1: Read Subagent Personas** - Extract the contents of `.gemini/agents/*.md`.
- [x] **Task 2: Update Manifest (Subagents & Skills)** - Inject the subagent definitions into `gemini-extension.json`. Add the `skills` pointer to the manifest.
- [x] **Task 3: Move Skill Directory** - Move `.gemini/skills/vector-protocol` to `skills/vector-protocol`.
- [x] **Task 4: Cleanup** - Delete the obsolete `.gemini/agents` directory. Delete `.gemini/skills` directory.

## 4. Review
Plan COMPLETED. Packaging fixed.

--- Archived on 2026-04-20 ---
