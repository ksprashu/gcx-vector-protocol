# ⚓️ THE ANCHOR
*Static Truths & Constitution*

## 1. Tech Stack
*   **Platform:** Gemini CLI Extension
*   **Architecture:** Prompt-Driven (Context + Commands)
*   **Manifest:** `gemini-extension.json`
*   **Language:** TOML (Commands), Markdown (Context/Prompts)
*   **No-Code:** This extension does not utilize an MCP server (Python/Node/Rust). It operates purely via prompt engineering and CLI context injection.

## 2. Project Structure
*   `gemini-extension.json`: Extension entry point.
*   `GEMINI.md`: The "brain" of the protocol. Contains the system prompt instructions.
*   `commands/vector/*.toml`: Slash command definitions (`/vector:init`, `/vector:plan`, etc.).

## 3. Invariants & Rules
*   **Parity:** The content of `GEMINI.md` must align with the behavior described in the TOML prompts.
*   **State Management:** The protocol relies on the existence of `.gemini/{ANCHOR,COMPASS,PULSE}.md` in the user's workspace.
*   **Idempotency:** Commands like `/vector:init` should handle existing states gracefully.