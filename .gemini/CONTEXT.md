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
- **State Management:** Uses the **4-File System** in `.gemini/` for strict state persistence.

## 5. The 4-File System (State Persistence)
Adhere to the Single Responsibility Principle for protocol files:

1.  **`.gemini/CONTEXT.md` (ROM / Static):**
    *   **Role:** Invariant standards, tech stack, and architectural rules.
    *   **Access:** Read-Only during most operations.
2.  **`.gemini/PLAN.md` (Sprint / Hot Path):**
    *   **Role:** The *current* execution roadmap. Only active tasks belong here.
    *   **Access:** Read/Write by `plan` and `work`.
3.  **`.gemini/STATE.md` (RAM / Volatile):**
    *   **Role:** Immediate session status, tool outputs, and scratchpad.
    *   **Access:** Read/Write by ALL commands.
4.  **`.gemini/BACKLOG.md` (Icebox / Cold Path):**
    *   **Role:** Future ideas, enhancements, and non-critical tech debt.
    *   **Access:** Write-Only by `improve`. Read-Only by `plan`.
