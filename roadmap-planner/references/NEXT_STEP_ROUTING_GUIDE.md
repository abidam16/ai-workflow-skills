# Next Step Routing Guide

Every roadmap output must end with exactly one concrete next step. Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md`.

## Required Block Shape

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

The block must appear exactly once in the final output and must be the final section.

## Common Routes

Use `CREATE_PLAN` when one roadmap slice is ready to become a new single-task plan.

Use `UPDATE_PLAN` when an existing plan still represents the correct task but must be adjusted based on roadmap changes.

Use `SPLIT_INTO_PLANS` when the selected roadmap slice contains multiple independent implementation tasks.

Use `UPDATE_ARCHITECTURE` when sequencing depends on stale or conflicting system-shape constraints.

Use `CREATE_ADR` or `UPDATE_ADR` when sequencing depends on one unresolved or changed technical decision.

Use `UPDATE_PRD` when product behavior, goals, non-goals, roles, flows, or success criteria are unclear or changed.

Use `REVISE_ROADMAP` when the roadmap is internally inconsistent or too broad and needs another roadmap pass.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when necessary source artifacts are absent and cannot be found in the repo.

Use `RESOLVE_SOURCE_CONFLICT` when source artifacts contradict each other and sequencing cannot safely continue.

Use `RUN_ARTIFACT_CONSISTENCY_REVIEW` when artifact consistency should be checked before implementation planning.

Use `STOP_AND_ESCALATE` when forward progress would create unsafe or misleading artifacts.

## Bad Next Steps

Do not use vague next steps such as "continue development", "implement the roadmap", "proceed as planned", "review later", or "fix issues".
