# Task 1: Define Evidence & Citation Schema (Theory) - SPEC

## 1. Intent
Establish a strict, deterministic schema for evidence gathering and citation across the Vector Protocol. This ensures every claim is grounded and verifiable.

## 2. Success Criteria
- **Schema Definition:** Clear format for Evidence IDs (`[E-XXX]`) where XXX is a zero-padded 3-digit integer.
- **Mandatory Usage:** Specification that all subagent logs (`LOG.md`) and status reports (`STATUS.json`) MUST use these IDs when making claims.
- **Enhanced EVIDENCE.json:** Updated schema including `task_id`, `timestamp` (ISO 8601), and `uri` (deep links/file paths).

## 3. Sub-plan
1.  **[Implementer]**:
    - Write `SPEC.md` (this file).
    - Define Citation Schema in `SPEC.md`.
    - Update `.gemini/EVIDENCE.json` with new fields for existing entries (dummy data or inferred).
    - Create `.gemini/tasks/task-1/LOG.md`.
    - Create `.gemini/tasks/task-1/STATUS.json`.
2.  **[Tester]**:
    - Validate `EVIDENCE.json` against the new schema requirements.
    - Confirm `SPEC.md` covers all requirements from `PLAN.md`.
3.  **[Critic]**:
    - Review for architectural alignment and completeness.

## 4. Citation Schema
- **Format**: `[E-XXX]`
- **Definition**: An Evidence ID is a unique pointer to a record in `.gemini/EVIDENCE.json`.
- **Constraint**: XXX must be unique and sequential (best effort, but uniqueness is mandatory).
- **Usage**: Whenever a subagent makes a factual claim about the codebase or task status, it must append the relevant Evidence ID.
