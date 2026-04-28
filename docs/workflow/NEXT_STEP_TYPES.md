# NEXT_STEP_TYPES.md

Purpose: define the canonical `next_step_type` values used by the shared `Concrete Next Step` block across the AI workflow skills.

This file exists to reduce vocabulary drift between skills. Every workflow phase should use one of these values in:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

See also:

- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`

---

## 1. Core Rules

### Use exact canonical values

Use the exact uppercase `UPPER_SNAKE_CASE` values listed in this document.

Do not invent local variants such as:

- `CREATE_OR_UPDATE_ARCHITECTURE`
- `START_IMPLEMENTATION`
- `NEXT_PLAN`
- `FIX_ISSUES`
- `CONTINUE_DEVELOPMENT`
- `UPDATE_DOCS`

If a skill needs a new value, add it here first, then update the skill-specific allowed list.

### Prefer specific create/update values

Use separate create and update values when possible:

- use `CREATE_ARCHITECTURE` when no suitable architecture artifact exists
- use `UPDATE_ARCHITECTURE` when an existing architecture artifact remains the right target

Avoid combined values such as `CREATE_OR_UPDATE_ARCHITECTURE` in final output.

### One block, one next step

`next_step_type` must represent exactly one immediate next action.

If several actions are needed, choose the first blocking action. Mention the later actions only inside `why_this_is_next` or `suggested_prompt` when necessary.

---

## 2. Canonical Values

## 2.1 Brainstorm and routing values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `RETURN_TO_BRAINSTORM` | The idea, evidence, or problem framing is not clear enough for a durable artifact. | Brainstorm discussion / `BRAINSTORM.md` |
| `REJECT_OR_DEFER` | The idea should not proceed now because value, evidence, timing, or feasibility is insufficient. | Rejection/defer decision |
| `REQUEST_MISSING_SOURCE_ARTIFACT` | A required upstream artifact is missing or unavailable. | Missing PRD, architecture, ADR, roadmap, plan, implementation summary, or evidence |
| `REQUEST_PRODUCT_DECISION` | Product intent, scope, user behavior, or business rule is unresolved. | PRD decision / user decision |
| `REQUEST_DECISION_INPUT` | A technical decision cannot be recorded because decision drivers or options are insufficient. | ADR decision input |
| `RESOLVE_SOURCE_CONFLICT` | Two or more source artifacts conflict and the current skill cannot safely choose one. | Conflicting artifacts |
| `STOP_AND_ESCALATE` | Work cannot proceed safely within the current phase. | User / owner decision |

---

## 2.2 PRD values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `CREATE_PRD` | No suitable PRD exists and product truth must be created. | `PRD.md` |
| `UPDATE_PRD` | Existing PRD remains valid but product truth changed. | `PRD.md` |
| `REVISE_PRD` | The current PRD output is incomplete, inconsistent, or needs correction before handoff. | `PRD.md` |
| `RETURN_TO_PRD` | A downstream phase discovered product ambiguity or contradiction. | `PRD.md` |

---

## 2.3 Architecture values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `CREATE_ARCHITECTURE` | No suitable canonical architecture exists and system-shape truth must be created. | `ARCHITECTURE.md` |
| `UPDATE_ARCHITECTURE` | Existing root architecture remains the correct target but needs changes. | `ARCHITECTURE.md` |
| `CREATE_INITIATIVE_ARCHITECTURE` | A large initiative needs a separate architecture document. | `docs/architecture/<initiative-slug>-architecture.md` |
| `UPDATE_INITIATIVE_ARCHITECTURE` | Existing initiative architecture remains the correct target but needs changes. | `docs/architecture/<initiative-slug>-architecture.md` |
| `RETURN_TO_ARCHITECTURE` | A downstream artifact or review found an architecture gap, contradiction, or missing constraint. | Root or initiative architecture |
| `FOLD_INITIATIVE_ARCHITECTURE_INTO_ROOT` | Stable initiative rules should be absorbed into canonical root architecture. | `ARCHITECTURE.md` |
| `ARCHIVE_INITIATIVE_ARCHITECTURE` | Initiative architecture is no longer active after stable rules are folded into root architecture. | `docs/architecture/archive/` |

---

## 2.4 ADR values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `CREATE_ADR` | One significant decision with credible options must be recorded. | `docs/adr/<number>-<decision>.md` |
| `UPDATE_ADR` | Existing ADR may be corrected or updated according to the repo's ADR policy. | Existing ADR |
| `REVISE_ADR` | The current ADR output is incomplete, unclear, or not decision-worthy yet. | ADR draft |
| `CREATE_SUPERSEDING_ADR` | A decision changed and rewriting the old ADR would damage history. | New ADR superseding old ADR |

---

## 2.5 Roadmap values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `CREATE_ROADMAP` | No suitable roadmap exists and staged delivery structure is needed. | `ROADMAP.md` or `docs/roadmap/<initiative>.md` |
| `UPDATE_ROADMAP` | Existing roadmap remains valid but sequencing, phases, dependencies, risks, or exit criteria changed. | Existing roadmap |
| `REVISE_ROADMAP` | Current roadmap output needs correction before it can hand off to planning. | Roadmap draft |

---

## 2.6 Plan values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `CREATE_PLAN` | One bounded task is ready and no suitable plan exists. | `PLAN.md` or task-specific plan file |
| `UPDATE_PLAN` | Existing plan remains the correct task contract but needs changes. | Existing plan |
| `REVISE_PLAN` | Current plan output is incomplete, too broad, or inconsistent before implementation. | Plan draft |
| `SPLIT_INTO_PLANS` | The current scope contains multiple independently reviewable tasks. | Multiple single-task plans |
| `START_NEXT_PLAN` | Current reviewed task is complete and the next roadmap slice or task should be planned. | Next `PLAN.md` |

---

## 2.7 Implementation and validation values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `IMPLEMENT_PLAN` | One approved plan is ready for implementation. | Approved `PLAN.md` |
| `RETURN_TO_IMPLEMENTATION` | Review or validation found required changes to the implementation. | Implementation task |
| `RUN_VALIDATION` | Implementation exists but required validation/tests have not been run or are incomplete. | Test/validation command or checklist |
| `APPLY_MINOR_FIXES` | Only small bounded fixes remain and no upstream artifact update is needed. | Specific files or implementation area |
| `RUN_REVIEW` | Implementation or validation is ready for review. | `review-phase` |
| `MERGE_OR_CLOSE_TASK` | Review approved the work and no further implementation change is required. | PR/branch/task |

---

## 2.8 Review and evidence values

| `next_step_type` | Use when | Common target |
|---|---|---|
| `REQUEST_MISSING_EVIDENCE` | Review cannot complete because required diff, tests, logs, plan, architecture, ADR, or validation evidence is missing. | Missing evidence |
| `SPLIT_REVIEW_SCOPE` | The review scope is too broad or combines unrelated tasks. | Separate review scopes |
| `RETURN_TO_REVIEW` | A previous phase must come back to review after a bounded correction or missing evidence is supplied. | Review report / `review-phase` |

---

## 3. Allowed Values by Workflow Phase

This section defines the default allowed set for each skill. A skill may expose a smaller subset, but should not invent values outside this file.

### `brainstorm-gate`

Recommended allowed values:

- `REJECT_OR_DEFER`
- `CREATE_PRD`
- `UPDATE_PRD`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`
- `RETURN_TO_BRAINSTORM`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `STOP_AND_ESCALATE`

