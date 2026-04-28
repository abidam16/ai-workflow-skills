# NEXT_STEP_TYPES.md

Purpose: define canonical `next_step_type` values for workflow handoffs so all skills route to the next artifact/action with consistent vocabulary.

This file is the shared enum contract for the `next_step_type` field in `## Concrete Next Step`.

---

## 1. Core Rule

Use exactly one canonical `next_step_type` in every `Concrete Next Step` block.

Prefer specific create/update/revise/return values instead of combined or vague values.

Good:

```text
CREATE_ARCHITECTURE
UPDATE_ARCHITECTURE
CREATE_PLAN
IMPLEMENT_PLAN
RUN_REVIEW
```

Avoid:

```text
CREATE_OR_UPDATE_ARCHITECTURE
CONTINUE
NEXT
DO_WORK
FIX_ISSUES
```

---

## 2. Canonical Values

### Brainstorm / routing

| Value | Meaning |
|---|---|
| `CREATE_PRD` | Create a new PRD because product intent needs durable definition |
| `UPDATE_PRD` | Update an existing PRD because product intent changed or is incomplete |
| `CREATE_ARCHITECTURE` | Create a root or initiative architecture document |
| `UPDATE_ARCHITECTURE` | Update architecture because system shape, boundaries, ownership, or constraints changed |
| `CREATE_ADR` | Create a new ADR for one meaningful decision |
| `UPDATE_ADR` | Update or supersede an ADR when decision context/status changed |
| `CREATE_ROADMAP` | Create a roadmap because staged delivery structure is needed |
| `UPDATE_ROADMAP` | Update an existing roadmap because sequence, dependencies, or exit criteria changed |
| `CREATE_PLAN` | Create a full single-task implementation plan |
| `CREATE_LIGHTWEIGHT_PLAN` | Create a lightweight plan for a small, local, low-risk task |
| `REJECT_OR_DEFER` | Reject, defer, or park an idea because it is not ready or not valuable enough |
| `REQUEST_CLARIFICATION` | Ask for missing input before routing can be safely decided |

### Product / architecture / decision docs

| Value | Meaning |
|---|---|
| `REVISE_PRD` | Revise PRD content before downstream work |
| `REVISE_ARCHITECTURE` | Revise architecture content before downstream work |
| `REVISE_ADR` | Revise ADR content before downstream work |
| `CREATE_SUPERSEDING_ADR` | Create a new ADR that supersedes an accepted older ADR |
| `RETURN_TO_PRD` | Route back to PRD because product truth is missing/conflicting |
| `RETURN_TO_ARCHITECTURE` | Route back to architecture because system-shape truth is missing/conflicting |
| `RETURN_TO_ADR` | Route back to ADR because decision truth is missing/conflicting |

### Roadmap / planning

| Value | Meaning |
|---|---|
| `REVISE_ROADMAP` | Revise roadmap content before planning or implementation |
| `UPDATE_PLAN` | Update an existing full plan |
| `UPDATE_LIGHTWEIGHT_PLAN` | Update an existing lightweight plan |
| `REVISE_PLAN` | Revise a plan before implementation |
| `SPLIT_INTO_PLANS` | Split broad work into multiple bounded plans |
| `REQUEST_MISSING_SOURCE_ARTIFACT` | Request a required upstream artifact before continuing |
| `RESOLVE_SOURCE_CONFLICT` | Resolve contradiction between artifacts before continuing |

### Implementation

| Value | Meaning |
|---|---|
| `IMPLEMENT_PLAN` | Implement an approved full plan |
| `IMPLEMENT_LIGHTWEIGHT_PLAN` | Implement an approved lightweight plan |
| `RUN_VALIDATION` | Run required validation before review can proceed |
| `RETURN_TO_IMPLEMENTATION` | Send work back to implementation for fixes |
| `APPLY_MINOR_FIXES` | Apply small review fixes that do not need plan/architecture changes |

### Review

