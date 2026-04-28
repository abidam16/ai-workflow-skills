# Next Step Routing Guide

Every PRD run must end with one concrete next step.

## Allowed next step types

### `CREATE_OR_UPDATE_ARCHITECTURE`

Use when product truth is stable enough but system shape must be created, checked, or updated before roadmap or plan.

Target examples:

- `ARCHITECTURE.md`
- `docs/architecture/notification-system-architecture.md`

### `CREATE_OR_UPDATE_ADR`

Use when one lasting technical decision is required and product truth is stable enough.

Target examples:

- `docs/adr/0003-use-outbox-for-invitation-events.md`

### `CREATE_OR_UPDATE_ROADMAP`

Use when product truth and necessary architecture/ADR context are stable enough and the next problem is sequencing.

Target examples:

- `ROADMAP.md`
- `docs/roadmap/notification-system-roadmap.md`

### `CREATE_OR_UPDATE_PLAN`

Use when the next action is one executable implementation contract.

Target examples:

- `PLAN.md`
- `docs/plans/accept-invitation-endpoint-plan.md`

### `REQUEST_PRODUCT_DECISION`

Use when PRD cannot proceed because a product question needs a decision.

### `REQUEST_MISSING_SOURCE_ARTIFACT`

Use when an expected input artifact is absent and must be provided or created first.

### `REVISE_PRD`

Use when this run produced findings or a partial delta, but the PRD itself still needs a targeted update.

### `RETURN_TO_REVIEW`

Use when the PRD was updated as a review fix and the next step is to rerun review.

### `START_IMPLEMENTATION`

Use only when a valid plan already exists and the PRD update does not require architecture, ADR, roadmap, or plan changes.

### `STOP_AND_ESCALATE`

Use when sources conflict in a way that cannot be resolved by one artifact update.

## Required fields

Each next step must include:

- `next_step_type`
- `target`
- `action`
- `why_this_is_next`
- `blocking_condition`
- `suggested_prompt`

## Vague wording to avoid

Do not write:

- continue development
- proceed to next phase
- update docs
- implement feature
- review if needed

Write:

```md
- `next_step_type`: CREATE_OR_UPDATE_ARCHITECTURE
- `target`: `ARCHITECTURE.md`
- `action`: Create architecture for invitation, membership, and notification boundaries based on this PRD.
- `why_this_is_next`: The PRD defines target behavior, but source-of-truth and transaction boundaries must be durable before roadmap or plan.
- `blocking_condition`: Cannot create implementation plan until architecture defines membership ownership and notification sync/async behavior.
- `suggested_prompt`: Use $architecture-writer to create ARCHITECTURE.md for invitation acceptance, membership ownership, and notification read model using PRD.md as source.
```
