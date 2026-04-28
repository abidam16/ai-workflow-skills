---
name: implement-task
description: Execute exactly one approved PLAN.md with strict plan fidelity, architecture/ADR constraint checks, scope control, validation, deviation reporting, and a concrete next-step handoff. Use only when the next step is implementation for one bounded task. Do not use for brainstorm, PRD, architecture, ADR, roadmap, plan creation, review, or multi-task execution.
---

# Implement Task

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on implementation.

## Purpose

Implement exactly one approved task from one existing `PLAN.md` or equivalent single-task plan.

This skill is the execution layer. It must not invent product intent, architecture decisions, ADR decisions, delivery sequencing, or review criteria. It implements the approved plan while preserving upstream source-of-truth constraints.

## Non-negotiable rules

### Rule 1: one plan, one task

Execute one approved implementation plan only.

If the request contains multiple independent tasks, stop with `BLOCKED_REQUIRES_PLAN_SPLIT` and identify the separate task candidates.

### Rule 2: plan-bound, but not plan-blind

The plan is the immediate execution contract, but implementation must not knowingly violate relevant upstream artifacts.

If `PLAN.md` conflicts with relevant `ARCHITECTURE.md`, initiative architecture, ADRs, PRD, or roadmap constraints, do not silently choose. Stop or report a deviation using the deviation protocol.

### Rule 3: architecture is optional to create, but binding when present and relevant

Do not create or redesign architecture in this skill.

But if the task touches any architecture-sensitive area, read and enforce the relevant architecture sections before coding:

- component/module/service boundaries
- data ownership or source of truth
- runtime flow
- API or integration boundary
- sync/async behavior
- event/message flow
- transaction boundary
- consistency model
- authorization/security rule
- observability/runtime/deployment assumption
- ADR links that affect implementation

### Rule 4: no hidden deviations

A deviation is allowed only when required for correctness, safety, repository constraints, or to resolve an explicit contradiction. Every deviation must be reported with impact and next-step routing.

### Rule 5: every run ends with a concrete next step

Do not end with “implementation done”, “review completed”, “continue”, or similar vague wording.

Every implementation summary or blocker report must end with a `Concrete Next Step` block.

## When to use

Use this skill when all of the following are true:

- one existing `PLAN.md` or equivalent single-task plan exists
- the plan is approved enough to implement
- the current job is coding / implementation
- the work should stay tightly aligned to the plan
- upstream architecture/ADR/product constraints are either already embedded in the plan or available to verify when relevant

## Do not use

Do not use this skill when:

- the task is still ambiguous or under-specified -> use `plan-writer`
- the work spans more than one task -> use `plan-writer` to split or create separate plans
- the plan needs to be created, rewritten, or split first -> use `plan-writer`
- product behavior must be decided -> use `prd-writer`
- system shape, boundaries, data ownership, runtime model, or integration design must be created or changed -> use `architecture-writer`
- one technical decision must be evaluated and recorded -> use `adr-writer`
- delivery sequencing is unclear -> use `roadmap-planner`
- completed work should be judged independently -> use `review-phase`

## Source-of-truth order

Before coding, read the narrowest valid source chain.

### Required minimum

1. `PLAN.md`
2. Relevant existing code and repository conventions
3. Tests or validation commands referenced by the plan

### Required when architecture-sensitive

1. `PLAN.md`
2. Relevant `ARCHITECTURE.md` or `docs/architecture/<initiative>-architecture.md` sections
3. Relevant ADRs linked by the plan or architecture
4. Relevant PRD section when product behavior/business rules affect implementation
5. Relevant roadmap section when phase/scope sequencing affects implementation
6. Existing code and repository conventions

### Conflict rule

If artifacts conflict:

- PRD governs product behavior.
- `ARCHITECTURE.md` governs system shape, boundaries, data ownership, runtime flows, and cross-cutting constraints.
- ADRs govern the specific technical decisions they record.
- `ROADMAP.md` governs sequencing and phase scope.
- `PLAN.md` governs the current implementation task only.

If the plan conflicts with a relevant upstream source, do not silently proceed. Use one of:

- `BLOCKED_REQUIRES_PLAN_CLARIFICATION`
- `BLOCKED_REQUIRES_ARCHITECTURE_CLARIFICATION`
- `BLOCKED_REQUIRES_ADR_DECISION`
- `BLOCKED_REQUIRES_UPSTREAM_DECISION`
- `IMPLEMENTED_WITH_REPORTED_DEVIATION`, only when a minimal safe deviation was necessary and fully reported

## Required execution flow

### 1. Read and extract the plan

Before changing code, extract:

- task summary
- objective
- in-scope items
- out-of-scope items
- detailed specification obligations
- files/components expected to change
- files/components that must not change
- binding product constraints
- binding architecture constraints
- binding ADR constraints
- roadmap or sequencing constraints
- validation expectations
- test expectations
- review checklist expectations
- known risks or trade-offs

If the plan lacks enough information to implement safely, stop and produce a blocker report.

### 2. Determine architecture sensitivity

Classify the task:

- `architecture_sensitive`: yes / no
- `architecture_sources_checked`: list source paths or “not relevant”
- `architecture_constraints`: extracted concrete constraints
- `architecture_conflicts`: none or list conflicts

