# PLAN: Task 1 - Harness-Aware Delegation Interface

## 1. Intent
Establish a "Harness-Aware Delegation Interface" that allows subagents to yield complex, agentic tasks to the orchestrator harness while maintaining a deterministic floor for standard operations. This ensures future-proofing and leverages the respective strengths of both the deterministic harness and the LLM agents.

## 2. Success Criteria & Definition of Done
- Subagents can output a structured delegation request.
- The system has a defined protocol for how these requests are formatted (e.g., specific JSON structure or markdown tags).
- The orchestrator harness can successfully parse and interpret these delegation requests.
- The deterministic floor of operations remains intact without over-reliance on agentic delegation for simple tasks.

## 3. Dependencies
- Approved Master Plan (`.gemini/PLAN.md`).

## 4. Side Effects
- Agent prompts and instructions will need updates to understand and utilize the delegation interface.
- Potential updates to the orchestrator's main loop to handle delegation yields.

## 5. Unknowns & Hypotheses
- **Risk:** Agents might over-delegate, causing infinite loops or stalling.
- **Hypothesis:** By strictly defining *when* and *how* to delegate in the agent instructions, we can mitigate over-delegation. A structured JSON format will be the most robust way to parse delegations.

## 6. Execution Roadmap
1. **Define Protocol:** Specify the exact JSON schema or markdown syntax for a delegation request.
2. **Update Subagent Prompts:** Modify `vector-planner`, `vector-implementer`, `vector-tester`, and `vector-critic` instructions to include guidelines on when to use the delegation interface and the required format.
3. **Harness Implementation:** Update the orchestrator scripts to intercept, parse, and queue tasks based on delegation requests.
4. **Verification:** Create a test case where a subagent successfully delegates a task that is then picked up by the orchestrator.