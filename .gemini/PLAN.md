# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Phase 5: Self-Healing & Integration Testing. Implement `/vector:lint` extension command and setup end-to-end integration tests using sub-agents.

## 2. Problem Breakdown
- **Functional:** 
    - *Linter Friction:* Users must manually run `python scripts/vector_lint.py`. They often forget, leading to broken protocol state.
    - *Regression Risk:* While we validate TOML syntax, we do not validate the *behavior* of the LLM given those TOML prompts. A prompt tweak might cause the model to stop outputting the dashboard correctly.
- **Technical:**
    - *Lint Command:* Need to wrap `scripts/vector_lint.py` into a new extension command (`commands/vector/lint.toml`).
    - *E2E Tests:* Need to leverage the Gemini CLI `generalist` sub-agent to simulate user commands and assert output structure.

## 3. Design Discussion
- **Lint Command Strategy:** `/vector:lint` should be a lightweight wrapper that runs the existing python script. If the script passes, it outputs success. If it fails, it should use its LLM capabilities to *auto-fix* the broken markdown files, rather than just complaining to the user. This creates a "self-healing" state loop.
- **Integration Test Strategy:** We can write a Python script (`scripts/e2e_test.py`) that uses the Gemini CLI natively (via `subprocess` or similar) to initialize a temporary repo, run `/vector:plan`, and assert that the output contains the `*   **Session Dashboard:**` string. 

## 4. Proposed Solution
1. **Self-Healing Linter:** 
   - Create `commands/vector/lint.toml`.
   - Update `save.toml` to recommend running `/vector:lint` if there are state issues.
2. **E2E Agent Tests:** 
   - Create a basic testing script to run CLI commands and capture output.

## 5. Revision History
- **2026-04-04:** Draft created from Backlog Review.

## 6. Implementation Roadmap
- [x] **Task 1: Create Linter Command** - Implement `commands/vector/lint.toml` as an auto-fixing wrapper around `vector_lint.py`.
- [x] **Task 2: Integrate Linter Suggestion** - Update `save.toml` to suggest `/vector:lint`.
- [x] **Task 3: E2E Test Stub** - Create `scripts/e2e_test.py` to simulate agent interactions.
- [x] **Task 4: Documentation & Version Bump (v1.18.0)** - Update README and increment manifest.

## 7. Review
- User, please review this Phase 5 roadmap. Does the focus on self-healing state and E2E testing align with expectations?
