# Next Step Routing Guide

Use this guide only to complete the final `## Concrete Next Step` block. Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md`.

## Required block

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

## Common Routes

Use `IMPLEMENT_PLAN` when a full plan is executable and no blocking upstream artifact is missing.

Use `IMPLEMENT_LIGHTWEIGHT_PLAN` when a lightweight plan is executable and its lightweight assumptions are explicit.

Use `UPDATE_PLAN` or `UPDATE_LIGHTWEIGHT_PLAN` when the existing plan remains the correct artifact but needs clearer scope, constraints, files, validation, or review criteria.

Use `SPLIT_INTO_PLANS` when the requested work contains multiple independently reviewable tasks.

Use `UPDATE_PRD` when product behavior, business rules, user flow, or acceptance criteria are insufficient or contradictory.

Use `UPDATE_ARCHITECTURE` when implementation is architecture-sensitive and system-shape guidance is missing, partial, or conflicting.

Use `CREATE_ADR` or `UPDATE_ADR` when one significant technical decision must be resolved before implementation can be planned safely.

Use `UPDATE_ROADMAP` when sequencing or phase boundaries are unclear.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when a required upstream artifact cannot be found or is not provided.

Use `RESOLVE_SOURCE_CONFLICT` when source artifacts contradict each other.

Use `RUN_ARTIFACT_CONSISTENCY_REVIEW` when durable artifacts should be checked for consistency before implementation starts.

Use `STOP_AND_ESCALATE` when sources are contradictory, unsafe, or impossible to reconcile within this skill.

## Required Field Quality

- `next_step_type`: one canonical value allowed for `plan-writer`.
- `target`: specific artifact, path, section, finding, or task.
- `action`: concrete imperative action.
- `why_this_is_next`: explain why this action is next instead of another artifact.
- `blocking_condition`: `none` if unblocked; otherwise name the precise blocker.
- `suggested_prompt`: directly usable as the next user instruction.
