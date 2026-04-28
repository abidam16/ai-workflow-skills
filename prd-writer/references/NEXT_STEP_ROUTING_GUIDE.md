# Next Step Routing Guide

Every PRD run must end with exactly one normalized `## Concrete Next Step` block. Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md`.

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

Use `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE` when product truth is stable enough but system shape must be created, checked, or updated before roadmap or plan.

Use `CREATE_ADR` or `UPDATE_ADR` when one lasting technical decision is required and product truth is stable enough.

Use `CREATE_ROADMAP` or `UPDATE_ROADMAP` when product truth and necessary architecture/ADR context are stable enough and the next problem is sequencing.

Use `CREATE_PLAN` or `UPDATE_PLAN` when the next action is one executable implementation contract.

Use `REVISE_PRD` when this PRD output is incomplete or internally weak.

Use `RETURN_TO_PRD` when product truth is still missing or conflicting and must be resolved before downstream work.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when an expected input artifact is absent and must be provided or created first.

Use `STOP_AND_ESCALATE` when sources conflict in a way that cannot be resolved by one artifact update.

## Required Field Quality

Each next step must include:

- `next_step_type`
- `target`
- `action`
- `why_this_is_next`
- `blocking_condition`
- `suggested_prompt`

The `target` must name a concrete artifact or action, not a vague phase.

## Vague Wording To Avoid

Do not write "continue development", "proceed to next phase", "update docs", "implement feature", or "review if needed".

Write:

```md
## Concrete Next Step

- `next_step_type`: CREATE_ARCHITECTURE
- `target`: `ARCHITECTURE.md`
- `action`: Create architecture for invitation, membership, and notification boundaries based on this PRD.
- `why_this_is_next`: The PRD defines target behavior, but source-of-truth and transaction boundaries must be durable before roadmap or plan.
- `blocking_condition`: Cannot create implementation plan until architecture defines membership ownership and notification sync/async behavior.
- `suggested_prompt`: Use `architecture-writer` to create `ARCHITECTURE.md` for invitation acceptance, membership ownership, and notification read model using `PRD.md` as source.
```
