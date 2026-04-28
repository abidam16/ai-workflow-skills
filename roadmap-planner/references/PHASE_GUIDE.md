# Phase Guide

Each phase should be an outcome slice, not a task bucket.

## Required Phase Fields

- objective
- why this phase exists now
- product outcome
- architecture constraints used
- ADR constraints used
- key outcomes
- in scope
- out of scope
- dependencies
- risks
- exit criteria
- plan handoff candidates

## Good Phase Shape

Good:

```text
Phase 1 — Foundation: Membership Source-of-Truth and Invitation Data Model
```

Why it is good:

- says what foundation is being established
- implies dependency for later behavior
- ties to architecture/data ownership

Weak:

```text
Phase 1 — Setup
```

Why it is weak:

- vague
- not outcome-driven
- cannot be reviewed

## Phase Size

A phase may contain multiple future plans, but it should have one coherent objective.

If a phase contains unrelated objectives, split it.

## Exit Criteria

Exit criteria should prove the phase outcome is complete enough for the next phase.

Good exit criteria:

- membership table is authoritative for authorization checks
- invitation acceptance updates membership transactionally
- notification read model is eventually consistent and observable

Weak exit criteria:

- code is done
- tests pass
- feature implemented
