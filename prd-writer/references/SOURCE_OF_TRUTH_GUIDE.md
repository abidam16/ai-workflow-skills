# Source of Truth Guide

## Authority model

| Artifact | Authority |
|---|---|
| `BRAINSTORM.md` | Exploration, uncertainty, discarded options, and artifact-routing rationale |
| `PRD.md` | Product behavior, goals, non-goals, user/business rules, constraints, and success criteria |
| `ARCHITECTURE.md` | System shape, component boundaries, data ownership, runtime flows, integration rules, and cross-cutting constraints |
| `docs/architecture/<initiative>-architecture.md` | Deep architecture for one large active initiative |
| ADRs | One accepted technical decision and rationale |
| `ROADMAP.md` | Delivery sequencing, phase boundaries, dependencies, and readiness gates |
| `PLAN.md` | One executable implementation contract |
| Codebase | Existing implementation reality and local conventions, but not a replacement for durable product truth |

## PRD responsibility

PRD owns product truth only.

A PRD may state:

```text
The user must be able to accept an invitation and gain access to the product after acceptance.
```

A PRD must not state:

```text
Create product_invitation, user_product_membership, Kafka invitation.accepted topic, and outbox_event publisher.
```

## Conflict handling

If artifacts conflict:

1. Identify the conflict explicitly.
2. Determine which artifact has authority for the conflicting topic.
3. Update PRD only when product behavior, product rules, goals, constraints, or success criteria are unclear, stale, or contradicted.
4. Route to architecture when product truth is stable but system shape is missing or stale.
5. Route to ADR when one technical decision is missing or stale.
6. Route to roadmap when sequencing is missing or stale.
7. Route to plan when only one executable implementation contract is missing.

## Downstream extraction rule

PRD must give downstream skills enough product clarity to proceed.

Architecture, roadmap, and plan writers should not need to infer core user behavior from brainstorm notes if the PRD exists.
