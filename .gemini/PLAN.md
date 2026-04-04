# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Streamline the Vector Protocol command surface by removing redundant and deprecated commands (`init`, `resume`, `status`, `reset`).

## 2. Strategic Analysis
- **Problem:** The command surface has grown to 10 commands, several of which overlap with the "auto-bootstrap" and "auto-resume" logic now embedded in the core loop (`plan`, `work`, `scan`, `save`).
- **Approach:** 
  1. Audit cross-command dependencies to ensure no critical recovery logic is lost.
  2. Remove redundant TOML files and update the extension manifest.
  3. Synchronize documentation (`README.md`, `AGENTS.md`, `GEMINI.md`) to reflect the new 6-command surface.
  4. Perform a version bump to `1.14.0`.

## 3. Implementation Roadmap
- [x] **Task 1: Code Audit & Final Verification** - Verify no remaining logic depends on `init`, `resume`, `status`, or `reset`.
- [x] **Task 2: Command Removal** - Delete `init.toml`, `resume.toml`, `status.toml`, `reset.toml` and update `gemini-extension.json`.
- [x] **Task 3: Documentation Sync** - Update `README.md`, `AGENTS.md`, and `GEMINI.md`.
- [x] **Task 4: Version Update** - Increment version to `1.14.0` in `gemini-extension.json`.

## 4. Review
- (Approved) Command surface streamlined to 6 core commands.
