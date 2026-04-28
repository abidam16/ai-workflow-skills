---
name: review-phase
description: Review implemented work against approved source artifacts and produce a severity-classified, architecture-aware, action-oriented report with exactly one concrete next step. Use for TASK_REVIEW of one implementation against one PLAN.md, or ROADMAP_IMPLEMENTATION_REVIEW of multiple completed tasks against one roadmap. Do not use to create PRDs, architecture documents, ADRs, roadmaps, implementation plans, or code changes.
---

# Review Phase

This skill performs structured review.

Its job is not to re-plan, re-design, or re-implement by default. Its job is to compare implementation against approved source artifacts, enforce artifact authority, classify findings by urgency, and end with exactly one concrete next step.

Review is the workflow enforcement layer. It must not approve work that violates relevant product, architecture, ADR, roadmap, or plan constraints unless the review explicitly routes to the correct artifact update before acceptance.

---

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing, artifact authority, create-vs-update decisions, and escalation rules across phases.
- `docs/workflow/HANDOFF_CONTRACTS.md` for required input/output fields between phases.

Apply the shared rules. Do not duplicate them as the primary authority here.

Before reviewing, verify that upstream artifacts satisfy the shared handoff contract. Use the decision matrix only to select the review mode and the next post-review step, not to re-plan upstream work.

If shared workflow docs are absent, proceed using this skill's local rules and explicitly state that shared workflow docs were not found.

---

## Core review principle

Read intent before judging code.

The review must answer:

1. Did the implementation satisfy the approved product/business intent?
2. Did it obey relevant architecture constraints?
3. Did it obey relevant ADR decisions?
4. Did it satisfy the roadmap slice, if relevant?
5. Did it satisfy the approved single-task plan?
6. Is the implementation technically safe, maintainable, and well-integrated?
7. Is the validation evidence sufficient?
8. What exact action should happen next?

Do not judge from code impression alone.

---

## Review modes

Select exactly one review mode before reviewing.

### `TASK_REVIEW`

Review one implemented task against one approved `PLAN.md`.

Use when the main question is whether a single implementation fulfilled its approved plan and is acceptable.

Typical inputs:

- one `PLAN.md` or one task plan document
- one implementation summary
- changed files / diff / tests / validation evidence
- relevant PRD, architecture, ADR, and roadmap sections when they constrain the task

### `ROADMAP_IMPLEMENTATION_REVIEW`

Review multiple implemented tasks under one roadmap.

Use when the main question is whether a roadmap slice or initiative is fulfilled, whether task implementations integrate correctly, and whether remaining delivery gaps exist.

Typical inputs:

- one roadmap or roadmap slice
- multiple task plans
- multiple implementation summaries or diffs
- relevant PRD, architecture, ADRs, and integration evidence

### Ambiguous target rule

If the requested review target is ambiguous, resolve the target first. Do not silently mix task review and roadmap review.

---

## Source-of-truth authority

Use each artifact for its own authority.

| Artifact | Review authority |
|---|---|
| PRD | Product behavior, user value, product rules, success criteria |
| Architecture | System shape, component boundaries, data ownership, runtime flows, integration boundaries, cross-cutting constraints |
| ADR | One recorded technical decision, rationale, and consequences |
| Roadmap | Delivery sequence, phase/slice objective, dependency order, exit criteria |
| PLAN | Exact scope and execution contract for one bounded task |
| Implementation Summary | What actually changed, what deviated, what was validated |
| Tests / validation evidence | Evidence supporting or weakening the implementation claim |

Conflict rules:

1. Do not silently resolve conflicts between artifacts.
2. PRD governs product behavior.
3. Architecture governs system structure and implementation constraints.
4. ADR governs the specific recorded decision and may supersede architecture text only for that decision.
5. Roadmap governs sequencing but cannot redefine product, architecture, or ADR truth.
6. PLAN governs the current task scope but cannot override PRD, architecture, or ADR constraints.
7. If implementation follows PLAN but PLAN conflicts with PRD, architecture, or ADRs, do not approve silently. Report the artifact conflict and route to the correct update or revision step.

