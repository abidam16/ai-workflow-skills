# Deviation Protocol

## Allowed deviation reasons

A deviation is allowed only when:

- the plan is internally inconsistent
- following the plan literally would break product correctness
- following the plan literally would violate architecture or ADR constraints
- following the plan literally would violate repository constraints
- the plan omits a small implementation detail required to satisfy the objective
- validation reveals a necessary minimal fix inside the same task scope

## Not allowed

Do not deviate because:

- a cleaner refactor is tempting
- another design seems better
- the codebase has unrelated issues
- the scope could be expanded conveniently
- the agent wants to make the implementation more complete than planned

## Deviation classification

Use one of:

- `PLAN_GAP`
- `PLAN_CONFLICT`
- `ARCHITECTURE_CONFLICT`
- `ADR_CONFLICT`
- `REPOSITORY_CONSTRAINT`
- `VALIDATION_CONSTRAINT`
- `MINIMAL_CORRECTION`

## Required deviation report

Every deviation must include:

- exact original instruction or constraint
- actual change made
- why it was necessary
- affected source artifact
- impact on scope
- impact on architecture/ADR compliance
- review implication
- required follow-up

## Follow-up routing

| Deviation type | Typical next step |
|---|---|
| Plan missing detail | `UPDATE_PLAN` if material; otherwise `RUN_REVIEW` with reported deviation |
| Architecture conflict | `UPDATE_ARCHITECTURE` or `UPDATE_PLAN` |
| ADR conflict | `CREATE_ADR`, `UPDATE_ADR`, or `UPDATE_PLAN` |
| Multi-task expansion | `SPLIT_INTO_PLANS` |
| Product ambiguity | `UPDATE_PRD` |
