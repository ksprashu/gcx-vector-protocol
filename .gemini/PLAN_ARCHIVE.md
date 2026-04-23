# Plan: task-policies

## 1. Intent
Implement permissive, autonomous execution policies for the Gemini CLI to allow long-running agent loops without constant human interaction, while preventing destructive actions like folder/file deletion by redirecting removals to an `archived/` directory. Note the security constraint: while the CLI discovers extension-level policies, it ignores `allow` decisions from them.

## 2. Success Criteria & Definition of Done
- A new policy file (`autonomous.toml`) is scaffolded at `policies/autonomous.toml` in the extension root (using the new folder convention) and also maintained in `.gemini/tasks/task-policies/autonomous.toml` [E-019].
- The policy explicitly allows file-system operations like `read_file`, `write_file`, `replace`, `list_directory`, `grep_search`, `glob` without human interaction [E-019]. *Note: The CLI ignores `allow` decisions defined within extension policies for security reasons; they are primarily used for `deny` or `ask_user` constraints. This file serves as a source of truth.*
- The policy pivots from a blacklist to a broad, permissive whitelist for `run_shell_command`. It explicitly allows prefixes for: `pnpm`, `uv`, `python`, `node`, `npm`, `git`, `mkdir`, `mv`, `ls`, `cp`, `grep`, `find`, `cat`, `echo`, `touch`. It falls back to `ask_user` for unlisted commands to maintain security while supporting known-safe autonomous workflows [E-019].
- A set of explicit shell commands and instructions is written to `.gemini/tasks/task-policies/INSTALL_INSTRUCTIONS.md` for the user/Orchestrator to execute manually in order to install the policy to the User Tier (`~/.gemini/policies/autonomous.toml`) to enable the required permissive (`allow`) behavior, and to scaffold the `.gemini/archived/` directory [E-019].
- The content for the new "Behavioral Mandates" section housing the strict mandate: "Do not delete files. Move them to `.gemini/archived/` instead." is written to `.gemini/tasks/task-policies/GEMINI_UPDATE.md` to prevent shared mutability risks [E-019].
- Fractal persistence updates (e.g., `STATUS.json` and evidence logging) are completed for all execution steps, confining all subagent writes strictly to `.gemini/tasks/task-policies/` [E-019].

## 3. Dependencies
- Knowledge of the Gemini CLI Policy Engine TOML schema [E-019].
- Existing `.gemini` directory structure.

## 4. Side Effects
- Agents will operate autonomously for whitelisted tools but will be paused to ask the user for approval when encountering unlisted commands.
- File removal workflows will result in moved files instead of deleted files, preserving history but slightly increasing disk usage over time.

## 5. Unknowns & Hypotheses
- *Scope Resolution & Security Constraints:* The CLI automatically discovers the `policies/` folder in the extension root, but for security reasons, it ignores `allow` decisions from extensions (they are only for `deny`/`ask_user`). We hypothesize a Dual-Path Strategy: using `policies/autonomous.toml` as the "source of truth" template in the repo, while explicitly instructing installation at `~/.gemini/policies/autonomous.toml` (User Tier) to achieve the actual autonomous functionality [E-019].
- *Behavioral Consistency vs Tool Security:* While `run_shell_command` requires `ask_user` for unlisted actions, the primary guard against data loss is the "Archive instead of Delete" directive in `GEMINI.md`. Bypassing a command filter is possible, but adherence to behavioral contracts prevents data loss [E-019].

## 6. Execution Roadmap

### Step 1: Scaffold Policy Configuration
- Create `policies/autonomous.toml` (in the extension root) and `.gemini/tasks/task-policies/autonomous.toml` with `[[rule]]` blocks [E-019]:
  - Allow file tools (`write_file`, `read_file`, `replace`, `list_directory`, `grep_search`, `glob`, etc.).
  - Implement a broad whitelist for `run_shell_command` allowing known-safe and necessary prefixes (`pnpm`, `uv`, `python`, `node`, `npm`, `git`, `mkdir`, `mv`, `ls`, `cp`, `grep`, `find`, `cat`, `echo`, `touch`).
  - Configure `run_shell_command` to fallback to `ask_user` for any command prefix not explicitly whitelisted.
