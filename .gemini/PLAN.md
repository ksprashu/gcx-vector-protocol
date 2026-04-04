# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Improve User Feedback Loop & Analytics. Gather analytics on agent effectiveness, implement standard issue templates, and establish a feedback command.

## 2. Problem Breakdown
- **Functional:** 
    - *Agentic Feedback:* Users have no native way to report if an agent turn was "good" or "bad" without leaving the CLI.
    - *Contribution Friction:* External contributors do not have standardized issue templates to report bugs or request features.
    - *Telemetry:* As maintainers, we do not know how frequently the protocol requires "self-healing" or how often `EVIDENCE.md` is accessed.
- **Technical:**
    - *Issue Templates:* Need to create `.github/ISSUE_TEMPLATE/` files.
    - *Telemetry Architecture:* Need to define a lightweight telemetry approach (e.g., adding a local `.gemini/METRICS.json` that tracks turn durations and failure rates).
    - *Feedback Command:* Create a `/vector:feedback` command.

## 3. Design Discussion
- **Feedback Command:** `/vector:feedback` should allow the user to append a note to `.gemini/BACKLOG.md` or a new `.gemini/FEEDBACK.md` file quickly. Let's append to the BACKLOG to keep the 5-File System pure.
- **Telemetry:** Adding a complex telemetry server is out of scope. We will instead create a local `scripts/metrics.py` that parses `STATE.md` and `STATE_ARCHIVE.md` to generate a local "DORA metrics" style report.
- **Issue Templates:** Standard GitHub Markdown templates are sufficient.

## 4. Proposed Solution
1. **GitHub Issue Templates:** Create `bug_report.md` and `feature_request.md`.
2. **Local Metrics Script:** Create `scripts/generate_metrics.py` to analyze session duration and execution success rates.
3. **Feedback Command:** Add `commands/vector/feedback.toml` to capture user sentiment.

## 5. Revision History
- **2026-04-04:** Draft created from Backlog Review.

## 6. Implementation Roadmap
- [x] **Task 1: Issue Templates** - Create `.github/ISSUE_TEMPLATE` bug and feature forms.
- [x] **Task 2: Local Metrics Script** - Implement `scripts/generate_metrics.py`.
- [x] **Task 3: Feedback Command** - Create `commands/vector/feedback.toml`.
- [x] **Task 4: Documentation & Version Bump (v1.19.0)** - Update README and increment manifest.

## 7. Review
- User, please review this roadmap for User Feedback & Analytics. Ready to proceed?
