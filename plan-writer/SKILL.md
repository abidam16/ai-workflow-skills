---
name: plan-writer
description: Create or update one architecture-aware, single-task PLAN.md that translates an approved roadmap slice, architecture change, ADR outcome, review finding, or bounded work item into an executable implementation contract. Use when the next step is exactly one implementable task with explicit scope, upstream source artifacts, architecture constraints, affected files/components, validation, review checks, risks, and concrete next action. Do not use for brainstorm, PRD, architecture creation, ADR creation, roadmap sequencing, implementation, review, or multi-task planning.
---

# Plan Writer

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

This skill creates or updates exactly one implementation plan for exactly one task.

## Purpose

Use this skill to convert one approved roadmap slice, one architecture-backed implementation need, one ADR-enabled follow-up item, one review finding, or one well-scoped work item into a single-task `PLAN.md`.

The plan is an execution contract for an implementation agent or human engineer. It must be concrete enough that implementation can proceed without inventing product intent, architecture decisions, ADR decisions, delivery sequencing, or review criteria.

## Non-negotiable rules

### Rule 1: one plan equals one task

One plan document covers one independently reviewable implementation task only.

If the requested work naturally splits into two or more independently reviewable tasks, do not force them into one plan. Either:

- write one plan for the single task currently being scoped, or
- stop with `SPLIT_REQUIRED` and identify the separate plan candidates.

### Rule 2: architecture is optional to create, but binding when present and relevant

Do not create or redesign architecture in this skill.

But when `ARCHITECTURE.md` or `docs/architecture/<initiative>-architecture.md` exists and is relevant, the plan must carry its constraints forward explicitly.

Relevant architecture includes any upstream rule about:

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
- ADR links that affect the task

### Rule 3: the plan must not invent upstream decisions

If implementation cannot be planned safely because product intent, architecture, or ADR decisions are missing or contradictory, do not pretend the task is ready. Route to the missing artifact.

## When to use

Use this skill when:

- product or technical intent is already clear enough
- the next need is one executable implementation task
- a roadmap phase must be converted into one bounded task
- an architecture section must be converted into one bounded implementation task
- an ADR outcome unlocks one bounded implementation task
- a review finding requires a concrete corrective implementation plan
- implementation drift risk would be reduced by sharper scope, constraints, and validation criteria

Do not use this skill when:

- the idea still needs discovery or artifact routing -> use brainstorm-gate
- product truth must be created or changed -> use PRD writer
- system shape, boundaries, data ownership, or runtime model must be created or changed -> use architecture-writer
- one technical decision must be evaluated and recorded -> use ADR writer
- delivery sequencing across multiple tasks/phases is needed -> use roadmap-planner
- code should be changed now -> use implement-task
- completed work should be judged -> use review-phase

## Source-of-truth order

Read the narrowest valid chain of upstream artifacts before writing the plan.

### For a roadmap-backed task

1. Relevant roadmap phase/slice
2. Relevant `PRD.md` section, if product behavior or business rules affect the task
3. Relevant `ARCHITECTURE.md` or initiative architecture section, if boundaries/data/flow/integration/transaction/security are affected
4. Relevant ADRs, if settled decisions constrain the task
5. Existing codebase conventions only after source artifacts are understood

### For an architecture-backed task

1. Relevant `ARCHITECTURE.md` or initiative architecture section
2. Related ADRs listed by the architecture
3. Relevant PRD section, if product behavior constrains implementation
4. Relevant roadmap section, if sequencing/scope is already defined
5. Existing codebase conventions only after source artifacts are understood

### For an ADR-backed task

1. Relevant ADR
2. Relevant `ARCHITECTURE.md` or initiative architecture section, if the ADR affects system shape
3. Relevant PRD section, if product assumptions are affected
4. Relevant roadmap section, if the task belongs to a planned phase
5. Existing codebase conventions only after source artifacts are understood

### For a review-fix task

1. Review report finding and review status
2. Original `PLAN.md`
3. Relevant `ARCHITECTURE.md` or initiative architecture section, especially for architecture violations
4. Relevant ADRs
5. Relevant PRD or roadmap sections
6. Implementation diff or changed files, only to identify corrective scope

## Architecture readiness gate

Before writing a plan, classify architecture readiness:

- `NOT_RELEVANT` - task does not touch architecture-sensitive areas
- `READY` - relevant architecture exists and gives enough constraints for this task
- `PARTIAL` - relevant architecture exists but one or more implementation-critical rules are ambiguous
- `MISSING` - task is architecture-sensitive but no usable architecture source exists
- `CONFLICTING` - source artifacts contradict each other on architecture-sensitive rules

Proceed to a plan only when readiness is `NOT_RELEVANT` or `READY`.

If readiness is `PARTIAL`, write a plan only for the safe subset if it remains one coherent task. Otherwise route to `ARCHITECTURE_UPDATE`, `CREATE_OR_UPDATE_ADR`, or `UPDATE_PRD`.

If readiness is `MISSING` or `CONFLICTING`, do not write an executable plan. End with a routed next step.

## Create vs update

Create a new plan when:

