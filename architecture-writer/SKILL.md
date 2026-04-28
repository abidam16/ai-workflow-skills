---
name: architecture-writer
description: Create or update root ARCHITECTURE.md or docs/architecture/<initiative>-architecture.md when system shape, component/module/service boundaries, data ownership, integration flows, runtime model, or cross-cutting technical constraints need durable documentation. Use after brainstorm routes to NEW_ARCHITECTURE/ARCHITECTURE_UPDATE or when approved PRD/ADR context requires architecture. Do not use for product scope, one-decision ADRs, delivery roadmaps, or single-task PLAN.md.
metadata:
  author: abidam16
  version: "1.0"
  workflow_stage: architecture
---

# Architecture Writer

## Purpose

Create or update durable architecture documentation that translates approved product intent into system-level implementation constraints.

This skill writes architecture documents, not product documents, ADRs, roadmaps, task plans, or implementation code.

A good architecture document answers:

> Given the approved product or technical intent, how is the system shaped, how do its parts interact, what constraints must implementation obey, and which decisions are already settled?

## Shared Workflow Docs

Use these shared repo docs as cross-skill sources of truth when they exist:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`

Do not duplicate the shared workflow rules. Apply them, then focus this skill on architecture-specific work.

If the shared docs do not exist, use this skill's local references:

- `references/CREATE_VS_UPDATE.md`
- `references/ROOT_VS_INITIATIVE.md`
- `references/STRUCTURE_GUIDE.md`
- `references/BOUNDARY_GUIDE.md`
- `references/QUALITY_BAR.md`
- `references/HANDOFF_GUIDE.md`
- `references/REVIEW_CHECKLIST.md`

## Core Principle

`ARCHITECTURE.md` is the durable system-shape source of truth.

It should be:

- stable enough to guide many tasks
- specific enough to prevent implementation drift
- concise enough to be repeatedly consumed by humans and coding agents
- explicit about boundaries, ownership, runtime flows, constraints, and open questions

## Use This Skill When

Use this skill when the next correct artifact is architecture.

Common triggers:

- brainstorm selected `NEW_ARCHITECTURE` or `ARCHITECTURE_UPDATE`
- PRD is stable enough but implementation would drift without system-level guidance
- a repo/product needs a canonical `ARCHITECTURE.md`
- a large initiative needs its own architecture document
- component, module, service, package, or layer boundaries must be clarified
- data ownership or source-of-truth rules must be made durable
- sync/async integration flows must be documented
- transaction, consistency, idempotency, retry, observability, deployment, or security rules must guide future tasks
- multiple future `PLAN.md` files need the same system-level context

## Do Not Use This Skill When

Do not use this skill when:

- product intent, user behavior, scope, or success criteria are still unclear -> use PRD
- the question is one bounded technical decision with alternatives -> use ADR
- the next need is phased delivery sequencing -> use roadmap
- the next need is one executable implementation task -> use PLAN
- the user asks to implement code -> use implementation workflow
- the user asks to review completed work -> use review workflow
- the requested change is local, obvious, and does not create durable architectural constraints

## Architecture vs Nearby Artifacts

Use the boundary rules in `references/BOUNDARY_GUIDE.md`.

Short version:

- PRD defines product truth.
- Architecture defines system shape.
- ADR records one decision and why.
- Roadmap defines delivery sequence.
- PLAN defines one task contract.
- Implementation changes code.
- Review checks whether implementation obeys approved artifacts.

## Output Modes

Choose exactly one output mode:

- `CREATE_ROOT_ARCHITECTURE`
- `UPDATE_ROOT_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `ROUTE_TO_PRD`
- `ROUTE_TO_ADR`
- `ROUTE_TO_ROADMAP`
- `ROUTE_TO_PLAN`
- `INSUFFICIENT_INPUT`

If architecture is not the correct next artifact, stop and route to the correct artifact instead.

## Path Conventions

Use these default paths:

```text
ARCHITECTURE.md
docs/architecture/<initiative-slug>-architecture.md
docs/architecture/archive/<initiative-slug>-architecture.md
```

Use root `ARCHITECTURE.md` as the canonical architecture entry point for the repo/product.

Use initiative architecture documents only when the initiative is large enough to need deeper, transitional, or multi-component design detail.

See `references/ROOT_VS_INITIATIVE.md`.

## Inputs Expected

Prefer these inputs when available:

- brainstorm output and artifact decision
- existing `ARCHITECTURE.md`, if any
- related initiative architecture documents, if any
- relevant `PRD.md`
- relevant ADRs
- relevant roadmap context
- existing codebase structure when updating architecture against reality
- API contracts, schema files, diagrams, deployment notes, or operational notes when relevant

If some inputs are missing, infer conservatively and record uncertainty in `Open Architecture Questions`.

