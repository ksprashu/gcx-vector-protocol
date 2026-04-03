# 🔍 Perception Phase (Scan & Context)

## Environment Analysis
1. **Auto-Bootstrap:** If protocol files are missing, create minimal templates for `CONTEXT.md`, `PLAN.md`, `STATE.md`, `BACKLOG.md`, and `EVIDENCE.md`.
2. **State Audit:** Read all protocol files to understand the current objective and status.
3. **Investigation:** Use `glob`, `list_directory`, or `search_file_content` to locate relevant files.
4. **Drift Detection:** Flag discrepancies between the current `PLAN.md`, `STATE.md`, and the actual codebase state.
5. **Evidence Table:** Record Topic, Source, and Last-checked status for all findings.

## Context Maintenance
1. **Drift Audit:** Scan configuration files (e.g., `package.json`, `go.mod`) to detect staleness in `CONTEXT.md`.
2. **Discrepancy Classification:**
   - **[MISSING]:** Real item exists but is absent from `CONTEXT.md`.
   - **[STALE]:** Documentation no longer matches reality.
   - **[OBSOLETE]:** Refers to removed patterns or dependencies.
3. **Surgical Proposals:** Present `ADD`, `UPDATE`, or `REMOVE` diffs.
4. **Wait for Approval:** Do NOT modify `CONTEXT.md` without explicit user confirmation.
