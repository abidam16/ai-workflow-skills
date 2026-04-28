# Root vs Initiative Architecture

## Core Rule

Each repo/product should have one canonical root architecture entry point:

```text
ARCHITECTURE.md
```

Large initiatives may have separate architecture documents:

```text
docs/architecture/<initiative-slug>-architecture.md
```

The root architecture remains the canonical map. Initiative architecture documents are deeper design workspaces for substantial changes.

## Use Root `ARCHITECTURE.md` For

Use root architecture for:

- current accepted system shape
- stable module/service/component boundaries
- source-of-truth data ownership
- integration boundary rules
- cross-cutting constraints
- security and authorization source rules
- observability and deployment assumptions
- links to active initiative architecture documents
- ADR index
- implementation rules for agents

The root file should be concise and repeatedly loadable.

## Use Initiative Architecture For

Use initiative architecture when the design is too large, transitional, or multi-component for the root file.

Use it when at least two or three of these are true:

- touches multiple modules or services
- changes data ownership
- introduces new infrastructure
- affects security or authorization
- changes transaction boundaries
- introduces async/event-driven flows
- creates long-term architectural constraints
- requires multiple ADRs
- affects multiple implementation plans
- requires staged rollout or migration
- contains temporary transition states that should not live permanently in root architecture

## Examples

Good initiative architecture candidates:

- `docs/architecture/notification-system-architecture.md`
- `docs/architecture/outbox-event-publishing-architecture.md`
- `docs/architecture/report-template-engine-architecture.md`
- `docs/architecture/openapi-contract-workflow-architecture.md`
- `docs/architecture/frontend-design-system-architecture.md`

Poor initiative architecture candidates:

- one endpoint addition
- one local refactor
- one bug fix
- one isolated schema column addition
- one narrow decision better captured by ADR
- one task already ready for `PLAN.md`

## Root Must Link Active Initiative Architectures

Root `ARCHITECTURE.md` should contain an `Active Initiative Architectures` section:

```md
## Active Initiative Architectures

| Initiative | Document | Status | Notes |
|---|---|---|---|
| Notification System | `docs/architecture/notification-system-architecture.md` | Active | Defines invitation, notification, and membership flows. |
```

## Lifecycle

Use this lifecycle for initiative architecture:

1. `Proposed`
2. `Active`
3. `Accepted`
4. `Folded into root ARCHITECTURE.md`
5. `Archived`

When an initiative becomes the stable architecture, move permanent rules into root `ARCHITECTURE.md` and archive the detailed initiative doc if it is no longer needed for active delivery.

Suggested archive path:

```text
docs/architecture/archive/<initiative-slug>-architecture.md
```

## Conflict Rule

If root architecture and initiative architecture conflict:

1. ADRs override both only for the specific decision they record.
2. Active initiative architecture may define temporary transition rules for that initiative.
3. Root `ARCHITECTURE.md` remains the canonical stable system shape.
4. Resolve conflict by updating root, initiative architecture, or ADR links explicitly.
