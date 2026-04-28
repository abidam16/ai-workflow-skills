# Source of Truth Guide

## Authority model

Use this authority model when planning:

| Artifact | Authority |
|---|---|
| `PRD.md` | Product behavior, goals, non-goals, user/business rules, success criteria |
| `ARCHITECTURE.md` | System shape, boundaries, data ownership, runtime flows, integration rules, cross-cutting constraints |
| `docs/architecture/<initiative>-architecture.md` | Deep architecture for one large active initiative |
| ADRs | One accepted technical decision and rationale |
| `ROADMAP.md` | Delivery sequencing, phase boundaries, dependencies, exit criteria |
| `PLAN.md` | One executable implementation contract |
| Codebase | Existing implementation reality and local conventions, but not a replacement for durable decisions |

## Conflict handling

If artifacts conflict:

1. Do not silently choose the convenient artifact.
2. Identify the conflict explicitly.
3. If product behavior conflicts with architecture, route to PRD or architecture update depending on which artifact is stale.
4. If architecture conflicts with ADR, route to ADR or architecture update. ADRs override architecture only for the specific decision they record.
5. If roadmap conflicts with architecture, route to roadmap update unless architecture itself is stale.
6. If plan conflicts with upstream artifacts, revise plan or block planning.

## Minimum extraction rule

Every plan must extract the relevant constraints. Do not just name upstream artifacts.

The implementation agent should be able to follow `PLAN.md` without rereading every upstream artifact, while still being able to verify the source path if needed.
