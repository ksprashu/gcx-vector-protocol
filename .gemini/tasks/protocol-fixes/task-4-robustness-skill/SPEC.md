# SPEC: Integrate Circuit Breakers in SKILL.md

## Objective
Enhance `skills/vector/SKILL.md` by explicitly defining loop limits and aligning terminology.

## Requirements
- Align loop naming conventions with `AGENTS.md` (e.g., ensure "Dynamic Multi-Angle Loop" is used consistently).
- Introduce explicit circuit breakers like `MAX_ITERATIONS` for dynamic loops to prevent infinite execution if tests repeatedly fail.
- Detail the fallback behavior when the iteration limit is reached.
