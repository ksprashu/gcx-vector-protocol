# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Concept Objective
- **Status:** `DRAFT`
- **Goal:** Implement XML-Structured Prompt Design & Cognitive Architecture Refactoring across all Vector Protocol commands.

## 2. Problem Breakdown
- **Functional:** Users relying on `/vector:*` commands might experience "instruction drift" or hallucination, especially on longer projects. By standardizing the prompt structures using XML tags and inserting CoT `<thinking>` blocks, the commands will act more deterministically across Gemini versions.
- **Technical:**
  - 6 `.toml` files (`plan.toml`, `work.toml`, `scan.toml`, `save.toml`, `improve.toml`, `context.toml`) need prompt strings rewritten.
  - The rewrite must replace markdown-header-based constraints with strict XML structures (`<role>`, `<instructions>`, `<constraints>`, `<context>`, `<thinking>`, `<output_format>`).
  - Context blocks must be shifted to appear before the final execution instructions ("Data First" architecture).
  - Explicit Strict Grounding clauses must be added to `scan` and `context` commands.

## 3. Design Discussion
- **Trade-offs:** XML is slightly less "human-readable" than raw markdown for casual browsing of the `.toml` files, but it provides a massive reliability increase for the LLM. 
- **Risks:** The structure of the `{{args}}` interpolation must be maintained accurately so the CLI parses commands correctly.
- **First Principles:** The "Context at the Top, Instructions at the Bottom" principle ensures the agent remembers its guardrails right before executing the final step.

## 4. Proposed Solution
1. Define a global XML schema template for all prompts.
2. Update `scan.toml` and `context.toml` with the Grounding constraints.
3. Update `plan.toml` and `work.toml` with mandatory `<thinking>` blocks.
4. Update `improve.toml` and `save.toml` for schema consistency.
5. Bump version to reflect systemic prompt architecture upgrade.

## 5. Alternatives Considered
- *Status Quo (Markdown Headers):* Less resilient over long contexts, rejected based on Anthropic/DeepMind best practices.
- *JSON prompts:* LLMs process XML semantic boundaries better natively than stringified JSON inside a text prompt.

## 6. Revision History
- **2026-04-04:** Draft created from IDEATION Backlog.

## 7. Implementation Roadmap
- [x] **Task 1: Define XML Schema & Update `scan.toml`** - Refactor to XML tags, move data first, add strict grounding constraint.
- [x] **Task 2: Update `context.toml` & `improve.toml`** - Refactor to XML tags, add strict grounding constraint to `context`.
- [x] **Task 3: Update `plan.toml` & `save.toml`** - Refactor to XML tags, add `<thinking>` block mandate to `plan`.
- [x] **Task 4: Update `work.toml`** - Refactor to XML tags, add `<thinking>` block mandate, ensure context-first structure.
- [x] **Task 5: Version Bump & Docs** - Increment extension version and verify documentation sync.

## 8. Review
- Please review this Deep Mode draft plan. Does the proposed schema and migration strategy align with expectations?
