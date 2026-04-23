# 📐 GCX Vector Protocol v2.0.0

**The Vector Protocol** is an autonomous, high-assurance development harness for the Gemini CLI. It transforms the agent from a single-session chat bot into a **Zero-Context Orchestrator** capable of executing complex, long-running engineering tasks through a swarm of specialized subagents and a fractal file system.

## 🚀 The 2-Command Workflow

Vector v2 simplifies the command surface to just two entry points:

1.  **`/vector:plan <objective>`**
    *   **Phase:** Strategy. 
    *   **Action:** Triggers the **Ralph Wiggum Planning Loop**.
    *   **Mechanism:** The Orchestrator spins off `planner` and `critic` subagents to iteratively draft and refine a technical roadmap.
    *   **Goal:** Produces a deeply dissected plan in `.gemini/PLAN.md` for human signoff.

2.  **`/vector:work`**
    *   **Phase:** Execution.
    *   **Action:** Triggers the **Autonomous Implementation Loop**.
    *   **Mechanism:** The Orchestrator parses the roadmap, delegates atomic tasks to `implementer`, `tester`, and `critic` subagents, and loops continuously until the mission is complete.
    *   **Outcome:** Verified code changes and automatic git commits.

## 🧠 Core Architecture

### 1. The Zero-Context Orchestrator
To prevent **Context Rot** and session drift, the main CLI agent never writes code or detailed plans itself. It acts as a project manager, coordinating specialized subagents and referring to the filesystem as the sole source of truth.

### 2. The Ralph Wiggum Protocol
Even low-power models can produce world-class results through iteration.
- **Planning:** Draft -> Critique -> Review -> Repeat 2x.
- **Execution:** Implement -> Test -> Critique -> Loop until success.
- **Parallel Swarm:** Vector v2 enables concurrent execution of independent tasks. Each task branch runs its own Ralph Wiggum loop in parallel, drastically reducing time-to-delivery for large features.

### 3. Fractal File System (`.gemini/tasks/`)
Vector v2 bypasses context limits by breaking tasks into a fractal directory structure. Each task has its own localized `PLAN.md`, `STATE.md`, and `EVIDENCE.md`, allowing the swarm to maintain infinite depth without polluting the main thread.

### 4. Specialized Subagent Swarm
The `generalist` agent is **deprecated** in favor of strict specialists to ensure higher quality and deterministic outcomes:
- `planner`: Roadmap architecture and goal decomposition.
- `implementer`: Atomic, thin-stack code implementation.
- `tester`: Rigorous verification and evidence logging.
- `critic`: Vulnerability detection and grounding verification.

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
