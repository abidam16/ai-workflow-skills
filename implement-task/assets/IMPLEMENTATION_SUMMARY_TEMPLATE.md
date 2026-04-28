# Implementation Summary

## Outcome

- `outcome_status`: IMPLEMENTED / IMPLEMENTED_WITH_REPORTED_DEVIATION
- `plan_used`:
- `task_identity`:
- `implementation_scope`: one task / other

## Source Artifacts Checked

| Artifact | Path / Section | Used For | Result |
|---|---|---|---|
| PLAN | | Execution scope | |
| PRD | | Product behavior | |
| Architecture | | System-shape constraints | |
| ADR | | Technical decision constraints | |
| Roadmap | | Sequencing / phase scope | |
| AGENTS / repo rules | | Local conventions | |

## Architecture Sensitivity

- `architecture_sensitive`: yes / no
- `architecture_sources_checked`:
- `architecture_constraints_enforced`:
- `architecture_conflicts`: none / list

## Scope Lock

### Changed

-

### Not Changed

-

### Assumptions Used

-

## What Was Implemented

-

## Files Changed

| File | Change | Reason | Source artifact |
|---|---|---|---|
| | | | |

## Plan Fulfillment

| Plan Obligation | Status | Evidence |
|---|---|---|
| | fulfilled / partial / not applicable | |

## Architecture / ADR Compliance

### Architecture Constraints

| Constraint | Status | Evidence |
|---|---|---|
| | satisfied / not relevant / deviated | |

### ADR Constraints

| Constraint | Status | Evidence |
|---|---|---|
| | satisfied / not relevant / deviated | |

## Validation and Tests

### Commands Run

```bash

```

### Results

-

### Validation Not Run

- `not_run_reason`:
- `risk`:
- `recommended_validation_follow_up`:

## Deviations

Use `assets/DEVIATION_REPORT_TEMPLATE.md` format if any deviation occurred.

If none:

- `deviation_status`: none

## Remaining Gaps

| Gap | Urgency | Recommended owner / phase |
|---|---|---|
| | critical / high / medium / low / none | |

## Concrete Next Step

- `next_step_type`: RUN_REVIEW
- `target`: implementation diff and this implementation summary
- `action`: Run `review-phase` against the implementation, `PLAN.md`, relevant architecture, ADRs, and validation evidence.
- `why_this_is_next`: Implementation is complete enough to be independently checked against approved artifacts.
- `blocking_condition`: None if validation passed; otherwise describe the validation gap.
- `suggested_prompt`: "Use review-phase to review this implementation against `PLAN.md`, relevant `ARCHITECTURE.md` sections, ADRs, and validation evidence. Classify findings and provide one concrete next step."
