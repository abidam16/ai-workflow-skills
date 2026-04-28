---
name: implement-task
description: Implement exactly one approved PLAN.md or lightweight PLAN. Use when there is a bounded implementation contract with scope, constraints, validation, and concrete next action. Preserve relevant PRD, architecture, ADR, roadmap, and plan constraints; stop instead of silently expanding scope or resolving upstream conflicts.
---

# Implement Task

## 1. Purpose

This skill executes one approved plan. It is plan-bound, but not plan-blind.

Supported execution modes:

- `FULL_PLAN_IMPLEMENTATION`
- `LIGHTWEIGHT_PLAN_IMPLEMENTATION`

## 2. Shared Workflow Sources

Use these shared workflow docs when present:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LIGHTWEIGHT_TASK_MODE.md`

## 3. Pre-Implementation Checks

Before editing code, extract:

- plan mode
- objective
- in-scope work
- out-of-scope work
- affected files/components
- architecture constraints, if relevant
- ADR constraints, if relevant
- validation checklist
- escalation/deviation triggers

If the plan conflicts with relevant PRD, architecture, ADR, roadmap, or review findings, stop and report the conflict.

## 4. Lightweight Implementation Rules

For `LIGHTWEIGHT_PLAN_IMPLEMENTATION`, implementation must:

- preserve the one-objective scope
- keep changes local and small
- avoid product behavior expansion
- avoid architecture boundary changes
- avoid new ADR-worthy decisions
- avoid roadmap/sequencing work
- run or describe the explicit validation path
- stop if the escalation trigger appears

A lightweight implementation must not silently become a full feature, migration, or architecture-sensitive refactor.

## 5. Escalation Triggers

Stop implementation and report a blocker when:

- the plan is ambiguous
- implementation requires product behavior clarification
- implementation requires architecture boundary/source-of-truth changes
- implementation introduces a durable technical decision
- implementation expands beyond one task
- validation requires broader integration than expected
- relevant source artifacts conflict

## 6. Completion Output

After implementation, produce an implementation summary.

For lightweight mode, include:

```md
## Lightweight Assumptions Check

- `product_behavior_unchanged_or_clear`: true | false
- `architecture_unchanged`: true | false
- `no_adr_decision_introduced`: true | false
- `no_roadmap_need_introduced`: true | false
- `escalation_trigger_hit`: true | false
```

## 7. Mandatory Closing

Every implementation summary, blocker report, or deviation report must end with exactly one:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Use `RUN_REVIEW` after successful implementation. Use `UPDATE_PLAN`, `UPDATE_ARCHITECTURE`, `CREATE_ADR`, `UPDATE_PRD`, or `STOP_AND_ESCALATE` when implementation reveals upstream gaps.
