# 📐 GCX Vector Protocol v2.0.0

**The Vector Protocol** is an autonomous, high-assurance development harness for the Gemini CLI. It transforms the agent from a single-session chat bot into a **Zero-Context Orchestrator** capable of executing complex, long-running engineering tasks through a **Parallel Swarm** of specialized subagents and a fractal file system.

## 🚀 The Vector Triad: Commands & Skill Synergy

Vector v2 operates through the synergy of three core components: two orchestrator commands (the triggers) and the `vector` skill (the procedural knowledge base).

1.  **The `vector` Skill (The Knowledge Base)**
    *   **Role:** The foundational memory and operating system for the Gemini agent.
    *   **Function:** Teaches the main agent how to behave as a **Zero-Context Orchestrator**, enforcing the rules of strict 1:1 isolated task assignment, subagent isolation, and strict filesystem reliance.

2.  **`/vector:plan <objective>` (The Strategy Trigger)**
    *   **Phase:** Strategy. 
    *   **Action:** Triggers the **Dynamic Strategy and Planning Loop**.
    *   **Mechanism:** The Orchestrator spins off `vector-planner` and `vector-critic` subagents to iteratively draft and refine a technical roadmap.
    *   **Goal:** Produces a deeply dissected plan in `.gemini/PLAN.md` for human signoff.

3.  **`/vector:work` (The Execution Trigger)**
    *   **Phase:** Execution.
    *   **Action:** Triggers the **Autonomous Implementation Loop**.
    *   **Mechanism:** The Orchestrator parses the roadmap, delegates atomic tasks to `vector-implementer`, `vector-tester`, and `vector-critic` subagents, and loops continuously until the mission is complete.
    *   **Outcome:** Verified code changes and automatic git commits.

## 🧠 Core Architecture

### 1. The Zero-Context Orchestrator
To prevent **Context Rot** and session drift, the main CLI agent never writes code or detailed plans itself. It acts as a project manager, coordinating specialized subagents and referring to the filesystem as the sole source of truth.

### 2. 1:1 Isolated Task Assignment
Iterative refinement enables high-quality, resilient output through rigorous 1:1 isolated task assignments.
- **Planning:** Draft -> Critique -> Review.
- **Execution:** Implement -> Test -> Critique.
- **Parallel Swarm:** Vector v2 enables concurrent execution of independent tasks. Each task branch runs strictly as a 1:1 isolated task assignment in parallel, drastically reducing time-to-delivery for large features.

### 3. Subagent Isolation (Fractal File System)
Vector v2 bypasses context limits and ensures **Subagent Isolation** by breaking tasks into a fractal directory structure (`.gemini/tasks/`). Each task has its own localized `PLAN.md`, `STATE.md`, and `EVIDENCE.md`, allowing the swarm to maintain infinite depth without polluting the main thread or causing state leakage.

### 4. Specialized Subagent Swarm
The `generalist` agent is **deprecated** in favor of strict specialists to ensure higher quality and deterministic outcomes:
- `vector-planner`: Roadmap architecture and goal decomposition.
- `vector-implementer`: Atomic, thin-stack code implementation.
- `vector-tester`: Rigorous verification and evidence logging.
- `vector-critic`: Vulnerability detection and grounding verification.

## 🧭 Core Tenets

*   **Strict External Grounding:** Conclusions must be backed by verifiable artifacts (files, docs, logs).
*   **Spec-Driven Development:** Behavioral contracts are established before implementation logic.
*   **Thin Stack Philosophy:** Favor native APIs and pure functions over complex abstractions.
*   **Persistence First:** Every interaction saves state to the filesystem. The filesystem is the Whole Truth.

## 🛠 Installation

```bash
gemini extensions install https://github.com/ksprashu/gcx-vector-protocol --auto-update
```

---
*Vector Protocol: Engineering with Direction and Magnitude.*
