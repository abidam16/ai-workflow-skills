# Source of Truth Guide

## Authority model

Use this authority model during implementation:

| Artifact | Authority |
|---|---|
| `PRD.md` | Product behavior, goals, non-goals, user/business rules, success criteria |
| `ARCHITECTURE.md` | System shape, boundaries, data ownership, runtime flows, integration rules, cross-cutting constraints |
| `docs/architecture/<initiative>-architecture.md` | Deep system shape for one active large initiative |
| ADRs | One accepted technical decision and rationale |
| `ROADMAP.md` | Delivery sequencing, phase boundaries, dependencies, exit criteria |
| `PLAN.md` | One executable implementation contract |
| Codebase | Existing implementation reality and local conventions, but not a replacement for durable decisions |

## Implementation order

The plan is the nearest instruction, but upstream artifacts constrain the plan.

If implementation discovers a conflict:

1. Stop if the conflict changes scope or correctness.
2. Report the conflicting artifacts and exact sections.
3. Route to the artifact that must change.
4. Do not silently implement a compromise.

## Common conflict examples

| Conflict | Correct response |
|---|---|
| Plan says use notification state for authorization; architecture says membership is source of truth | Stop or deviate minimally only if explicitly safe; route to `UPDATE_PLAN` or `UPDATE_ARCHITECTURE` |
| Plan requires direct Kafka publish; ADR says use outbox | Stop or implement outbox-compliant path if in scope; report deviation if plan said otherwise |
| Roadmap phase says API only; plan includes schema migration | Stop or route to plan split/update |
| PRD does not define user-visible behavior required by plan | Route to PRD clarification |

## Minimum reporting rule

Always list source artifacts checked. If a source was not checked, say why it was not relevant.
