# Handoff Guide

Roadmap must hand off to planning, not implementation.

## Roadmap → Plan Required Payload

- artifact type and status
- roadmap mode
- selected phase or slice
- phase objective
- why this slice is next
- in scope for this slice
- out of scope for this slice
- dependencies
- risks
- exit criteria
- plan handoff candidates
- relevant architecture constraints
- relevant ADR constraints
- final `## Concrete Next Step` block

## Plan Handoff Candidate Required Fields

- task name
- task objective
- why it is one task
- scope boundary
- expected components or layers
- architecture constraints to include
- ADR constraints to include
- validation direction

## Rule

Roadmap may propose several future plan candidates, but it must identify exactly one recommended next candidate.

## Concrete Next Step Rule

Roadmap outputs must identify exactly one next action. The final block must be the last section in the output and must use this exact shape:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use `Immediate Next Step`, `Continuation Prompt`, loose `next_step`, or loose `follow_up` fields.
