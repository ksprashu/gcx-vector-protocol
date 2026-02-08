# 📄 CONTEXT
> The invariant truths. The project's Constraints and Standards.

## 1. Tech Stack
- **Project Type:** Gemini CLI Extension
- **Manifest:** `gemini-extension.json`
- **Language:** TOML (Commands), Markdown (Docs)

## 2. Core Constraints
- **Manifest:** `gemini-extension.json` is the source of truth for extension metadata.
- **Commands:** Defined in `commands/*.toml`.
- **Context:** `GEMINI.md` provides the LLM context.

## 3. Coding Standards
- **TOML:** Valid TOML syntax for command definitions.
- **Markdown:** Standard Markdown for documentation.
- **Conventions:** Follow the structure defined in the `gemini-extension.json`.

## 4. Architecture
- **Extension:** Standard Gemini CLI Extension structure.
- **State Management:** Uses `.gemini/` for protocol state.