---
name: adr-writer
description: Create, supersede, or update Architecture Decision Records for one meaningful technical or architectural decision. Use when architecture, planning, implementation, or review exposes a lasting choice with real alternatives, trade-offs, consequences, or architecture impact. Do not use for broad system design, PRD scope, roadmap sequencing, task planning, implementation, or review.
---

# ADR Writer

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, ADR-vs-architecture routing, handoff payloads, and the required final next-step block.

## Purpose

Use this skill to record one important technical or architectural decision so future humans and agents understand the decision, alternatives, rationale, consequences, and architecture linkage.

An ADR is narrow but durable. It explains one accepted decision; it does not replace `ARCHITECTURE.md`.

## Use this skill when

Use this skill when:

- brainstorm selected `NEW_ADR` or `ADR_UPDATE`
- architecture identified an ADR candidate
- PRD requirements imply a technical choice with meaningful alternatives
- roadmap or plan-writing is blocked by one unresolved decision
- implementation or review exposed an unrecorded decision
- an accepted decision must be superseded
- a decision materially affects boundaries, data ownership, runtime flow, integration pattern, consistency, authorization, deployment, reliability, or operations

## Do not use this skill when

Route elsewhere when the current uncertainty is not one technical decision:

- product behavior or business rule -> `prd-writer`
- broad system shape or integration design -> `architecture-writer`
- delivery sequencing -> `roadmap-planner`
- one implementation task -> `plan-writer`
- code changes -> `implement-task`
- conformance checking -> `review-phase`

## Inputs expected

Prefer these inputs when available:

- architecture section or ADR candidate that created the decision need
- existing ADRs on related topics
- relevant PRD constraints or product assumptions
- relevant roadmap/plan/review context
- codebase or operational evidence that affects alternatives

If decision drivers or alternatives are not clear enough, stop with a decision-input request instead of fabricating certainty.

## ADR-worthiness gate

Write an ADR only when the decision is lasting, consequential, and likely to guide future work.

Do not write ADRs for trivial implementation choices, local refactors, temporary workarounds, or decisions already fully covered by an accepted ADR.

## Procedure

1. Validate that ADR is the correct artifact using the shared decision matrix.
2. Identify the single decision boundary.
3. Determine create, update, or supersede.
4. Capture context and decision drivers.
5. Compare credible alternatives.
6. Record the chosen option and rationale.
7. Capture consequences and required follow-up.
8. Link back to root or initiative architecture when relevant.
9. End with `## Concrete Next Step`.

## ADR content requirements

An ADR should normally include:

- title and status
- date
- decision scope
- related artifacts
- context
- decision drivers
- options considered
- decision
- rationale
- consequences
- architecture linkage
- follow-up artifacts or implementation constraints

Use `assets/ADR_TEMPLATE.md` for new ADRs unless the repo already has a compatible ADR format.

## Output requirements

Every output must include:

```md
## ADR Handoff Summary

- ADR path:
- Decision status:
- Architecture linkage:
- Required architecture update:
- Roadmap impact:
- Plan readiness:

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

A good ADR is:

- about one decision only
- explicit about alternatives and trade-offs
- linked to architecture when system shape is affected
- clear about consequences
- short enough to be reread during planning and review
