# Next Step Routing Guide

Every review must end with exactly one concrete next step.

Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md` when available. This local guide includes compatibility values for repos that have not yet adopted the shared enum file.

## Allowed next step types

- `MERGE_OR_CLOSE_TASK`
- `APPLY_MINOR_FIXES`
- `RETURN_TO_IMPLEMENTATION`
- `RUN_IMPLEMENTATION`
- `RUN_REVIEW`
- `CREATE_PLAN`
- `UPDATE_PLAN`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `CREATE_OR_UPDATE_ADR`
- `UPDATE_ROADMAP`
- `UPDATE_PRD`
- `REQUEST_MISSING_EVIDENCE`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `SPLIT_REVIEW_SCOPE`
- `START_NEXT_PLAN`
- `STOP_AND_ESCALATE`

## Selection algorithm

1. Missing diff, test result, implementation summary, or validation evidence needed for fair implementation review -> `REQUEST_MISSING_EVIDENCE`.
2. Missing PRD, architecture, ADR, roadmap, plan, or workflow source needed for artifact review -> `REQUEST_MISSING_SOURCE_ARTIFACT`.
3. Review request mixes unrelated tasks, multiple roadmaps, or too many scopes -> `SPLIT_REVIEW_SCOPE`.
4. Product truth is wrong, missing, or contradicted -> `UPDATE_PRD`.
5. Architecture is missing and required for safe implementation -> `CREATE_ARCHITECTURE`.
6. Architecture is outdated, contradicted, or insufficient -> `UPDATE_ARCHITECTURE`.
7. One important technical decision is missing -> `CREATE_ADR`.
8. An accepted decision is contradicted or stale -> `UPDATE_ADR`.
9. Roadmap sequencing or exit criteria are wrong -> `UPDATE_ROADMAP`.
10. PLAN is incomplete, contradictory, too broad, or no longer valid -> `UPDATE_PLAN`.
11. Artifact chain is consistent and no plan exists -> `CREATE_PLAN`.
12. Artifact chain is consistent and a valid plan exists -> `RUN_IMPLEMENTATION`.
13. Implementation has required fixes but upstream artifacts are valid -> `RETURN_TO_IMPLEMENTATION`.
14. Implementation is acceptable but small fixes should be made first -> `APPLY_MINOR_FIXES`.
15. Implementation is accepted and the current branch/task should be closed -> `MERGE_OR_CLOSE_TASK`.
16. Current task is accepted and the next roadmap slice should be planned -> `START_NEXT_PLAN`.
17. No safe next action is available -> `STOP_AND_ESCALATE`.

## Concrete next step format

```md
## Concrete Next Step

- `next_step_type`: UPDATE_PLAN
- `target`: `PLAN.md` task "Accept invitation"
- `action`: Revise the plan so membership creation and invitation acceptance happen in the same transaction.
- `why_this_is_next`: The artifact chain is otherwise coherent, but the current plan violates architecture's transaction boundary.
- `blocking_condition`: Do not implement until the plan is revised and rechecked.
- `suggested_prompt`: "Use plan-writer to update the invitation acceptance PLAN.md based on the artifact consistency review findings."
```

## Bad next steps

Do not write:

- "The review is done."
- "Fix the issues."
- "Continue development."
- "Proceed if desired."
- "The next step depends."

Make the next step executable.
