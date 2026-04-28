---
name: architecture-writer
description: Create or update root or initiative architecture documents when system shape, component boundaries, data ownership, runtime flows, integration boundaries, consistency rules, or cross-cutting technical constraints need durable definition. Do not use for PRD product truth, one-decision ADRs, roadmap sequencing, task planning, implementation, or review.
---

# Architecture Writer

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, root-vs-initiative routing, handoff payloads, and the required final next-step block.

## Purpose

Use this skill to define durable system-shape truth.

Architecture should explain how approved product intent is supported by system structure, boundaries, ownership, flows, integrations, and cross-cutting constraints.

It should guide many implementation tasks without becoming an implementation plan.

## Use this skill when

Use this skill when:

- brainstorm selected `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE`
- PRD is stable enough but implementation needs system-shape guidance
- multiple modules, services, layers, data models, integrations, or runtime flows are affected
- roadmap or plan-writing is unsafe without boundary or ownership decisions
- implementation or review exposed architecture drift
- an initiative is too large or transitional for only root `ARCHITECTURE.md`

## Do not use this skill when

Route elsewhere when the current uncertainty is not system shape:

- product behavior or business rule -> `prd-writer`
- one bounded technical decision -> `adr-writer`
- delivery sequence -> `roadmap-planner`
- one implementation task -> `plan-writer`
- code changes -> `implement-task`
- conformance checking -> `review-phase`

## Inputs expected

Prefer these inputs when available:

- brainstorm handoff or PRD section that created architecture need
- existing `ARCHITECTURE.md`
- existing initiative architecture documents
- relevant ADRs
- relevant roadmap or plan if architecture is being updated from downstream learning
- codebase structure, module boundaries, integration contracts, runtime constraints, and deployment assumptions

If inputs are incomplete, capture uncertainty in `Open Architecture Questions`. Do not invent settled architecture.

## Procedure

1. Validate that architecture is the correct artifact using the shared decision matrix.
2. Decide root architecture vs initiative architecture.
3. Decide create vs update.
4. Extract stable system-shape constraints from source artifacts and codebase evidence.
5. Identify ADR candidates without writing ADRs.
6. Identify roadmap or plan readiness impact.
7. Write or update the architecture document.
8. End with `## Concrete Next Step`.

## Output modes

Produce exactly one of:

- create root `ARCHITECTURE.md`
- update root `ARCHITECTURE.md`
- create `docs/architecture/<initiative>-architecture.md`
- update an initiative architecture document
- route to PRD, ADR, roadmap, plan, implementation, or review when architecture is not the correct next artifact
- blocker response when required source artifacts are missing

## Architecture content requirements

Architecture documents should normally cover:

- status and related artifacts
- purpose and scope
- system context
- component/module/service boundaries
- data ownership and source-of-truth rules
- important runtime flows
- integration/API/event boundaries
- consistency, transaction, and concurrency rules
- security/authorization rules
- reliability, error handling, and observability constraints
- deployment/runtime assumptions
- linked ADRs and ADR candidates
- implementation rules for agents
- open architecture questions

Use:

- `assets/ARCHITECTURE_TEMPLATE.md` for root architecture
- `assets/INITIATIVE_ARCHITECTURE_TEMPLATE.md` for large initiative architecture

## Output requirements

Every output must include:

```md
## Architecture Handoff Summary

- Architecture scope:
- Architecture path:
- Sections created or changed:
- ADR impact:
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

A good architecture document is:

- boundary-focused
- explicit about data ownership
- specific enough to prevent implementation drift
- concise enough for repeated agent use
- linked to ADRs without duplicating them
- clear about what is settled versus open