### `prd-writer`

Recommended allowed values:

- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ADR`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`
- `CREATE_PLAN`
- `UPDATE_PLAN`
- `REVISE_PRD`
- `REQUEST_PRODUCT_DECISION`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RETURN_TO_BRAINSTORM`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

### `architecture-writer`

Recommended allowed values:

- `CREATE_ADR`
- `UPDATE_ADR`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`
- `CREATE_PLAN`
- `UPDATE_PLAN`
- `UPDATE_PRD`
- `REVISE_PRD`
- `RETURN_TO_ARCHITECTURE`
- `FOLD_INITIATIVE_ARCHITECTURE_INTO_ROOT`
- `ARCHIVE_INITIATIVE_ARCHITECTURE`
- `REQUEST_PRODUCT_DECISION`
- `REQUEST_DECISION_INPUT`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `STOP_AND_ESCALATE`

### `adr-writer`

Recommended allowed values:

- `UPDATE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ROADMAP`
- `UPDATE_ROADMAP`
- `CREATE_PLAN`
- `UPDATE_PLAN`
- `UPDATE_PRD`
- `RETURN_TO_ARCHITECTURE`
- `REVISE_ADR`
- `CREATE_SUPERSEDING_ADR`
- `REQUEST_DECISION_INPUT`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

