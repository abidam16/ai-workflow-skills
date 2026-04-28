# implement-task

Executes exactly one approved implementation plan with strict plan fidelity, architecture/ADR constraint checks, validation, deviation reporting, and a normalized `Concrete Next Step` handoff.

## This patch scope

This update only normalizes the terminal next-step contract for `implement-task`.

It preserves:

- one-plan-one-task execution
- architecture-aware implementation checks
- plan-bound execution behavior
- blocker/deviation reporting
- validation and review handoff behavior

## Required terminal block

Every implementation summary, blocker report, or deviation-bearing report must end with exactly one:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use:

- `Immediate Next Step`
- `Continuation Prompt`
- loose `next_step`
- loose `follow_up`

## Typical next step

For successful implementation, the usual next step is:

```md
- `next_step_type`: RUN_REVIEW
```

For blocked implementation, route to the artifact or decision that must be fixed first.
