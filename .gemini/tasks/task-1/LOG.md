# Findings: Missing Priorities in `autonomous.toml`

## `policies/autonomous.toml`
- `[[tools.rules]]` for `name = "run_shell_command"` with `action = "allow"` lacks `priority`.
- `[[tools.rules]]` for `name = "run_shell_command"` with `action = "ask_user"` lacks `priority`.

## `.gemini/tasks/task-policies/autonomous.toml`
- `[[tools.rules]]` for `name = "run_shell_command"` with `action = "allow"` lacks `priority`.
- `[[tools.rules]]` for `name = "run_shell_command"` with `action = "ask_user"` lacks `priority`.
