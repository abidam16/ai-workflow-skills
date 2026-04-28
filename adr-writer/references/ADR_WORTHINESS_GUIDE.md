# ADR-Worthiness Guide

## ADR-worthy decisions

Create an ADR when the decision has at least three of these traits:

- lasting architectural or technical impact
- credible alternatives
- meaningful trade-offs
- cross-module or cross-service effect
- effect on data ownership, consistency, authorization, integration, or deployment
- costly to reverse
- likely to be questioned later
- likely to guide multiple future tasks
- needed to unblock architecture, roadmap, plan, implementation, or review

## Not ADR-worthy

Do not create ADRs for:

- one-off bug fixes
- local implementation details
- tiny refactors with no broader effect
- product behavior or business rules
- delivery sequencing
- style preferences already covered by existing conventions
- decisions with no real alternative

## Readiness classifications

### `ADR_READY`

Use when one decision is clear enough and has source context, drivers, options, and consequences.

### `BLOCKED_BY_PRD`

Use when the decision depends on unclear product behavior or business rules.

### `BLOCKED_BY_ARCHITECTURE`

Use when system-shape context is missing or too vague.

### `BLOCKED_BY_MISSING_OPTIONS`

Use when the request only names one preferred option and no credible alternatives have been explored.

### `BLOCKED_BY_CONFLICTING_SOURCES`

Use when source artifacts disagree in a way that affects the decision.

### `NOT_ADR_WORTHY`

Use when the issue is too small or already covered.

### `ROUTE_TO_ARCHITECTURE`

Use when the request asks for broad design, not one bounded decision.
