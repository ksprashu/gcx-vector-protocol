# SPEC.md - Task 3: Update Agent Mandates

## Intent
Update `AGENTS.md` and `skills/vector-protocol/SKILL.md` to formally codify the "Lock-Free Filesystem Persistence Mandate" and "Citation Hygiene" rules. This ensures all agents operate under a unified protocol for state isolation and evidence-based grounding.

## Success Criteria
1. **AGENTS.md Updated:**
   - Section on "Lock-Free Filesystem Persistence Mandate" added, emphasizing that subagents must only write to their own fractal task directories.
   - Section on "Citation Hygiene" enhanced, mandating `[E-XXX]` references for all factual claims.
2. **skills/vector-protocol/SKILL.md Updated:**
   - Instructions updated to reflect the lock-free mandate.
   - Explicit requirement for subagents to return localized status in `STATUS.json`.
3. **Traceability:**
   - All changes must be logged in `LOG.md` within the task directory.
   - Final status must be saved to `STATUS.json`.

## Sub-plan
1. [Vector-Implementer] Edit `AGENTS.md` to add mandates.
2. [Vector-Implementer] Edit `skills/vector-protocol/SKILL.md` to add mandates.
3. [Vector-Implementer] Generate `LOG.md` documenting tool calls.
4. [Vector-Implementer] Create `STATUS.json`.
5. [Vector-Tester] Verify markdown structure and content.
6. [Vector-Critic] Review against success criteria.
