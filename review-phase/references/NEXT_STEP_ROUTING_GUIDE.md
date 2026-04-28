# Next Step Routing Guide

Every review must end with exactly one concrete next step.

## Allowed next step types

- `MERGE_OR_CLOSE_TASK`
- `APPLY_MINOR_FIXES`
- `RETURN_TO_IMPLEMENTATION`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `UPDATE_ROADMAP`
- `UPDATE_PRD`
- `REQUEST_MISSING_EVIDENCE`
- `SPLIT_REVIEW_SCOPE`
- `START_NEXT_PLAN`
- `STOP_AND_ESCALATE`

## Selection algorithm

1. Missing diff, test result, implementation summary, or source artifact needed for fair review -> `REQUEST_MISSING_EVIDENCE`.
2. Review request mixes unrelated tasks, multiple roadmaps, or too many scopes -> `SPLIT_REVIEW_SCOPE`.
3. Product truth is wrong, missing, or contradicted -> `UPDATE_PRD`.
4. Architecture is missing, outdated, contradicted, or required before fair acceptance -> `UPDATE_ARCHITECTURE`.
5. One technical decision is missing or contradicted -> `CREATE_OR_UPDATE_ADR`.
6. Roadmap sequencing or exit criteria are wrong -> `UPDATE_ROADMAP`.
7. PLAN is incomplete, contradictory, or no longer a valid one-task contract -> `UPDATE_PLAN`.
8. Implementation has required fixes but upstream artifacts are valid -> `RETURN_TO_IMPLEMENTATION`.
9. Implementation is acceptable but small fixes should be made first -> `APPLY_MINOR_FIXES`.
10. Implementation is accepted and the current branch/task should be closed -> `MERGE_OR_CLOSE_TASK`.
11. Current task is accepted and the next roadmap slice should be planned -> `START_NEXT_PLAN`.
12. No safe next action is available -> `STOP_AND_ESCALATE`.

## Concrete next step format

```md
## Concrete Next Step

- `next_step_type`: RETURN_TO_IMPLEMENTATION
- `target`: `src/...` and `PLAN.md` task "Accept invitation"
- `action`: Fix membership creation so invitation acceptance updates `user_product_membership` in the same transaction, then rerun the relevant service and repository tests.
- `why_this_is_next`: The plan remains valid, but implementation missed a high-urgency source-of-truth requirement.
- `blocking_condition`: Do not merge until the revised implementation passes tests and the review is rerun.
- `suggested_prompt`: "Use implement-task to revise the accepted-invitation implementation according to the review findings, without changing scope."
```

## Bad next steps

Do not write:

- "The review is done."
- "Fix the issues."
- "Continue development."
- "Proceed if desired."
- "The next step depends."

Make the next step executable.
