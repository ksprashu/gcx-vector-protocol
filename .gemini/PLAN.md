# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Fix relative script paths in command definitions to support cross-project usage.

## 2. Strategic Analysis
- **Problem:** The `save.toml`, `lint.toml`, and `metrics.toml` command definitions instruct the agent to run python scripts using hardcoded relative paths like `scripts/vector_lint.py`. When users run these commands from their own project workspaces, the CLI attempts to resolve `scripts/vector_lint.py` within the user's directory, resulting in an error.
- **Solution:** The Gemini CLI extension framework provides the `${extensionPath}` and `${/}` runtime variables. We must update the `.toml` prompts to tell the AI to execute `python3 ${extensionPath}${/}scripts${/}vector_lint.py` instead. This ensures the CLI engine interpolates the correct absolute path to the extension's installation directory before the AI executes it.
- **Risk Assessment:** Low risk. This is a text replacement in prompt templates. The agent will read the interpolated string and execute the command safely regardless of the user's CWD.

## 3. Implementation Roadmap
- [x] **Task 1: Update `lint.toml`** - Replace all occurrences of `python3 scripts/vector_lint.py` with `python3 ${extensionPath}${/}scripts${/}vector_lint.py`.
- [x] **Task 2: Update `save.toml`** - Replace `python3 scripts/vector_lint.py` with `python3 ${extensionPath}${/}scripts${/}vector_lint.py`.
- [x] **Task 3: Update `metrics.toml`** - Replace `scripts/generate_metrics.py` with `${extensionPath}${/}scripts${/}generate_metrics.py`.
- [x] **Task 4: Bump Version** - Increment `gemini-extension.json` minor/patch version (e.g., to `1.21.1`) to reflect this portability bug fix.

## 4. Review
Plan established. Ready to Execute?
