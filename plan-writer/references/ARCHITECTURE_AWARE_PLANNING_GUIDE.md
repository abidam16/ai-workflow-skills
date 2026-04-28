# Architecture-Aware Planning Guide

## Architecture-sensitive task indicators

Treat a task as architecture-sensitive when it touches:

- module/service/package boundaries
- ownership of tables, entities, DTOs, or read models
- authorization source of truth
- API boundary or OpenAPI contract
- event/message publishing or consuming
- queue/topic semantics
- transaction boundaries
- retry/idempotency behavior
- optimistic locking or concurrency
- scheduler/worker runtime behavior
- observability/logging/audit requirements
- deployment/runtime configuration
- data migration or data retention

## Required architecture fields in a plan

If the task is architecture-sensitive, include:

- `architecture_readiness`
- source architecture path/section
- extracted architecture constraints
- must-not-change boundaries
- review checks for architecture conformance

## Readiness outcomes

### `NOT_RELEVANT`

Use only when the task has no meaningful architecture impact.

### `READY`

Architecture exists and is sufficient for this task. Proceed with plan.

### `PARTIAL`

Architecture exists but lacks one or more details. Proceed only if the missing details are outside this task's implementation boundary. Otherwise block.

### `MISSING`

The task requires architecture decisions that do not exist in durable form. Route to architecture-writer.

### `CONFLICTING`

Architecture conflicts with PRD, ADR, roadmap, existing plan, or implementation assumptions. Route to the stale/conflicting artifact before implementation.

## Do not design architecture inside PLAN.md

The plan may state:

```text
Use `user_product_membership` as the source of truth because ARCHITECTURE.md says so.
```

The plan must not invent:

```text
Let's make `user_product_membership` the source of truth.
```

If the architecture decision is not durable yet, route to architecture-writer or ADR writer.
