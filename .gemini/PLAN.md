# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Phase 3: Validation & Reliability. Implement automated verification tooling and CI for the Vector Protocol.

## 2. Problem Breakdown
- **Functional:** Users and developers need a guarantee that the extension's commands and state files are structurally correct. Errors in TOML prompts (like missing XML tags) or Markdown files (like missing Dashboard headers) break the deterministic loop.
- **Technical:**
  - *TOML Auditor:* Needs to parse `gemini-extension.json`, locate every `.toml` command, and verify it contains mandatory XML sections (`<role>`, `<goal>`, `<output_format>`, etc.).
  - *Markdown Linter:* Needs to check `.gemini/` files for adherence to the 5-File System schemas (e.g., `STATE.md` must have a "Phase").
  - *CI Integration:* These checks must run automatically on every push/PR to prevent regressions.

## 3. Design Discussion
- **Language:** Python 3.x. It's pre-installed on most dev machines and CI runners, and excellent for file/text processing.
- **Validation Logic:** 
  - Regex-based checking for XML tags in prompts.
  - Mandatory section presence in Markdown files.
  - Manifest consistency (all listed commands must exist).
- **Risks:** The linter shouldn't be too rigid; it should allow for scratchpad variability while enforcing core invariants.

## 4. Proposed Solution
1.  **`scripts/validate_commands.py`**:
    *   Load `gemini-extension.json`.
    *   Check if all listed paths exist.
    *   Parse TOML content.
    *   Validate prompt string for mandatory XML tags: `<context>`, `<role>`, `<goal>`, `<interaction_standards>`, `<protocol>`, `<output_format>`.
2.  **`scripts/vector_lint.py`**:
    *   Target `.gemini/*.md`.
    *   Validate `STATE.md` has `# 💾 STATE`, `## 1. Status`, `## 2. Context`.
    *   Validate `PLAN.md` has `# 🗺️ PLAN` or `# 🗺️ DESIGN`.
    *   Validate `CONTEXT.md` has `# 📄 CONTEXT`.
3.  **`.github/workflows/protocol-audit.yml`**:
    *   Trigger: `push`, `pull_request`.
    *   Run both scripts.
4.  **Argument Guardrails**:
    *   Update `plan.toml` and `work.toml` to check `if args is empty` and provide a helpful message.

## 5. Alternatives Considered
- *Node.js scripts:* Equally valid, but Python is slightly more idiomatic for standalone "linter" scripts in many engineering environments.
- *Manual Checklists:* Rejected due to scale and high risk of human error.

## 6. Revision History
- **2026-04-04:** Draft created from Backlog Review.

## 7. Implementation Roadmap
- [x] **Task 1: Command Validation Script** - Create `scripts/validate_commands.py` to audit TOML prompt structure and manifest sync.
- [x] **Task 2: Vector State Linter** - Create `scripts/vector_lint.py` to audit `.gemini/` file invariants.
- [x] **Task 3: GitHub Actions CI** - Implement `.github/workflows/protocol-audit.yml` to automate verification.
- [x] **Task 4: Argument Guardrails** - Update command prompts to handle empty/missing arguments gracefully.
- [x] **Task 5: Version Bump (v1.16.0)** - Update manifest and release notes.

## 8. Review
- User, please review this roadmap for Phase 3: Validation & Reliability. Ready to proceed?
