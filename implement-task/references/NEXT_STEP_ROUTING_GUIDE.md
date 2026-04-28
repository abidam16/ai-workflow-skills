# Next Step Routing Guide

Every `implement-task` output must end with exactly one normalized `## Concrete Next Step` block. Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md`.

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

## Selection Rule

Choose the one next action that unblocks the workflow first. Do not list several next steps.

## Common Routes

Use `RUN_REVIEW` when full-plan implementation is complete enough for independent review.

Use `RUN_LIGHTWEIGHT_REVIEW` when lightweight-plan implementation is complete enough for lightweight review.

Use `RUN_VALIDATION` when implementation is complete but required validation still needs to run.

Use `APPLY_MINOR_FIXES` when a small correction remains inside the approved plan scope.

Use `UPDATE_PLAN` or `UPDATE_LIGHTWEIGHT_PLAN` when the plan is incomplete, unclear, or no longer matches the safe implementation path.

Use `UPDATE_ARCHITECTURE` when implementation exposes an architecture gap or conflict.

Use `CREATE_ADR` or `UPDATE_ADR` when a non-trivial technical decision blocks or changes implementation.

Use `UPDATE_ROADMAP` when delivery sequencing or phase scope must change.

Use `UPDATE_PRD` when product behavior or business rules must be clarified or changed.

Use `SPLIT_INTO_PLANS` when the implementation request contains multiple independent tasks.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when a required source artifact is missing.

Use `RESOLVE_SOURCE_CONFLICT` when source artifacts conflict and implementation cannot safely proceed.

Use `ESCALATE_TO_FULL_WORKFLOW` when lightweight assumptions break.

Use `STOP_AND_ESCALATE` when the issue cannot be safely resolved by this workflow step.

## Anti-Patterns

Do not use vague actions such as "continue", "continue development", "fix issues", "update docs as needed", "review later", or "implementation complete".
