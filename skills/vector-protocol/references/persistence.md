# 💾 Persistence Phase (Save, Resume, Status)

## Save & Commit
1. **State Sync:** Ensure `STATE.md` reflects the final outcome of the work.
2. **Scratchpad Rotation:** If the scratchpad exceeds 20 entries, archive it to `STATE_ARCHIVE.md` and replace it with a summary.
3. **Git Integration:** Stage changed files (including `.gemini/`) and commit with a concise message.
4. **Report:** Provide the commit hash and final status.

## Resume & Recovery
1. **Protocol Check:** Verify existence of core state files.
2. **Context Loading:** Reload the Context, Plan, State, and Evidence to restore the agent's mental model.
3. **Status Dashboard:** Display a structured view of the current Phase, Objective, and Next Step.

## Initialization
- Create the `.gemini/ directory and bootstrap the 5-File System.
- Perform initial Context Discovery to populate `CONTEXT.md`.

## Reset
- Archive the current `STATE.md` to `STATE_ARCHIVE.md` and reset to a clean template for a fresh session.
