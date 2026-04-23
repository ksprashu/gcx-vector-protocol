# Task 4 Spec: State Synchronization Tooling

## Intent
Implement a lock-free state aggregation script in `scripts/sync_state.py`. This script will dynamically generate/update `.gemini/STATE.md` by reading isolated state files (`STATUS.json`) from individual task directories in `.gemini/tasks/*/`. This eliminates race conditions by ensuring subagents write only to their task-specific files.

## Success Criteria
1. `scripts/sync_state.py` reads all `.gemini/tasks/*/STATUS.json` files.
2. It aggregates these statuses into a DAG or progress list in `.gemini/STATE.md`.
3. Existing Phase and Objective logic (if any) is preserved or correctly formatted.
4. Script executes cleanly without locking issues.

## Sub-plan
1. Inspect current `sync_state.py` logic.
2. Modify `sync_state.py` to include a `render_state` function.
3. The function will glob for `.gemini/tasks/*/STATUS.json`, parse them, and rewrite the DAG/Progress section of `STATE.md`.
4. Test the script by running it.
