---
name: plan-writer
description: Create or update exactly one implementation plan for exactly one bounded task. Use when product, architecture, ADR, and sequencing context are clear enough to produce an executable PLAN.md. Do not use for brainstorm, PRD, architecture, ADR, roadmap, implementation, review, or multi-task planning.
---

# Plan Writer

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, handoff payloads, next-step values, and architecture-sensitive planning rules.

## Purpose

Use this skill to create one execution contract for one implementation task.

A plan must be concrete enough that an implementation agent can execute without inventing product intent, architecture decisions, ADR decisions, sequencing, or review criteria.

## Non-negotiable rule

One `PLAN.md` covers one independently reviewable implementation task only.

If the requested work contains multiple independent tasks, stop with a split recommendation and identify separate plan candidates.

## Use this skill when

Use this skill when:

- a roadmap phase/slice must become one implementation task
- architecture or ADR output unlocks one bounded implementation task
- review found an issue that needs a corrective plan
- the next step is not coding yet, but a precise implementation contract
- scope, constraints, files, validation, and review criteria need to be made explicit

## Do not use this skill when

Route elsewhere when the current uncertainty is not one implementation task:

- artifact routing -> `brainstorm-gate`
- product truth -> `prd-writer`
- system shape -> `architecture-writer`
- one technical decision -> `adr-writer`
- delivery sequencing -> `roadmap-planner`
- code changes -> `implement-task`
- conformance checking -> `review-phase`

## Inputs expected

Prefer the narrowest valid source chain:

- roadmap slice, architecture section, ADR, or review finding that created the task
- relevant PRD section if product behavior matters
- relevant architecture section if boundaries, data, flows, integrations, security, consistency, or runtime assumptions matter
- relevant ADRs if decisions constrain implementation
- existing `PLAN.md`, if updating
- codebase evidence needed to scope files and validation

If upstream sources conflict or are missing, stop and route to the correct artifact.

## Procedure

1. Validate that plan-writing is the correct phase using the shared decision matrix.
2. Confirm one-task scope.
3. Classify readiness and blockers.
4. Extract binding product, architecture, ADR, and roadmap constraints.
5. Identify affected files/components and non-goals.
6. Define implementation steps, validation, tests, risks, and review checklist.
7. End with `## Concrete Next Step`.

## Plan requirements

A plan should normally include:

- status and source artifacts
- task objective
- scope and non-goals
- binding constraints
- affected files/components
- implementation steps
- validation and tests
- risks and rollback notes, when relevant
- review checklist
- open blockers, if any

Use `assets/PLAN_TEMPLATE.md` for new plans unless the repo already has a compatible structure.

## Output requirements

Every output must include:

```md
## Plan Handoff Summary

- Plan path:
- Task scope:
- Architecture readiness:
- ADR readiness:
- Implementation readiness:
- Validation required:

## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Use canonical `next_step_type` values from `docs/workflow/NEXT_STEP_TYPES.md`.

## Quality bar

A good plan is:

- one-task only
- implementation-ready
- architecture-aware when relevant
- explicit about validation
- strict about non-goals
- easy for `implement-task` to execute and `review-phase` to verify
