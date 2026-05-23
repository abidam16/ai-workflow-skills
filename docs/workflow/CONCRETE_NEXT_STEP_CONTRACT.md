# CONCRETE_NEXT_STEP_CONTRACT.md

Purpose: define the mandatory terminal block used by every workflow phase so an AI agent never ends with an ambiguous “done” message.

This contract is shared by all workflow skills.

---

## 1. Core Rule

Every phase output must end with exactly one `Concrete Next Step` block.

The block must identify the single next artifact or action that should happen after the current phase.

Do not end a phase with only:

- “review complete”
- “implementation done”
- “plan ready”
- “continue development”
- “fix issues”
- general commentary without a routed next action

---

## 2. Required Block

Use this exact markdown shape:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

The heading must be exactly:

```md
## Concrete Next Step
```

Do not rename it to:

- `Immediate Next Step`
- `Next Step`
- `Continuation Prompt`
- `Follow-up`
- `Recommendation`

---

## 3. Field Definitions

| Field | Meaning | Required Quality |
|---|---|---|
| `next_step_type` | Canonical action enum from `docs/workflow/NEXT_STEP_TYPES.md` | Must be specific and machine-readable |
| `target` | The artifact, file, skill, branch, PR, or task that should be acted on next | Must name a concrete target |
| `action` | The exact next action to perform | Must be executable, not vague |
| `why_this_is_next` | Reason this is the correct next action | Must connect to current findings/output |
| `blocking_condition` | What would prevent or change this next step | Use `none` only when truly unblocked |
| `suggested_prompt` | A ready-to-copy prompt for the next phase | Must be specific enough for the next agent invocation |

---

## 4. Valid Examples

### Route from PRD to architecture

```md
## Concrete Next Step

- `next_step_type`: CREATE_ARCHITECTURE
- `target`: `ARCHITECTURE.md`
- `action`: Create the initial root architecture document using the approved PRD as product input.
- `why_this_is_next`: The PRD introduces runtime flow, data ownership, and integration boundaries that must be defined before roadmap or implementation planning.
- `blocking_condition`: Product behavior must be clarified first if the PRD acceptance criteria are still disputed.
- `suggested_prompt`: Use `architecture-writer` to create `ARCHITECTURE.md` from the approved PRD, focusing on component boundaries, data ownership, runtime flows, and implementation constraints.
```

### Route from plan to implementation

```md
## Concrete Next Step

- `next_step_type`: IMPLEMENT_PLAN
- `target`: `PLAN.md`
- `action`: Implement the approved single-task plan and preserve all listed architecture and ADR constraints.
- `why_this_is_next`: The plan is bounded, validation expectations are explicit, and no upstream artifact is blocking execution.
- `blocking_condition`: Stop and route back to `plan-writer` if implementation reveals scope expansion or a source-of-truth conflict.
- `suggested_prompt`: Use `implement-task` to implement `PLAN.md`, report changed files, validation performed, deviations, and the next review action.
```

### Route from implementation to review

```md
## Concrete Next Step

- `next_step_type`: RUN_REVIEW
- `target`: implementation summary and changed files
- `action`: Review the implementation against the approved plan and relevant upstream artifacts.
- `why_this_is_next`: Implementation is complete and needs acceptance, revision, or escalation decision.
- `blocking_condition`: Missing validation evidence must be supplied before review can approve the task.
- `suggested_prompt`: Use `review-phase` in `TASK_REVIEW` mode to review the implementation summary, changed files, validation evidence, `PLAN.md`, and relevant PRD/architecture/ADR constraints.
```

### Route from approved review to closure

```md
## Concrete Next Step

- `next_step_type`: MERGE_OR_CLOSE_TASK
- `target`: `PLAN.md` and `checkpoint.md`
- `action`: Close the approved task by updating plan status, review checklist, closure summary, final next step, and checkpoint evidence before merge.
- `why_this_is_next`: Review approved the implementation, but durable closure artifacts still need to reflect that approval.
- `blocking_condition`: Re-run review if any code or source artifact changes before closure.
- `suggested_prompt`: Close the approved task by updating `PLAN.md` and `checkpoint.md` with implementation status, review approval, checklist completion, validation evidence, and the next handoff, then stage the closure changes.
```

---

## 5. Invalid Examples

Invalid:

```md
## Concrete Next Step

- `next_step_type`: CONTINUE
- `target`: code
- `action`: Continue development.
- `why_this_is_next`: More work is needed.
- `blocking_condition`: none
- `suggested_prompt`: Continue.
```

Why invalid:

- `CONTINUE` is not specific.
- `target` is not concrete.
- `action` is vague.
- `suggested_prompt` is not useful.

Invalid:

```md
## Immediate Next Step

Create a plan next.
```

Why invalid:

- Wrong heading.
- Missing required fields.
- No canonical `next_step_type`.
- No blocking condition or reusable prompt.

---

## 6. Relationship to `NEXT_STEP_TYPES.md`

`next_step_type` must use a canonical value from:

```text
docs/workflow/NEXT_STEP_TYPES.md
```

If a skill needs a new `next_step_type`, update `NEXT_STEP_TYPES.md` first or route through the closest existing canonical value.

Avoid combined values such as:

- `CREATE_OR_UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ADR`
- `CREATE_OR_UPDATE_PLAN`

Prefer explicit values:

- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_ADR`
- `CREATE_PLAN`
- `UPDATE_PLAN`

---

## 7. Validation Rules

A valid output has:

1. Exactly one `## Concrete Next Step` section.
2. All six required fields.
3. A canonical `next_step_type`.
4. A concrete `target`.
5. An executable `action`.
6. A clear rationale in `why_this_is_next`.
7. A real `blocking_condition`.
8. A ready-to-copy `suggested_prompt`.

A valid output must not include legacy terminal fields such as:

- `Immediate Next Step`
- `Continuation Prompt`
- loose `next_step`
- loose `follow_up`

---

## 8. Scope

This contract defines the shape of the next-step block only.

It does not decide which workflow phase should run next. That decision is governed by:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`
- `docs/workflow/NEXT_STEP_TYPES.md`
- skill-specific `SKILL.md` files
