
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
- User, please review this roadmap for enabling Best-of-N evaluations natively within the protocol. Ready to proceed?# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Set dynamic default values for `N` in the "Best-of-N" evaluation loop based on the model class (N=3 for Flash, N=1 for Pro, N=5 for Flash-Lite) when the user requests multiple options but does not specify an exact number.

## 2. Strategic Analysis
- **First Principles:** The Vector Protocol commands (`plan` and `work`) instruct the main agent on how to behave. By modifying the prompt instructions in these `.toml` files, we can explicitly define the heuristic the agent should use to infer `N` based on its own model capabilities.
- **Trade-offs:** 
  - *Pro Models:* N=1 minimizes token cost and latency since Pro models are highly capable and expensive.
  - *Flash Models:* N=3 provides a balanced, fast synthesis.
  - *Flash-Lite Models:* N=5 leverages the extreme speed and low cost of lite models to overcome their lower individual accuracy through volume synthesis.
- **Risk Assessment:** 
  - *Model Awareness:* The LLM might not explicitly know its own tier. However, the system instructions or the user's prompt generally provide context, or the agent can deduce it based on the capabilities. The instruction will direct the agent to infer its model class and apply the corresponding `N`.

## 3. Design Specification
We will update the `N-Trial Synthesis` step in `plan.toml` and the `N-Trial Execution` step in `work.toml`.

**Updated Instruction snippet:**
```text
(If `trials=N` or multiple options requested. If N is unspecified, default to: N=3 for Flash models, N=1 for Pro models, N=5 for Flash-Lite models):
```

## 4. Alternatives Considered
- **CLI Framework Argument:** We could parse the model flag in the CLI framework itself and pass `N` as an argument. *Rejected:* This extension focuses on the protocol via prompt engineering (`.toml` files) rather than modifying the core CLI source code. Using prompt-based heuristics is simpler and adheres to the extension boundaries.

## 5. Implementation Roadmap
- [x] **Step 1:** Update the `N-Trial Synthesis` instruction in `commands/vector/plan.toml` to include the dynamic default N heuristic.
- [x] **Step 2:** Update the `N-Trial Execution` instruction in `commands/vector/work.toml` to include the same heuristic.
- [x] **Step 3:** Increment extension minor version in `gemini-extension.json`.

## 6. Review
- User, please review this roadmap for establishing the default `N` heuristics. Ready to proceed?\n### Archive Date: 2026-03-29\n- Implemented dynamic Best-of-N heuristics in plan/work commands.\n- Validated Gemini model tiers against official docs.\n- Deployed unified Markdown table Dashboards across all protocol commands (version 1.8.0).\n- Resolved '4-File System' architectural drift in CONTEXT.md and validated backlog promotion flow.