---

## Source-of-truth order

### For `TASK_REVIEW`

Read in this order:

1. `PLAN.md` or selected task plan
2. relevant PRD sections when product behavior or acceptance intent matters
3. relevant root `ARCHITECTURE.md` and/or initiative architecture when the task touches architecture-sensitive areas
4. relevant ADRs when recorded decisions constrain the implementation
5. relevant roadmap slice when sequencing, dependencies, or exit criteria matter
6. implementation summary
7. changed files / diff / tests / validation evidence

Use the plan as the task boundary, but use PRD, architecture, and ADRs as higher-order constraints.

### For `ROADMAP_IMPLEMENTATION_REVIEW`

Read in this order:

1. roadmap or selected roadmap slice
2. relevant PRD sections
3. relevant root `ARCHITECTURE.md` and/or initiative architecture
4. relevant ADRs
5. all relevant `PLAN.md` files under that roadmap slice
6. implementation summaries
7. changed files / diffs / tests / integration evidence

Use the roadmap as the delivery boundary, but use PRD, architecture, and ADRs as higher-order constraints.

---

## When architecture must be reviewed

Architecture review is mandatory when the implementation touches any of these:

- module, package, service, layer, or component boundaries
- source-of-truth data ownership
- database ownership, read model, write model, or migration behavior
- API, event, message, queue, scheduler, worker, or integration flow
- sync vs async behavior
- transaction boundary
- consistency model
- idempotency, retry, recovery, or dead-letter behavior
- authorization, security, role, permission, or audit behavior
- observability, logging, metrics, tracing, or operational behavior
- deployment/runtime assumptions
- performance or scalability constraints
- architecture-sensitive UI composition or frontend system boundaries

If architecture is relevant but no architecture artifact exists, classify this as a review risk. The next step may be `ROUTE_TO_ARCHITECTURE_WRITER` if the implementation cannot be fairly accepted without durable system-shape truth.

---

## Required review dimensions

Every review must explicitly assess these dimensions.

1. Business / product alignment
   - Does the implementation fulfill the intended business need, workflow, product rule, or success condition?

2. Architecture alignment
   - Does the implementation obey component boundaries, source-of-truth rules, runtime flows, integration rules, consistency rules, and other relevant architecture constraints?

3. ADR / decision alignment
   - Does the implementation obey accepted ADR decisions? Does it create a new lasting decision that requires an ADR?

4. Roadmap alignment, if relevant
   - Does the implementation fulfill the selected phase/slice, dependency order, and exit criteria?

5. Plan alignment
   - Does the implementation match the approved objective, in-scope items, out-of-scope items, detailed spec, expected changes, and validation requirements?

6. Technical quality
   - Is the implementation maintainable, coherent, consistent with local code style, safe for the context, and not over-engineered?

7. Validation and test adequacy
   - Were the right tests, checks, manual validations, or evidence provided? Are they meaningful enough for the risk level?

8. Integration and downstream impact
   - Does the implementation fit future tasks and existing system behavior without hidden gaps, broken assumptions, or architecture drift?

9. Next action clarity
   - Is there exactly one concrete next step that a user or agent can execute immediately?

---

## Review procedure

Follow this sequence:

1. Identify the exact review target.
2. Select `TASK_REVIEW` or `ROADMAP_IMPLEMENTATION_REVIEW`.
3. Identify and list all source artifacts used.
4. Check whether required source artifacts are missing, weak, stale, or contradictory.
5. Read source artifacts in the correct source-of-truth order.
6. Extract concrete obligations from each relevant source artifact.
7. Compare implementation to business/product intent.
8. Compare implementation to architecture constraints.
9. Compare implementation to ADR decisions.
10. Compare implementation to roadmap slice, if relevant.
11. Compare implementation to plan scope and detailed spec.
12. Evaluate technical quality and maintainability.
13. Evaluate validation and test adequacy.
14. Evaluate integration and downstream impact.
15. Classify findings by urgency.
16. Decide review status.
17. Select exactly one concrete next step using the next-step routing rules.
18. Write the structured review report.