- no plan exists for this task
- the task is materially different from existing plans
- a roadmap/architecture/ADR/review item needs its own isolated implementation contract
- a split is required and this is one of the resulting bounded tasks

Update an existing plan only when:

- the same task identity remains valid
- the objective remains the same
- new source artifacts clarify scope, constraints, files, validation, risks, or review expectations
- architecture or ADR constraints must be added to an otherwise valid plan
- review feedback requires tightening the implementation contract before rework

Do not update an existing plan when:

- the task identity changed
- the plan now contains multiple independent tasks
- the plan contradicts upstream PRD/architecture/ADR/roadmap truth
- the old plan should remain as historical context

## Required planning procedure

Follow this sequence:

1. Identify the exact requested task or planning target.
2. Identify the upstream source artifacts used.
3. Determine whether this is `NEW_PLAN`, `PLAN_UPDATE`, or `SPLIT_REQUIRED`.
4. Check whether the work is architecture-sensitive.
5. Apply the architecture readiness gate.
6. Extract binding constraints from PRD, architecture, ADRs, roadmap, and review findings.
7. Define one objective and one implementation boundary.
8. State in-scope and out-of-scope work.
9. Define expected files/components to change and must-not-change boundaries.
10. Define validation, tests, and review checks.
11. Identify risks, blockers, and future improvements.
12. End with one concrete immediate next step and continuation prompt.

## Required plan sections

Use this shape for a full plan:

1. `Task Summary`
2. `Plan Status`
3. `Source Artifacts`
4. `Architecture Readiness`
5. `Objective`
6. `Scope`
   - `In Scope`
   - `Out of Scope`
7. `Binding Constraints`
   - `Product / PRD Constraints`
   - `Architecture Constraints`
   - `ADR Constraints`
   - `Roadmap / Sequencing Constraints`
   - `Review-Fix Constraints`, if applicable
8. `Detailed Specification`
9. `Files / Components to Change`
   - `Expected Changes`
   - `Must Not Change`
10. `Implementation Notes`
11. `Validation and Tests`
    - `Validation`
    - `Tests`
12. `Review Checklist`
13. `Trade-offs and Risks`
14. `Deferred Items / Future Improvements`
15. `Concrete Next Step`

Read `references/SECTION_GUIDE.md` for section quality standards.

## Binding constraint rules

The plan must not merely list source artifacts. It must extract the constraints that implementation must obey.

Good:

```md
## Binding Constraints

### Architecture Constraints
- `notification` is a read/display model and must not be used as the authorization source of truth.
- `user_product_membership` is the source of truth for product access.
- Invitation acceptance and membership creation must remain in one database transaction.
```

Bad:

```md
## Source Artifacts
- ARCHITECTURE.md
```

A plan that references architecture but does not extract relevant architecture constraints is incomplete.

## Split rule

If the requested work has any of these signs, it is probably more than one task:

- more than one primary objective
- mixed feature + refactor + migration content
- separate backend and frontend flows with independent validation
- separate schema migration and behavior change that can be reviewed independently
- unrelated file clusters
- unrelated validation paths
- unrelated review criteria
- multiple architecture boundaries changed at once
- multiple ADR-driven decisions being implemented in one plan
- natural “and also” structure

Follow `references/SPLIT_RULES.md` rather than forcing a combined plan.

## Output contract

Every run must end with:

1. `Decision`
2. `Why this decision`
3. `Plan Status`
4. `Architecture Readiness`
5. `Source Artifacts Used`
6. `Immediate Next Step`
7. `Continuation Prompt`

Allowed `Plan Status` values:

- `NEW_PLAN`
- `PLAN_UPDATE`
- `SPLIT_REQUIRED`
- `BLOCKED_BY_PRD`
- `BLOCKED_BY_ARCHITECTURE`
- `BLOCKED_BY_ADR`
- `BLOCKED_BY_ROADMAP`
- `BLOCKED_BY_CONFLICTING_SOURCES`
- `INSUFFICIENT_INPUT`

## Concrete next-step requirement

The immediate next step must be one concrete action, not a vague summary.

Allowed `next_step_type` values:

- `IMPLEMENT_PLAN`
- `SPLIT_INTO_PLANS`
- `UPDATE_PRD`
- `CREATE_OR_UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `UPDATE_ROADMAP`
- `REVISE_PLAN`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

Use this final block exactly:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not end with “the plan is ready” unless the concrete next step tells the user exactly what to run next.

## References

Consult as needed:

- `references/SOURCE_OF_TRUTH_GUIDE.md`
- `references/ARCHITECTURE_AWARE_PLANNING_GUIDE.md`
- `references/SECTION_GUIDE.md`
- `references/SPLIT_RULES.md`
- `references/QUALITY_BAR.md`
- `references/CREATE_VS_UPDATE.md`
- `references/REVIEW_CHECKLIST.md`

Reusable templates:

- `assets/PLAN_TEMPLATE.md`
- `assets/PLAN_DELTA_TEMPLATE.md`
- `assets/PLAN_CHANGELOG_TEMPLATE.md`
- `assets/NEXT_STEP_BLOCK_TEMPLATE.md`