### `roadmap-planner`

Recommended allowed values:

- `CREATE_PLAN`
- `UPDATE_PLAN`
- `SPLIT_INTO_PLANS`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `UPDATE_PRD`
- `REVISE_ROADMAP`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

### `plan-writer`

Recommended allowed values:

- `IMPLEMENT_PLAN`
- `SPLIT_INTO_PLANS`
- `UPDATE_PRD`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `UPDATE_ROADMAP`
- `REVISE_PLAN`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RESOLVE_SOURCE_CONFLICT`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

### `implement-task`

Recommended allowed values:

- `RUN_REVIEW`
- `RUN_VALIDATION`
- `APPLY_MINOR_FIXES`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `UPDATE_ROADMAP`
- `UPDATE_PRD`
- `SPLIT_INTO_PLANS`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `RESOLVE_SOURCE_CONFLICT`
- `STOP_AND_ESCALATE`

### `review-phase`

Recommended allowed values:

- `MERGE_OR_CLOSE_TASK`
- `APPLY_MINOR_FIXES`
- `RETURN_TO_IMPLEMENTATION`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `UPDATE_ROADMAP`
- `UPDATE_PRD`
- `REQUEST_MISSING_EVIDENCE`
- `SPLIT_REVIEW_SCOPE`
- `START_NEXT_PLAN`
- `RETURN_TO_REVIEW`
- `STOP_AND_ESCALATE`

---

## 4. Deprecated Aliases and Migration Map

These values may exist in older skill files or generated outputs. Replace them with the canonical values below.

| Deprecated / loose value | Replace with |
|---|---|
| `CREATE_OR_UPDATE_ARCHITECTURE` | `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE` |
| `CREATE_OR_UPDATE_ADR` | `CREATE_ADR`, `UPDATE_ADR`, or `CREATE_SUPERSEDING_ADR` |
| `CREATE_OR_UPDATE_ROADMAP` | `CREATE_ROADMAP` or `UPDATE_ROADMAP` |
| `CREATE_OR_UPDATE_PLAN` | `CREATE_PLAN` or `UPDATE_PLAN` |
| `START_IMPLEMENTATION` | `IMPLEMENT_PLAN` |
| `SPLIT_PLAN` | `SPLIT_INTO_PLANS` |
| `APPLY_MINOR_FIX` | `APPLY_MINOR_FIXES` |
| `REQUEST_MISSING_SOURCE` | `REQUEST_MISSING_SOURCE_ARTIFACT` |
| `START_NEXT_TASK` | `START_NEXT_PLAN` if a new plan is required, otherwise `IMPLEMENT_PLAN` |
| `STOP` | `STOP_AND_ESCALATE` or `REJECT_OR_DEFER`, depending on context |
| `NEW_PRD` | `CREATE_PRD` |
| `PRD_UPDATE` | `UPDATE_PRD` |
| `NEW_ARCHITECTURE` | `CREATE_ARCHITECTURE` or `CREATE_INITIATIVE_ARCHITECTURE` |
| `ARCHITECTURE_UPDATE` | `UPDATE_ARCHITECTURE` or `UPDATE_INITIATIVE_ARCHITECTURE` |
| `NEW_ADR` | `CREATE_ADR` |
| `ADR_UPDATE` | `UPDATE_ADR` or `CREATE_SUPERSEDING_ADR` |
| `NEW_PRODUCT_ROADMAP` | `CREATE_ROADMAP` |
| `PRODUCT_ROADMAP_UPDATE` | `UPDATE_ROADMAP` |
| `NEW_INITIATIVE_ROADMAP` | `CREATE_ROADMAP` |
| `INITIATIVE_ROADMAP_UPDATE` | `UPDATE_ROADMAP` |

Routing decisions such as `NEW_PRD` may still appear in a `decision` field for brainstorm outputs. They should not be used as the terminal `next_step_type` once this enum is adopted.

---

## 5. Choosing Between Similar Values

### `CREATE_*` vs `UPDATE_*`

Use `CREATE_*` when:

- no suitable existing artifact exists
- the scope/objective is materially new
- reusing an existing artifact would reduce clarity

Use `UPDATE_*` when:

- the existing artifact still represents the same underlying object
- only part of the artifact changed
- updating preserves clarity better than creating a new artifact

### `REVISE_*` vs `UPDATE_*`

Use `REVISE_*` when the current generated artifact is not yet acceptable as output of the current phase.

Use `UPDATE_*` when an already-existing durable artifact needs to change because upstream/downstream truth changed.

Example:

- `REVISE_PLAN`: the current plan draft is too broad and must be corrected before implementation.
- `UPDATE_PLAN`: a completed review found that the approved plan must be changed before re-implementation.

### `RETURN_TO_*` vs `UPDATE_*`

Use `RETURN_TO_*` when the next phase should re-enter a skill or workflow phase, but the exact artifact update is not yet known.

Use `UPDATE_*` when the exact target artifact is known.

Example:

- `RETURN_TO_ARCHITECTURE`: review found architecture conflict, but the owner must decide root vs initiative architecture.
- `UPDATE_ARCHITECTURE`: review found a specific missing root architecture constraint.

### `REQUEST_*` vs `STOP_AND_ESCALATE`

Use `REQUEST_*` when a specific missing input would unblock the workflow.

Use `STOP_AND_ESCALATE` when the current phase cannot safely route the next step, or the conflict requires human ownership.

---

## 6. Valid Examples

### Architecture handoff to ADR

```md
## Concrete Next Step

