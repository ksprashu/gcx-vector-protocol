
--- Archive Sun Jan  4 10:26:17 IST 2026 ---

# 💾 STATE

**Phase:** [EXECUTION]
**Objective:** Enforce strict "Stopping Criteria" and prevent slash command execution.

## 📝 Scratchpad
- **User Issue:** Agent went Scan -> Plan -> Work autonomously and tried to run `/vector:work` as a shell command.
- **Investigation:**
    - Analyzed `GEMINI.md` (Navigation Logic) and `commands/vector/*.toml`.
    - **Finding 1:** "Recommended Action" in `Navigation Logic` might be interpreted as an imperative instruction to *act* immediately, bypassing the "Stopping Criteria".
    - **Finding 2:** There is no explicit guardrail preventing the agent from trying to run `/vector:*` commands as shell scripts.
- **Execution Log:**
    - Updated `GEMINI.md` with "6. ANTI-PATTERNS".
    - Updated `commands/vector/scan.toml` (Hardened Stopping Criteria).
    - Updated `commands/vector/plan.toml` (Hardened Stopping Criteria).
    - Updated `commands/vector/work.toml` (Prevented auto-looping).
    - Verified `GEMINI.md`.

--- Archive Mon Jan  5 10:41:48 IST 2026 ---

# 💾 STATE

**Phase:** [IDLE]
**Objective:** Awaiting Instruction

## 📝 Scratchpad
*   **Last Action:** Saved execution state.
*   **Commit:** `afee910` - Enforce strict anti-patterns and stopping criteria in TOML prompts
# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Implement an autonomous "Best-of-N" evaluation loop within the Vector Protocol using parallel sub-agents (e.g., `generalist`), enabling cheaper models (like Gemini 2.5 Flash) to generate, evaluate, and consolidate multiple attempts of a plan or implementation autonomously.

## 2. Strategic Analysis
- **First Principles:** The Gemini CLI supports parallel tool execution and sub-agent delegation (`generalist`). A single invocation of a Vector Protocol command (like `/vector:plan` or `/vector:work`) can orchestrate N independent, parallel sub-agent calls to draft proposals or code. The main orchestrating agent then receives all N responses, evaluates them against a rubric, and synthesizes the final optimal result into the protocol state (`PLAN.md` or the codebase).
- **Trade-offs:** 
  - *Context Window Size:* Parallel responses from `generalist` will rapidly consume the main agent's context window. We must instruct the sub-agents to be terse or return only the final structured artifact.
  - *Compute Cost:* Even with a cheaper model like Flash, running 3-5 concurrent prompts uses more tokens. However, the higher quality synthesis offsets the cost of iterative manual debugging.
- **Risk Assessment:** 
  - *Sub-agent hallucinations:* Evaluated away by the main agent's synthesis step.
  - *Implementation conflicts:* If N sub-agents write to the *same* files during `/vector:work`, they will overwrite each other. 
  - *Mitigation:* For `/vector:work`, sub-agents must draft code in isolated temporary files or purely return code blocks for the main agent to apply.

## 3. Design Specification
We will introduce a new cognitive pattern to the Vector Protocol called **"N-Trial Synthesis"**.

### Phase 1: Planning (`/vector:plan --trials=N`)
1.  **Drafting (Parallel):** The orchestrating agent calls the `generalist` tool $N$ times concurrently. Each call provides the objective and constraints from `CONTEXT.md`.
2.  **Evaluation:** The main agent receives $N$ distinct plans. It generates a brief evaluation matrix (Pros/Cons/Completeness).
3.  **Synthesis:** The main agent extracts the best elements from the evaluated plans and writes a single, consolidated `PLAN.md`.

### Phase 2: Implementation (`/vector:work --trials=N`)
1.  **Isolated Execution:** The orchestrating agent calls `generalist` $N$ times. Crucially, each `generalist` is instructed to *only output the patch/code* or write to isolated scratchpad files (`.gemini/trials/trial_1/`, etc.).
2.  **Verification:** The main agent reviews the output code blocks, validates them against the plan, and applies the most robust solution to the actual codebase.
3.  **Self-Healing:** If the applied code fails tests, the main agent falls back to Trial 2's implementation automatically, updating `STATE.md`.

## 4. Alternatives Considered
- **New Slash Command (`/vector:explore`):** Rejected. It's better to enhance the existing `plan` and `work` commands with instructions on how to handle N-trials natively, maintaining protocol simplicity.
- **Sequential Trials:** Rejected. Running trials sequentially is too slow. Parallel execution of the `generalist` agent maximizes speed, which is the primary benefit of the Flash model.

## 5. Implementation Roadmap
- [x] **Step 1:** Update `commands/vector/plan.toml` prompt to explicitly document the "N-Trial Synthesis" protocol when the user requests multiple options or trials.
- [x] **Step 2:** Update `commands/vector/work.toml` prompt to establish the isolated execution strategy (instructing the agent to use `generalist` to generate code blocks, evaluate them, and then apply the winner).
- [x] **Step 3:** Update `.gemini/CONTEXT.md` to officially define the "Best-of-N" / "N-Trial" cognitive pattern as a standard capability of the Vector Protocol.
- [x] **Step 4:** Increment extension version in `gemini-extension.json` (Minor version bump).

## 6. Review
- User, please review this roadmap for enabling Best-of-N evaluations natively within the protocol. Ready to proceed?
## [2026-03-11 10:48:00] Scratchpad Archive

## [2026-03-04 15:30:00] Scratchpad Archive
- Decomposed vector-protocol mega-skill into 5 phase-specific granular skills (vector-scan, vector-plan, vector-work, vector-persist, vector-improve) to enable intent-based selection.
- Initialized directories, transferred logic, integrated core rules, and packaged all 5 skills.
- Updated manifest to v1.9.0 and registered granular skills.
- Verified installation via gemini skills list.
