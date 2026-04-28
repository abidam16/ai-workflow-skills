---
name: roadmap-planner
description: Create or update architecture-aware roadmap documents that translate approved PRD, ARCHITECTURE.md, and ADR constraints into staged delivery structure. Use when delivery sequencing, phase boundaries, dependencies, risks, and plan handoff candidates are needed. Do not use for PRD writing, architecture writing, ADR authoring, one-task planning, implementation, or review.
---

# Roadmap Planner

## Purpose

This skill creates or updates roadmap documents that bridge approved intent and architecture into sequenced delivery phases.

A roadmap must be:

- outcome-driven
- phase-based
- dependency-aware
- architecture-aware
- plan-ready
- explicit about the concrete next step

Use this skill only when the next correct artifact is a roadmap.

## Shared Workflow Docs

Use these shared repo docs as cross-skill sources of truth:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on roadmap-specific work.

Validate that the incoming artifact choice matches the decision matrix. If it does not, stop and route to the correct artifact.

## Core Principle

A roadmap is not a PRD summary, not an architecture document, not an ADR, and not a task list.

A roadmap defines:

- what delivery outcomes should be achieved
- in what sequence
- why that sequence is correct
- which dependencies, risks, and deferrals shape delivery
- which roadmap slice should become the next single-task plan

## Artifact Authority Model

When planning delivery sequence, use this authority order:

1. `PRD.md` / PRD deltas for product truth
2. `ARCHITECTURE.md` / initiative architecture docs for system-shape truth
3. ADRs for decision truth
4. Existing `ROADMAP.md` or initiative roadmap for sequencing truth
5. Existing `PLAN.md` files only as execution history or already-planned slices
6. Codebase only as evidence of current implementation state, not as a replacement for approved artifacts

Do not let roadmap invent upstream truth.

If PRD, architecture, ADR, or existing roadmap conflict, stop and produce a concrete next step to resolve the conflict before creating or updating roadmap phases.

## Architecture-Aware Rule

Architecture is optional to create, but authoritative when present and relevant.

Before drafting or updating a roadmap, check whether the initiative touches architecture-sensitive areas:

- component, module, service, or layer boundaries
- data ownership or source-of-truth rules
- API, integration, event, or messaging boundaries
- transaction, consistency, idempotency, retry, or concurrency rules
- authorization, security, audit, or privacy rules
- observability, deployment, runtime, scheduler, or worker behavior
- migrations, staged rollout, or compatibility constraints

If yes, use relevant architecture sections as sequencing constraints.

If relevant architecture is missing, incomplete, stale, or conflicting, do not invent architecture inside the roadmap. Route to `CREATE_OR_UPDATE_ARCHITECTURE` or `CREATE_OR_UPDATE_ADR` as the concrete next step.

## Supported Outputs

Choose exactly one output mode:

- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `ROUTE_TO_PRD`
- `ROUTE_TO_ARCHITECTURE`
- `ROUTE_TO_ADR`
- `ROUTE_TO_PLAN`
- `INSUFFICIENT_INPUT`

If roadmap is not the correct artifact, stop and state which artifact is needed instead.

## Mode Selection

### Use product-roadmap mode when

- the document is a strategic product index
- the goal is to summarize major active, deferred, completed, or upcoming initiatives
- the document should stay lightweight and durable
- the document is not the main planning artifact for one specific initiative
- multiple initiative roadmaps may be linked from it

### Use initiative-roadmap mode when

- the work is a specific feature, migration, refactor, reliability effort, platform change, or product capability
- the work needs its own phased delivery shape
- architecture or ADR constraints materially affect sequencing
- downstream planning should focus on this initiative directly
- forcing it into a product-level roadmap would reduce clarity

Default to initiative-roadmap mode for substantial executable work.

## Roadmap Readiness Gate

Before creating or updating a roadmap, classify readiness:

- `READY`: product intent and relevant architecture/ADR constraints are clear enough to sequence delivery
- `READY_WITH_ASSUMPTIONS`: sequencing can proceed with explicit assumptions and no unsafe architecture invention
- `BLOCKED_BY_PRD`: product truth is unclear or changed materially
- `BLOCKED_BY_ARCHITECTURE`: system-shape constraints are missing, stale, or conflicting
- `BLOCKED_BY_ADR`: one or more major technical decisions must be recorded before sequencing
- `BLOCKED_BY_CONFLICTING_SOURCES`: upstream artifacts disagree
- `NOT_A_ROADMAP_TASK`: the request belongs to another artifact

If readiness is not `READY` or `READY_WITH_ASSUMPTIONS`, do not produce a normal roadmap. Produce a stop/routing output with a concrete next step.

## Required Thinking Order

Before drafting or updating a roadmap:

1. Confirm the initiative or product scope.
2. Identify whether this is product-roadmap or initiative-roadmap mode.
3. Confirm the delivery objective.
4. Identify upstream product truth from PRD or accepted equivalent.
5. Identify relevant architecture constraints.
6. Identify relevant ADR decisions and unresolved ADR candidates.
7. Classify roadmap readiness.
8. Choose sequencing logic: value-first, dependency-first, risk-first, architecture-foundation-first, rollout-first, or mixed.
9. Define phased delivery slices.
10. Define dependencies, risks, deferrals, and exit criteria.
11. Define plan handoff candidates.
12. End with exactly one concrete next step.

## Sequencing Logic

Roadmap phase order must include rationale. Use one or more sequencing strategies:

