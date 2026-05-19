# Intent
Implement the final HTML generation in `scripts/sync_state.py` by integrating the parsing logic and the chosen HTML mockup template to output a rich user-facing plan artifact.

# Success Criteria & Definition of Done
- `scripts/sync_state.py` successfully generates a rich `.gemini/VIEW.html` instead of the Trello-like board.
- The HTML incorporates the extracted high-level plan context (Intent, Criteria, etc.).
- The execution roadmap is presented in a cohesive, readable flow rather than loose task cards.

# Dependencies
- `task-rich-html-1` (mockup selection).
- `task-rich-html-2` (parsing logic).

# Side Effects
- Overwrites the behavior of `scripts/sync_state.py`'s `generate_html_dashboard` function.
- Drastically changes `.gemini/VIEW.html`.

# Unknowns & Hypotheses
- Ensuring backwards compatibility or removing old CSS classes no longer needed.

# Execution Roadmap
- [ ] Replace `generate_html_dashboard` template string in `scripts/sync_state.py` with the rich HTML structure.
- [ ] Integrate the `extract_plan_details` function to inject plan context.
- [ ] Adapt the task iteration loop to render roadmap items clearly.