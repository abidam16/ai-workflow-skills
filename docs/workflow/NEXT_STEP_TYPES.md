# NEXT_STEP_TYPES.md

Purpose: define canonical `next_step_type` values for the workflow. Individual skills may expose a subset, but should not invent local aliases when a canonical value exists.

---

## Canonical Values

### Product / Architecture / Decision / Delivery

- `CREATE_PRD`
- `UPDATE_PRD`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`

### Planning / Implementation / Review

- `CREATE_PLAN`
- `UPDATE_PLAN`
- `SPLIT_INTO_PLANS`
- `IMPLEMENT_PLAN`
- `RUN_REVIEW`
- `RUN_ARTIFACT_CONSISTENCY_REVIEW`
- `RETURN_TO_IMPLEMENTATION`

### Lightweight Mode

Use the same canonical values where possible:

- `CREATE_PLAN` for lightweight plan creation
- `IMPLEMENT_PLAN` for lightweight implementation
- `RUN_REVIEW` for lightweight review

Optional mode marker should live in the artifact body as `mode: LIGHTWEIGHT_TASK`, not in `next_step_type`.

### Requests / Stops

- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `REQUEST_PRODUCT_DECISION`
- `REQUEST_DECISION_INPUT`
- `RESOLVE_SOURCE_CONFLICT`
- `STOP_AND_ESCALATE`
- `REJECT_OR_DEFER`

---

## Deprecated Aliases

| Deprecated | Use instead |
|---|---|
| `CREATE_OR_UPDATE_PRD` | `CREATE_PRD` or `UPDATE_PRD` |
| `CREATE_OR_UPDATE_ARCHITECTURE` | `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE` |
| `CREATE_OR_UPDATE_ADR` | `CREATE_ADR` or `UPDATE_ADR` |
| `CREATE_OR_UPDATE_ROADMAP` | `CREATE_ROADMAP` or `UPDATE_ROADMAP` |
| `CREATE_OR_UPDATE_PLAN` | `CREATE_PLAN` or `UPDATE_PLAN` |
| `START_IMPLEMENTATION` | `IMPLEMENT_PLAN` |
| `APPLY_MINOR_FIX` | `RETURN_TO_IMPLEMENTATION` or `UPDATE_PLAN` |
| `SPLIT_PLAN` | `SPLIT_INTO_PLANS` |
| `STOP` | `STOP_AND_ESCALATE` or `REJECT_OR_DEFER` |
| `RUN_LIGHTWEIGHT_REVIEW` | `RUN_REVIEW` with `mode: LIGHTWEIGHT_TASK` |
| `CREATE_LIGHTWEIGHT_PLAN` | `CREATE_PLAN` with `mode: LIGHTWEIGHT_TASK` |
| `IMPLEMENT_LIGHTWEIGHT_TASK` | `IMPLEMENT_PLAN` with `mode: LIGHTWEIGHT_TASK` |

---

## Examples

Good:

```md
## Concrete Next Step

- `next_step_type`: CREATE_PLAN
- `target`: plans/PLAN-014-fix-null-date-handling.md
- `action`: Create a lightweight single-task plan for the null-date handling bug.
- `why_this_is_next`: The task is local, product behavior is already clear, and no architecture or ADR work is needed.
- `blocking_condition`: Stop if implementation requires changing date ownership, API contract, or persistence semantics.
- `suggested_prompt`: Use plan-writer to create a lightweight PLAN for the null-date handling bug using the attached issue context.
```

Bad:

```md
- `next_step_type`: CREATE_OR_UPDATE_PLAN
- `action`: Continue development.
```
