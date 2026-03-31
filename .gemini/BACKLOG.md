# 💡 BACKLOG
> Future Ideas. The Icebox.

## [New] Automated Test Suite for Protocol Definitions (CI)
- **Problem:** The Vector Protocol relies heavily on the prompt strings inside `commands/vector/*.toml`. There is no automated way to ensure these files are syntactically valid or contain required structural sections (like `**Output:**` tables) before a release.
- **Solution:** Implement a GitHub Actions CI workflow with a script to parse `gemini-extension.json` and validate the syntax and structure of every `.toml` command file.
- **Impact:** Prevents broken releases and ensures all commands consistently adhere to the protocol's output standards (e.g., the 5-File System dashboards).

## [New] Protocol State Git Hooks (State Integrity)
- **Problem:** Users might make manual commits using `git commit` outside of the `/vector:save` command, causing `.gemini/STATE.md` to fall out of sync with the actual repository timeline (e.g., the phase remains `[EXECUTION]`).
- **Solution:** Provide an optional installation script that installs a `pre-commit` git hook. This hook would auto-update `.gemini/STATE.md` to `[IDLE]` or warn the user if they are bypassing the protocol.
- **Impact:** Guarantees the 5-File System state remains perfectly synchronized with the Git history, even when developers mix CLI and GUI git tools.

## [New] Implement `/vector:next` Routing Helper (UX)
- **Problem:** As identified in the `COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` (Phase 2), users may still feel friction deciding which command to run, despite the tiered documentation.
- **Solution:** Implement the `/vector:next` command. This command would read `.gemini/STATE.md` and `.gemini/PLAN.md` and act as a dynamic router, automatically suggesting or executing the logical next step.
- **Impact:** Creates a seamless, low-friction workflow loop for the developer, turning the Vector Protocol into a guided wizard.