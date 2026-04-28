# Next Step Routing Guide

Every ADR run must end with exactly one `## Concrete Next Step` block. Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md`.

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

## Routing Rules

Use `UPDATE_ARCHITECTURE` when the ADR changes component boundaries, data ownership, runtime flow, integration pattern, consistency rule, authorization rule, or cross-cutting constraint.

Use `CREATE_ROADMAP` or `UPDATE_ROADMAP` when the ADR is accepted, architecture is already updated or unaffected, and delivery sequencing is now the next problem.

Use `CREATE_PLAN` or `UPDATE_PLAN` when the ADR is accepted, roadmap is ready or unnecessary, and exactly one implementation task is clear.

Use `RETURN_TO_PRD` when product behavior or business-rule uncertainty blocks the decision.

Use `RETURN_TO_ARCHITECTURE` when broad system shape must be defined or corrected before one ADR can be written.

Use `RETURN_TO_ADR` when an existing ADR must be revisited before this decision can proceed.

Use `REVISE_ADR` when the ADR is close but missing drivers, options, consequences, or architecture linkage.

Use `CREATE_SUPERSEDING_ADR` when an accepted ADR is no longer valid and the decision has changed.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when a named source artifact is needed but not available.

Use `STOP_AND_ESCALATE` when a source-of-truth conflict or unsafe ambiguity should not be resolved by the agent alone.

## Bad Next Steps

Avoid vague actions such as "continue", "proceed", "fix issues", "review later", "implement changes", or "update docs as needed".
