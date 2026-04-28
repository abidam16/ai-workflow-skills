# Next Step Routing Guide

Use this guide only to complete the final `## Concrete Next Step` block.

The next step must route to one concrete action. Do not use vague wording such as "continue development", "fix issues", "move forward", or "the plan is ready".

## Allowed `next_step_type` values

### `IMPLEMENT_PLAN`

Use when the plan is executable and no blocking upstream artifact is missing.

- `target`: the plan path, usually `PLAN.md`
- `action`: implement the plan exactly as scoped
- `blocking_condition`: `None`

### `SPLIT_INTO_PLANS`

Use when the requested work contains multiple independently reviewable tasks.

- `target`: the current planning request or source artifact section
- `action`: create separate single-task plans for the listed plan candidates
- `blocking_condition`: current request is too broad for one plan

### `UPDATE_PRD`

Use when product behavior, business rules, user flow, or acceptance criteria are insufficient or contradictory.

- `target`: `PRD.md` or the relevant PRD section
- `action`: update product truth before planning implementation

### `CREATE_OR_UPDATE_ARCHITECTURE`

Use when implementation is architecture-sensitive and system-shape guidance is missing, partial, or conflicting.

- `target`: `ARCHITECTURE.md` or `docs/architecture/<initiative>-architecture.md`
- `action`: create or update architecture before writing an executable plan

### `CREATE_OR_UPDATE_ADR`

Use when one significant technical decision must be made before implementation can be planned safely.

- `target`: `docs/adr/<decision>.md`
- `action`: create or update the ADR before planning implementation

### `UPDATE_ROADMAP`

Use when sequencing or phase boundaries are unclear.

- `target`: `ROADMAP.md` or relevant roadmap section
- `action`: update delivery sequencing before task planning

### `REVISE_PLAN`

Use when an existing plan remains the correct artifact but needs clearer scope, constraints, files, validation, or review criteria.

- `target`: the existing plan path
- `action`: revise the plan before implementation

### `REQUEST_MISSING_SOURCE_ARTIFACT`

Use when a required upstream artifact cannot be found or is not provided.

- `target`: the missing artifact path or section
- `action`: provide or create the missing source artifact

### `RETURN_TO_REVIEW`

Use when the plan update is complete and the correct next action is to review whether the plan resolves previous findings.

- `target`: the review report or finding identifier
- `action`: run review against the revised plan or evidence

### `STOP_AND_ESCALATE`

Use when the sources are contradictory, unsafe, or impossible to reconcile within this skill.

- `target`: the conflicting artifacts or unresolved decision
- `action`: stop and escalate the conflict instead of writing an unsafe plan

## Required field quality

- `next_step_type`: one of the allowed values above.
- `target`: specific artifact, path, section, finding, or task.
- `action`: concrete imperative action.
- `why_this_is_next`: explain why this action is next instead of another artifact.
- `blocking_condition`: `None` if unblocked; otherwise name the precise blocker.
- `suggested_prompt`: directly usable as the next user instruction.
