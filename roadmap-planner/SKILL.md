---
name: roadmap-planner
description: Create or update roadmap documents that translate approved product or technical intent into staged delivery structure. Use this after PRD or ADR is stable enough, or when brainstorm explicitly routes to roadmap. Supports product-roadmap index mode and initiative-roadmap mode. Do not use for PRD writing, ADR authoring, or single-task planning.
---

# Roadmap Planner

## Purpose
This skill creates or updates roadmap documents that bridge approved intent into sequenced delivery phases. A roadmap must be outcome-driven, phase-based, and plan-ready.

Use this skill only when the next correct artifact is a roadmap.

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Validate that the incoming artifact choice matches the decision matrix. Produce outputs that satisfy the shared handoff contract for the next phase.

## Core Principle
A roadmap is not a PRD summary and not a task list. It defines:
- what outcomes should be delivered
- in what sequence
- why that sequence is correct
- what dependencies, risks, and deferrals shape delivery
- what later planning should expand into single-task plans

## Supported Outputs
This skill must choose exactly one output mode:
- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`

If roadmap is not the correct artifact, stop and state which artifact is needed instead.

## Mode Selection
### Use product-roadmap mode when:
- the document is a strategic product index
- the goal is to summarize major active, deferred, completed, or upcoming initiatives
- the document should stay lightweight and durable
- the document is not the main planning artifact for one specific initiative

### Use initiative-roadmap mode when:
- the work is a specific feature, innovation, migration, refactor, reliability effort, or platform initiative
- the work needs its own phased delivery shape
- downstream planning should focus on this initiative directly
- forcing it into an older roadmap would reduce clarity

Default to initiative-roadmap mode for substantial new work.

## Roadmap Quality Bar
A good roadmap must be:
- outcome-driven
- sequenced with rationale
- explicit about dependencies and risks
- bounded by phase scope
- useful for later planning
- concise enough to scan quickly
- stable enough to update without rewriting everything

A weak roadmap is:
- just a feature list
- just a task list
- missing sequencing logic
- missing phase boundaries
- missing exit criteria
- missing deferred work

## Required Thinking Order
Before drafting or updating a roadmap:
1. confirm the initiative or product scope
2. identify whether this is product-roadmap or initiative-roadmap mode
3. confirm the delivery objective
4. identify sequencing logic: value-first, dependency-first, risk-first, rollout-first, or mixed
5. define phased delivery slices
6. define dependencies, risks, and deferrals
7. define what planning should derive next

## Product-Roadmap Rules
A product roadmap should stay compact. It should contain:
- product/initiative overview
- strategic themes or capability areas
- active initiatives
- deferred/later initiatives
- completed or already-established initiatives when useful for context
- high-level sequencing rationale

Do not turn a product roadmap into a detailed execution roadmap.

## Initiative-Roadmap Rules
An initiative roadmap is the main bridge into planning. It should usually include:
- optional Foundation phase when groundwork is required
- MVP phase
- Enhancement phases only when they represent meaningful maturity, not leftover work
- cross-cutting concerns
- deferred/later items
- open delivery questions

Use both a phase label and a meaningful phase title.
Example:
- Phase 1 — MVP: Basic Invitation Creation and Delivery
- Phase 2 — Enhancement: Acceptance Lifecycle and Notification State

## Phase Design Rules
Each phase must include:
- objective
- why this phase exists now
- key outcomes
- in scope
- out of scope
- dependencies
- risks
- exit criteria

Do not write phases that are too vague or too task-like.

## Create vs Update
Create a new roadmap when:
- the work is a new initiative or new strategic product index
- no existing roadmap cleanly fits the objective
- the work needs a new phased delivery shape

Update an existing roadmap when:
- the objective is the same
- the roadmap already exists and still represents the correct initiative/product scope
- only sequencing, scope, dependencies, risks, or deferrals changed

## Handoff to Planning
A roadmap must end in a way that makes the next step obvious.
Always include:
- chosen roadmap mode
- why this roadmap exists
- what later planning should focus on next
- what is explicitly not part of the next planning step
- whether the next recommended step is creating single-task plan documents

## Mandatory Closing Behavior
Every final result must end with:
1. `Decision`
2. `Why this decision`
3. `What planning should do next`
4. `What is explicitly deferred or not next`
5. `Immediate next step`

Do not end with a descriptive roadmap only. Always make the handoff explicit.

## Reference Files
Use these only when needed:
- `references/QUALITY_BAR.md`
- `references/CREATE_VS_UPDATE.md`
- `references/STRUCTURE_GUIDE.md`
- `references/PHASE_GUIDE.md`
- `references/REVIEW_CHECKLIST.md`
- `assets/ROADMAP_TEMPLATE.md`
- `assets/ROADMAP_DELTA_TEMPLATE.md`
- `assets/ROADMAP_CHANGELOG_TEMPLATE.md`
- `assets/PLAN_HANDOFF_TEMPLATE.md`
