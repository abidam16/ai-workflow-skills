# Next Step Routing Guide

Use this guide to choose the final `Concrete Next Step` after architecture writing.

## Core rule

Architecture-writer must end with exactly one concrete next step.

Do not list several possible paths as equal choices. If multiple actions are needed, choose the immediate blocker or the next artifact that unlocks the rest of the workflow.

## Routing rules

### Use `CREATE_ADR`

Use when the architecture exposes one important technical decision that has alternatives, trade-offs, and long-term consequences.

Examples:

- choose outbox vs direct Kafka publishing
- choose database ownership strategy
- choose sync API vs async event flow
- choose authorization source of truth

### Use `UPDATE_ADR`

Use when an existing ADR is contradicted, superseded, incomplete, or must be linked to the new architecture.

### Use `CREATE_ROADMAP`

Use when architecture is stable enough and the next uncertainty is delivery sequencing.

### Use `UPDATE_ROADMAP`

Use when an existing roadmap now conflicts with architecture constraints, dependencies, or phase ordering.

### Use `CREATE_PLAN`

Use when architecture is stable enough and there is one obvious bounded implementation task to execute next.

### Use `UPDATE_PLAN`

Use when a current `PLAN.md` exists but must be revised to obey architecture constraints.

### Use `UPDATE_PRD`

Use when architecture cannot proceed or cannot be considered valid because product behavior, scope, or business rules are unclear.

### Use `REVISE_ARCHITECTURE`

Use when the architecture document itself needs another pass before downstream artifacts should consume it.

### Use `REQUEST_MISSING_SOURCE_ARTIFACT`

Use when a required source artifact is missing and guessing would create false certainty.

### Use `REQUEST_ARCHITECTURE_DECISION`

Use when architecture work exposed a structural question that cannot be resolved from available sources.

### Use `RUN_REVIEW`

Use when architecture or architecture delta is complete and should be checked for consistency before downstream planning or implementation.

### Use `STOP_AND_ESCALATE`

Use when sources conflict, architecture would be unsafe, or the correct next action cannot be determined without human decision.

## Bad next steps

Do not use vague next steps such as:

- continue development
- implement the feature
- review later
- update docs as needed
- proceed with the next phase

Replace them with a concrete artifact/action target.
