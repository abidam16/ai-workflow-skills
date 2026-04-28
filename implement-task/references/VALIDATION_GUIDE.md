# Validation Guide

## Validation goal

Validation must prove the implementation satisfies:

- the plan objective
- in-scope requirements
- relevant product behavior
- architecture constraints
- ADR constraints
- out-of-scope protection

## Preferred evidence

Use the strongest available evidence:

1. automated tests requested by the plan
2. focused new/updated tests for the changed behavior
3. build/lint/typecheck commands
4. migration validation when schema changes are involved
5. manual verification steps when automation is unavailable
6. static inspection only as a last resort

## Architecture-aware validation examples

- Source-of-truth rule preserved by checking service/repository usage.
- Transaction boundary validated by inspecting transactional method or integration test.
- Async behavior validated by outbox/event record creation rather than direct side effect.
- Authorization rule validated with positive and negative tests.
- API boundary validated with contract or controller tests.

## Reporting validation gaps

If validation is not run, report:

- exact command not run
- reason
- risk level
- what should be run next
- whether review can proceed safely

## Validation failure

If validation fails:

- fix only if the fix is inside task scope
- otherwise stop with `BLOCKED_BY_VALIDATION_FAILURE`
- include failure details and concrete next step
