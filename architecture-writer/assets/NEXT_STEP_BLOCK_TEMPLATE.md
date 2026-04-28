# Concrete Next Step Template

Every architecture-writer output must end with this exact section.

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

## Field rules

- `next_step_type`: one concrete routed action.
- `target`: the exact artifact, file, folder, skill, review action, or decision that should be handled next.
- `action`: the concrete operation to perform.
- `why_this_is_next`: explain why this is the immediate next step, not a later step.
- `blocking_condition`: write `none` when there is no blocker; otherwise state what blocks progress.
- `suggested_prompt`: provide a ready-to-copy prompt for the next agent invocation.

## Architecture-writer allowed next_step_type values

- `CREATE_ADR`
- `UPDATE_ADR`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`
- `CREATE_PLAN`
- `UPDATE_PLAN`
- `UPDATE_PRD`
- `REVISE_ARCHITECTURE`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `REQUEST_ARCHITECTURE_DECISION`
- `RUN_REVIEW`
- `STOP_AND_ESCALATE`
