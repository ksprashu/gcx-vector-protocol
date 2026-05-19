# PLAN: Task 3 - Semantic Information Design for HTML Layer

## 1. Intent
Develop a "Semantic Information Design for HTML Layer" to provide a rich, read-only UI dashboard of the swarm's state. This layer will reside in `sync_state.py` and must dynamically generate HTML by re-imagining the standardized MD/JSON data, rather than simply parsing Markdown directly to HTML.

## 2. Success Criteria & Definition of Done
- `scripts/sync_state.py` includes a Python-based HTML generator.
- The generator reads the standardized `STATUS.json` and key `.md` files from all `.gemini/tasks/` directories.
- The output is a single, self-contained HTML file (or a set of static files) that provides a rich visual representation of the project roadmap, task statuses, and agent activities.
- The design is semantic, structuring the raw data into a cohesive UI dashboard.

## 3. Dependencies
- Task 2 (Source-of-Truth MD/JSON Standardization) must be completed so the HTML generator has a reliable, structured data source.

## 4. Side Effects
- Introduces HTML/CSS generation logic to the repository.
- Provides a significant usability enhancement for human operators monitoring the swarm.

## 5. Unknowns & Hypotheses
- **Risk:** The HTML generation logic could become overly complex and hard to maintain within a single Python script.
- **Hypothesis:** By keeping the UI framework lightweight (e.g., using CDN-hosted Tailwind CSS for styling) and using simple string formatting or a minimalistic templating approach in Python, we can maintain the "Thin Stack" philosophy.

## 6. Execution Roadmap
1. **Dashboard Design:** Draft a conceptual layout for the UI dashboard (e.g., Global Status Header, Task Grid, Subagent Log Viewer).
2. **Data Aggregation:** Update `sync_state.py` to aggregate all necessary data from the standardized `STATUS.json` and `.md` files across the fractal task directories.
3. **HTML Generation Implementation:** Write the Python logic in `sync_state.py` to construct the semantic HTML structure, injecting the aggregated data.
4. **Styling:** Apply lightweight styling (e.g., inline styles or a simple CSS framework) to organize the information visually.
5. **Testing & Refinement:** Run the generator against a populated `.gemini/tasks/` directory and refine the output for clarity and semantic accuracy.