# Intent
Analyze `scripts/sync_state.py` and write the data extraction logic required to pull high-level plan details from `.gemini/PLAN.md` (which aren't currently parsed) to populate the new rich HTML template.

# Success Criteria & Definition of Done
- A Python function `extract_plan_details(md_path)` is created to parse the Deep Dissection schema from `.gemini/PLAN.md`.
- The function successfully returns a dictionary containing Intent, Success Criteria, Dependencies, Side Effects, Unknowns, and Roadmap.

# Dependencies
- `scripts/sync_state.py` structure.
- Python markdown parsing or regex extraction logic.

# Side Effects
- Prepares necessary utilities for the final HTML generation.

# Unknowns & Hypotheses
- The `PLAN.md` format is mostly standard, but string matching/regex must be robust enough to handle slight variations in heading names.

# Execution Roadmap
- [ ] Review `scripts/sync_state.py`.
- [ ] Write a standalone function that parses the `.gemini/PLAN.md` sections based on ATX headings.
- [ ] Test the extraction logic on the current `.gemini/PLAN.md`.