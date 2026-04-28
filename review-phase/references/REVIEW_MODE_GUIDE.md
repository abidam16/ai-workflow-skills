# Review Mode Guide

Select exactly one mode for each review.

## `TASK_REVIEW`

Use when reviewing one implemented task against one approved `PLAN.md`.

Primary question:

> Did this implementation fulfill the approved plan while obeying PRD, architecture, ADR, and roadmap constraints?

Inputs:

- one plan
- implementation summary
- diffs/changed files
- tests or validation evidence
- relevant upstream artifacts

## `ROADMAP_IMPLEMENTATION_REVIEW`

Use when reviewing multiple completed tasks under one roadmap or initiative slice.

Primary question:

> Does the completed implementation set fulfill the roadmap slice and integrate correctly?

Inputs:

- roadmap or slice
- relevant PRD
- relevant architecture
- relevant ADRs
- multiple plans
- multiple implementation summaries or diffs
- integration evidence

## `ARTIFACT_CONSISTENCY_REVIEW`

Use before implementation or before continuing implementation when the artifact chain itself must be checked.

Primary question:

> Are PRD, architecture, ADRs, roadmap, and PLAN mutually consistent enough for safe implementation?

Inputs:

- PRD
- architecture
- ADRs
- roadmap
- one or more plans or plan candidates
- shared workflow docs, if present

This mode should not judge code unless implementation evidence is included only to expose artifact drift.

## Selection rules

| Situation | Mode |
|---|---|
| One implementation against one plan | `TASK_REVIEW` |
| Multiple completed tasks against roadmap | `ROADMAP_IMPLEMENTATION_REVIEW` |
| PRD/architecture/ADR/roadmap/plan consistency before coding | `ARTIFACT_CONSISTENCY_REVIEW` |
| Ambiguous or mixed review target | Choose `REQUEST_MISSING_EVIDENCE`, `UPDATE_PLAN`, or `STOP_AND_ESCALATE` based on what makes the review actionable |

Do not silently merge modes.
