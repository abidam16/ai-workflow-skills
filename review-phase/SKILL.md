---
name: review-phase
description: Review implementation or artifact-chain consistency against approved source artifacts. Use for task review, roadmap implementation review, or pre-implementation ARTIFACT_CONSISTENCY_REVIEW. Produces severity-classified findings and exactly one concrete next action. Do not use to write PRD, architecture, ADR, roadmap, plan, or implementation changes.
---

# Review Phase

## Shared workflow policy

Apply these shared docs instead of restating their rules here:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- `docs/workflow/ARTIFACT_CONSISTENCY_REVIEW_CONTRACT.md`
- `docs/workflow/LOCAL_SKILL_AUTHORING_RULES.md`

Shared docs define artifact authority, handoff payloads, artifact-consistency review rules, and the required final next-step block.

## Purpose

Use this skill to decide whether completed work or artifact chains conform to approved source artifacts.

Review does not rewrite artifacts or code. It produces findings and one concrete next action.

## Review modes

Use one mode per run:

### `TASK_REVIEW`

Review one implemented plan against its source artifacts, changed files, tests, and validation evidence.

### `ROADMAP_IMPLEMENTATION_REVIEW`

Review whether a set of completed plans implements a roadmap phase or roadmap slice correctly.

### `ARTIFACT_CONSISTENCY_REVIEW`

Review PRD, architecture, ADRs, roadmap, and plan consistency before implementation.

Use this mode to catch contradictions before code is written.

## Use this skill when

Use this skill when:

- implementation is complete and needs acceptance/revision decision
- a roadmap phase needs implementation-level verification
- artifacts need consistency review before implementation
- review must classify defects, drift, missing validation, or source-artifact conflicts
- the user needs a concrete next step after review

## Do not use this skill when

Route elsewhere when the task is to create or modify artifacts/code:

- product truth -> `prd-writer`
- system shape -> `architecture-writer`
- one technical decision -> `adr-writer`
- delivery sequencing -> `roadmap-planner`
- one implementation task -> `plan-writer`
- code changes -> `implement-task`

## Inputs expected

For `TASK_REVIEW`, prefer:

- `PLAN.md`
- implementation summary
- changed files/diff
- validation/test evidence
- relevant PRD, architecture, ADR, and roadmap sections

For `ROADMAP_IMPLEMENTATION_REVIEW`, prefer:

- roadmap section
- completed plans
- implementation summaries
- review reports, validation evidence, and relevant source artifacts

For `ARTIFACT_CONSISTENCY_REVIEW`, prefer:

- PRD
- root or initiative architecture
- relevant ADRs
- roadmap
- plan(s)
- prior review findings, if any

If critical evidence is missing, produce a missing-evidence review instead of guessing.

## Procedure

1. Select exactly one review mode.
2. Identify the applicable source artifacts and evidence.
3. Check conformance against the shared authority and handoff contracts.
4. Classify findings by severity and type.
5. Decide whether the work/artifact chain is acceptable, needs revision, or is blocked.
6. Route to exactly one concrete next action.
7. End with `## Concrete Next Step`.

## Finding severity

Use severity consistently:

- `BLOCKER` — cannot proceed safely
- `MAJOR` — must fix before acceptance or implementation
- `MINOR` — should fix, but does not block core acceptance
- `OBSERVATION` — useful note, not a required fix

## Output requirements

Every review report must include:

```md
## Review Summary

- Review mode:
- Review status:
- Source artifacts reviewed:
- Evidence reviewed:
- Overall decision:

## Findings

| Severity | Type | Finding | Required action |
|---|---|---|---|

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

A good review is:

- evidence-based
- source-artifact aware
- explicit about severity
- clear about whether work can proceed
- strict about architecture and ADR conflicts
- never vague about the next step
