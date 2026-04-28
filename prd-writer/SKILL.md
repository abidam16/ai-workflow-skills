---
name: prd-writer
description: Create or update a concise product-level PRD when product intent, user behavior, business rules, success criteria, or product constraints need durable definition. Use after brainstorm routes to PRD or when downstream work exposes missing product truth. Do not use for architecture design, ADRs, roadmap sequencing, implementation plans, implementation, or review.
---

# PRD Writer

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, routing order, handoff payloads, and the required final next-step block.

## Purpose

Use this skill to convert validated product thinking into `PRD.md` product truth.

The PRD should be clear enough to guide architecture, ADRs, roadmap sequencing, task planning, implementation, and review without becoming those artifacts.

## Use this skill when

Use this skill when:

- brainstorm selected `CREATE_PRD` or `UPDATE_PRD`
- a new initiative needs product-level source of truth
- product intent, user roles, flows, business rules, constraints, or success criteria changed
- architecture, roadmap, plan, implementation, or review is blocked by unclear product truth
- a technical artifact introduced product-facing assumptions that need product validation

## Do not use this skill when

Route elsewhere when the current uncertainty is not product truth:

- system shape, boundaries, data ownership, runtime flows, or integration rules -> `architecture-writer`
- one technical decision and rationale -> `adr-writer`
- delivery sequencing -> `roadmap-planner`
- one implementation task -> `plan-writer`
- code changes -> `implement-task`
- conformance checking -> `review-phase`

## Inputs expected

Prefer these inputs when available:

- brainstorm output and artifact decision
- existing `PRD.md`, if updating
- relevant architecture/ADR/roadmap/plan/review context that exposed product ambiguity
- product notes, user feedback, bug reports, stakeholder decisions, or business constraints

If inputs are missing, infer conservatively and capture uncertainty in `Open Product Questions`.

## Procedure

1. Validate that PRD is the correct artifact using the shared decision matrix.
2. Identify whether the work is `CREATE` or `UPDATE`.
3. Extract product behavior, rules, constraints, and success criteria.
4. Identify downstream impacts without designing downstream artifacts.
5. Write or update the PRD using the local template or existing repo structure.
6. End with `## Concrete Next Step`.

## PRD requirements

A PRD should normally include:

- document status
- product summary
- problem statement
- goals and non-goals
- users / actors / roles
- current behavior
- target behavior
- core user flows
- product rules
- product constraints
- success criteria
- scope boundaries
- open product questions
- architecture impact
- ADR impact
- roadmap impact
- implementation plan readiness

Use `assets/PRD_TEMPLATE.md` for new PRDs unless the repo already has a compatible structure.

For updates, preserve good existing structure and change only sections that need change.

## Output requirements

Every run must produce one of:

1. new `PRD.md`
2. updated `PRD.md`
3. compact PRD delta summary
4. routing/blocker response when PRD is not the correct next artifact

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

Use canonical `next_step_type` values from `docs/workflow/NEXT_STEP_TYPES.md`.

## Quality bar

A good PRD is:

- product-focused
- implementation-neutral
- clear about goals and non-goals
- explicit about rules and constraints
- honest about open questions
- concise enough for repeated agent use
- explicit about whether architecture, ADR, roadmap, or plan should happen next
