# Next Step Routing Guide

Every ADR run must end with exactly one `## Concrete Next Step` block.

Do not use legacy terminal fields:

- `Immediate Next Step`
- `Continuation Prompt`
- loose `next_step`
- loose `follow_up`

## Required block

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

## Use `UPDATE_ARCHITECTURE` when

- the ADR changes component boundaries, data ownership, runtime flow, integration pattern, consistency rule, authorization rule, or cross-cutting constraint
- architecture needs an ADR index entry
- architecture currently contradicts the ADR

## Use `CREATE_OR_UPDATE_ROADMAP` when

- the ADR is accepted
- architecture is already updated or no architecture update is needed
- the next problem is delivery sequencing

## Use `CREATE_OR_UPDATE_PLAN` when

- the ADR is accepted
- roadmap is ready or not needed
- exactly one implementation task is now clear

## Use `RETURN_TO_PRD` when

- product behavior or business rule uncertainty blocks the decision

## Use `RETURN_TO_ARCHITECTURE` when

- broad system shape must be defined before one ADR can be written
- architecture conflict must be resolved before accepting the ADR

## Use `REVISE_ADR` when

- the ADR is close but missing drivers, options, consequences, or linkage

## Use `CREATE_SUPERSEDING_ADR` when

- an accepted ADR is no longer valid and the decision has changed

## Use `REQUEST_MISSING_SOURCE_ARTIFACT` when

- a named source artifact is needed but not available

## Use `REQUEST_DECISION_INPUT` when

- missing information is not an artifact but a human decision or constraint

## Use `RETURN_TO_REVIEW` when

- the ADR was created specifically to resolve a review finding and review should be rerun

## Use `START_IMPLEMENTATION` when

- an approved plan already exists and the ADR only removed a final blocker

## Use `STOP_AND_ESCALATE` when

- there is a major source-of-truth conflict or unsafe ambiguity that should not be resolved by the agent alone

## Bad next steps

Avoid vague actions:

- "continue"
- "proceed"
- "fix issues"
- "review later"
- "implement changes"
- "update docs as needed"

Prefer specific actions:

- "Update `ARCHITECTURE.md` section `Data Ownership` to link ADR-0004 and mark `user_product_membership` as the authorization source of truth."
- "Create `ROADMAP.md` phase handoff for notification read model after ADR-0004 is accepted and indexed in `ARCHITECTURE.md`."
- "Revise ADR-0004 to add the rejected alternative for direct Kafka publishing without outbox."
