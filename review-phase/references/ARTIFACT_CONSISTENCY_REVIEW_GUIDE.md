# Artifact Consistency Review Guide

`ARTIFACT_CONSISTENCY_REVIEW` is a pre-implementation or pre-continuation review mode.

Use it to verify that durable artifacts agree with each other before an agent implements, continues implementation, or starts the next plan.

## Purpose

The mode answers:

> Are PRD, architecture, ADRs, roadmap, and PLAN mutually consistent enough for safe implementation?

It does not create, rewrite, or repair those artifacts directly. It identifies the highest-value next correction and routes to exactly one next step.

## When to use

Use this mode when:

- the user asks to review multiple durable artifacts together
- a `PLAN.md` is about to be implemented and upstream consistency is uncertain
- architecture or ADR changes may have invalidated roadmap or plan
- review after implementation exposed artifact conflicts
- the artifact chain feels too broad, duplicated, or unclear for Codex to execute safely
- the next action is unclear because several artifacts appear stale or contradictory

Do not use it when:

- the user wants to review actual code against an approved plan -> use `TASK_REVIEW`
- the user wants to review completed tasks against roadmap delivery -> use `ROADMAP_IMPLEMENTATION_REVIEW`
- the user wants to create or update PRD, architecture, ADR, roadmap, or plan -> route to the relevant writer skill

## Source order

Read artifacts in this order:

1. shared workflow docs, if available
2. brainstorm/handoff only as historical context
3. PRD
4. root or initiative architecture
5. ADRs
6. roadmap
7. plan files or plan candidates
8. implementation summaries only when they expose drift relevant to future artifacts

## Consistency checks

### PRD to Architecture

Check whether product behavior has enough system-shape support.

Common findings:

- PRD requires behavior that architecture does not support
- architecture introduces constraints not justified by PRD
- product rule is split between PRD and architecture inconsistently
- architecture is missing for an architecture-sensitive feature

### Architecture to ADR

Check whether major decisions are recorded and reflected.

Common findings:

- architecture states a lasting decision but no ADR exists
- ADR contradicts current architecture
- ADR consequence is missing from architecture
- obsolete ADR is still treated as active

### Architecture/ADR to Roadmap

Check whether delivery sequencing respects technical dependencies.

Common findings:

- roadmap implements UI before required source-of-truth foundation
- roadmap skips migration or integration prerequisites
- roadmap ignores an ADR consequence
- roadmap phase exit criteria are not architecture-aware

### Roadmap/Source Artifacts to Plan

Check whether the plan is a valid one-task execution contract.

Common findings:

- plan is too broad
- plan uses the wrong source of truth
- plan bypasses architecture constraints
- plan includes product or architecture decisions that belong upstream
- plan does not map to roadmap slice

## Output standard

The report must end with exactly one `Concrete Next Step` block.

Choose the next step by highest-authority unresolved issue:

1. Product truth issue -> `UPDATE_PRD`
2. Missing architecture -> `CREATE_ARCHITECTURE`
3. Architecture truth issue -> `UPDATE_ARCHITECTURE`
4. Missing decision record -> `CREATE_ADR`
5. Decision contradiction -> `UPDATE_ADR`
6. Sequencing issue -> `UPDATE_ROADMAP`
7. Execution-contract issue -> `UPDATE_PLAN`
8. Missing source -> `REQUEST_MISSING_SOURCE_ARTIFACT`
9. Scope too broad -> `UPDATE_PLAN` or `SPLIT_INTO_PLANS`
10. Safe to implement -> `IMPLEMENT_PLAN`
11. Safe to plan next task -> `CREATE_PLAN`

## Good next-step examples

```md
## Concrete Next Step

- `next_step_type`: UPDATE_ARCHITECTURE
- `target`: `ARCHITECTURE.md` section "Data Ownership"
- `action`: Clarify that `user_product_membership` is the authorization source of truth and `notification` is only a read/display model.
- `why_this_is_next`: The current PLAN assumes notification state can drive access checks, which conflicts with the intended source-of-truth model.
- `blocking_condition`: Do not implement the invitation acceptance plan until architecture is updated and the plan is checked again.
- `suggested_prompt`: "Use architecture-writer to update ARCHITECTURE.md with the membership and notification source-of-truth rules, then rerun artifact consistency review."
```

```md
## Concrete Next Step

- `next_step_type`: IMPLEMENT_PLAN
- `target`: `PLAN.md` task "Add invitation acceptance endpoint"
- `action`: Implement the approved plan without changing product behavior, architecture boundaries, ADR decisions, or roadmap scope.
- `why_this_is_next`: PRD, architecture, ADR, roadmap, and plan are consistent enough for safe execution.
- `blocking_condition`: Stop implementation if new source-of-truth, transaction, or ADR conflicts are discovered.
- `suggested_prompt`: "Use implement-task to execute the approved invitation acceptance PLAN.md exactly as scoped."
```
