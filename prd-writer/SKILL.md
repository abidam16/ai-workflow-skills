---
name: prd-writer
description: Create or update a concise, product-level PRD when product intent, user behavior, business rules, or success criteria need to be defined or changed. Use this after brainstorm selects PRD as the next artifact. Do not use this for roadmap sequencing, one-task execution planning, or purely technical decisions that belong in an ADR.
---

# PRD Writer


## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Validate that the incoming artifact choice matches the decision matrix. Produce outputs that satisfy the shared handoff contract for the next phase.
This skill creates or updates a portable, product-level `PRD.md`.

## Purpose

Use this skill to convert validated product thinking into a stable decision document that is clear enough for roadmap planning, execution planning, implementation, and review.

A good PRD:
- defines product truth, not implementation detail
- states goals and non-goals clearly
- explains current and target behavior
- captures business rules, user flows, success criteria, and open questions
- stays concise enough for repeated use by humans and AI

## Use this skill when

Use this skill when one or more of the following is true:
- a new initiative needs a product-level source of truth
- product intent changed after brainstorming or discovery
- user roles, flows, or business rules changed
- success criteria changed materially
- the current PRD is stale, vague, or missing key product decisions

## Do not use this skill when

Do not use this skill when:
- the next artifact should be a roadmap only
- the issue is a technical architecture decision that belongs in an ADR
- the work is already product-clear and only needs one-task execution planning
- the task is implementation or review

## Inputs expected

Prefer these inputs when available:
- brainstorm output and artifact decision
- existing `PRD.md`, if any
- relevant roadmap context, if the PRD is being updated because of roadmap learning
- relevant ADRs, if technical constraints affect product behavior
- product/business notes, user feedback, bug reports, or decision summaries

If some inputs are missing, infer conservatively and keep unknowns in `Open Product Questions` rather than inventing certainty.

## Output contract

Produce one of:
1. a new `PRD.md`
2. an updated `PRD.md`
3. a compact PRD delta summary when only a change note is requested

Every run must also state:
- whether this was CREATE or UPDATE
- what sections changed or were introduced
- what downstream artifact should happen next
- whether roadmap changes are required
- whether ADR changes are required

## Portable writing rules

Keep the PRD portable across domains and stacks:
- write at product level, not framework level
- avoid naming technology unless it materially changes product behavior or constraints
- avoid environment-specific commands, code paths, or team-specific process unless explicitly required
- write reusable section content that works for frontend, backend, SaaS, healthcare, finance, and internal systems
- put domain-specific compliance or regulation requirements inside product rules, constraints, or success criteria only when they are truly relevant

## Quality rules

Follow these rules strictly:
- keep the PRD concise but concrete
- avoid duplicate content across sections
- separate current behavior from target behavior
- distinguish goals from non-goals
- keep business rules explicit
- keep unresolved uncertainty in `Open Product Questions`
- do not smuggle roadmap sequencing or task-level steps into the PRD
- do not include class names, table schemas, endpoints, or implementation pseudocode unless they are genuinely product-defining constraints

Read `references/QUALITY_BAR.md`, `references/SECTION_GUIDE.md`, and `references/CREATE_VS_UPDATE.md` before drafting or revising a PRD.

## Drafting workflow

1. Confirm that PRD is the correct artifact.
2. Decide CREATE vs UPDATE.
3. Extract product truth:
   - product overview
   - goals
   - non-goals
   - users/roles/actors
   - domains
   - core flows
   - product rules
   - current behavior
   - target behavior
   - known product problems
   - success criteria
   - open questions
   - deferred directions
4. Draft or revise only the sections that need change.
5. Check for product-level clarity and redundancy.
6. State downstream next step explicitly:
   - roadmap creation/update
   - ADR creation/update
   - no further artifact needed yet

## Mandatory next-step behavior

Do not leave the result hanging.
At the end, state:
- `PRD Decision`: CREATE or UPDATE
- `Roadmap Impact`: none / create roadmap / update roadmap
- `ADR Impact`: none / create ADR / update ADR
- `Immediate Next Step`: one concrete next action

## Templates

Use:
- `assets/PRD_TEMPLATE.md` for new PRDs
- `assets/PRD_DELTA_TEMPLATE.md` for update summaries
- `assets/PRD_CHANGELOG_TEMPLATE.md` if a changelog entry is needed
