# SCOPE_AND_SPLIT_RULES

## Scope rules

The implementation must stay within the task boundary defined by the plan.

Treat the task as out of scope if it:
- introduces a second independent objective
- changes a separate user flow not required by the plan
- requires a broad architecture redesign not named in the plan
- creates a second validation path that could be reviewed independently
- produces multiple unrelated commit themes

## Split triggers

Do not continue implementation under one plan if any of these are true:
- the work clearly covers more than one coherent task
- the plan requires multiple independently reviewable deliverables
- different parts of the work have different acceptance criteria
- the file changes span multiple unrelated bounded contexts
- the safest implementation would require multiple separate plans

If a split trigger occurs, stop and report `BLOCKED_REQUIRES_PLAN_SPLIT`.
