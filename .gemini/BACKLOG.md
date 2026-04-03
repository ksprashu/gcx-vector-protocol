# 💡 BACKLOG
> Future Ideas. The Icebox.

## [New] Automated Test Suite for Protocol Definitions (CI)
- **Problem:** The Vector Protocol relies heavily on the prompt strings inside `commands/vector/*.toml`. There is no automated way to ensure these files are syntactically valid or contain required structural sections (like `**Output:**` tables) before a release.
- **Solution:** Implement a GitHub Actions CI workflow with a script to parse `gemini-extension.json` and validate the syntax and structure of every `.toml` command file.
- **Impact:** Prevents broken releases and ensures all commands consistently adhere to the protocol's output standards (e.g., the 5-File System dashboards).

## [New] Protocol State Git Hooks (State Integrity)
- **Problem:** Users might make manual commits using `git commit` outside of the `/vector:save` command, causing `.gemini/STATE.md` to fall out of sync with the actual repository timeline (e.g., the phase remains `[EXECUTION]`).
- **Solution:** Provide an optional installation script that installs a `pre-commit` git hook. This hook would auto-update `.gemini/STATE.md` to `[IDLE]` or warn the user if they are bypassing the protocol.
- **Impact:** Guarantees the 5-File System state remains perfectly synchronized with the Git history, even when developers mix CLI and GUI git tools.

## [New] Implement `/vector:next` Routing Helper (UX)
- **Problem:** As identified in the `COMMAND_SURFACE_SIMPLIFICATION_PLAN.md` (Phase 2), users may still feel friction deciding which command to run, despite the tiered documentation.
- **Solution:** Implement the `/vector:next` command. This command would read `.gemini/STATE.md` and `.gemini/PLAN.md` and act as a dynamic router, automatically suggesting or executing the logical next step.
- **Impact:** Creates a seamless, low-friction workflow loop for the developer, turning the Vector Protocol into a guided wizard.

## [New] Command Argument Validation (Reliability)
- **Problem:** Some commands (like `/vector:plan` or `/vector:work`) rely on the `{{args}}` placeholder. If a user provides invalid or empty arguments where they are required, the agent might behave unpredictably.
- **Solution:** Add explicit guardrails in the `.toml` prompts to check for required arguments and provide usage examples if they are missing.
- **Impact:** Improves UX and prevents common execution errors.

## [New] Protocol Invariant Validator (State Linter)
- **Problem:** The 5-File System relies on the LLM adhering strictly to Markdown structural conventions (e.g., `[x]` checklists, `E-001` format). Hallucinated formatting breaks the state machine.
- **Solution:** Introduce a CLI script/tool (e.g., `vector-lint` or an extension command) that strictly enforces the markdown schemas and ensures referential integrity (e.g., an Evidence ID cited in `PLAN.md` actually exists in `EVIDENCE.md`).
- **Impact:** Hardens the protocol, prevents state corruption, and keeps context machine-readable for deterministic handoffs.

## [New] Automated Evidence Schema (Structured Data Transition)
- **Problem:** `EVIDENCE.md` is currently unstructured text. As it grows, retrieving and validating prior evidence becomes token-expensive and prone to retrieval hallucination.
- **Solution:** Transition the Evidence Ledger to a structured format (e.g., Markdown with YAML frontmatter per entry, or a companion `EVIDENCE.json`).
- **Impact:** Reduces token consumption during `scan` and `work` by enabling programmatic, targeted retrieval (RAG optimization), making the protocol scalable for enterprise monorepos.

## [New] Cross-Session Efficacy Telemetry (Metrics Tracking)
- **Problem:** There is currently no feedback loop to measure how often "context drift" occurs or how frequently the execution agent falls back during tasks.
- **Solution:** Introduce lightweight, local metric logging (e.g., into `.gemini/METRICS.md` or `.json`) to track phase durations, drift counts, and verification failure rates.
- **Impact:** Provides quantitative DORA-style metrics to track workflow efficiency, helping refine extension prompts and measure ROI.