A task is architecture-sensitive when it touches:

- module/service/package boundaries
- data ownership/source of truth
- database schema or persistence rules
- API contracts or integration boundaries
- authorization/security logic
- event publishing, messaging, async workers, schedulers, retries, idempotency
- transaction boundaries or consistency behavior
- observability, audit, deployment, runtime configuration

### 3. Scope lock

Before coding, state the intended scope:

- what will be changed
- what will not be changed
- assumptions used
- source artifacts checked

If the plan implies multiple independent tasks, stop and route to `plan-writer` for split.

### 4. Pre-implementation safety check

Stop before coding if any of these are true:

- plan is internally inconsistent
- plan conflicts with relevant architecture or ADRs
- plan requires a product behavior not defined in PRD
- plan requires an architecture change not approved by architecture
- plan depends on an undecided technical choice that deserves ADR
- implementation would require broader scope than the plan allows
- validation cannot be performed or cannot prove correctness

### 5. Implement

Implement only the approved task.

During implementation:

- preserve relevant architecture constraints
- follow ADR decisions
- keep changes minimal and local
- do not add unrelated abstractions
- do not perform opportunistic cleanup
- do not silently change contracts
- do not bypass source-of-truth data ownership
- do not introduce new sync/async boundaries unless approved
- do not modify unrelated files to make tests pass
- follow repository conventions and `AGENTS.md`
- follow `EXECUTION_PROTOCOL.md` if present for non-trivial execution behavior

### 6. Validate

Validate against both the plan and relevant upstream constraints.

Check:

- objective achieved
- all in-scope items covered
- out-of-scope respected
- detailed specification fulfilled
- expected files/components changed appropriately
- architecture constraints preserved
- ADR constraints preserved
- product behavior preserved
- roadmap phase/scope respected
- tests added/updated/run as required
- validation evidence collected
- review checklist conditions satisfied

If validation cannot be run, state why and classify the residual risk.

### 7. Self-check before reporting

Before final output, perform this self-check:

- Did I implement exactly one task?
- Did I stay inside scope?
- Did I avoid unrelated refactors?
- Did I check architecture if the task was architecture-sensitive?
- Did I preserve source-of-truth ownership?
- Did I preserve transaction/consistency/security rules?
- Did I report every deviation?
- Did I run or explain validation?
- Is the next step concrete and routed?

## Output statuses

End with exactly one status:

- `IMPLEMENTED`
- `IMPLEMENTED_WITH_REPORTED_DEVIATION`
- `BLOCKED_REQUIRES_PLAN_CLARIFICATION`
- `BLOCKED_REQUIRES_PLAN_SPLIT`
- `BLOCKED_REQUIRES_ARCHITECTURE_CLARIFICATION`
- `BLOCKED_REQUIRES_ARCHITECTURE_UPDATE`
- `BLOCKED_REQUIRES_ADR_DECISION`
- `BLOCKED_REQUIRES_UPSTREAM_DECISION`
- `BLOCKED_BY_CONFLICTING_SOURCES`
- `BLOCKED_BY_VALIDATION_FAILURE`

## Mandatory reporting behavior

Always report:

- outcome status
- plan used
- source artifacts checked
- architecture sensitivity result
- architecture/ADR constraints enforced or “not relevant”
- what was implemented
- files changed
- validation/tests performed
- plan sections fulfilled
- deviations, if any
- remaining gaps classified by urgency
- concrete next step

If blocked, do not produce a vague partial summary. Use `assets/BLOCKER_REPORT_TEMPLATE.md`.

If implemented, use `assets/IMPLEMENTATION_SUMMARY_TEMPLATE.md`.

If deviation occurred, include the deviation details from `assets/DEVIATION_REPORT_TEMPLATE.md` inside the implementation summary.

## Deviation rule

A deviation is allowed only when one of the following is true:

- the plan is internally inconsistent
- the plan is incomplete in a way that blocks safe implementation
- following the plan literally would break correctness, safety, architecture constraints, ADR decisions, or repository constraints
- a minimal implementation adjustment is required to satisfy the stated objective

If deviating:

- state the exact deviation
- identify the source artifact affected
- explain why it was necessary
- state the implementation impact
- state the review impact
- state whether the plan, architecture, ADR, or roadmap should be updated

Never hide a deviation.

## Concrete next step requirement

Every output must end with:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Allowed `next_step_type` values:

- `RUN_REVIEW`
- `RUN_VALIDATION`
- `APPLY_MINOR_FIX`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `UPDATE_ROADMAP`
- `UPDATE_PRD`
- `SPLIT_PLAN`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RESOLVE_SOURCE_CONFLICT`
- `STOP_AND_ESCALATE`

## Additional guidance

For deeper rules, consult:

- `references/SOURCE_OF_TRUTH_GUIDE.md`
- `references/ARCHITECTURE_AWARE_IMPLEMENTATION_GUIDE.md`
- `references/EXECUTION_FLOW_GUIDE.md`
- `references/DEVIATION_PROTOCOL.md`
- `references/SCOPE_AND_SPLIT_RULES.md`
- `references/VALIDATION_GUIDE.md`
- `references/COMPLETION_REPORT_GUIDE.md`
- `references/QUALITY_BAR.md`
- `references/NEXT_STEP_ROUTING_GUIDE.md`
