---
name: plan-writer
description: Create or update a single-task PLAN.md that translates one roadmap slice or one approved work item into a bounded implementation contract. Use when the next step is to define exactly one executable task with explicit scope, spec, validation, files to change, tests, review checks, risks, and deferred improvements. Do not use for PRD, roadmap, ADR, or multi-task planning.
---

# Plan Writer


## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Validate that the incoming artifact choice matches the decision matrix. Produce outputs that satisfy the shared handoff contract for the next phase.
This skill creates or updates exactly one implementation plan for exactly one task.

## Purpose

Use this skill to convert one approved roadmap slice, one approved follow-up item, or one well-scoped implementation need into a single-task `PLAN.md` that is clear, concise, bounded, and directly usable by a human engineer or implementation agent.

The plan must be an execution contract, not a brainstorm note, roadmap, ADR, or generic to-do list.

## Non-Negotiable Rule

**One plan document covers one task only.**

If the requested work naturally splits into two or more independently reviewable tasks, do not force them into one plan. Either:
- write one plan for the single task that is currently being scoped, or
- stop and explicitly recommend splitting into multiple plans.

## When To Use

Use this skill when:
- product or technical intent is already clear enough
- the next need is to define one executable task
- a roadmap phase, initiative, or approved change must be turned into one bounded implementation contract
- implementation drift risk would be reduced by sharper scope and validation criteria

Do not use this skill when:
- the user still needs product discovery or artifact routing -> use brainstorm
- product truth must be created or updated -> use PRD
- delivery sequencing or phased maturity must be defined -> use roadmap
- one architectural decision must be evaluated and recorded -> use ADR
- the code should already be implemented -> use implementation execution / review workflows

## Create vs Update

Create a new plan when:
- no plan exists yet for this task
- the task is materially different from existing plans
- a split is required and the current task needs its own isolated plan

Update an existing plan only when:
- the task is still the same task
- the objective remains the same
- scope, files, validation, risks, or review expectations need refinement
- new information clarifies the implementation contract without changing the task identity

If the task identity changes, create a new plan instead of mutating the old one.

## Writing Rules

The plan must be:
- single-task only
- concise
- concrete
- bounded
- implementation-oriented
- reviewable
- portable across domains and technology stacks

Avoid project-specific assumptions unless the source artifacts require them.

Do not include:
- broad product history
- roadmap sequencing details beyond what this task needs
- multiple independent tasks
- low-value filler
- vague aspirations
- generic “improve quality” wording without concrete meaning

## Required Sections

The plan should use this shape:

1. Task Summary
2. Objective
3. Scope
   - In Scope
   - Out of Scope
4. Detailed Specification
5. Files / Components to Change
   - Expected Changes
   - Must Not Change
6. Validation and Test
   - Validation
   - Tests
7. Review Checklist
8. Trade-offs and Risks
9. Future Improvements

Read `references/SECTION_GUIDE.md` for the quality standard of each section.

## Split Rule

If the requested work has:
- more than one primary objective
- multiple unrelated validation paths
- multiple unrelated file clusters
- different review criteria
- mixed feature + refactor + migration content
- a natural “and also” structure

then it is probably more than one task.

Follow `references/SPLIT_RULES.md` rather than forcing a combined plan.

## Output Contract

Every run must end with:
1. a clear plan status: `NEW_PLAN`, `PLAN_UPDATE`, or `SPLIT_REQUIRED`
2. the plan body or plan delta
3. a short explanation of why this is the correct plan action
4. the immediate next step

The immediate next step must be explicit, for example:
- implement this plan as a single task
- split into multiple plan documents
- revise the roadmap item first
- clarify one blocking question before implementation

Do not end with a hanging summary that leaves the next action unclear.

## Mandatory Closing Format

End with all of the following:

- `Decision`
- `Why this decision`
- `Plan Status`
- `Immediate Next Step`
- `Continuation Prompt`

Example continuation prompts:
- “Proceed to implement this plan as one bounded task.”
- “Split this work into separate plans before implementation.”
- “Revise the roadmap item first, then regenerate the plan.”

## References

Consult as needed:
- `references/QUALITY_BAR.md`
- `references/CREATE_VS_UPDATE.md`
- `references/SECTION_GUIDE.md`
- `references/SPLIT_RULES.md`
- `references/REVIEW_CHECKLIST.md`

Reusable templates:
- `assets/PLAN_TEMPLATE.md`
- `assets/PLAN_DELTA_TEMPLATE.md`
- `assets/PLAN_CHANGELOG_TEMPLATE.md`
