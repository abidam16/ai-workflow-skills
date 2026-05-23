---
name: review-phase
description: Review completed implementation work or artifact consistency against the approved source artifacts. Supports task review, lightweight task review, roadmap implementation review, and artifact consistency review. Use to produce severity-classified findings, architecture/product/ADR/plan alignment checks, validation assessment, and one concrete next step.
---

# Review Phase

## 1. Purpose

This skill is the enforcement layer. It reviews implementation or artifact consistency against relevant approved sources of truth and decides one concrete next action.

Review decides acceptance, revision, or escalation. It does not implement fixes and does not silently mutate source artifacts. Approval is not the same as task closure; closure is a separate `MERGE_OR_CLOSE_TASK` action unless the user explicitly asks this turn to update closure artifacts.

## 2. Shared Workflow Sources

Use these shared workflow docs when present:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/LIGHTWEIGHT_TASK_MODE.md`

## 3. Review Modes

Supported modes:

- `TASK_REVIEW` — review one implementation against one full plan
- `LIGHTWEIGHT_TASK_REVIEW` — review one lightweight implementation against one lightweight plan
- `ROADMAP_IMPLEMENTATION_REVIEW` — review roadmap-level implementation status across multiple tasks
- `ARTIFACT_CONSISTENCY_REVIEW` — review PRD ↔ Architecture ↔ ADR ↔ Roadmap ↔ Plan before implementation

## 4. Lightweight Task Review

Use when reviewing implementation produced from a lightweight plan.

Assess:

- lightweight eligibility remained valid
- one-task scope was preserved
- implementation matches the lightweight plan
- no hidden product decision was introduced
- no architecture boundary/source-of-truth change was introduced
- no ADR-worthy decision was introduced
- no roadmap/sequencing need was introduced
- validation evidence is sufficient
- next step is concrete

If lightweight assumptions failed, do not approve. Route to the correct full artifact or plan update.

## 5. Finding Types

Use relevant finding types:

- `PRODUCT_ALIGNMENT`
- `ARCHITECTURE_VIOLATION`
- `ADR_CONFLICT`
- `ROADMAP_ALIGNMENT`
- `PLAN_ALIGNMENT`
- `LIGHTWEIGHT_SCOPE_VIOLATION`
- `LIGHTWEIGHT_ESCALATION_REQUIRED`
- `VALIDATION_GAP`
- `TECHNICAL_QUALITY`
- `SOURCE_OF_TRUTH_CONFLICT`

Severity:

- `BLOCKER`
- `MAJOR`
- `MINOR`
- `NOTE`

## 6. Review Statuses

For task and lightweight task review:

- `APPROVED`
- `APPROVED_WITH_MINOR_IMPROVEMENTS`
- `NEEDS_REVISION`
- `BLOCKED`

For artifact consistency review:

- `CONSISTENT`
- `CONSISTENT_WITH_MINOR_GAPS`
- `NEEDS_ARTIFACT_REVISION`
- `BLOCKED`

## 6.5 Approved Task Closure Routing

For `TASK_REVIEW` and `LIGHTWEIGHT_TASK_REVIEW` with `APPROVED` or `APPROVED_WITH_MINOR_IMPROVEMENTS`:

- If plan/checkpoint closure artifacts are not current, route to `MERGE_OR_CLOSE_TASK`.
- The next action should explicitly update any applicable plan status fields, review checklist checkboxes, closure summary, final `Concrete Next Step`, and checkpoint entry.
- If closure artifacts are already current, route to `MERGE_OR_CLOSE_TASK` for merge/commit handling or `START_NEXT_PLAN` only when the current task is already closed.
- Do not use `START_NEXT_PLAN` while the approved task's closure docs are stale.
- Do not update closure docs inside review unless the user explicitly asked review to do that mutation in the same turn.

## 7. Mandatory Closing

Every review report must end with exactly one:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Typical next steps:

- `RUN_REVIEW` for additional required review
- `RETURN_TO_IMPLEMENTATION` for code corrections
- `UPDATE_PLAN` for plan correction
- `UPDATE_PRD` for product ambiguity
- `UPDATE_ARCHITECTURE` for architecture gap/conflict
- `CREATE_ADR` for durable decision gap
- `UPDATE_ROADMAP` for sequencing gap
- `STOP_AND_ESCALATE` for unresolved conflict
