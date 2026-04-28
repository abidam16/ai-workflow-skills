# Next Step Routing Guide

Every `implement-task` output must end with exactly one normalized `## Concrete Next Step` block.

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

## Selection rule

Choose the one next action that unblocks the workflow first.

Do not list several next steps. If multiple follow-ups are useful, mention only the most immediate one in the block and explain secondary follow-up only when needed in `why_this_is_next`.

## Allowed local next_step_type values

| `next_step_type` | Use when | Typical target |
|---|---|---|
| `RUN_REVIEW` | Implementation is complete enough for independent review. | Implementation diff, summary, `PLAN.md`, architecture/ADR evidence |
| `RUN_VALIDATION` | Implementation is complete but validation was not run or needs to be rerun before review. | Test command, build command, validation suite |
| `APPLY_MINOR_FIX` | A small implementation correction is needed before review. | Specific file/function/change |
| `UPDATE_PLAN` | The plan is incomplete, unclear, or no longer matches the safe implementation path. | `PLAN.md` |
| `UPDATE_ARCHITECTURE` | The implementation exposes a required architecture update or an architecture conflict. | `ARCHITECTURE.md` or `docs/architecture/<initiative>-architecture.md` |
| `CREATE_OR_UPDATE_ADR` | A technical decision is required or changed. | `docs/adr/<decision>.md` |
| `UPDATE_ROADMAP` | Delivery sequencing or phase scope must change. | `ROADMAP.md` |
| `UPDATE_PRD` | Product behavior or business rule must be clarified or changed. | `PRD.md` |
| `SPLIT_PLAN` | The implementation request contains multiple independent tasks. | `PLAN.md` or new plan candidates |
| `REQUEST_MISSING_SOURCE_ARTIFACT` | Required source artifact is missing. | Missing PRD / architecture / ADR / roadmap / plan |
| `RESOLVE_SOURCE_CONFLICT` | Source artifacts conflict and implementation cannot safely proceed. | Conflicting artifacts |
| `STOP_AND_ESCALATE` | The issue cannot be safely resolved by this workflow step. | Specific blocker or decision owner |

## Preferred mappings

### Successful implementation

Use `RUN_REVIEW` when:

- implementation is complete
- validation is either passed or the residual validation gap is clearly reported
- no blocking source-artifact conflict remains

### Validation gap

Use `RUN_VALIDATION` when:

- implementation is likely complete
- tests/builds were not run
- running validation is the most immediate useful next step

### Small known implementation defect

Use `APPLY_MINOR_FIX` when:

- a localized issue remains
- the fix is still inside the same plan scope
- review would be premature before applying it

### Plan problem

Use `UPDATE_PLAN` when:

- the plan is incomplete
- the plan is internally inconsistent
- the plan does not include necessary architecture/ADR constraints
- the actual safe implementation path differs from the approved plan

### Architecture problem

Use `UPDATE_ARCHITECTURE` when:

- the implementation exposes an architecture gap
- the plan requires structural change not approved by architecture
- source-of-truth/data ownership/runtime-flow rules are unclear

### ADR problem

Use `CREATE_OR_UPDATE_ADR` when:

- a non-trivial technical decision blocks implementation
- implementation requires changing or superseding an accepted decision

### Source conflict

Use `RESOLVE_SOURCE_CONFLICT` when:

- PRD, architecture, ADR, roadmap, and/or plan conflict
- the agent cannot safely determine which source to follow within this skill

## Anti-patterns

Do not use vague actions such as:

- continue
- continue development
- fix issues
- update docs as needed
- review later
- implementation complete

Do not use old terminal fields:

- `Immediate Next Step`
- `Continuation Prompt`
- loose `next_step`
- loose `follow_up`