| Value | Meaning |
|---|---|
| `RUN_REVIEW` | Run standard task review |
| `RUN_LIGHTWEIGHT_REVIEW` | Run lightweight task review |
| `RUN_ROADMAP_REVIEW` | Run roadmap implementation review |
| `RUN_ARTIFACT_CONSISTENCY_REVIEW` | Review PRD, architecture, ADRs, roadmap, and plan for consistency before implementation |
| `REQUEST_MISSING_EVIDENCE` | Request missing validation, diff, or artifact evidence before approval |
| `MERGE_OR_CLOSE_TASK` | Accept the work and proceed to merge/close the task |
| `START_NEXT_PLAN` | Start planning the next roadmap/task slice after approval |
| `RETURN_TO_REVIEW` | Return to review after fixes or missing evidence are supplied |

### Stop / escalation

| Value | Meaning |
|---|---|
| `STOP_AND_ESCALATE` | Stop because the workflow cannot safely continue without human or upstream decision |
| `ESCALATE_TO_FULL_WORKFLOW` | Leave lightweight mode and route to the normal artifact workflow |

---

## 3. Allowed Values by Phase

### `brainstorm-gate`

```text
CREATE_PRD
UPDATE_PRD
CREATE_ARCHITECTURE
UPDATE_ARCHITECTURE
CREATE_ADR
UPDATE_ADR
CREATE_ROADMAP
UPDATE_ROADMAP
CREATE_PLAN
CREATE_LIGHTWEIGHT_PLAN
REJECT_OR_DEFER
REQUEST_CLARIFICATION
STOP_AND_ESCALATE
```

### `prd-writer`

```text
CREATE_ARCHITECTURE
UPDATE_ARCHITECTURE
CREATE_ADR
UPDATE_ADR
CREATE_ROADMAP
UPDATE_ROADMAP
CREATE_PLAN
UPDATE_PLAN
REVISE_PRD
RETURN_TO_PRD
REQUEST_MISSING_SOURCE_ARTIFACT
STOP_AND_ESCALATE
```

### `architecture-writer`

```text
CREATE_ADR
UPDATE_ADR
CREATE_ROADMAP
UPDATE_ROADMAP
CREATE_PLAN
UPDATE_PLAN
REVISE_ARCHITECTURE
RETURN_TO_PRD
RETURN_TO_ARCHITECTURE
REQUEST_MISSING_SOURCE_ARTIFACT
STOP_AND_ESCALATE
```

### `adr-writer`

```text
UPDATE_ARCHITECTURE
CREATE_ROADMAP
UPDATE_ROADMAP
CREATE_PLAN
UPDATE_PLAN
REVISE_ADR
CREATE_SUPERSEDING_ADR
RETURN_TO_PRD
RETURN_TO_ARCHITECTURE
RETURN_TO_ADR
REQUEST_MISSING_SOURCE_ARTIFACT
STOP_AND_ESCALATE
```

### `roadmap-planner`

```text
CREATE_PLAN
UPDATE_PLAN
SPLIT_INTO_PLANS
UPDATE_PRD
UPDATE_ARCHITECTURE
CREATE_ADR
UPDATE_ADR
REVISE_ROADMAP
REQUEST_MISSING_SOURCE_ARTIFACT
RESOLVE_SOURCE_CONFLICT
RUN_ARTIFACT_CONSISTENCY_REVIEW
STOP_AND_ESCALATE
```

### `plan-writer`

```text
IMPLEMENT_PLAN
IMPLEMENT_LIGHTWEIGHT_PLAN
UPDATE_PLAN
UPDATE_LIGHTWEIGHT_PLAN
SPLIT_INTO_PLANS
UPDATE_PRD
UPDATE_ARCHITECTURE
CREATE_ADR
UPDATE_ADR
UPDATE_ROADMAP
REQUEST_MISSING_SOURCE_ARTIFACT
RESOLVE_SOURCE_CONFLICT
RUN_ARTIFACT_CONSISTENCY_REVIEW
STOP_AND_ESCALATE
```

### `implement-task`

```text
RUN_REVIEW
RUN_LIGHTWEIGHT_REVIEW
RUN_VALIDATION
APPLY_MINOR_FIXES
UPDATE_PLAN
UPDATE_LIGHTWEIGHT_PLAN
SPLIT_INTO_PLANS
UPDATE_ARCHITECTURE
CREATE_ADR
UPDATE_ADR
UPDATE_ROADMAP
UPDATE_PRD
REQUEST_MISSING_SOURCE_ARTIFACT
RESOLVE_SOURCE_CONFLICT
ESCALATE_TO_FULL_WORKFLOW
STOP_AND_ESCALATE
```

### `review-phase`

