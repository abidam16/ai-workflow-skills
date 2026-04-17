---
name: review-phase
description: Review implemented work against approved source artifacts and produce a severity-classified, action-oriented report. Use when you need an independent review of one task against one PLAN.md, or a broader review of multiple completed tasks against one roadmap and its upstream product/business intent. Do not use to create plans, roadmaps, or PRDs, and do not use as a generic coding helper.
---

# Review Phase

This skill performs structured review. Its job is not to re-plan, re-design, or re-implement by default. Its job is to compare implementation against approved intent and produce a decision-ready report.

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Before review, verify that the upstream artifacts satisfy the shared handoff contract. Use the decision matrix only for routing the review mode and the next post-review step, not for re-planning upstream work.

## Review modes

Select exactly one mode before reviewing:

1. `TASK_REVIEW`
   - Review one implemented task against one approved `PLAN.md`.
   - Use when the main question is whether a single task fulfilled its plan and is acceptable.

2. `ROADMAP_IMPLEMENTATION_REVIEW`
   - Review multiple implemented tasks under one roadmap.
   - Use when the main question is whether the roadmap slice is fulfilled, whether task implementations integrate correctly, and whether there are remaining delivery gaps.

If the requested review target is ambiguous, resolve the target first. Do not silently mix the two modes.

## Source-of-truth order

Read intent before judging code. Use the narrowest valid chain of source artifacts:

### For `TASK_REVIEW`
1. `PLAN.md`
2. relevant roadmap section if needed
3. relevant PRD / ADR sections if needed
4. implementation diff / changed files / tests / validation evidence

### For `ROADMAP_IMPLEMENTATION_REVIEW`
1. roadmap
2. relevant PRD / ADR sections if needed
3. all relevant `PLAN.md` files under that roadmap
4. implementation diffs / changed files / tests / validation evidence

Do not start from code impression alone.

## Required review dimensions

Every review must assess these dimensions explicitly:

1. Business alignment
   - Does the implementation fulfill the intended business need, workflow, rule, or success condition?

2. Plan / roadmap / design alignment
   - Does the implementation match the approved objective, scope, detailed spec, and constraints?

3. Technical quality
   - Is the implementation maintainable, coherent, consistent, and safe enough for the context?

4. Validation and test adequacy
   - Was the work verified appropriately, and are tests meaningful enough?

5. Integration impact
   - Does the implementation fit the surrounding roadmap, future tasks, and existing architecture without creating hidden gaps?

## Review procedure

Follow this sequence:

1. Identify the exact review target.
2. Identify the source artifacts used.
3. Read the source artifacts in the correct order.
4. Compare implementation to business intent.
5. Compare implementation to plan / roadmap / design intent.
6. Evaluate technical quality and code health.
7. Evaluate validation and tests.
8. Evaluate integration and downstream impact.
9. Classify findings by urgency.
10. Decide review status.
11. Write a concise, action-oriented report.

## Review findings

Classify every finding into one of these levels:

- `HIGH_URGENCY`
  - Must be fixed before acceptance or before the next dependent task proceeds.
- `MEDIUM_URGENCY`
  - Important issue that should be fixed soon; context may determine whether it blocks acceptance.
- `LOW_URGENCY`
  - Improvement or minor issue that does not usually block acceptance.
- `FUTURE_IMPROVEMENT`
  - Intentionally deferred or optional improvement outside the current required acceptance bar.

Do not collapse all issues into one list. Severity should drive next action.

## Decision statuses

Conclude with exactly one status:

- `APPROVED`
- `APPROVED_WITH_MINOR_IMPROVEMENTS`
- `NEEDS_REVISION`
- `BLOCKED`

The chosen status must match the actual findings.

## Important review rules

- Do not confuse passing tests with full acceptance.
- Do not judge only technical quality. Business fulfillment is mandatory.
- Do not reward extra out-of-scope work as if it were automatically good.
- Do not re-open settled upstream decisions unless implementation exposes a real conflict or missing requirement.
- If the source artifacts are incomplete, contradictory, or too weak to review fairly, say so explicitly in the report.

## Output contract

Produce a structured review report using the appropriate template in `assets/`:

- `TASK_REVIEW_REPORT_TEMPLATE.md`
- `ROADMAP_REVIEW_REPORT_TEMPLATE.md`

The report must tell the audience:
- what was reviewed
- what source artifacts were used
- what is good
- what is wrong
- how serious each problem is
- whether the intended business and plan/design outcomes were fulfilled
- what should happen next
- final status

## When to stop and escalate

Stop and explicitly flag the issue if:
- the source artifacts conflict materially
- the implementation cannot be mapped to the claimed plan or roadmap
- required evidence for fair review is missing
- the requested review target is broader than can be reviewed credibly in one pass
