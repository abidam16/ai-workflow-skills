# Next Step Routing Guide

Every implementation output must end with exactly one concrete next step.

## Allowed next step types

| next_step_type | Use when |
|---|---|
| `RUN_REVIEW` | Implementation is complete enough for independent review |
| `RUN_VALIDATION` | Code changes are made but required validation still needs to be run |
| `APPLY_MINOR_FIX` | A small in-scope issue remains before review |
| `UPDATE_PLAN` | Plan was wrong, incomplete, or contradicted upstream artifacts |
| `UPDATE_ARCHITECTURE` | Implementation revealed stale/missing architecture guidance |
| `CREATE_OR_UPDATE_ADR` | A lasting technical decision is required or changed |
| `UPDATE_ROADMAP` | Sequencing/scope changed beyond the current phase |
| `UPDATE_PRD` | Product behavior or requirement ambiguity blocks completion |
| `SPLIT_PLAN` | Work must be broken into multiple implementation tasks |
| `REQUEST_MISSING_SOURCE_ARTIFACT` | Required source artifact is missing or inaccessible |
| `RESOLVE_SOURCE_CONFLICT` | Source artifacts conflict and cannot be safely reconciled in implementation |
| `STOP_AND_ESCALATE` | Safe progress is blocked by unresolved risk or authority conflict |

## Good examples

```md
## Concrete Next Step

- `next_step_type`: RUN_REVIEW
- `target`: implementation diff, `PLAN.md`, `ARCHITECTURE.md`, and this summary
- `action`: Run `review-phase` to verify plan fulfillment, architecture compliance, and validation evidence.
- `why_this_is_next`: Implementation is complete and validation passed.
- `blocking_condition`: None.
- `suggested_prompt`: "Use review-phase to review the current implementation against the approved plan, relevant architecture sections, ADRs, and validation results."
```

```md
## Concrete Next Step

- `next_step_type`: UPDATE_PLAN
- `target`: `PLAN.md`
- `action`: Revise the plan to resolve the conflict with `ARCHITECTURE.md` data ownership rules.
- `why_this_is_next`: The current plan requires using a read model as source of truth, which architecture forbids.
- `blocking_condition`: Implementation must not proceed until the plan is corrected or architecture is changed.
- `suggested_prompt`: "Use plan-writer to update `PLAN.md` so it follows the source-of-truth rules in `ARCHITECTURE.md`."
```

## Bad examples

Avoid:

- `action`: Continue.
- `action`: Review done.
- `action`: Fix issues.
- `action`: Proceed to next task.
- `suggested_prompt`: Do the next step.