- `next_step_type`: CREATE_ADR
- `target`: `docs/adr/0004-use-transactional-outbox.md`
- `action`: Create one ADR deciding whether invitation notification events should use transactional outbox.
- `why_this_is_next`: The architecture defines async notification flow but the reliable publishing mechanism is a lasting decision with credible alternatives.
- `blocking_condition`: Roadmap and plan creation should wait until the publishing decision is recorded.
- `suggested_prompt`: "Use adr-writer to create one ADR for the invitation notification event publishing mechanism, using `ARCHITECTURE.md` as the source of architecture constraints."
```

### Review handoff to implementation

```md
## Concrete Next Step

- `next_step_type`: RETURN_TO_IMPLEMENTATION
- `target`: `PLAN.md` implementation for invitation acceptance
- `action`: Fix the missing membership transaction update and rerun the affected service tests.
- `why_this_is_next`: Review found that the implementation violates the architecture rule that invitation acceptance and membership creation must occur in the same transaction.
- `blocking_condition`: The task cannot be approved until the transaction boundary violation is fixed and validated.
- `suggested_prompt`: "Use implement-task to revise the invitation acceptance implementation according to the approved `PLAN.md` and the transaction rules in `ARCHITECTURE.md`."
```

---

## 7. Invalid Examples

Invalid because the type is vague and not canonical:

```md
- `next_step_type`: CONTINUE_DEVELOPMENT
```

Invalid because create/update is ambiguous:

```md
- `next_step_type`: CREATE_OR_UPDATE_ARCHITECTURE
```

Invalid because the field uses a brainstorm decision value instead of a next-step type:

```md
- `next_step_type`: NEW_PRD
```

Invalid because the action does not identify the concrete work:

```md
- `next_step_type`: APPLY_MINOR_FIXES
- `action`: Fix issues.
```

---

## 8. Migration Rule

Adopt this file in two steps:

1. Keep `Concrete Next Step` field structure unchanged.
2. Replace each skill's local `next_step_type` list with the phase-specific subset from this file.

During migration, validators may accept deprecated aliases as warnings. After all skills are updated, validators should reject aliases as errors.
