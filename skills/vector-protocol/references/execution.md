# 🔨 Execution Phase (Work)

## Atomic Implementation
1. **Task Retrieval:** Identify the next pending task from `PLAN.md`.
2. **Auto-Recovery:** Perform a fast scan of protocol files before starting work to ensure no drift occurred.
3. **N-Trial Execution:** For complex tasks, use parallel sub-agents to generate isolated solutions, then select and apply the most robust one.
4. **Execution Loop:**
   - **Implement:** Use `replace` or `write_file`.
   - **Verify:** Immediately run build or test commands.
   - **Record:** Append results to the `STATE.md` scratchpad.
   - **Trace:** Reference Evidence IDs for implementation decisions.
5. **Error Handling:** If verification fails, stop, log the failure reason, and mark the step with `[!]` in the plan.

## Standards
- Adhere strictly to the `Tech Stack` and `Coding Standards` in `CONTEXT.md`.
- Never proceed if immediate verification fails.
