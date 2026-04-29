# Vector Protocol: Generalized Grounding & Verification Plan

## 1. Intent
Generalize the Vector Protocol's grounding and verification loops to systematically eliminate hallucinations across ALL technical claims (library names, CLI flags, file paths, architectural assumptions, etc.), shifting from a narrow model-centric validation to a universal 'Empirical Validation' mandate.

## 2. Success Criteria & Definition of Done
- `AGENTS.md` explicitly mandates 'Empirical Validation' for all technical entities, requiring every claim to answer "Where is the evidence for X?".
- The 'Technical Truth Broker' concept or step is fully integrated into the protocol.
- `skills/vector/SKILL.md` includes a strict 'Verification Loop' mandating the use of at least one external grounding tool (e.g., `grep`, `web_fetch`, `query-docs`) before proposing solutions.
- A Failure Mandate is active: any claim not explicitly backed by `EVIDENCE.json` or a verifiable tool output is immediately rejected.
- Existing grounding scripts (e.g., `scripts/grounding_validator.py`) are refactored to support generalized technical claim validation.
- All independent execution steps are clearly identified for parallel execution.

## 3. Dependencies
- Current state of `AGENTS.md`.
- Current state of `skills/vector/SKILL.md`.
- Current implementation of `scripts/grounding_validator.py` and related testing tools.

## 4. Side Effects
- Increased latency in agent execution due to mandatory grounding tool calls.
- Stricter failure conditions for subagents, potentially leading to more retry loops if initial claims lack evidence.
- Restructuring of the `EVIDENCE.json` schema to accommodate a wider variety of technical claims.

## 5. Unknowns & Hypotheses
- **Unknown:** What defines the boundary of a "technical claim" versus a general statement?
- **Hypothesis:** We will need to define a clear heuristic in the prompt (e.g., specific file names, command syntax, API methods) to prevent the orchestrator from stalling on trivial linguistic constructs.
- **Unknown:** How effectively can the automated validator enforce tool usage retroactively?
- **Hypothesis:** By inspecting the `EVIDENCE.json` trace and requiring a one-to-one mapping between claims in the solution and executed tool outputs.

## 6. Execution Roadmap

### Phase 1: Planning & Setup
- [x] **Task 1:** Initialize fractal task directory (`.gemini/tasks/task-generalized-grounding`) for this overarching goal.

### Phase 2: Core Refactoring [PARALLEL BATCH]
- [x] **Task 2 (Policy Update):** Refactor `AGENTS.md` to introduce the 'Empirical Validation' mandate. Define the 'Technical Truth Broker' role/step and establish the rule that every technical claim must cite its evidence source. Explicitly define the 'Technical Claim' heuristic (API methods, CLI flags, file paths, library names, etc.) in the formal role definition to clarify what needs grounding.
- [x] **Task 3 (Skill Update):** Update `skills/vector/SKILL.md` to enforce the 'Verification Loop'. Add explicit instructions that a solution cannot be proposed without prior invocation of a grounding tool (`grep_search`, `web_fetch`, `mcp_context7_query-docs`, etc.). Establish the rejection mandate for ungrounded claims.
- [x] **Task 4 (Script Generalization):** Refactor `scripts/grounding_validator.py` (and any related test scripts like `scripts/e2e_grounding_test.py`) to transition from model-whitelisting to generalized claim validation. Define a new schema for `EVIDENCE.json` (e.g., mapping 'claim' to 'source_output_hash' or 'tool_invocation_id'). Clarify the mechanic for the validator script: instead of just regex on models, it must verify that every entity mentioned in a 'Technical Claims' section of the output has a corresponding entry in the evidence ledger.

### Phase 3: Integration & Testing
- [x] **Task 5 (Integration):** Synchronize the updated policies, skills, and scripts. 
- [x] **Task 6 (E2E Validation):** Run test suites to simulate both grounded and ungrounded technical claims. Verify that the system correctly rejects hallucinations and accepts claims backed by tool output.
- [x] **Task 7 (Final Audit):** Complete the Merge-Readiness Checklist and commit the generalized grounding protocol.