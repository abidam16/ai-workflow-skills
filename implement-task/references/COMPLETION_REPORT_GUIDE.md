# Completion Report Guide

An `implement-task` completion report must tell the user what was done, what was checked, what remains uncertain, and exactly what should happen next.

## Required completion report qualities

A good completion report is:

- tied to one approved plan
- explicit about source artifacts checked
- explicit about architecture sensitivity
- clear about files changed
- clear about validation performed or not performed
- honest about deviations and residual risk
- ended by exactly one normalized `## Concrete Next Step` block

## Required terminal block

All implementation summaries and blocker reports must end with:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

The final block must be the last section in the report.

## Good examples

```md
## Concrete Next Step

- `next_step_type`: RUN_REVIEW
- `target`: implementation diff, `PLAN.md`, `ARCHITECTURE.md#Notification Flow`, and validation output
- `action`: Run `review-phase` to check this implementation against the approved plan and relevant architecture constraints.
- `why_this_is_next`: The implementation is complete and validation passed; independent review is now the correct enforcement step.
- `blocking_condition`: None.
- `suggested_prompt`: "Use review-phase to review this implementation against `PLAN.md`, relevant architecture sections, ADRs, and validation evidence. Classify findings and provide one concrete next step."
```

```md
## Concrete Next Step

- `next_step_type`: UPDATE_PLAN
- `target`: `PLAN.md`
- `action`: Revise the plan to resolve the conflicting persistence requirements before implementation continues.
- `why_this_is_next`: The current plan conflicts with the architecture source-of-truth rule for membership ownership.
- `blocking_condition`: Implementation must not continue until the plan and architecture agree on the source of truth.
- `suggested_prompt`: "Use plan-writer to update `PLAN.md` so it respects the membership source-of-truth rule in `ARCHITECTURE.md`, then produce one implementation-ready task plan."
```

## Bad examples

Avoid:

```md
Next step: continue development.
```

Avoid:

```md
Immediate Next Step: review this later.
Continuation Prompt: continue.
```

Avoid:

```md
## Concrete Next Step
- `next_step_type`: RUN_REVIEW
- `action`: fix issues
```

The last example is invalid because required fields are missing and the action is vague.
