# Vector Protocol Plan: Fix Autonomous Policy Format

## 1. Intent
The user reported that shell commands (mkdir, python, etc.) are prompting for permission despite `policies/autonomous.toml` attempting to allow them. The intent is to refactor the legacy policy structure (`[tools.allow]`, `[[tools.rules]]`) into the correct format for Gemini CLI 0.39.0 (`[[rule]]` blocks) to restore autonomous execution.

## 2. Success Criteria & Definition of Done
- `policies/autonomous.toml` is completely refactored to use `[[rule]]` blocks.
- The `rule` for `run_shell_command` correctly targets command prefixes (`pnpm`, `python`, `mkdir`, etc.) and sets `decision = "allow"`.
- The legacy `[tools.allow]` array is migrated to valid `[[rule]]` configurations.
- The policy file is syntactically valid TOML.

## 3. Dependencies
- Understanding of Gemini CLI 0.39.0 policy TOML schema (`[[rule]]`, `toolName`, `decision`, `priority`).
- The current `policies/autonomous.toml` legacy structure as a reference.

## 4. Side Effects
- Adjusting the policy will directly impact the autonomy level of all subagents using the workspace. Improper formatting might lock down the agent completely or open up unsafe execution.

## 5. Unknowns & Hypotheses
- **Unknown**: The exact parameter schema for matching command contents in `run_shell_command` rules for Gemini CLI 0.39.0 (e.g., regex matching in parameters vs string conditions).
- **Hypothesis**: Updating the TOML to the standard schema will immediately resolve the permission prompts.

## 6. Execution Roadmap

[PARALLEL BATCH]
- [x] Task 12: Refactor `policies/autonomous.toml`
  - Directory: `.gemini/tasks/task-12/`
  - Responsibility: Rewrite the policy file replacing `[tools.allow]` and `[[tools.rules]]` with compliant `[[rule]]` blocks. Define the tool names, decision logic (`allow`, `askUser`), priority levels, and any condition mapping for shell commands.

[SEQUENTIAL]
- [x] Task 13: Validate Policy Configuration
  - Directory: `.gemini/tasks/task-13/`
  - Responsibility: Review the refactored policy file against Gemini CLI 0.39.0 documentation (or verify syntactically via a validation script if available) to ensure the regexes/conditions are correctly formed.
