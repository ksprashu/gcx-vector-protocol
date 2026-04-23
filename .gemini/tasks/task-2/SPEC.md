# Task 2: Define Fractal Task Structure (Structure) - SPEC

## 1. Intent
Establish a mandatory, standardized filesystem structure for all sub-tasks within the Vector Protocol. This structure ensures isolation, traceability, and lock-free state aggregation.

## 2. Success Criteria
- **Mandatory Files Defined:** Clear definitions for `SPEC.md`, `LOG.md`, `CRITIQUE.md`, and `STATUS.json` within each `.gemini/tasks/task-ID/` directory.
- **Citation Integration:** Requirement for all logs to use the `[E-XXX]` citation schema defined in Task 1.
- **Lock-Free Readiness:** `STATUS.json` must provide enough structured data for `scripts/sync_state.py` to aggregate the global state.

## 3. Sub-plan
1.  **[Implementer]**:
    - Define file templates and mandatory fields in this `SPEC.md`.
    - Create `LOG.md` and `STATUS.json` for Task 2.
    - Document the structure in `SPEC.md`.
2.  **[Tester]**:
    - Verify that the defined structure meets the requirements of `PLAN.md`.
    - Ensure templates include citation requirements.
3.  **[Critic]**:
    - Audit the structure for architectural consistency and state persistence reliability.

## 4. Fractal Task Directory Structure Definition

Each task directory MUST contain:

### A. SPEC.md (Specification)
- **Purpose**: Defines the "What" and "How" of the task.
- **Mandatory Sections**:
    - `## 1. Intent`: High-level goal.
    - `## 2. Success Criteria`: Testable outcomes.
    - `## 3. Sub-plan`: Sequential steps for implementer/tester/critic.
    - `## 4. [Task Specific Context]`: Any schemas or definitions relevant to the task.

### B. LOG.md (Execution Log)
- **Purpose**: The "How it happened" record.
- **Mandatory Requirements**:
    - Every significant tool call or decision MUST be logged.
    - **Citation Hygiene**: All factual claims MUST use `[E-XXX]` format.
    - Sequential entries with timestamps or step identifiers.

### C. CRITIQUE.md (Audit)
- **Purpose**: Independent verification by the `critic` subagent.
- **Mandatory Requirements**:
    - Must evaluate the implementer's work against the `SPEC.md` success criteria.
    - Must explicitly Approve or Reject the task.
    - Must note any architectural regressions or security concerns.

### D. STATUS.json (Machine-Readable State)
- **Purpose**: Enables lock-free aggregation by `scripts/sync_state.py`.
- **Schema**:
```json
{
  "task_id": "task-ID",
  "status": "todo | in-progress | completed | failed",
  "completion_percentage": 0-100,
  "dependencies": ["task-X", "task-Y"],
  "last_updated": "ISO-8601 Timestamp",
  "artifacts": ["path/to/artifact1", "path/to/artifact2"]
}
```