```text
MERGE_OR_CLOSE_TASK
APPLY_MINOR_FIXES
IMPLEMENT_PLAN
IMPLEMENT_LIGHTWEIGHT_PLAN
RETURN_TO_IMPLEMENTATION
CREATE_PLAN
UPDATE_PLAN
UPDATE_LIGHTWEIGHT_PLAN
SPLIT_INTO_PLANS
CREATE_ARCHITECTURE
UPDATE_ARCHITECTURE
CREATE_ADR
UPDATE_ADR
UPDATE_ROADMAP
UPDATE_PRD
REQUEST_MISSING_EVIDENCE
RUN_ARTIFACT_CONSISTENCY_REVIEW
START_NEXT_PLAN
ESCALATE_TO_FULL_WORKFLOW
STOP_AND_ESCALATE
```

---

## 4. Deprecated Alias Migration Map

During migration, replace older local values with the canonical values below.

| Deprecated / Local Value | Canonical Value |
|---|---|
| `CREATE_OR_UPDATE_PRD` | `CREATE_PRD` or `UPDATE_PRD` |
| `CREATE_OR_UPDATE_ARCHITECTURE` | `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE` |
| `CREATE_OR_UPDATE_ADR` | `CREATE_ADR` or `UPDATE_ADR` |
| `CREATE_OR_UPDATE_ROADMAP` | `CREATE_ROADMAP` or `UPDATE_ROADMAP` |
| `CREATE_OR_UPDATE_PLAN` | `CREATE_PLAN` or `UPDATE_PLAN` |
| `START_IMPLEMENTATION` | `IMPLEMENT_PLAN` |
| `IMPLEMENT` | `IMPLEMENT_PLAN` |
| `RUN_TASK_REVIEW` | `RUN_REVIEW` |
| `RUN_LIGHTWEIGHT_TASK_REVIEW` | `RUN_LIGHTWEIGHT_REVIEW` |
| `APPLY_MINOR_FIX` | `APPLY_MINOR_FIXES` |
| `SPLIT_PLAN` | `SPLIT_INTO_PLANS` |
| `REQUEST_PRODUCT_DECISION` | `RETURN_TO_PRD` or `REQUEST_CLARIFICATION` |
| `REQUEST_DECISION_INPUT` | `RETURN_TO_ADR` or `REQUEST_CLARIFICATION` |
| `REQUEST_MISSING_ARTIFACT` | `REQUEST_MISSING_SOURCE_ARTIFACT` |
| `STOP` | `STOP_AND_ESCALATE` |
| `CONTINUE` | Use a specific canonical value |

---

## 5. Selection Rules

### Create vs update

Use `CREATE_*` when the target artifact does not exist or should be newly created.

Use `UPDATE_*` when the target artifact already exists and must be changed.

Do not use combined values such as `CREATE_OR_UPDATE_*`.

### Revise vs update

Use `REVISE_*` when the current artifact produced by the active skill is incomplete or internally weak.

Use `UPDATE_*` when a different existing artifact must be changed.

Example:

```text
A PRD writer produces a weak PRD draft -> REVISE_PRD
A review finds the approved architecture conflicts with the plan -> UPDATE_ARCHITECTURE
```

### Return vs request

Use `RETURN_TO_*` when the correct target artifact is known.

Use `REQUEST_CLARIFICATION` when the needed decision/input is not yet tied to one artifact.

Use `REQUEST_MISSING_SOURCE_ARTIFACT` when an expected artifact is absent.

### Stop vs escalate

Use `ESCALATE_TO_FULL_WORKFLOW` when lightweight mode becomes invalid.

Use `STOP_AND_ESCALATE` when no safe workflow continuation exists without external/human decision.

---

## 6. Invalid Values

Do not use:

```text
NEXT
CONTINUE
PROCEED
FOLLOW_UP
DONE
FIX
FIX_ISSUES
UPDATE_DOCS
KEEP_GOING
CREATE_OR_UPDATE_*
```

These values are too vague or ambiguous.

---

## 7. Adding New Values

Add a new `next_step_type` only when:

1. no existing canonical value fits,
2. multiple skills need the new route, and
3. the value can be described as one concrete next action.

When adding a new value:

1. update this file,
2. update affected skill `SKILL.md` files,
3. update affected templates,
4. update validators if present.
