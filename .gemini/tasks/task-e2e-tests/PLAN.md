# Task: Integration & E2E Testing for Grounding

## 1. Intent
Write End-to-End tests to simulate hallucinated claims and verify the protocol rejects them.

## 2. Success Criteria & Definition of Done
- `scripts/e2e_test.py` contains tests that intentionally inject ungrounded claims.
- The tests verify that the Vector Protocol execution halts and returns a failure status.

## 3. Dependencies
- Completion of the `task-update-docs` and `task-verification-script` tasks.

## 4. Side Effects
- Test suite runtime will increase.

## 5. Unknowns & Hypotheses
- It may be challenging to inject a hallucination dynamically without the orchestrator catching it too early.

## 6. Execution Roadmap
- [ ] Set up a mock environment with a fake subagent that outputs an ungrounded claim.
- [ ] Run the Vector Protocol via `scripts/e2e_test.py`.
- [ ] Assert that the validation script and `vector-critic` catch the hallucination and fail the workflow.
