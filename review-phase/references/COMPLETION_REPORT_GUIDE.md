# Completion Report Guide

A review report is complete only when it provides a decision and one concrete next step.

## Required for all review modes

- selected review mode
- source artifacts used
- missing/stale/conflicting artifact assessment
- final status
- findings with severity and category
- risk assessment
- exactly one `Concrete Next Step`

## Additional requirement for `ARTIFACT_CONSISTENCY_REVIEW`

The report must explicitly check:

- PRD to Architecture consistency
- Architecture to ADR consistency
- Architecture/ADR to Roadmap consistency
- Roadmap/Source Artifacts to PLAN consistency
- Handoff contract completeness
- implementation readiness or reason not ready

## Completion rule

Do not end with a narrative summary only. The final actionable section must be:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```
