# Architecture Impact Guide

## Purpose

This guide prevents PRD from either ignoring architecture needs or accidentally designing architecture.

The PRD should identify when architecture work is required, but it should not decide the system shape.

## Impact values

### `NONE`

Use when the product change has no meaningful effect on system shape, boundaries, data ownership, runtime flows, integrations, consistency, security, observability, or deployment.

### `CREATE_ARCHITECTURE`

Use when no sufficient architecture document exists and product requirements need durable system-shape guidance before roadmap or plan.

### `UPDATE_ARCHITECTURE`

Use when existing architecture exists but product requirements change boundaries, flows, ownership, constraints, or runtime assumptions.

### `CHECK_EXISTING_ARCHITECTURE`

Use when architecture likely already covers the issue, but the next agent must verify the relevant section before roadmap or plan.

### `ARCHITECTURE_BLOCKED_BY_PRODUCT_QUESTIONS`

Use when architecture cannot proceed because product behavior is still unclear.

## Architecture-sensitive product signals

Route to architecture when product requirements imply or change:

- new major domain concept
- new user role or authorization behavior
- new source-of-truth question
- cross-module or cross-service flow
- sync vs async behavior
- event, notification, queue, or background processing
- multi-step lifecycle
- external integration
- audit, compliance, or security constraint
- consistency or transaction expectation
- scale, performance, or reliability constraint
- frontend/backend contract boundary
- deployment/runtime assumption

## Examples

### Correct architecture impact

```md
## Architecture Impact

- `architecture_impact`: CREATE_ARCHITECTURE
- `reason`: The product introduces invitation acceptance, membership granting, and notification visibility. The PRD defines required behavior, but data ownership, transaction boundary, and notification sync/async design require architecture.
- `architecture_questions_or_constraints`:
  - Determine the source of truth for membership.
  - Define whether notification is a read model or transactional record.
  - Define acceptance transaction boundary and failure behavior.
```

### Incorrect architecture impact

```md
## Architecture Impact

- Use PostgreSQL table `user_product_membership` with optimistic locking and Kafka topic `invitation.accepted`.
```

That belongs in architecture or ADR, not PRD.
