---
name: prd-writer
description: Create or update a concise product-level PRD when product intent, user behavior, business rules, success criteria, or product constraints need durable definition. Use after brainstorm routes to NEW_PRD or PRD_UPDATE, or when downstream planning/review finds product truth missing or stale. Do not use for architecture design, ADR decisions, roadmap sequencing, one-task implementation planning, implementation, or review.
---

# PRD Writer

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing, create-vs-update decisions, and authority boundaries across phases.
- `docs/workflow/HANDOFF_CONTRACTS.md` for required input/output fields between brainstorm, PRD, architecture, ADR, roadmap, plan, implementation, and review.

Do not duplicate those shared rules here. Apply them, then focus this skill on product-truth work.

Validate that the incoming artifact choice matches the decision matrix. If the request should go to architecture, ADR, roadmap, plan, implementation, or review instead, do not write PRD content; route explicitly.

## Purpose

Use this skill to convert validated product thinking into a stable product decision document that is clear enough to guide architecture, ADRs, roadmap sequencing, execution planning, implementation, and review.

A good PRD:

- defines product truth, not implementation design
- states goals and non-goals clearly
- explains current and target behavior
- captures users, roles, flows, rules, success criteria, constraints, and open product questions
- identifies architecture impact without designing architecture
- identifies ADR impact without making technical decisions
- identifies roadmap impact without sequencing delivery
- stays concise enough for repeated use by humans and AI agents

## Authority model

Use this authority model:

| Artifact | Authority |
|---|---|
| `BRAINSTORM.md` | Exploration, uncertainty, discarded options, and artifact-routing rationale |
| `PRD.md` | Product behavior, goals, non-goals, user/business rules, constraints, and success criteria |
| `ARCHITECTURE.md` | System shape, component boundaries, data ownership, runtime flows, integration rules, and cross-cutting constraints |
| `docs/architecture/<initiative>-architecture.md` | Deep system design for one large active initiative |
| ADRs | One accepted technical decision and rationale |
| `ROADMAP.md` | Delivery sequencing, phase boundaries, dependencies, and readiness gates |
| `PLAN.md` | One executable implementation contract |

PRD is product truth. It must not become architecture, roadmap, ADR, or task plan.

## Use this skill when

Use this skill when one or more of the following is true:

- brainstorm selected `NEW_PRD` or `PRD_UPDATE`
- a new initiative needs product-level source of truth
- product intent changed after brainstorming, discovery, review, or implementation learning
- user roles, flows, business rules, product constraints, or success criteria changed
- the current PRD is stale, vague, contradictory, or missing product decisions
- downstream architecture, roadmap, plan, implementation, or review is blocked by unclear product truth
- a technical artifact introduced product-facing assumptions that need product validation

## Do not use this skill when

Do not use this skill when:

- the issue is system shape, component boundary, data ownership, runtime flow, integration map, transaction rule, or cross-cutting architecture constraint -> route to `architecture-writer`
- the issue is one technical decision with trade-offs and consequences -> route to `adr-writer`
- the issue is delivery sequencing -> route to `roadmap-planner`
- the issue is one bounded implementation task -> route to `plan-writer`
- the task is implementation -> route to `implement-task`
- the task is conformance checking -> route to `review-phase`

## Inputs expected

Prefer these inputs when available:

- brainstorm output and artifact decision
- existing `PRD.md`, if any
- relevant `ARCHITECTURE.md` or initiative architecture when PRD is being updated because architecture exposed product ambiguity
- relevant ADRs when accepted technical constraints affect product behavior or user-facing limits
- relevant roadmap context when PRD is being updated because sequencing exposed missing product truth
- relevant plan/review output when product ambiguity blocked implementation or review
- product/business notes, user feedback, bug reports, decision summaries, or stakeholder constraints

If inputs are missing, infer conservatively and keep uncertainty in `Open Product Questions`. Do not invent product certainty.

## Output contract

Produce one of:

