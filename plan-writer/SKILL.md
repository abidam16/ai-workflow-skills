---
name: plan-writer
description: Create or update one architecture-aware, single-task PLAN.md or lightweight PLAN for one small/local task. Use when the next step is exactly one implementable task with explicit scope, source artifacts, relevant constraints, validation, review checks, and concrete next action. Do not use for PRDs, architecture docs, ADRs, roadmaps, broad multi-task plans, or implementation.
---

# Plan Writer

## 1. Purpose

This skill creates or updates exactly one executable implementation contract.

A plan may be:

- `FULL_PLAN` for normal artifact-driven work
- `LIGHTWEIGHT_PLAN` for small, local, low-risk work that passed lightweight classification

One plan must cover one task only.

## 2. Shared Workflow Sources

Use these shared workflow docs when present:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LIGHTWEIGHT_TASK_MODE.md`

## 3. When to Use

Use this skill when the next action is to produce or update a bounded implementation plan.

Use `LIGHTWEIGHT_PLAN` only when the incoming request includes a valid lightweight classification or the task clearly satisfies the lightweight mode rules.

Use `FULL_PLAN` when the work depends on PRD, architecture, ADR, roadmap, or review findings.

## 4. When Not to Use

Do not create a plan when:

- product behavior is unclear and needs PRD work
- architecture constraints are missing but needed
- one durable technical decision needs ADR
- phased sequencing is needed before task planning
- the task has multiple independent objectives
- implementation is already requested against an approved plan

## 5. Lightweight Plan Gate

Before creating a lightweight plan, verify:

- one primary objective
- small/local scope
- product behavior clear or unaffected
- architecture clear or unaffected
- no ADR-worthy decision
- no roadmap need
- small validation path
- explicit escalation trigger

If any item fails, output a blocking result and route to the correct artifact.

## 6. Required Full Plan Content

A full plan must include:

- source artifacts
- objective
- in scope / out of scope
- architecture constraints when relevant
- ADR constraints when relevant
- affected files/components
- implementation approach
- validation and tests
- risks and assumptions
- review checklist
- concrete next step

## 7. Required Lightweight Plan Content

A lightweight plan must include:

```md
# PLAN: <task title>

## Plan Mode

- `mode`: LIGHTWEIGHT_TASK
- `why_lightweight`: 
- `escalation_trigger`: 

## Objective

## Scope

### In Scope

### Out of Scope

## Existing Behavior

## Target Behavior

## Affected Files / Components

## Implementation Approach

## Validation Checklist

## Risk Check

- `product_risk`: none | low | blocked
- `architecture_risk`: none | low | blocked
- `adr_risk`: none | low | blocked
- `roadmap_risk`: none | low | blocked

## Review Checklist

## Concrete Next Step

- `next_step_type`: IMPLEMENT_PLAN
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

## 8. Split Rule

Split instead of writing one plan when:

- there is more than one primary objective
- validation paths are independent
- files/components belong to unrelated areas
- one part can be completed without the other
- risk or review criteria differ materially

## 9. Escalation Rule

If plan creation exposes missing product truth, architecture constraints, ADR decision, roadmap sequencing, or source conflict, stop and route to the correct artifact using `Concrete Next Step`.

## 10. Mandatory Closing

Every output must end with exactly one `Concrete Next Step` block.
