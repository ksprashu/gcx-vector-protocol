# Gemini Agent Templates

This directory contains strict structured templates and schemas for agent communication and state management.

## A-to-A (Agent-to-Agent)
Located in `a-to-a/`. These templates define the rigid structures used for swarm state synchronization and task delegation between subagents.
- `swarm_state_schema.json` / `swarm_state.md`: Represents the overall orchestration plan status.
- `task_context_schema.json` / `task_context.md`: Represents specific atomic task requirements and execution logs.

## H-to-A (Human-to-Agent)
Located in `h-to-a/`. These templates define how human context is persisted and retrieved by the agents.
- `memory_schema.json`: Strict JSON structure for long-term user preferences and facts.
- `reference.md`: Markdown template for broad guidelines and instructions provided by the human.

## Usage
Agents MUST strictly adhere to these schemas to ensure minimal token consumption and maximum parsing reliability during swarm operations.