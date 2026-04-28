---
name: brainstorm-gate
description: Use as the first decision gate for ideas, feature changes, bugs, technical concerns, architecture concerns, roadmap shifts, documentation workflow changes, and product changes. It pressure-tests the request, classifies whether it can use lightweight mode, and routes to exactly one next artifact/action. Do not use it to write full PRDs, architecture docs, ADRs, roadmaps, plans, or implementation code.
---

# Brainstorm Gate

## 1. Purpose

This skill decides what should happen next. It preserves only the minimum context needed by the next phase.

## 2. Shared Workflow Sources

Use these shared workflow docs when present:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LIGHTWEIGHT_TASK_MODE.md`

Use local references only when shared docs are absent.

## 3. Allowed Decisions

Every run must end with exactly one decision:

- `REJECT_OR_DEFER`
- `USE_LIGHTWEIGHT_MODE`
- `NEW_PRD`
- `PRD_UPDATE`
- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`
- `NEW_ADR`
- `ADR_UPDATE`
- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_DOCUMENT_PLAN`
- `DOCUMENT_PLAN_UPDATE`

Do not end with multiple competing next steps.

## 4. Lightweight Mode Gate

Before routing to PRD, Architecture, ADR, Roadmap, or Document Plan, check if the work is eligible for lightweight mode.

Choose `USE_LIGHTWEIGHT_MODE` only when all are true:

- one primary objective
- small/local change
- product behavior is clear or unaffected
- architecture boundaries are clear or unaffected
- no data ownership, source-of-truth, integration, async, transaction, authorization, security, observability, deployment, or performance change
- no ADR-worthy decision
- no roadmap sequencing need
- validation is small and explicit
- review can judge the result against one bounded task

If any condition is uncertain, do **not** use lightweight mode. Route to the full artifact workflow.

## 5. Full Routing Rules

Use PRD when product intent, user-facing behavior, goals, non-goals, scope, rules, or success criteria must be defined or changed.

Use Architecture when system structure, boundaries, ownership, runtime flow, integration map, or cross-cutting constraints must be made durable.

Use ADR when the main unresolved issue is one lasting technical or architectural decision with meaningful alternatives.

Use Roadmap when intent and relevant architecture/ADR constraints are stable enough and the next need is staged delivery sequencing.

Use Document Plan when the accepted work is about producing or refactoring bounded durable documents.

Use Reject/Defer when the idea is weak, premature, low-value, or missing material evidence.

## 6. Output Modes

### `CHAT_ONLY_BRAINSTORM`

Use when no durable artifact is needed. Output a concise decision and `Concrete Next Step`.

### `DURABLE_BRAINSTORM_OUTPUT`

Use when the brainstorm result must be referenced by a downstream skill. Default path:

```text
docs/brainstorm/BRAINSTORM-XXX-<slug>.md
```

### `LIGHTWEIGHT_MODE_CLASSIFICATION`

Use when the request should proceed directly to a lightweight plan. Include the mandatory `Lightweight Classification` section from `docs/workflow/LIGHTWEIGHT_TASK_MODE.md`.

## 7. Required Lightweight Classification

When choosing `USE_LIGHTWEIGHT_MODE`, include:

```md
## Lightweight Classification

- `mode`: LIGHTWEIGHT_TASK
- `reason`:
- `scope`:
- `why_prd_not_needed`:
- `why_architecture_not_needed`:
- `why_adr_not_needed`:
- `why_roadmap_not_needed`:
- `validation_path`:
- `escalation_trigger`:
```

## 8. Mandatory Closing Behavior

Every output must end with exactly one:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

For lightweight mode, use:

- `next_step_type`: `CREATE_PLAN`
- `target`: the lightweight plan path or planned path
- `action`: create a lightweight single-task plan
- `blocking_condition`: the escalation trigger that would exit lightweight mode

## 9. Quality Bar

A good brainstorm output is decision-explicit, artifact-explicit, value-aware, constraint-aware, concise, and routed to exactly one next step.
