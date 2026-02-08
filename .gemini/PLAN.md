# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Current Objective
- Implement a safety check in `/vector:init` to prevent accidental overwrites of existing work.

## 2. Roadmap
- [ ] Modify `commands/vector/init.toml` to include a Pre-flight Check.
- [ ] Verify that the check logic correctly handles existing files and the `--force` flag.

## 3. Specification
- **Pre-flight Check:**
    - Detect existence of `.gemini/PLAN.md` or `.gemini/STATE.md`.
    - If found + no `--force`: Read files, report status, and abort.
    - If found + `--force`: Proceed with overwrite.
    - If not found: Proceed with initialization.
