# Finding Classification Guide

Use severity to drive the final review status and concrete next step.

## `HIGH_URGENCY`

Blocks acceptance, merge, release, or dependent work.

Common triggers:

- product behavior is incorrect
- accepted plan objective is not fulfilled
- architecture boundary or source-of-truth rule is violated
- accepted ADR is contradicted
- authorization/security behavior is unsafe
- transaction/consistency rule is violated
- validation evidence is missing for high-risk logic

Allowed statuses:

- usually `NEEDS_REVISION`
- `BLOCKED` if source artifacts or evidence are insufficient

Typical next steps:

- `RETURN_TO_IMPLEMENTATION`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `REQUEST_MISSING_EVIDENCE`

## `MEDIUM_URGENCY`

Important but may not block acceptance depending on context.

Common triggers:

- maintainability risk
- partial validation gap
- non-fatal integration concern
- small architecture ambiguity that should be resolved soon

Allowed statuses:

- `APPROVED_WITH_MINOR_IMPROVEMENTS`
- `NEEDS_REVISION` if risk is accumulating or impacts dependent work

## `LOW_URGENCY`

Minor improvement that usually does not block acceptance.

Common triggers:

- naming clarity
- small duplication
- local readability improvement
- minor test coverage improvement

Allowed statuses:

- `APPROVED`
- `APPROVED_WITH_MINOR_IMPROVEMENTS`

## `FUTURE_IMPROVEMENT`

Out-of-scope improvement that should not affect current acceptance.

Do not put required fixes here.
