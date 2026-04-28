# Source of Truth Guide

Use this order when evaluating inputs for an ADR:

1. Shared workflow docs
   - `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
   - `docs/workflow/HANDOFF_CONTRACTS.md`
2. Product truth
   - `PRD.md`
3. System-shape truth
   - `ARCHITECTURE.md`
   - `docs/architecture/<initiative>-architecture.md`
4. Decision truth
   - existing ADRs
5. Sequencing truth
   - `ROADMAP.md`
6. Execution truth
   - `PLAN.md`
7. Evidence
   - code, diffs, tests, review reports, incidents, production observations

## Conflict handling

If artifacts conflict:

- PRD beats architecture for product behavior.
- Architecture beats roadmap and plan for system shape.
- ADR beats architecture only for the specific decision recorded.
- Roadmap sequences work but does not redefine architecture.
- Plan defines one task but must obey PRD, architecture, and ADRs.

If a conflict affects the decision, do not hide it. Classify the run as `BLOCKED_BY_CONFLICTING_SOURCES`, `ARCHITECTURE_CONFLICT_FOUND`, or create a superseding ADR only when the intended new decision is clear.

## Architecture and ADR authority

Architecture explains the current or target system shape.

ADR explains why one important decision was made.

When accepted ADRs alter the system shape, architecture must link to the ADR and reflect the stable constraint. Do not duplicate the full ADR in architecture.
