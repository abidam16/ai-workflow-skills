# Review Modes

## TASK_REVIEW

Use when reviewing one implemented task against one approved `PLAN.md`.

Primary focus:
- objective fulfillment
- scope discipline
- detailed-spec compliance
- validation and tests
- local technical quality
- explicit deviations from the plan

Typical source chain:
- `PLAN.md`
- related roadmap / PRD / ADR only when needed
- changed code / tests / evidence

Typical outcomes:
- approved
- revise task implementation
- update plan because implementation exposed a gap or mismatch

## ROADMAP_IMPLEMENTATION_REVIEW

Use when reviewing multiple completed task implementations under one roadmap.

Primary focus:
- roadmap outcome fulfillment
- cross-task integration
- business outcome across the roadmap slice
- hidden dependency gaps
- sequencing readiness for next phases
- cumulative risk and deferred work

Typical source chain:
- roadmap
- relevant PRD / ADR
- all relevant `PLAN.md`
- code / tests / evidence for the completed tasks

Typical outcomes:
- roadmap slice approved
- additional task fixes required
- roadmap gaps identified
- documents need updating before next phase
