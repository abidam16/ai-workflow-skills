# Artifact Decision Matrix

This document defines how AI workflow skills choose the next durable artifact or action.

## Core rule

Do not create every artifact every time.

Choose exactly one immediate next artifact/action that resolves the current uncertainty.

## Artifact authority model

| Artifact | Authority |
|---|---|
| `BRAINSTORM.md` | Historical exploration and routing context only |
| `PRD.md` | Product behavior, scope, user value, business rules, success criteria |
| `ARCHITECTURE.md` | Canonical system-shape truth for the repo/product |
| `docs/architecture/<initiative>-architecture.md` | Deep system-shape truth for a large active initiative |
| `docs/adr/*.md` | One accepted technical/architectural decision and its consequences |
| `ROADMAP.md` | Delivery sequencing, phases, dependencies, exit criteria |
| `PLAN.md` | One bounded implementation task execution contract |
| Implementation summary | What actually changed and what validation was done |
| Review report | Conformance assessment and exactly one concrete next step |

## Preferred artifact flow

```text
BRAINSTORM
-> PRD
-> ARCHITECTURE
-> ADR
-> ROADMAP
-> PLAN
-> IMPLEMENTATION
-> REVIEW
```

This order is conceptual, not mandatory. Skip artifacts that are not needed for the current uncertainty.

## Routing rules

### Route to PRD

Choose PRD when the uncertainty is product behavior, user value, product scope, success criteria, workflow, or business rule.

### Route to Architecture

Choose architecture when the uncertainty is system shape, component boundaries, data ownership, runtime flow, integration boundary, transaction/consistency rule, security/authorization model, observability, deployment/runtime assumption, or architecture-sensitive UI/system boundary.

### Route to ADR

Choose ADR when one bounded technical or architectural decision has meaningful alternatives, durable consequences, and should be recorded for future readers.

### Route to Roadmap

Choose roadmap when product, architecture, and decision intent are stable enough, and the remaining uncertainty is delivery sequencing.

### Route to Plan

Choose plan when one bounded implementation task is ready to be specified.

### Route to Implementation

Choose implementation only when a valid plan exists and relevant PRD, architecture, ADR, and roadmap constraints are not missing or contradictory.

### Route to Review

Choose review when implementation evidence exists, or when artifact consistency must be checked before implementation continues.

## Review-mode decision matrix

| Review target | Review mode |
|---|---|
| One implementation against one approved plan | `TASK_REVIEW` |
| Multiple completed tasks against one roadmap or roadmap slice | `ROADMAP_IMPLEMENTATION_REVIEW` |
| PRD, architecture, ADR, roadmap, and/or plan consistency before implementation | `ARTIFACT_CONSISTENCY_REVIEW` |
| Mixed or unclear scope | Split the review or choose `SPLIT_REVIEW_SCOPE` as the next step |

## `ARTIFACT_CONSISTENCY_REVIEW`

Use this mode before implementation or before continuing implementation when multiple durable artifacts exist and may be inconsistent.

It checks:

1. PRD -> Architecture
2. Architecture -> ADRs
3. Architecture / ADRs -> Roadmap
4. PRD / Architecture / ADRs / Roadmap -> PLAN
5. Handoff completeness
6. Implementation readiness

It must not create or rewrite artifacts. It only identifies gaps and routes to exactly one next artifact/action.

## Conflict routing

When artifacts conflict, route to the highest-authority artifact that must change first.

| Conflict | Next step |
|---|---|
| product behavior is unclear or contradicted | `UPDATE_PRD` |
| architecture is required but missing | `CREATE_ARCHITECTURE` |
| system-shape truth is outdated or contradicted | `UPDATE_ARCHITECTURE` |
| one durable technical decision is missing | `CREATE_ADR` |
| recorded decision is stale or contradicted | `UPDATE_ADR` |
| delivery sequence violates dependencies | `UPDATE_ROADMAP` |
| plan violates upstream source artifacts | `UPDATE_PLAN` |
| source artifacts required for fair review are missing | `REQUEST_MISSING_SOURCE_ARTIFACT` |
| review target is too broad or mixed | `SPLIT_REVIEW_SCOPE` |

## Concrete next step requirement

Every phase output must end with exactly one `Concrete Next Step` block.

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```