- Ensure the creation of the extension-level `policies/` directory.
- Update `.gemini/tasks/task-policies/STATUS.json`.

### Step 2: Prepare Updates
- Write the new "Behavioral Mandates" section containing the "Archive instead of Delete" directive to `.gemini/tasks/task-policies/GEMINI_UPDATE.md` [E-019]. This explicitly states that it is the primary guard against data loss.
- Update `.gemini/tasks/task-policies/STATUS.json`.

### Step 3: Scaffold Installation Instructions
- Write explicit shell commands and steps to `.gemini/tasks/task-policies/INSTALL_INSTRUCTIONS.md` [E-019] that:
  - Create the `.gemini/archived/` directory (`mkdir -p .gemini/archived`).
  - Copy the policy from `policies/autonomous.toml` to `~/.gemini/policies/autonomous.toml` to address the security constraint and enable `allow` rules.
  - Provide instructions for the Main Orchestrator to merge `.gemini/tasks/task-policies/GEMINI_UPDATE.md` into the root `.gemini/GEMINI.md`.
- Update `.gemini/tasks/task-policies/STATUS.json`.

### Step 4: Validation & Final Persistence
- Verify the TOML syntax of the generated policy file.
- Update the final status in `.gemini/tasks/task-policies/STATUS.json`.
- Confine all remaining state outputs and logs within `.gemini/tasks/task-policies/` [E-019].\n## Execution Status\n- [x] task-policies implementation complete and approved.
# Vector Protocol Plan: Auto-Commit Authorization Fix

## 1. Intent
Ensure the `/vector:work` cycle successfully performs the final commit after completing all tasks, satisfying the "Working tree is clean" requirement of the Merge-Readiness Checklist.

## 2. Success Criteria & Definition of Done
- The conflict between the global anti-commit mandate and the `/vector:work` final commit step is resolved.
- `commands/vector/work.toml` explicitly instructs the orchestrator to perform `git add` and `git commit` at the end of the execution loop.
- `AGENTS.md` and `GEMINI.md` explicitly override the global anti-commit rule for the final step of the `/vector:work` command.
- The working tree is left clean upon successful completion of the work cycle.

## 3. Dependencies
- `commands/vector/work.toml`
- `AGENTS.md`
- `GEMINI.md`

## 4. Side Effects
- The agent will now automatically commit changes to the local repository history at the end of a successful `/vector:work` run.
- Unintended changes could be committed if the `vector-critic` validation is flawed, placing higher importance on test coverage.

## 5. Unknowns & Hypotheses
- **Hypothesis**: The global context mandate "Do not stage or commit changes unless specifically requested by the user" is currently preventing the agent from executing the final commit step in `commands/vector/work.toml`. By adding explicit authorization and clear CLI instructions to the project-level context (`AGENTS.md`, `GEMINI.md`) and the command prompt, the orchestrator will safely perform the commit.

## 6. Execution Roadmap

[PARALLEL BATCH]
- [x] Task 1: Update Command Prompt (.gemini/tasks/task-7/)
  - Modify `commands/vector/work.toml` under "State Synchronization & Handoff".
- [x] Task 2: Update Protocol Mandates (.gemini/tasks/task-8/)
  - Modify `AGENTS.md` section 7 (Merge-Readiness Checklist).
- [x] Task 3: Update Local GEMINI.md (.gemini/tasks/task-9/)
  - Apply the same updates to `GEMINI.md` and `.gemini/GEMINI.md` to ensure context parity.

[SEQUENTIAL]
- [x] Task 4: Verify and Commit (.gemini/tasks/task-10/)
  - Validate that the updated markdown and TOML files are syntactically correct.
  - Run the commit to apply these protocol updates.
