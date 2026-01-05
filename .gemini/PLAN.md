# 🗺️ PLAN

## Current Objective
Formalize Context Retention Mechanism & Enable Backlog.

## Rationale
The user highlighted two needs:
1.  **Clarity:** Understanding how context persists between Scan/Plan/Work phases.
2.  **Capability:** The ability to "park" ideas (Backlog) without distracting from the active task.
This plan addresses both by documenting the persistence model in `GEMINI.md` and upgrading the Protocol to support a "Backlog".

## Strategy
1.  **Documentation (The "Why"):** Explicitly define the `STATE.md` -> `PLAN.md` data flow in `GEMINI.md`. This ensures future agents (and users) understand the retention mechanism.
2.  **Protocol Upgrade (The "How"):** Modify `plan.toml` and `scan.toml` to formally recognize a `## 📦 Backlog` section in the Plan. This creates a sanctioned "Parking Lot" for ideas.

## Roadmap
- [x] **Step 1: Document Data Flow in `GEMINI.md`**
    - **Action:** Add a section "2.1 THE CONTEXT BRIDGE" to `GEMINI.md`.
    - **Content:** Explain that `STATE.md` is the *shared memory* where Scan writes and Plan reads, and `PLAN.md` is the *instruction tape* where Work reads.
- [x] **Step 2: Update `commands/vector/plan.toml` (Schema Change)**
    - **Action:** Update the `prompt` in `plan.toml`.
    - **Change:** Add `## 📦 Backlog` to the required Output Format. Instruct agent to preserve parked items.
- [x] **Step 3: Update `commands/vector/scan.toml` (Recommendation Logic)**
    - **Action:** Update the `prompt` in `scan.toml`.
    - **Change:** Allow the agent to recommend "Add to Backlog" or "Update Backlog" as a valid outcome.
- [x] **Step 4: Migrate `.gemini/PLAN.md`**
    - **Action:** Append a `## 📦 Backlog` section to the current `.gemini/PLAN.md` to initialize the feature.

## Active Spec
*Focus on updating the protocol definitions (TOML/Markdown) to support multi-threaded idea tracking.*

## 📦 Backlog
*(Empty. Add parked ideas here.)*
