# Handoff Contracts

This document defines the minimum fields each workflow phase must pass to the next phase.

## Universal output contract

Every phase output must end with exactly one `Concrete Next Step` block:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use loose alternatives such as `Immediate Next Step`, `Continuation Prompt`, or `next_step`.

## Brainstorm -> Durable Artifact

Required handoff fields:

- decision
- target artifact/action
- problem framing
- explored alternatives summary
- rationale for chosen next artifact
- explicit non-next artifacts/actions
- concrete next step

## PRD -> Architecture

Required handoff fields:

- product behaviors requiring system-shape support
- business rules that constrain architecture
- user flows that cross component boundaries
- data/source-of-truth implications
- integration/runtime implications
- architecture impact classification
- concrete next step

## Architecture -> ADR

Required handoff fields:

- decision pressure
- architecture area affected
- options that require decision record
- consequences if unresolved
- related architecture sections
- concrete next step

## Architecture -> Roadmap

Required handoff fields:

- architecture scope
- component/data/integration dependencies
- required ADRs and their status
- sequencing constraints
- implementation readiness
- concrete next step

## ADR -> Architecture

Required handoff fields:

- ADR identifier
- decision summary
- architecture sections affected
- constraints introduced or changed
- whether root or initiative architecture must be updated
- concrete next step

## Roadmap -> Plan

Required handoff fields:

- selected phase/slice
- objective
- dependencies already satisfied
- dependencies not satisfied
- architecture/ADR constraints to carry into plan
- candidate one-task plan boundary
- concrete next step

## Plan -> Implementation

Required handoff fields:

- one-task objective
- in-scope items
- out-of-scope items
- expected file/component changes
- relevant PRD/architecture/ADR/roadmap constraints
- validation requirements
- stop conditions
- concrete next step

## Implementation -> Review

Required handoff fields:

- plan reference
- implementation summary
- changed files / diff reference
- validations run
- known deviations
- architecture/ADR conflicts discovered, if any
- concrete next step

## Artifact Consistency Review Input

Use this input contract for `ARTIFACT_CONSISTENCY_REVIEW`.

Required when available:

- `PRD.md`
- root `ARCHITECTURE.md` and/or initiative architecture
- relevant ADRs
- `ROADMAP.md` or roadmap slice
- one or more `PLAN.md` files or plan candidates
- shared workflow docs

Optional:

- brainstorm handoff, as historical context only
- implementation summaries, only when they expose artifact drift

## Artifact Consistency Review Output

The output must include:

- selected review mode: `ARTIFACT_CONSISTENCY_REVIEW`
- artifacts reviewed
- missing/stale/conflicting source artifacts
- PRD -> Architecture consistency assessment
- Architecture -> ADR consistency assessment
- Architecture/ADR -> Roadmap consistency assessment
- Source artifacts -> PLAN consistency assessment
- handoff contract completeness assessment
- findings with severity and category
- final status: `CONSISTENT`, `CONSISTENT_WITH_MINOR_GAPS`, `NEEDS_ARTIFACT_REVISION`, or `BLOCKED`
- exactly one concrete next step

## Review -> Next Action

Review may route to:

- merge/close task
- apply minor fixes
- return to implementation
- create/update PRD
- create/update architecture
- create/update ADR
- update roadmap
- create/update plan
- request missing evidence/source artifact
- split review scope
- stop and escalate

The review must choose exactly one immediate next step.