---

## Finding classification

Classify every finding into one of these levels.

### `HIGH_URGENCY`

Must be fixed before acceptance, merge, release, or the next dependent task proceeds.

Typical examples:

- product behavior is wrong
- source-of-truth is violated
- architecture boundary is crossed unsafely
- accepted ADR is contradicted
- security or authorization is wrong
- transaction or consistency rule is violated
- implementation is incomplete for the approved plan
- validation evidence is insufficient for high-risk work

### `MEDIUM_URGENCY`

Important issue that should be fixed soon. It may or may not block acceptance depending on risk and context.

Typical examples:

- maintainability issue likely to cause follow-up friction
- partial validation gap
- unclear but non-fatal integration risk
- minor architecture drift that should be corrected before more tasks build on it

### `LOW_URGENCY`

Minor issue that does not usually block acceptance.

Typical examples:

- naming clarity
- small duplication
- local readability improvement
- non-blocking test improvement

### `FUTURE_IMPROVEMENT`

Useful but intentionally outside the current acceptance bar.

Do not disguise required fixes as future improvements.

---

## Common finding categories

Use precise categories.

- `BUSINESS_ALIGNMENT_GAP`
- `PRODUCT_RULE_GAP`
- `ARCHITECTURE_VIOLATION`
- `SOURCE_OF_TRUTH_VIOLATION`
- `BOUNDARY_VIOLATION`
- `RUNTIME_FLOW_VIOLATION`
- `TRANSACTION_CONSISTENCY_GAP`
- `SECURITY_AUTHORIZATION_GAP`
- `ADR_CONFLICT`
- `MISSING_ADR`
- `ROADMAP_ALIGNMENT_GAP`
- `PLAN_SCOPE_MISS`
- `PLAN_SCOPE_CREEP`
- `PLAN_ARCHITECTURE_CONFLICT`
- `IMPLEMENTATION_BUG`
- `TECHNICAL_QUALITY_RISK`
- `TEST_VALIDATION_GAP`
- `INTEGRATION_RISK`
- `MISSING_ARCHITECTURE_UPDATE`
- `MISSING_PLAN_UPDATE`
- `MISSING_ROADMAP_UPDATE`

---

## Decision statuses

Conclude with exactly one status.

### `APPROVED`

Use only when:

- no blocking findings exist
- implementation satisfies the plan or roadmap scope
- implementation satisfies relevant PRD, architecture, and ADR constraints
- validation evidence is adequate for the risk level
- remaining issues are absent or clearly outside the current acceptance bar

### `APPROVED_WITH_MINOR_IMPROVEMENTS`

Use when:

- implementation is acceptable
- no high-urgency findings exist
- remaining findings are low-urgency or clearly non-blocking medium-urgency items
- next action is still clear and bounded

### `NEEDS_REVISION`

Use when:

- implementation is not acceptable yet
- one or more issues must be corrected before acceptance
- the plan or source artifacts are still sufficient enough to guide revision
- the work should return to implementation or plan update rather than stop completely

### `BLOCKED`

Use when:

- fair review cannot proceed due to missing evidence or source artifacts
- source artifacts materially conflict
- implementation cannot be mapped to the claimed plan or roadmap
- required architecture or ADR decisions are missing
- the requested review scope is too broad for one credible review pass

---

## Mandatory concrete next step

Every review report must end with exactly one `Concrete Next Step`.

Do not end with vague statements such as:

- "review is done"
- "fix the issues"
- "continue development"
- "proceed as needed"
- "consider improvements"
- "next step depends on the team"

The next step must include:

- `next_step_type`
- `target`
- `action`
- `why_this_is_next`
- `blocking_condition`
- `suggested_prompt`

### Allowed `next_step_type` values

Use exactly one:

- `MERGE_OR_CLOSE_TASK`
- `APPLY_MINOR_FIXES`
- `RETURN_TO_IMPLEMENTATION`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `UPDATE_ROADMAP`
- `UPDATE_PRD`
- `REQUEST_MISSING_EVIDENCE`
- `SPLIT_REVIEW_SCOPE`
- `START_NEXT_PLAN`
- `STOP_AND_ESCALATE`

