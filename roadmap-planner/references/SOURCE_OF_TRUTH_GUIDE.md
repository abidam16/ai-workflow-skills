# Source of Truth Guide

Roadmap planning must use approved artifacts in the correct authority order.

## Authority Order

1. `PRD.md` or PRD delta: product truth.
2. `ARCHITECTURE.md` or initiative architecture docs: system-shape truth.
3. ADRs: decision truth.
4. Existing roadmap: sequencing truth.
5. Existing plans: already-planned execution slices.
6. Codebase: implementation evidence, not upstream intent.

## Conflict Handling

If sources conflict, do not resolve by guessing.

Examples:

- PRD says notification is user-visible immediately, but architecture says notification creation is eventually consistent.
  - Route to PRD/architecture reconciliation.
- Architecture says membership is source of truth, but an old roadmap phase uses invitation state for authorization.
  - Update roadmap before planning.
- ADR says use outbox, but roadmap assumes direct Kafka publish inside business transaction.
  - Update roadmap or architecture.

## Roadmap Rule

Roadmap sequencing may interpret approved constraints, but must not invent new product behavior, architecture boundaries, or technical decisions.
