# Architecture-Aware Implementation Guide

## Architecture-sensitive triggers

Treat a task as architecture-sensitive if it touches any of these:

- module, package, layer, service, or component boundaries
- data ownership or source-of-truth rules
- database schema, persistence lifecycle, or migration behavior
- API contract, integration contract, or messaging contract
- event publishing, queue consumption, scheduler behavior, async worker behavior
- transaction boundary, consistency model, idempotency, retries, locking
- authorization, authentication, permission checks, sensitive data handling
- observability, audit logs, operational logs, metrics, tracing, deployment/runtime config

## What to extract from architecture

Do not copy the whole architecture into the implementation summary. Extract concrete obligations:

- which component owns the behavior
- where the new code belongs
- which data model/table is authoritative
- which read models are not authoritative
- sync vs async expectations
- transaction and consistency requirements
- allowed integration direction
- logging/monitoring/audit expectations
- ADRs that must be obeyed

## Implementation safeguards

During coding:

- do not move behavior across component boundaries without approved architecture change
- do not use read models as write/source-of-truth models unless architecture allows it
- do not introduce new cross-service coupling without approved architecture or ADR
- do not make async side effects synchronous unless explicitly required
- do not bypass outbox, retry, idempotency, or transaction rules
- do not weaken authorization or security rules to satisfy a local test

## When architecture is missing

If the task is architecture-sensitive and there is no relevant architecture guidance:

- proceed only if the plan explicitly contains enough approved architecture constraints
- otherwise stop with `BLOCKED_REQUIRES_ARCHITECTURE_CLARIFICATION` or `BLOCKED_REQUIRES_ARCHITECTURE_UPDATE`

## When implementation discovers architecture drift

If current code and architecture differ:

- implement according to the approved plan only if the plan explicitly accounts for the drift
- otherwise report `BLOCKED_BY_CONFLICTING_SOURCES`
- recommend review or architecture update depending on which source appears stale
