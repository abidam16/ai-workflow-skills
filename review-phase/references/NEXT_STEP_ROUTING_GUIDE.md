# Next Step Routing Guide

Every review must end with exactly one concrete next step. Use canonical values from `docs/workflow/NEXT_STEP_TYPES.md`.

## Common Routes

Use `REQUEST_MISSING_EVIDENCE` when diff, test result, implementation summary, or validation evidence is needed for fair review.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when PRD, architecture, ADR, roadmap, plan, or workflow source evidence is missing.

Use `UPDATE_PRD` when product truth is wrong, missing, or contradicted.

Use `CREATE_ARCHITECTURE` when required architecture is missing.

Use `UPDATE_ARCHITECTURE` when architecture is outdated, contradicted, or insufficient.

Use `CREATE_ADR` or `UPDATE_ADR` when one important decision is missing, stale, or contradicted.

Use `UPDATE_ROADMAP` when roadmap sequencing or exit criteria are wrong.

Use `CREATE_PLAN` when the artifact chain is consistent and no executable plan exists.

Use `UPDATE_PLAN` or `UPDATE_LIGHTWEIGHT_PLAN` when a plan is incomplete, contradictory, too broad, or no longer valid.

Use `SPLIT_INTO_PLANS` when reviewed work must be decomposed into multiple bounded plans.

Use `RUN_ARTIFACT_CONSISTENCY_REVIEW` when durable artifacts need a consistency check before implementation continues.

Use `IMPLEMENT_PLAN` or `IMPLEMENT_LIGHTWEIGHT_PLAN` when artifact review confirms a valid plan is ready to execute.

Use `RETURN_TO_IMPLEMENTATION` when implementation has required fixes but upstream artifacts are valid.

Use `APPLY_MINOR_FIXES` when implementation is acceptable but small local fixes should be made first.

Use `MERGE_OR_CLOSE_TASK` when the reviewed implementation is accepted and the current branch or task should be closed.

Use `START_NEXT_PLAN` when the current task is accepted and the next roadmap slice should be planned.

Use `ESCALATE_TO_FULL_WORKFLOW` when a lightweight task review discovers product, architecture, ADR, or roadmap work is needed.

Use `STOP_AND_ESCALATE` when no safe next action is available.

## Concrete Next Step Format

```md
## Concrete Next Step

- `next_step_type`: UPDATE_PLAN
- `target`: `PLAN.md` task "Accept invitation"
- `action`: Revise the plan so membership creation and invitation acceptance happen in the same transaction.
- `why_this_is_next`: The artifact chain is otherwise coherent, but the current plan violates architecture's transaction boundary.
- `blocking_condition`: Do not implement until the plan is revised and rechecked.
- `suggested_prompt`: Use `plan-writer` to update the invitation acceptance PLAN.md based on the review findings.
```

## Bad Next Steps

Do not write "the review is done", "fix the issues", "continue development", "proceed if desired", or "the next step depends".
