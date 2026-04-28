---
name: roadmap-planner
description: Create or update product or initiative roadmaps that translate approved PRD, architecture, and ADR constraints into staged delivery sequencing. Use when the next uncertainty is what to build first, next, and later. Do not use for PRD, architecture design, ADR decisions, one-task planning, implementation, or review.
---

# Roadmap Planner

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, roadmap routing, handoff payloads, and the required final next-step block.

## Purpose

Use this skill to convert approved product and technical intent into delivery sequence.

A roadmap answers:

> In what order should the work be delivered, and why?

It must respect PRD, architecture, and ADR constraints without redefining them.

## Use this skill when

Use this skill when:

- brainstorm selected a roadmap create/update decision
- PRD, architecture, or ADRs are stable enough to sequence delivery
- a large initiative needs phases, milestones, dependencies, or readiness gates
- multiple implementation plans are needed but their order is unclear
- review found that completed work no longer matches the intended delivery sequence

## Do not use this skill when

Route elsewhere when the current uncertainty is not sequencing:

- product truth -> `prd-writer`
- system shape -> `architecture-writer`
- one technical decision -> `adr-writer`
- one implementation task -> `plan-writer`
- code changes -> `implement-task`
- conformance checking -> `review-phase`

## Inputs expected

Prefer these inputs when available:

- PRD sections defining scope and success criteria
- root or initiative architecture sections defining constraints and dependencies
- accepted ADRs that affect sequencing
- existing roadmap, if updating
- review findings, implementation summaries, or blockers that affect sequence

If sequencing depends on missing product, architecture, or ADR decisions, stop and route to the missing artifact.

## Procedure

1. Validate that roadmap is the correct artifact using the shared decision matrix.
2. Determine product roadmap vs initiative roadmap.
3. Determine create vs update.
4. Identify delivery outcomes and dependencies.
5. Sequence phases based on value, risk, architecture dependencies, ADR constraints, and implementation readiness.
6. Define phase exit criteria and plan handoff candidates.
7. End with `## Concrete Next Step`.

## Roadmap requirements

A roadmap should normally include:

- status and related artifacts
- roadmap goal
- scope and non-goals
- sequencing principles
- phases or milestones
- dependencies and readiness gates
- risks and assumptions
- architecture and ADR constraints
- plan handoff candidates
- review checkpoints

Use `assets/ROADMAP_TEMPLATE.md` for new roadmaps unless the repo already has a compatible structure.

## Output requirements

Every output must include:

```md
## Roadmap Handoff Summary

- Roadmap path:
- Roadmap type:
- Phases created or changed:
- Architecture constraints applied:
- ADR constraints applied:
- Plan handoff candidates:

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

A good roadmap is:

- outcome-driven
- dependency-aware
- architecture-aware without becoming architecture
- clear about phase boundaries
- ready to generate one-task plans
- concise enough to remain useful during review
