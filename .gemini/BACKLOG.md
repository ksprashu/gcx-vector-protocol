# 💡 BACKLOG
> Future Ideas. The Icebox.

## [New] Protocol Invariant Validator (State Linter Extension)
- **Problem:** The 5-File System relies on the LLM adhering strictly to Markdown structural conventions. While we have `scripts/vector_lint.py`, users have to run it manually.
- **Solution:** Wrap the linter in an extension command (`/vector:lint`) and suggest running it during `save`.
- **Impact:** Keeps context machine-readable for deterministic handoffs with zero friction.

## [New] Automated Test Suite for Protocol Definitions (Full Integration)
- **Problem:** We have a basic command validator, but we don't have "integration tests" that simulate an agent turn.
- **Solution:** Use the Gemini CLI `generalist` sub-agent to "run" commands against a dummy repo and verify the output schema.
- **Impact:** Prevents regression in complex prompt interactions.