- `VALUE_FIRST`: deliver the smallest useful capability first
- `DEPENDENCY_FIRST`: build required foundations before dependent behavior
- `RISK_FIRST`: validate risky assumptions early
- `ARCHITECTURE_FOUNDATION_FIRST`: establish system-shape prerequisites before features
- `MIGRATION_FIRST`: prepare compatibility, data, or runtime migration before new behavior
- `ROLLOUT_FIRST`: sequence around safe release, flags, migration, or adoption
- `OPERABILITY_FIRST`: add logging, metrics, recovery, or supportability before scale

Do not use phase names like “Phase 1: Setup” without explaining why that phase exists now.

## Product-Roadmap Rules

A product roadmap should stay compact.

It should contain:

- product or initiative overview
- strategic themes or capability areas
- active initiatives
- deferred/later initiatives
- completed or already-established initiatives when useful for context
- links to initiative roadmaps
- links to relevant architecture or ADRs only when they shape product sequencing
- high-level sequencing rationale

Do not turn a product roadmap into detailed execution planning.

## Initiative-Roadmap Rules

An initiative roadmap is the main bridge into planning.

It should usually include:

- optional Foundation phase when product, architecture, migration, or operational groundwork is required
- MVP phase
- enhancement or maturity phases only when they represent meaningful staged capability
- cross-cutting concerns
- deferred/later items
- open delivery questions
- plan handoff candidates

Use both a phase label and a meaningful phase title.

Example:

- `Phase 1 — Foundation: Membership Source-of-Truth and Invitation Data Model`
- `Phase 2 — MVP: Invitation Creation and Acceptance Lifecycle`
- `Phase 3 — Enhancement: Notification Read Model and Badge Count`

## Architecture-Aware Phase Design

Each phase must include:

- objective
- why this phase exists now
- product outcome
- architecture constraints used
- ADR constraints used
- key outcomes
- in scope
- out of scope
- dependencies
- risks
- exit criteria
- plan handoff candidates

If a phase depends on an architecture decision not yet documented, mark it as blocked or deferred rather than assuming the decision.

## Create vs Update

Create a new roadmap when:

- the work is a new initiative or new strategic product index
- no existing roadmap cleanly fits the objective
- the work needs a new phased delivery shape
- architecture constraints create a distinct delivery stream
- merging into an older roadmap would reduce clarity

Update an existing roadmap when:

- the objective is the same
- the roadmap already exists and still represents the correct initiative or product scope
- only sequencing, scope, dependencies, risks, deferrals, architecture constraints, or plan handoff candidates changed

Prefer a new roadmap when updating would rewrite history or blur a materially different initiative.

## Handoff to Planning

A roadmap must end in a way that makes the next planning step obvious.

Always include:

- chosen roadmap mode
- roadmap readiness status
- why this roadmap exists
- upstream artifacts used
- architecture constraints that shaped sequencing
- ADR constraints that shaped sequencing
- selected next phase or slice
- exactly one recommended next plan candidate
- what is explicitly not part of the next planning step
- whether architecture or ADR must be updated before planning

## Mandatory Closing Behavior

Every final result must end with `Concrete Next Step`.

Required block:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Allowed `next_step_type` values:

- `CREATE_PLAN`
- `UPDATE_PLAN`
- `SPLIT_INTO_PLANS`
- `CREATE_OR_UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `UPDATE_PRD`
- `REVISE_ROADMAP`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

Do not end with “roadmap is done” or a descriptive summary only.

## Output Requirements

For normal roadmap creation/update, include:

1. `Decision`
2. `Roadmap Mode`
3. `Readiness Status`
4. `Source Artifacts`
5. `Architecture Constraints Used`
6. `ADR Constraints Used`
7. `Roadmap Body`
8. `Plan Handoff Candidates`
9. `Deferred / Not Next`
10. `Concrete Next Step`

For stop/routing output, include:

1. `Decision`
2. `Why roadmap is not the correct next artifact`
3. `Missing or conflicting source`
4. `Correct next artifact`
5. `Concrete Next Step`

## Quality Bar

A good roadmap is:

- outcome-driven
- sequenced with rationale
- explicit about dependencies and risks
- bounded by phase scope
- architecture-aware without becoming architecture
- ADR-aware without duplicating ADRs
- useful for later single-task planning
- concise enough to scan quickly
- stable enough to update without rewriting everything

A weak roadmap is:

- just a feature list
- just a task list
- missing sequencing logic
- missing phase boundaries
- missing exit criteria
- inventing architecture
- ignoring source-of-truth ownership
- mixing roadmap phases with implementation instructions
- ending without a concrete next step

## Reference Files

Use these only when needed:

- `references/SOURCE_OF_TRUTH_GUIDE.md`
- `references/ARCHITECTURE_AWARE_ROADMAP_GUIDE.md`
- `references/ROADMAP_MODE_GUIDE.md`
- `references/PHASE_GUIDE.md`
- `references/QUALITY_BAR.md`
- `references/CREATE_VS_UPDATE.md`
- `references/HANDOFF_GUIDE.md`
- `references/REVIEW_CHECKLIST.md`
- `references/NEXT_STEP_ROUTING_GUIDE.md`
- `assets/ROADMAP_TEMPLATE.md`
- `assets/ROADMAP_DELTA_TEMPLATE.md`
- `assets/ROADMAP_CHANGELOG_TEMPLATE.md`
- `assets/PLAN_HANDOFF_TEMPLATE.md`
- `assets/NEXT_STEP_BLOCK_TEMPLATE.md`
