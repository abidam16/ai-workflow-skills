---
name: brainstorm-gate
description: Route brainstorm output to exactly one next durable artifact or rejection/defer outcome. Use when an idea, discussion, or uncertainty needs classification before PRD, architecture, ADR, roadmap, plan, implementation, or review. Do not use to write the downstream artifact itself.
---

# Brainstorm Gate

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, routing order, create/update rules, handoff payloads, and the required final next-step block.

## Purpose

Use this skill to turn messy brainstorm discussion into one explicit routing decision.

The output must answer:

> What is the single correct next artifact or action?

This skill may summarize reasoning, but it must not create the selected PRD, architecture, ADR, roadmap, plan, implementation, or review report.

## Use this skill when

Use this skill when:

- a new idea has been discussed but the next artifact is unclear
- multiple possible artifacts appear useful and one must be selected
- a user asks what durable document should be created or updated next
- a brainstorm result needs to be preserved as compact handoff context
- downstream work is blocked because the workflow entry point is unclear

## Do not use this skill when

Do not use this skill when the correct next artifact is already explicit and the user wants that artifact written.

Route directly to the relevant skill:

- product truth -> `prd-writer`
- system shape -> `architecture-writer`
- one technical decision -> `adr-writer`
- delivery sequencing -> `roadmap-planner`
- one executable task plan -> `plan-writer`
- implementation -> `implement-task`
- conformance checking -> `review-phase`

## Inputs expected

Prefer these inputs when available:

- brainstorm notes or discussion summary
- existing artifact paths, if any
- known current source-of-truth documents
- explicit user preference or constraint
- uncertainty that must be resolved before continuing

If inputs are incomplete, infer conservatively and keep uncertainty visible.

## Procedure

1. Extract the core idea, problem, motivation, and uncertainty.
2. Identify which artifact type would resolve the current uncertainty.
3. Apply the shared decision matrix.
4. Choose exactly one immediate next artifact/action.
5. Produce a compact handoff payload for that next skill.
6. End with `## Concrete Next Step`.

## Valid decisions

Use the decision names from the shared decision matrix.

Common decisions include:

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
- `REJECT_OR_DEFER`

## Output requirements

Every output must include:

```md
## Brainstorm Decision

- Decision:
- Target artifact/action:
- Why this is the correct next step:
- What is explicitly not next:

## Handoff Payload

- Problem / idea:
- Relevant context:
- Key constraints:
- Open questions:
- Suggested next skill:

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

A good brainstorm-gate output is:

- decisive
- short
- explicit about why this artifact is next
- explicit about what is not next
- useful as handoff context
- free of downstream artifact content
