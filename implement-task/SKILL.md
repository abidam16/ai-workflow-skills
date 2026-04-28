---
name: implement-task
description: Execute exactly one approved PLAN.md with strict plan fidelity, source-artifact checks, scope control, validation, deviation reporting, and concrete next-step handoff. Use only when the next step is implementation for one bounded task. Do not use for brainstorm, PRD, architecture, ADR, roadmap, plan creation, review, or multi-task execution.
---

# Implement Task

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, handoff payloads, conflict handling, and the required final next-step block.

## Purpose

Use this skill to implement exactly one approved task from one `PLAN.md` or equivalent single-task plan.

Implementation is plan-bound, but not allowed to knowingly violate relevant upstream product, architecture, ADR, or roadmap constraints.

## Non-negotiable rules

1. Execute one plan only.
2. Do not expand scope silently.
3. Do not redesign product, architecture, ADRs, roadmap, or plan during implementation.
4. If the plan conflicts with relevant upstream artifacts, stop or report a deviation.
5. Every run must end with `## Concrete Next Step`.

## Use this skill when

Use this skill when:

- one approved implementation plan exists
- the plan is sufficiently specific to execute
- the current job is code/config/test/documentation changes required by that plan
- validation can be performed or clearly reported as unavailable

## Do not use this skill when

Route elsewhere when implementation is not ready:

- task is still ambiguous -> `plan-writer`
- multiple tasks are mixed together -> `plan-writer`
- product truth changed -> `prd-writer`
- architecture must be created or changed -> `architecture-writer`
- one technical decision must be recorded -> `adr-writer`
- delivery order is unclear -> `roadmap-planner`
- completed work should be judged -> `review-phase`

## Inputs expected

Required:

- one `PLAN.md` or equivalent approved single-task plan
- relevant codebase files
- validation commands or expected test strategy, if available

Also read relevant upstream artifacts when the plan or task references them.

If required sources are missing or contradictory, produce a blocker report rather than coding through ambiguity.

## Procedure

1. Read the plan and extract obligations.
2. Check for source-artifact conflicts using the shared decision matrix and handoff contracts.
3. Identify scope, non-goals, files, validation, and risks.
4. Implement the smallest complete change that satisfies the plan.
5. Run or describe validation.
6. Report deviations, blockers, and changed files.
7. End with `## Concrete Next Step`.

## Deviation handling

A deviation must be reported when implementation:

- changes scope
- changes behavior not requested by the plan
- encounters a source-artifact conflict
- requires architecture, ADR, roadmap, or PRD changes
- cannot validate required behavior
- discovers the plan is incorrect or incomplete

Do not hide deviations inside the implementation summary.

## Output requirements

Every implementation summary or blocker report must include:

```md
## Implementation Summary

- Plan executed:
- Status:
- Files changed:
- Behavior changed:
- Validation performed:
- Deviations:
- Blockers:

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

A good implementation is:

- faithful to one plan
- minimal but complete
- source-artifact aware
- validated or honest about missing validation
- explicit about deviations
- ready for `review-phase`
