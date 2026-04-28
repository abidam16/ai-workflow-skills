# Architecture Handoff Guide

Every architecture-writer run must end with a concrete handoff.

## Mandatory Closing Format

```text
Decision:
Architecture Scope:
Architecture Path:
Why this decision:
Sections created or changed:
ADR Impact:
Roadmap Impact:
Plan Readiness:
Immediate Next Step:
Continuation Prompt:
```

## Decision Values

Use exactly one:

- `CREATE_ROOT_ARCHITECTURE`
- `UPDATE_ROOT_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `ROUTE_TO_PRD`
- `ROUTE_TO_ADR`
- `ROUTE_TO_ROADMAP`
- `ROUTE_TO_PLAN`
- `INSUFFICIENT_INPUT`

## Architecture Scope Values

Use one:

- `root`
- `initiative`
- `not architecture`

## ADR Impact Values

Use one:

- `none`
- `create ADR`
- `update/supersede ADR`
- `review existing ADRs`

## Roadmap Impact Values

Use one:

- `none`
- `create roadmap`
- `update roadmap`
- `review roadmap`

## Plan Readiness Values

Use one:

- `ready for PLAN`
- `not ready - needs PRD`
- `not ready - needs ADR`
- `not ready - needs roadmap`
- `not ready - unresolved architecture questions`

## Examples

### New Root Architecture

```text
Decision: CREATE_ROOT_ARCHITECTURE
Architecture Scope: root
Architecture Path: ARCHITECTURE.md
Why this decision: The repo has no canonical system-shape source of truth and future tasks need shared boundaries.
Sections created or changed: all root architecture sections
ADR Impact: create ADR
Roadmap Impact: review roadmap
Plan Readiness: not ready - needs ADR
Immediate Next Step: Create ADR for the selected integration pattern.
Continuation Prompt: Proceed to create an ADR for the integration pattern identified in ARCHITECTURE.md.
```

### Initiative Architecture

```text
Decision: CREATE_INITIATIVE_ARCHITECTURE
Architecture Scope: initiative
Architecture Path: docs/architecture/notification-system-architecture.md
Why this decision: The notification initiative changes data ownership, runtime flows, async side effects, and multiple future plans.
Sections created or changed: target architecture, component boundaries, data ownership, runtime flows, transaction rules, ADR candidates
ADR Impact: create ADR
Roadmap Impact: update roadmap
Plan Readiness: not ready - needs ADR
Immediate Next Step: Create ADR for the outbox/event publishing decision.
Continuation Prompt: Proceed to create the outbox/event publishing ADR based on docs/architecture/notification-system-architecture.md.
```

### Route to ADR

```text
Decision: ROUTE_TO_ADR
Architecture Scope: not architecture
Architecture Path: n/a
Why this decision: The unresolved issue is one bounded decision with clear alternatives.
Sections created or changed: none
ADR Impact: create ADR
Roadmap Impact: none
Plan Readiness: not ready - needs ADR
Immediate Next Step: Create an ADR for the bounded decision.
Continuation Prompt: Proceed to create an ADR for the selected technical decision.
```
