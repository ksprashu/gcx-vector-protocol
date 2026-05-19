# PLAN: Task 2 - Source-of-Truth MD/JSON Standardization

## 1. Intent
Enforce a strict "Source-of-Truth MD/JSON Standardization" across the entire Vector Protocol swarm. All subagents must write exclusively to Markdown and JSON files, creating a fully machine-readable and deterministic source of truth for the system's state.

## 2. Success Criteria & Definition of Done
- All subagents (`vector-planner`, `vector-implementer`, `vector-tester`, `vector-critic`) write state, logs, and artifacts ONLY as `.md` or `.json` files.
- A strict JSON schema exists for `STATUS.json` within each fractal task directory.
- Standardized markdown headers/structures are defined for files like `LOG.md` and `CRITIQUE.md`.
- No reliance on implicit memory or non-standard file formats for state tracking.

## 3. Dependencies
- Task 1 (Harness-Aware Delegation Interface) to ensure any delegation metadata aligns with this standardization.

## 4. Side Effects
- Requires updates to any existing scripts that read agent state if they rely on older, less structured formats.
- Simplifies state synchronization and aggregation.

## 5. Unknowns & Hypotheses
- **Risk:** Some agent logic might be difficult to express in strict JSON schemas.
- **Hypothesis:** Separating structural state (JSON) from semantic reasoning/logs (Markdown) provides the right balance of machine readability and expressive freedom.

## 6. Execution Roadmap
1. **Schema Definition:** Create the authoritative JSON schema for `STATUS.json`.
2. **Markdown Templates:** Define the required structure for standard markdown files (e.g., `LOG.md`, `CRITIQUE.md`).
3. **Agent Constraint Updates:** Update all subagent instructions to strictly mandate writing to these defined formats and prohibit unstructured state files.
4. **Validation Logic:** Implement a lightweight validation script (or update `sync_state.py`) to verify that all task directories contain valid `STATUS.json` and adhere to the markdown standards.