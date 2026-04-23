# Plan: Update Autonomous Policy

## 1. Intent
Update `policies/autonomous.toml` to support all safe and non-destructive tools and agents identified by `cli_help` to improve autonomous execution capabilities.

## 2. Success Criteria & Definition of Done
- `policies/autonomous.toml` includes all the newly requested safe tools in its `[tools.allow] names` array.
- `cli_help` and `codebase_investigator` are added to the allowed agents/tools configuration.
- The policy remains structurally consistent with its existing format.
- A verification step confirms the updated policy file.

## 3. Dependencies
- `policies/autonomous.toml` must exist.

## 4. Side Effects
- Future agent operations will have access to more tools without triggering human confirmation prompts.

## 5. Unknowns & Hypotheses
- **Hypothesis:** Adding agent names to `[tools.allow].names` will allow them if the CLI treats them as tools, which `cli_help` suggested is the case for policy matching.

## 6. Execution Roadmap
1. Modify `policies/autonomous.toml` to append the new tools and agents to the `[tools.allow] names` list.
   - Tools: `read_many_files`, `get_internal_docs`, `ask_user`, `write_todos`, `enter_plan_mode`, `exit_plan_mode`, `google_web_search`, `activate_skill`, `tracker_add_dependency`, `tracker_create_task`, `tracker_get_task`, `tracker_list_tasks`, `tracker_update_task`, `tracker_visualize`, `update_topic`, `complete_task`.
   - Agents: `cli_help`, `codebase_investigator`.
2. Verify the file content.
