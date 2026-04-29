# Task: Implement Grounding Validator Script

## 1. Intent
Ensure all claims are verified by enforcing that `STATUS.json` and agent outputs reference valid Evidence IDs from `EVIDENCE.json`.

## 2. Success Criteria & Definition of Done
- A validation script (e.g., `scripts/validate_evidence.py`) is created or updated.
- The script parses `EVIDENCE.json` and verifies that no agent output lacks a required citation.
- The script fails the build/merge if unverified claims are found.

## 3. Dependencies
- Existing JSON schema for `EVIDENCE.json` and `STATUS.json`.

## 4. Side Effects
- Increases the strictness of the merge-readiness checklist.

## 5. Unknowns & Hypotheses
- Defining what constitutes a "technical claim" programmatically might be difficult, requiring regex heuristics or LLM-based evaluation in the script.

## 6. Execution Roadmap
- [ ] Analyze the current structure of `EVIDENCE.json`.
- [ ] Write a script to validate citations.
- [ ] Add the script to the pre-merge checklist in `scripts/sync_state.py`.
- [ ] Test the script with valid and invalid evidence files.