1. a new `PRD.md`
2. an updated `PRD.md`
3. a compact PRD delta summary when only a change note is requested
4. a routing/blocker response when PRD is not the correct next artifact

Every run must end with `## Concrete Next Step`.

## PRD output requirements

A PRD must include enough product truth for downstream artifacts without becoming those artifacts.

For new PRDs, use `assets/PRD_TEMPLATE.md` unless the repository already has a compatible PRD structure.

For updates, preserve existing section style when it is good enough. Change only sections that need change.

A full PRD should normally include:

- document status
- product summary
- problem statement
- goals
- non-goals
- users / actors / roles
- current behavior
- target behavior
- core user flows
- product rules
- product constraints
- success criteria
- scope boundaries
- architecture impact
- ADR impact
- roadmap impact
- implementation-plan readiness
- open product questions
- concrete next step

## Architecture impact rule

Every PRD run must classify architecture impact.

Allowed values:

- `NONE`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CHECK_EXISTING_ARCHITECTURE`
- `ARCHITECTURE_BLOCKED_BY_PRODUCT_QUESTIONS`

Use `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE` when product requirements imply or change:

- system/module/service boundaries
- data ownership or source-of-truth rules
- authorization model or role semantics
- sync vs async behavior
- messaging/event flow
- transaction/consistency expectations
- integration with external systems
- runtime, observability, reliability, or deployment constraints
- large initiative architecture requiring `docs/architecture/<initiative>-architecture.md`

Do not design those architecture details inside the PRD. State the product need and route to architecture.

Good:

```text
Architecture Impact: CREATE_ARCHITECTURE
Reason: The product requires invitation acceptance to grant membership and notify the target user, but source-of-truth, transaction boundary, and sync/async behavior need durable system design.
```

Bad:

```text
Architecture Impact: Use Kafka, outbox_event, and product_invitation_v2 table.
```

## ADR impact rule

Every PRD run must classify ADR impact.

Allowed values:

- `NONE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `CHECK_EXISTING_ADR`
- `ADR_BLOCKED_BY_PRODUCT_QUESTIONS`

Use ADR impact when the PRD introduces or changes product constraints that require a lasting technical decision. Do not decide the technical option inside the PRD.

## Roadmap impact rule

Every PRD run must classify roadmap impact.

Allowed values:

