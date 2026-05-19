# Vector Protocol Evolution: Harness Alignment & Read-Only HTML View Layer

## 1. Intent
Ensure the Vector Protocol complements rather than overrides Gemini CLI's native agentic capabilities. Transition human-facing state views from Markdown to rich, semantic HTML for better readability, while strictly maintaining Markdown and JSON as the machine-readable sources of truth. HTML will be generated as a read-only presentation layer with semantic meaning.

## 2. Success Criteria & Definition of Done
- A detailed review document mapping Vector's context engineering against native Gemini CLI capabilities, ensuring the `vector` skill instructions do not force unnecessary context already provided by the CLI harness.
- MD/JSON files are strictly maintained as the underlying source-of-truth for state and planning by all subagents.
- A new HTML Generator component in `sync_state.py` that reads the MD/JSON sources of truth and compiles them into a read-only HTML view for human consumption using a classless CSS framework (e.g., Pico.css).
- Updated `vector` skill and commands that integrate seamlessly with native CLI harness features through Complementary Delegation.

## 3. Dependencies
- Gemini CLI architecture documentation (to understand native vs. overridden features).
- Classless CSS stylesheet choice (e.g., Pico.css) for the HTML generator.
- `sync_state.py` for housing the HTML generation logic.

## 4. Side Effects
- Users will view the protocol's progress and state via an HTML browser view, providing a significantly better user experience.
- The `sync_state.py` script will become responsible for the one-way generation of HTML from markdown and JSON.
- Subagents are completely isolated from HTML generation and remain focused on writing machine-friendly Markdown and JSON.

## 5. Unknowns & Hypotheses
- *Hypothesis:* Isolating HTML generation to a Python script keeps the LLM context clean and prevents subagents from wasting tokens on formatting, while still delivering a rich UI to the human user.
- *Risk:* Over-relaxing the Vector constraints might lead to loss of the deterministic execution loops that make the protocol valuable. We must find the "sweet spot" of alignment with the CLI harness.

## 6. Execution Roadmap

### Workspace Allocation
- **Task 1:** `skills/vector/SKILL.md`, `commands/`
- **Task 2:** `.gemini/tasks/` (subagent output templates)
- **Task 3:** `scripts/sync_state.py`, `.gemini/VIEW.html`

### [PARALLEL BATCH]
- [ ] **Task 1: Harness-Aware Delegation Interface** (See `.gemini/tasks/task-001/PLAN.md`)
    - *Focus:* Define a "Complementary Delegation" model where Vector handles protocol-specific state/loops but yields to the harness for general agentic tasks (tool usage, safety, model steering). Ensure the Vector Protocol is never handicapped if the agent/harness is insufficient, but avoids overriding tuned behaviors of the evolving harness.
- [ ] **Task 2: Source-of-Truth Markdown/JSON Standardization** (See `.gemini/tasks/task-002/PLAN.md`)
    - *Focus:* Ensure all subagent outputs are strictly formalized in machine-readable MD/JSON.
- [ ] **Task 3: Semantic Information Design for HTML Layer** (See `.gemini/tasks/task-003/PLAN.md`)
    - *Focus:* Implement "Semantic Mapping" for the HTML generator. Re-imagine the HTML content in a user-friendly, information-presentation-focused way instead of just re-rendering Markdown. Transform raw state data into specific UI components (dashboards, progress trackers for execution, collapsible trees for planning, task-cards).