Do not invent certainty.

## Required Analysis Before Writing

Before creating or updating architecture:

1. Confirm architecture is the correct artifact.
2. Decide root vs initiative architecture.
3. Decide create vs update.
4. Identify source artifacts and authority order.
5. Extract stable product or technical intent.
6. Identify affected components, modules, services, data stores, integrations, and runtime flows.
7. Identify source-of-truth data ownership rules.
8. Identify sync vs async boundaries.
9. Identify transaction, consistency, idempotency, retry, and failure rules.
10. Identify security, authorization, observability, deployment, performance, and operational constraints.
11. Identify settled ADRs and missing ADR candidates.
12. Draft only durable architecture content.
13. Explicitly route follow-up work.

## Writing Rules

Architecture content must:

- define current or target system shape
- define ownership and boundaries
- describe important runtime flows
- preserve source-of-truth rules
- make implementation constraints explicit
- link to ADRs instead of duplicating them
- separate accepted design from open questions
- be concise and navigable
- avoid generic textbook explanations
- avoid task-level implementation detail

Do not include:

- product goals or user stories except as brief context
- full PRD sections
- full ADR decision history
- delivery phases or milestone sequencing
- one-task implementation steps
- detailed migration scripts
- class-by-class design
- endpoint-by-endpoint API documentation unless architecture-critical
- speculative diagrams or components not justified by source artifacts

## Root Architecture Rules

Use or update root `ARCHITECTURE.md` when documenting canonical repo/product architecture.

The root file should contain stable rules that apply across many future tasks:

- system context
- module/service/component boundaries
- data ownership
- integration boundaries
- cross-cutting constraints
- active initiative architecture links
- ADR index
- implementation rules for agents
- open architecture questions

Use `assets/ARCHITECTURE_TEMPLATE.md` for new root architecture documents.

## Initiative Architecture Rules

Use an initiative architecture document when the work is too large, transitional, or multi-component for root `ARCHITECTURE.md`.

Typical examples:

- notification/invitation system
- outbox/event publishing
- monolith-to-microservice migration
- authentication or authorization model redesign
- frontend design-system architecture
- report-template engine architecture
- OpenAPI contract workflow
- database ownership restructuring

Use `assets/INITIATIVE_ARCHITECTURE_TEMPLATE.md`.

The root `ARCHITECTURE.md` must link active initiative architecture documents. When an initiative becomes stable, fold permanent rules back into root architecture and archive the initiative document.

## Create vs Update Rules

Read `references/CREATE_VS_UPDATE.md`.

Default behavior:

- Create when no correct architecture document exists.
- Update when the same architecture scope already exists and remains authoritative.
- Create initiative architecture when the design is large enough to need isolated depth.
- Do not rewrite ADRs as architecture history.
- Do not mutate root architecture to contain temporary delivery detail.

## Mandatory Output Contract

Every run must produce one of:

1. a new architecture document
2. an updated architecture document
3. a compact architecture delta summary
4. a routing note explaining why another artifact is correct
5. an insufficient-input note with the minimum missing inputs

Every final result must end with:

```text
Decision:
Architecture Scope:
Architecture Path:
Why this decision:
Sections created or changed:
ADR Impact:
Roadmap Impact:
Plan Readiness:
Immediate Next Step:
Continuation Prompt:
```

Allowed `ADR Impact` values:

- `none`
- `create ADR`
- `update/supersede ADR`
- `review existing ADRs`

Allowed `Roadmap Impact` values:

- `none`
- `create roadmap`
- `update roadmap`
- `review roadmap`

Allowed `Plan Readiness` values:

- `ready for PLAN`
- `not ready - needs PRD`
- `not ready - needs ADR`
- `not ready - needs roadmap`
- `not ready - unresolved architecture questions`

## Templates

Use these assets:

- `assets/ARCHITECTURE_TEMPLATE.md` for root architecture
- `assets/INITIATIVE_ARCHITECTURE_TEMPLATE.md` for large initiative architecture
- `assets/ARCHITECTURE_DELTA_TEMPLATE.md` for update summaries
- `assets/ARCHITECTURE_CHANGELOG_TEMPLATE.md` when a changelog entry is useful
- `assets/ARCHITECTURE_INDEX_ENTRY_TEMPLATE.md` when linking initiative architecture from root

## Validation

Before finalizing, check against:

- `references/QUALITY_BAR.md`
- `references/REVIEW_CHECKLIST.md`

If you edited or created a file and the environment allows scripts, optionally run:

```bash
python architecture-writer/scripts/check_architecture_doc.py ARCHITECTURE.md
```

or:

```bash
python architecture-writer/scripts/check_architecture_doc.py docs/architecture/<initiative-slug>-architecture.md
```

Do not fail the task only because the script is unavailable.
