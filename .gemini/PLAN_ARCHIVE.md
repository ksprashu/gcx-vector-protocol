# Vector Protocol Deep Dissection Plan

## 1. Intent
Overhaul the Vector Protocol to be dynamic, flexible, and massively parallel while resolving permission prompts for `mkdir`/`sed` and preventing file race conditions. The rigid execution loop will be replaced by a dynamic, multi-angle parallel approach. Explicit philosophical terminology will be scrubbed and replaced with functional descriptions of these behaviors.

## 2. Success Criteria & Definition of Done
- `mkdir` and `sed` are added to the command allowlist in `policies/autonomous.toml`.
- `AGENTS.md` and `skills/vector/SKILL.md` define strict file-locking or mutually exclusive workspace allocation to prevent parallel implementers from modifying the same files simultaneously.
- Orchestrator commands (`commands/vector/plan.toml`, `commands/vector/work.toml`) and `skills/vector/SKILL.md` are redesigned to mandate dynamic iteration calculation and multi-angle parallel implementations.
- All references to "Ralph Wiggum", "First Principles", and "Critical Thinking" are removed from `README.md`, `AGENTS.md`, and `skills/vector/SKILL.md` and replaced with functional descriptions.

## 3. Dependencies
- Existing policy files (`policies/autonomous.toml`).
- Existing documentation and skill definitions (`AGENTS.md`, `README.md`, `skills/vector/SKILL.md`, `commands/vector/plan.toml`, `commands/vector/work.toml`).

## 4. Side Effects
- Agents will dynamically dictate the length and depth of execution loops rather than following a static 3-step constraint.
- Multi-angle implementations might increase token usage/context consumption but will yield more robust solutions.
- Modifying policy files will change execution permissions for all future tasks.

## 5. Unknowns & Hypotheses
- *Hypothesis:* Enforcing strict workspace allocation will eliminate file corruption from parallel implementations without overly constraining concurrent execution.
- *Unknown:* Whether "multi-angle parallel implementation" will confuse the `vector-critic` when reviewing disparate approaches to the same task.
- *Risk:* Over-scrubbing philosophical terms might accidentally remove necessary functional constraints if not carefully rewritten.

## 6. Execution Roadmap

### [PARALLEL BATCH 1: Policy & Documentation Scrub]
- **Task 1.1:** Update `policies/autonomous.toml` to allowlist `mkdir` and `sed`. (Target: `policies/autonomous.toml`)
- **Task 1.2:** Scrub "Ralph Wiggum", "First Principles", and related philosophical terms from `README.md` and replace with functional descriptions. (Target: `README.md`)

### [PARALLEL BATCH 2: Architectural Documentation - Race Conditions & Loop Evolution]
- **Task 2.1:** Update `AGENTS.md` to define strict file-locking/workspace allocation rules and describe the dynamic, parallel multi-angle loop, scrubbing old philosophical terms. (Target: `AGENTS.md`)
- **Task 2.2:** Update `skills/vector/SKILL.md` to mandate dynamic iterations, multi-angle implementations, and strict file isolation, scrubbing old philosophical terms. (Target: `skills/vector/SKILL.md`)

### [PARALLEL BATCH 3: Orchestrator Commands Redesign]
- **Task 3.1:** Redesign `commands/vector/plan.toml` to support dynamic loop evolution and parallel multi-angle strategies. (Target: `commands/vector/plan.toml`)
- **Task 3.2:** Redesign `commands/vector/work.toml` to implement the dynamic execution loop and enforce non-overlapping file constraints during parallel task distribution. (Target: `commands/vector/work.toml`)