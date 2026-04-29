# Vector Protocol Grounding Plan

## 1. Intent
Implement strict verification loops and full grounding in the Vector Protocol to eliminate hallucinations. Mandate tools (`grep_search`, `web_fetch`, `mcp_context7_query-docs`) as the exclusive sources of truth, explicitly prohibiting reliance on internal model weights. Explicitly mandate that all entities (models, APIs, tools) must be verified against external docs before use.

## 2. Success Criteria & Definition of Done
- No source of truth from internal weights is allowed in agent execution.
- Verification loops (e.g., "does X exist?", "does X solve intent?") are strictly required at every execution point.
- All entities (models, APIs, tools) are verified against external docs before use.
- The protocol automatically fails if any claim cannot be verified or grounded.
- All independent tasks are grouped under a `[PARALLEL BATCH]` in the roadmap.

## 3. Dependencies
- Access to Vector Protocol documentation (`AGENTS.md`, `skills/vector/SKILL.md`).
- Availability of grounding tools (`grep_search`, `web_fetch`, `mcp_context7_query-docs`).
- Testing framework for End-to-End validation.

## 4. Side Effects
- Execution time will increase due to mandatory external tool validation for all claims.
- The size of `EVIDENCE.json` and fractal task logs will increase.

## 5. Unknowns & Hypotheses
- **Hypothesis:** Strict tool-based grounding will drop hallucination rates to zero.
- **Risk:** Agents may over-query tools leading to rate limits or context window exhaustion.

## 6. Execution Roadmap

### [PARALLEL BATCH]
- [x] **Task 1: Update Agent Instructions**
  - Update `AGENTS.md` and related agent prompts to enforce Zero-Weight Grounding, including the mandate that all entities (models, APIs, tools) must be verified against external docs before use.
  - Assigned to: `vector-implementer`
  - Workspace: `.gemini/tasks/task-update-docs/`

- [x] **Task 2: Implement Grounding Validator**
  - Develop a script to enforce that all claims are backed by external tool evidence. This must be comprehensive enough to handle full entity verification (models, APIs, tools).
  - Assigned to: `vector-implementer`
  - Workspace: `.gemini/tasks/task-verification-script/`

- [x] **Task 3: Integrate Grounding Validator into Core Dynamic Loops**
  - Procedurally integrate the Grounding Validator into the core dynamic loops (e.g., in `skills/vector/SKILL.md`).
  - Assigned to: `vector-implementer`
  - Workspace: `.gemini/tasks/task-integrate-validator/`

### [SEQUENTIAL]
- [x] **Task 4: Add E2E Verification Tests**
  - Create integration tests that intentionally introduce hallucinations to ensure the protocol halts and fails gracefully.
  - Assigned to: `vector-tester`
  - Workspace: `.gemini/tasks/task-e2e-tests/`
