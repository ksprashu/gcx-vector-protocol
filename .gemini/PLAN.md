# 🗺️ PLAN

## Current Objective
Implement "Next Step Recommendation" logic across the Vector Protocol.

## Rationale
Users often lose track of the strict "Scan -> Plan -> Work" cycle. By embedding a "Navigation Engine" into the prompts, the Protocol becomes self-guiding, reducing friction and ensuring adherence to the workflow.

## Strategy
1.  **Centralized Logic:** Define the "State -> Command" mapping in `.gemini/GEMINI.md` so all agents share the same navigation rules.
2.  **Distributed Execution:** Update each TOML prompt to explicitly consult this mapping and output a `> Recommended Action: /vector:command` line.

## Roadmap
- [ ] **Step 1: Update `.gemini/GEMINI.md` (Protocol Definition)**
    - Add "5. NAVIGATION LOGIC" section defining the rules (e.g., Scan -> Plan, Plan -> Work).
- [ ] **Step 2: Update `commands/vector/init.toml`**
    - Add instruction: Recommend `/vector:scan`.
- [ ] **Step 3: Update `commands/vector/scan.toml`**
    - Add instruction: Recommend `/vector:plan`.
- [ ] **Step 4: Update `commands/vector/plan.toml`**
    - Add instruction: Recommend `/vector:work`.
- [ ] **Step 5: Update `commands/vector/work.toml`**
    - Add instruction: Recommend `/vector:work` (next task) OR `/vector:save` (done).
- [ ] **Step 6: Update `commands/vector/status.toml` & `resume.toml`**
    - Add instruction: Analyze state and recommend next command based on Global Logic.
- [ ] **Step 7: Verification**
    - Dry-run the logic by simulating a flow (Init -> Scan -> Plan -> Work) and verifying the recommended output.

## Active Spec
*Focus on adding the "Navigation Logic" section and updating the `Output` sections of TOML files.*