### Next-step selection rules

Use this routing order:

1. If review evidence is missing, choose `REQUEST_MISSING_EVIDENCE`.
2. If the review target is too broad or mixed, choose `SPLIT_REVIEW_SCOPE`.
3. If source artifacts conflict materially, choose the artifact update that resolves the highest-authority conflict:
   - product behavior conflict -> `UPDATE_PRD`
   - architecture/system-shape conflict -> `UPDATE_ARCHITECTURE`
   - one technical decision conflict -> `CREATE_OR_UPDATE_ADR`
   - sequencing conflict -> `UPDATE_ROADMAP`
   - task execution contract conflict -> `UPDATE_PLAN`
4. If implementation violates plan but the plan is still valid, choose `RETURN_TO_IMPLEMENTATION`.
5. If implementation is acceptable but minor fixes should happen before merge, choose `APPLY_MINOR_FIXES`.
6. If implementation is acceptable and there is an active branch/PR/reviewable changeset, choose `MERGE_OR_CLOSE_TASK`.
7. If implementation is accepted and the current task is closed, choose `START_NEXT_PLAN`.
8. If no safe route exists, choose `STOP_AND_ESCALATE`.

### Status-to-next-step guidance

| Status | Typical next step |
|---|---|
| `APPROVED` | `MERGE_OR_CLOSE_TASK` or `START_NEXT_PLAN` |
| `APPROVED_WITH_MINOR_IMPROVEMENTS` | `APPLY_MINOR_FIXES`, then merge/close task |
| `NEEDS_REVISION` | `RETURN_TO_IMPLEMENTATION` or `UPDATE_PLAN` |
| `BLOCKED` | `REQUEST_MISSING_EVIDENCE`, `UPDATE_ARCHITECTURE`, `CREATE_OR_UPDATE_ADR`, `UPDATE_PRD`, `SPLIT_REVIEW_SCOPE`, or `STOP_AND_ESCALATE` |

The status and next step must be consistent. A report with `HIGH_URGENCY` findings usually cannot have `MERGE_OR_CLOSE_TASK` as the immediate next step.

---

## Output contract

Use the appropriate template in `assets/`:

- `assets/TASK_REVIEW_REPORT_TEMPLATE.md`
- `assets/ROADMAP_REVIEW_REPORT_TEMPLATE.md`

The report must tell the audience:

- what was reviewed
- which review mode was used
- what source artifacts were used
- whether any source artifacts were missing, stale, weak, or conflicting
- what is good
- what is wrong
- how serious each problem is
- whether intended business/product outcomes were fulfilled
- whether architecture constraints were respected
- whether ADR constraints were respected
- whether roadmap or plan outcomes were fulfilled
- whether validation evidence is sufficient
- what should happen next
- final status
- exactly one concrete next step

The final section must be `Concrete Next Step`. It must be the last actionable section of the report.

---

## When to stop and escalate

Stop and explicitly flag the issue if:

- the source artifacts conflict materially
- required source artifacts are missing
- implementation cannot be mapped to the claimed plan or roadmap
- implementation violates architecture but the correct fix requires architecture redesign
- implementation contradicts an accepted ADR
- the plan appears wrong because it conflicts with PRD, architecture, or ADRs
- required evidence for fair review is missing
- the requested review target is broader than can be reviewed credibly in one pass

A stop condition must still end with exactly one concrete next step.

---

## Review discipline

- Do not confuse passing tests with full acceptance.
- Do not judge only technical quality.
- Business fulfillment is mandatory.
- Architecture alignment is mandatory when architecture is relevant.
- Do not reward extra out-of-scope work as automatically good.
- Do not reopen settled upstream decisions unless implementation exposes a real conflict or missing requirement.
- Do not invent missing product, architecture, ADR, roadmap, or plan decisions inside review.
- Do not produce a report without a concrete next step.