- `NONE`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`
- `CHECK_EXISTING_ROADMAP`
- `ROADMAP_BLOCKED_BY_PRODUCT_QUESTIONS`

Use roadmap impact when product scope or priority changes delivery sequencing, phase boundaries, dependencies, or milestones.

## Plan readiness rule

Every PRD run must classify implementation-plan readiness.

Allowed values:

- `READY_FOR_ARCHITECTURE`
- `READY_FOR_ADR`
- `READY_FOR_ROADMAP`
- `READY_FOR_PLAN`
- `NOT_READY_PRODUCT_QUESTIONS`
- `NOT_READY_CONFLICTING_ARTIFACTS`

Use `READY_FOR_PLAN` only when product behavior is clear and no architecture, ADR, or roadmap work is required before a one-task plan.

If architecture is needed, prefer `READY_FOR_ARCHITECTURE` over roadmap or plan.

## Conflict handling

If artifacts conflict:

1. Identify the conflict explicitly.
2. Do not silently pick the most convenient artifact.
3. If product behavior is unclear or stale, update PRD.
4. If product truth is stable but system shape is unclear or stale, route to architecture.
5. If one accepted technical decision is missing or stale, route to ADR.
6. If delivery sequencing is stale, route to roadmap.
7. If only task execution details are missing, route to plan.

## Portable writing rules

Keep the PRD portable across domains and stacks:

- write at product level, not framework level
- avoid naming technology unless it materially changes user-visible behavior, compliance, constraints, or business rules
- avoid environment-specific commands, code paths, team rituals, branch names, and implementation details unless explicitly product-defining
- put domain-specific compliance or regulation requirements inside product rules, constraints, or success criteria only when truly relevant
- use stable nouns and definitions so downstream architecture and plan writers do not invent concepts

## Quality rules

Follow these rules strictly:

- keep the PRD concise but concrete
- avoid duplicate content across sections
- separate current behavior from target behavior
- distinguish goals from non-goals
- define users/actors and role semantics explicitly
- make business rules testable
- keep unresolved uncertainty in `Open Product Questions`
- do not smuggle roadmap sequencing into the PRD
- do not smuggle architecture design into the PRD
- do not include class names, table schemas, endpoints, package names, migrations, or pseudocode unless they are genuinely product-defining constraints
- do not create long generic explanations

Read these references before drafting or revising a PRD when relevant:

- `references/SOURCE_OF_TRUTH_GUIDE.md`
- `references/ARCHITECTURE_IMPACT_GUIDE.md`
- `references/SECTION_GUIDE.md`
- `references/CREATE_VS_UPDATE.md`
- `references/QUALITY_BAR.md`
- `references/NEXT_STEP_ROUTING_GUIDE.md`

## Drafting workflow

1. Confirm PRD is the correct artifact using the shared decision matrix.
2. Decide `CREATE_PRD`, `UPDATE_PRD`, `PRD_DELTA_ONLY`, or `ROUTE_ELSEWHERE`.
3. Read available upstream and downstream artifacts.
4. Extract product truth:
   - problem
   - users/roles/actors
   - goals/non-goals
   - current behavior
   - target behavior
   - core flows
   - business/product rules
   - constraints
   - success criteria
   - open questions
5. Identify architecture impact without designing architecture.
6. Identify ADR impact without making ADR decisions.
7. Identify roadmap impact without sequencing roadmap phases.
8. Identify plan readiness without creating a task plan.
9. Draft or revise only necessary sections.
10. Run quality checks.
11. End with `## Concrete Next Step`.

## Mandatory terminal contract

Every response must end with this block:

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

- `CREATE_OR_UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `CREATE_OR_UPDATE_ROADMAP`
- `CREATE_OR_UPDATE_PLAN`
- `RETURN_TO_BRAINSTORM`
- `REQUEST_PRODUCT_DECISION`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `REVISE_PRD`
- `START_IMPLEMENTATION`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

Do not use vague next steps such as:

- continue development
- review later
- proceed as needed
- update docs
- implement the feature

The next step must name the concrete target artifact or action.

## Required closing metadata

Before `## Concrete Next Step`, include:

```md
## PRD Handoff Summary

- `prd_decision`: CREATE_PRD / UPDATE_PRD / PRD_DELTA_ONLY / ROUTE_ELSEWHERE
- `target_prd`:
- `sections_created_or_changed`:
- `architecture_impact`: NONE / CREATE_ARCHITECTURE / UPDATE_ARCHITECTURE / CHECK_EXISTING_ARCHITECTURE / ARCHITECTURE_BLOCKED_BY_PRODUCT_QUESTIONS
- `adr_impact`: NONE / CREATE_ADR / UPDATE_ADR / CHECK_EXISTING_ADR / ADR_BLOCKED_BY_PRODUCT_QUESTIONS
- `roadmap_impact`: NONE / CREATE_ROADMAP / UPDATE_ROADMAP / CHECK_EXISTING_ROADMAP / ROADMAP_BLOCKED_BY_PRODUCT_QUESTIONS
- `plan_readiness`: READY_FOR_ARCHITECTURE / READY_FOR_ADR / READY_FOR_ROADMAP / READY_FOR_PLAN / NOT_READY_PRODUCT_QUESTIONS / NOT_READY_CONFLICTING_ARTIFACTS
```

## Templates

Use:

- `assets/PRD_TEMPLATE.md` for new PRDs
- `assets/PRD_DELTA_TEMPLATE.md` for update summaries
- `assets/PRD_CHANGELOG_TEMPLATE.md` if a changelog entry is needed
- `assets/NEXT_STEP_BLOCK_TEMPLATE.md` for the terminal block
