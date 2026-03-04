# 🗺️ PLAN
> The dynamic direction. The Execution Roadmap.

## 1. Objective
- **Goal:** Set dynamic default values for `N` in the "Best-of-N" evaluation loop based on the model class (N=3 for Flash, N=1 for Pro, N=5 for Flash-Lite) when the user requests multiple options but does not specify an exact number.

## 2. Strategic Analysis
- **First Principles:** The Vector Protocol commands (`plan` and `work`) instruct the main agent on how to behave. By modifying the prompt instructions in these `.toml` files, we can explicitly define the heuristic the agent should use to infer `N` based on its own model capabilities.
- **Trade-offs:** 
  - *Pro Models:* N=1 minimizes token cost and latency since Pro models are highly capable and expensive.
  - *Flash Models:* N=3 provides a balanced, fast synthesis.
  - *Flash-Lite Models:* N=5 leverages the extreme speed and low cost of lite models to overcome their lower individual accuracy through volume synthesis.
- **Risk Assessment:** 
  - *Model Awareness:* The LLM might not explicitly know its own tier. However, the system instructions or the user's prompt generally provide context, or the agent can deduce it based on the capabilities. The instruction will direct the agent to infer its model class and apply the corresponding `N`.

## 3. Design Specification
We will update the `N-Trial Synthesis` step in `plan.toml` and the `N-Trial Execution` step in `work.toml`.

**Updated Instruction snippet:**
```text
(If `trials=N` or multiple options requested. If N is unspecified, default to: N=3 for Flash models, N=1 for Pro models, N=5 for Flash-Lite models):
```

## 4. Alternatives Considered
- **CLI Framework Argument:** We could parse the model flag in the CLI framework itself and pass `N` as an argument. *Rejected:* This extension focuses on the protocol via prompt engineering (`.toml` files) rather than modifying the core CLI source code. Using prompt-based heuristics is simpler and adheres to the extension boundaries.

## 5. Implementation Roadmap
- [x] **Step 1:** Update the `N-Trial Synthesis` instruction in `commands/vector/plan.toml` to include the dynamic default N heuristic.
- [x] **Step 2:** Update the `N-Trial Execution` instruction in `commands/vector/work.toml` to include the same heuristic.
- [x] **Step 3:** Increment extension minor version in `gemini-extension.json`.

## 6. Review
- User, please review this roadmap for establishing the default `N` heuristics. Ready to proceed?