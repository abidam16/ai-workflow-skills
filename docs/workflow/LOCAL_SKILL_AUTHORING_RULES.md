# Local Skill Authoring Rules

## Purpose

This document prevents workflow skills from repeating the same cross-skill philosophy in every `SKILL.md`.

Local skill files should be small, phase-specific instruction files. Shared workflow rules belong in shared workflow docs.

## Shared sources of truth

Use these docs for global workflow behavior:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` — artifact authority, artifact routing, create/update rules, conflict rules, and architecture-aware workflow order.
- `docs/workflow/HANDOFF_CONTRACTS.md` — required handoff payloads between phases.
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md` — required final `Concrete Next Step` block structure.
- `docs/workflow/NEXT_STEP_TYPES.md` — canonical `next_step_type` values.
- `docs/workflow/ARTIFACT_CONSISTENCY_REVIEW_CONTRACT.md` — pre-implementation artifact-chain review contract, when present.

## Local skill responsibility

Each local skill should define only:

1. what the skill owns
2. when to use it
3. when not to use it
4. minimum inputs
5. phase-specific procedure
6. phase-specific output requirements
7. required final `Concrete Next Step`

## Avoid repeating in every skill

Do not repeat full versions of:

- global artifact authority tables
- full end-to-end workflow diagrams
- long explanations of why architecture exists
- full handoff schemas for other phases
- full `Concrete Next Step` field explanations
- global `next_step_type` enum lists
- generic AI-agent philosophy

Use a short pointer instead.

## Allowed local repetition

Local skills may repeat short routing reminders when they directly affect skill selection.

Examples:

- `prd-writer` may say PRD must not become architecture or roadmap.
- `plan-writer` may say one plan equals one task.
- `implement-task` may say implementation is plan-bound but not allowed to violate upstream artifacts.
- `review-phase` may say review must end with one concrete next action.

## Conflict rule

If a local skill file conflicts with shared workflow docs:

1. Shared workflow docs win for cross-skill policy.
2. The local skill wins only for phase-specific execution details that do not contradict shared policy.
3. If the conflict affects implementation safety, stop and route to `ARTIFACT_CONSISTENCY_REVIEW` or the relevant writer skill.

## Quality target

A good local skill file should be concise enough for repeated agent loading, but specific enough to prevent the agent from performing the wrong phase.

Target local `SKILL.md` size:

- small/simple skill: 80–140 lines
- complex skill: 120–220 lines

Prefer references and assets for detailed examples.
