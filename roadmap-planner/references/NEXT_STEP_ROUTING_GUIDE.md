# Next Step Routing Guide

Every roadmap output must end with exactly one concrete next step.

## Required Block Shape

Use the exact terminal block below:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

The block must appear exactly once in the final output. It must be the final section. Do not also include `Immediate Next Step`, `Continuation Prompt`, loose `next_step`, or loose `follow_up`.

## Allowed Next Step Types

### CREATE_PLAN

Use when one roadmap slice is ready to become a new single-task plan.

### UPDATE_PLAN

Use when an existing plan still represents the correct task but must be adjusted based on roadmap changes.

### SPLIT_INTO_PLANS

Use when the selected roadmap slice contains multiple independent implementation tasks.

### CREATE_OR_UPDATE_ARCHITECTURE

Use when sequencing depends on missing, stale, or conflicting system-shape constraints.

### CREATE_OR_UPDATE_ADR

Use when sequencing depends on one unresolved technical decision with credible alternatives.

### UPDATE_PRD

Use when product behavior, goals, non-goals, roles, flows, or success criteria are unclear or changed.

### REVISE_ROADMAP

Use when the roadmap is internally inconsistent or too broad and needs another roadmap pass.

### REQUEST_MISSING_SOURCE_ARTIFACT

Use when the user did not provide necessary source artifacts and they cannot be found in repo.

### RETURN_TO_REVIEW

Use when roadmap was changed in response to implementation review and should be reviewed again.

### STOP_AND_ESCALATE

Use when forward progress would create unsafe or misleading artifacts.

## Bad Next Steps

Do not use vague next steps such as:

- continue development
- implement the roadmap
- proceed as planned
- review later
- fix issues

Name the exact next artifact or action.
