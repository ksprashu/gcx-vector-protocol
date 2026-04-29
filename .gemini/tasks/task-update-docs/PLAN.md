# Task: Update Agent Directives & Prompts

## 1. Intent
Update all agent documentation to enforce strict verification and grounding, prohibiting reliance on internal model weights.

## 2. Success Criteria & Definition of Done
- `AGENTS.md`, `skills/vector/SKILL.md`, and files in `agents/` explicitly state the new rules.
- Grounding tools (`grep_search`, `web_fetch`, `mcp_context7_query-docs`) are mandated for all technical claims.

## 3. Dependencies
- The new core mandates defined in the root `PLAN.md`.

## 4. Side Effects
- Agent behavior will shift significantly toward tool usage rather than immediate answering.

## 5. Unknowns & Hypotheses
- Modifying prompt files might cause agents to over-index on search tools, leading to rate limits or slow responses.

## 6. Execution Roadmap
- [ ] Read `AGENTS.md`, `skills/vector/SKILL.md`, and `agents/*.md`.
- [ ] Add explicit clauses regarding Zero-Weight Grounding and mandatory verification loops.
- [ ] Review changes using `vector-critic`.
