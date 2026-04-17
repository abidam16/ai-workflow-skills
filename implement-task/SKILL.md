---
name: implement-task
description: Execute one approved task from one existing PLAN.md with strict plan fidelity, scope control, validation, self-check, and explicit deviation/blocker reporting. Use when a single-task plan already exists and the next step is implementation, not re-planning.
---

# implement-task

## Purpose

Implement exactly one approved task from one existing `PLAN.md`.

This skill is a plan-bound execution layer. It does not replace brainstorming, PRD, roadmap, ADR, or plan creation. It assumes the task is already defined and approved.

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Before implementation, verify that the incoming plan handoff satisfies the shared handoff contract. After implementation, produce an implementation summary that satisfies the review handoff contract.

## Use this skill when

Use this skill when all of the following are true:
- there is one existing `PLAN.md` or equivalent single-task plan
- the plan is approved enough to implement
- the current job is coding / implementation
- the work should stay tightly aligned to the plan

## Do not use this skill when

Do not use this skill when:
- the task is still ambiguous or under-specified
- the work spans more than one task
- the plan needs to be created, rewritten, or split first
- the main work is technical decision-making rather than execution
- the main work is independent review rather than implementation

## Core operating rules

1. One plan only.
2. One task only.
3. Extract obligations from the plan before coding.
4. Stay within scope unless a deviation is explicitly required and reported.
5. Do not silently reinterpret the plan.
6. Do not do unrelated refactors.
7. Validate against the plan before claiming completion.
8. If the plan is unsafe, contradictory, or materially incomplete, stop and report the blocker.

## Required execution flow

### 1. Read and extract the plan

Before changing code, explicitly identify from the plan:
- task summary
- objective
- in-scope items
- out-of-scope items
- detailed specification obligations
- files/components expected to change
- files/components that must not change
- validation expectations
- test expectations
- review checklist expectations
- known risks or trade-offs

### 2. Scope lock

Before coding, define the working scope:
- what will be changed
- what will not be changed
- what assumptions are being used

If the plan implies more than one task or more than one coherent change unit, stop and report that the task must be split upstream.

### 3. Implement

Implement only the approved task.

During implementation:
- preserve existing architecture unless the plan explicitly requires structural change
- keep changes minimal and local
- avoid opportunistic cleanup
- do not add unrelated abstractions
- do not silently change contracts
- follow repository conventions and `AGENTS.md`
- follow `EXECUTION_PROTOCOL.md` for non-trivial execution behavior

### 4. Validate

After implementation, validate against the plan:
- objective achieved?
- all in-scope items covered?
- out-of-scope respected?
- detailed specification fulfilled?
- expected files/components changed appropriately?
- tests added/updated/run as required?
- review checklist conditions satisfied?

### 5. Report

Always end with one of these outcomes:
- `IMPLEMENTED`
- `IMPLEMENTED_WITH_REPORTED_DEVIATION`
- `BLOCKED_REQUIRES_PLAN_CLARIFICATION`
- `BLOCKED_REQUIRES_PLAN_SPLIT`
- `BLOCKED_REQUIRES_UPSTREAM_DECISION`

## Mandatory reporting behavior

Do not end with an ambiguous summary.
Always report:
- outcome status
- what was implemented
- files changed
- tests/validation performed
- plan sections fulfilled
- deviations, if any
- remaining gaps classified by urgency
- immediate next step

## Deviation rule

A deviation is allowed only when one of the following is true:
- the plan is internally inconsistent
- the plan is incomplete in a way that blocks safe implementation
- following the plan literally would break correctness, safety, or repository constraints
- a minimal implementation adjustment is required to satisfy the stated objective

If deviating:
- state the exact deviation
- explain why it was necessary
- state the impact
- state whether the plan should be updated

Never hide a deviation.

## Output shape

Use the structure from `assets/IMPLEMENTATION_SUMMARY_TEMPLATE.md`.
If blocked, use `assets/BLOCKER_REPORT_TEMPLATE.md`.

## Additional guidance

For deeper rules, consult:
- `references/QUALITY_BAR.md`
- `references/SCOPE_AND_SPLIT_RULES.md`
- `references/DEVIATION_PROTOCOL.md`
- `references/SELF_CHECK_PROTOCOL.md`
- `references/REVIEW_GAP_CLASSIFICATION.md`
