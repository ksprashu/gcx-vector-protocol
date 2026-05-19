# Intent
The user finds the current `view.html` (a Trello-like task board) ineffective for communicating the overall plan for approval. The goal is to redesign `view.html` into a rich, narrative HTML document optimized for human readability and plan approval, replacing the raw dashboard view.

# Success Criteria & Definition of Done
- At least 2-3 sample HTML mockups demonstrating rich plan presentation are generated for user review.
- The system generating the HTML view (`scripts/sync_state.py`) is updated to use the new rich HTML structure instead of the Trello-like cards.
- The HTML view clearly articulates the goal, success criteria, dependencies, side effects, and execution roadmap.
- The user is presented with the HTML file for approval instead of a Markdown file (though the internal `.gemini/PLAN.md` is kept for the agent swarm).

# Dependencies
- Existing `STATUS.json` and internal `.gemini/PLAN.md` state.
- `scripts/sync_state.py` orchestration logic.

# Side Effects
- The visualization of swarm progress and plan structure changes significantly.
- Internal tools or scripts that generate `.gemini/VIEW.html` will be heavily refactored.

# Unknowns & Hypotheses
- Should the HTML be static or dynamically updated with JS? Hypothesis: Keep it static/server-rendered using Tailwind, with minimal JS, but structured like a formal report or document.
- Does the user want this HTML to replace `PLAN.md` completely? While the prompt suggests "No MD files needed for that artifact", `AGENTS.md` strictly requires `.gemini/PLAN.md` for the swarm. We will maintain the internal `.gemini/PLAN.md` for swarm orchestration, but the *user-facing* approval artifact will be solely the rich HTML document.

# Execution Roadmap
## [PARALLEL BATCH]
- [x] task-rich-html-1: Generate 3 sample rich HTML mockups (Executive Report, Timeline View, Structured Doc) in a `.gemini/mockups/` directory for user review to confirm understanding.
- [x] task-rich-html-2: Analyze `scripts/sync_state.py` and write the data extraction logic required to pull Intent, Success Criteria, and Roadmap details from `.gemini/PLAN.md`.

## [PARALLEL BATCH]
- [x] task-rich-html-3: Refactor `scripts/sync_state.py` to generate the `.gemini/VIEW.html` using the chosen rich HTML template, integrating the parsed plan details and roadmap status.