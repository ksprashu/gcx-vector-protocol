# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Enforce "File-First State" architecture with SOLID-based file responsibilities.
- **Outcome:** A robust workflow where `CONTEXT`, `PLAN`, `STATE`, and `BACKLOG` serve distinct, focused roles, optimizing LLM context usage and persistence.

## 2. Strategic Analysis
- **Philosophy:** "Context is Volatile; Files are Persistent." The LLM should never rely solely on chat history for critical state.
- **Architecture:** "The 4-File System"
    1.  **`.gemini/CONTEXT.md` (ROM):** Static Constraints & Standards.
    2.  **`.gemini/PLAN.md` (Sprint):** Active Execution Roadmap (Hot Path).
    3.  **`.gemini/STATE.md` (RAM):** Volatile Session Status (Scratchpad).
    4.  **`.gemini/BACKLOG.md` (Icebox):** Ideas & Future Enhancements (Cold Path).

- **Workflow:**
    - `improve` -> **READ** `CONTEXT` -> **WRITE** (Append) to `BACKLOG.md` (Icebox) + Summary in Chat.
    - `plan` -> **READ** `BACKLOG.md` -> **WRITE** (Move) to `PLAN.md` (Sprint) -> **WRITE** (Remove/Mark) in `BACKLOG.md`.
    - `work` -> **READ** `PLAN.md` (Hot Path) -> **WRITE** (Update Status) in `STATE.md`.
    - `scan` -> **READ** All 4 files -> **WRITE** (Reconcile/Report) to `STATE.md`.

## 3. Design Specification
### File Structure Updates
- **`.gemini/BACKLOG.md`**: New file for `improve` outputs.
- **`.gemini/CONTEXT.md`**: Update to document the 4-File System.
- **`.gemini/GEMINI.md`**: Update Protocol Definition.

### Command Updates
- **`commands/vector/improve.toml`**:
    - Update prompt to **APPEND** proposals to `BACKLOG.md` AND summarize in chat.
- **`commands/vector/plan.toml`**:
    - Update prompt to **READ** `BACKLOG.md`, **SELECT** items, **WRITE** to `PLAN.md` (Active), and **UPDATE** `BACKLOG.md` (Archived).
- **`commands/vector/scan.toml`**:
    - Update prompt to **AUDIT** all 4 files and **WRITE** discrepancies to `STATE.md`.
- **`commands/vector/work.toml`**:
    - Enforce "Context Loading": Step 1 is always `read_file` of `.gemini/CONTEXT.md`, `.gemini/PLAN.md`, `.gemini/STATE.md`.
    - Ensure Step 3 (Record) always **WRITES** outcome to `STATE.md`.

## 4. Implementation Roadmap
- [x] **Step 1: Protocol Definition (`GEMINI.md`)**: Update "The Vector Protocol" to include `BACKLOG.md` and define the "4-File System".
- [x] **Step 2: Update Context (`.gemini/CONTEXT.md`)**: Document the file responsibilities as project standards.
- [x] **Step 3: Enhance `improve` Command**: Update to persist findings to `.gemini/BACKLOG.md`.
- [x] **Step 4: Enhance `plan` Command**: Update to integrate Backlog review (Read/Write).
- [x] **Step 5: Enhance `scan` & `work`**: Update for full state awareness (Read/Write) and strict context loading.
- [x] **Step 6: Verification**: Create dummy backlog item, move to plan, and verify flow.

## 5. Review
- Confirmed: All commands have explicit Read/Write responsibilities defined.
