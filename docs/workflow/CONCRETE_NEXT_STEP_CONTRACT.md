# CONCRETE_NEXT_STEP_CONTRACT.md

Purpose: define the shared terminal output contract used by every AI workflow phase so no artifact, review, implementation report, or blocker report ends without a concrete routed next action.

---

## 1. Core Rule

Every workflow phase must end with exactly one `Concrete Next Step` block.

A phase may produce analysis, a document, a delta, a blocker report, a review report, or a rejection/defer decision, but it must still finish with one explicit next action.

Do not end with vague statements such as:

- "review is complete"
- "continue development"
- "fix the issues"
- "proceed as needed"
- "the next step is implementation" without target, action, and reason

The next step must be actionable by the user or by the next AI agent invocation.

---

## 2. Canonical Block

Every phase output must end with this exact section heading and field set:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

### Field meaning

| Field | Meaning |
|---|---|
| `next_step_type` | A canonical routing label from `docs/workflow/NEXT_STEP_TYPES.md`. Use exact `UPPER_SNAKE_CASE`; do not invent local variants. |
| `target` | The exact artifact, file, phase, or action target. Examples: `ARCHITECTURE.md`, `docs/adr/0003-use-outbox.md`, `ROADMAP.md`, `PLAN.md`, implementation, review. |
| `action` | The concrete action to perform next. Use imperative wording: create, update, revise, implement, review, validate, split, stop. |
| `why_this_is_next` | The reason this is the correct immediate next step based on artifact authority, readiness, blockers, or findings. |
| `blocking_condition` | What must be true before moving beyond this next step. Use `none` only when the next step is unblocked. |
| `suggested_prompt` | A ready-to-copy prompt for the next agent invocation. It must include the target artifact/action and the key constraints to preserve. |

---

## 3. Canonical Next-Step Types

`next_step_type` values are defined in `docs/workflow/NEXT_STEP_TYPES.md`.

Rules:

- use exact canonical values from `NEXT_STEP_TYPES.md`
- prefer specific create/update values such as `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE`
- do not use combined values such as `CREATE_OR_UPDATE_ARCHITECTURE`
- do not use brainstorm routing decisions such as `NEW_PRD` as terminal `next_step_type` values
- do not invent vague values such as `CONTINUE_DEVELOPMENT`, `FIX_ISSUES`, or `UPDATE_DOCS`

During migration, deprecated aliases may be accepted only as temporary warnings. Final workflow output should use canonical values.

---

## 4. Required Quality Bar

A valid `Concrete Next Step` block must be:

- singular: exactly one immediate next action
- routed: points to the correct artifact or workflow phase
- concrete: names the target and action
- justified: explains why this is next
- bounded: states the blocking condition or `none`
- usable: includes a prompt the user can copy into the next agent run

---

## 5. Prohibited Next-Step Output

Do not use vague `action` values:

- continue
- proceed
- fix issues
- improve code
- polish implementation
- review later
- address feedback
- update docs

Use specific actions instead:

- update `ARCHITECTURE.md` to reflect the accepted ADR constraint
- revise `PLAN.md` to include missing authorization validation
- return to implementation to fix the transaction boundary violation
- create one ADR for the outbox publishing decision
- run task review against `PLAN.md`, implementation diff, and validation evidence

---

## 6. Relationship to Handoffs

`Concrete Next Step` is the terminal routing block.

A handoff may also contain compact fields such as `decision`, `source_artifacts`, `constraints`, `architecture_constraints`, and `open_questions`, but the final user-visible action must be expressed through `Concrete Next Step`.

Legacy field names such as `Immediate Next Step`, `Continuation Prompt`, or plain `next_step` should be treated as superseded by this contract.

During migration, a document may keep `next_step` only as an internal handoff field, but the final output must still include the canonical `Concrete Next Step` block.

---

## 7. Artifact-Specific Guidance

### Brainstorm

The next step should route to exactly one artifact or stop condition.

Common targets:

- `PRD.md`
- `ARCHITECTURE.md`
- `docs/architecture/<initiative-slug>-architecture.md`
- `docs/adr/<number>-<decision>.md`
- `ROADMAP.md`
- reject/defer decision

### PRD

The next step should usually route to architecture, ADR, roadmap, plan, revision, or stop.

The PRD must not design architecture. If system shape is the next uncertainty, route to architecture.

### Architecture

The next step should usually route to ADR, roadmap, plan, PRD revision, architecture revision, or stop.

Architecture-producing phases may still include architecture-specific fields such as `Architecture Scope`, `Architecture Path`, `ADR Impact`, `Roadmap Impact`, and `Plan Readiness`, but the final action must use `Concrete Next Step`.

### ADR

The next step should usually route to architecture update, roadmap, plan, superseding ADR, PRD revision, or stop.

If the accepted decision changes system shape or constraints, route back to architecture.

### Roadmap

The next step should usually route to one single-task plan, roadmap revision, architecture/ADR update, or stop.

Do not route directly to implementation unless a valid one-task plan already exists.

### Plan

The next step should usually route to implementation, plan revision, split into multiple plans, architecture/ADR update, or stop.

If `decision != PROCEED_TO_IMPLEMENTATION`, do not route to implementation.

### Implementation

The next step should usually route to review, validation, minor fix, plan update, architecture update, ADR, or stop.

If implementation found a source conflict, route to the artifact that must resolve the conflict.

### Review

The next step must state what the user or agent should do after the review verdict.

Examples:

- merge/close task
- apply minor fixes
- return to implementation
- update plan
- update architecture
- create/update ADR
- update roadmap
- update PRD
- request missing evidence
- split review scope
- start next plan
- stop/escalate

---

## 8. Review Rule

A review report is invalid if it gives a verdict without a concrete next step.

Valid example:

```md
## Concrete Next Step

- `next_step_type`: RETURN_TO_IMPLEMENTATION
- `target`: `src/main/kotlin/.../InvitationService.kt`
- `action`: Fix the missing membership transaction update and rerun the affected service tests.
- `why_this_is_next`: The implementation follows the API behavior but violates the architecture rule that invitation acceptance and membership creation must occur in the same transaction.
- `blocking_condition`: The task cannot be approved until the transaction boundary violation is fixed and validated.
- `suggested_prompt`: "Use implement-task to revise the invitation acceptance implementation so it creates membership and marks the invitation accepted in the same transaction, preserving the architecture constraints from `ARCHITECTURE.md` and the approved `PLAN.md`."
```

Invalid example:

```md
Review complete. Fix the issues and continue development.
```

---

## 9. Token Efficiency Rule

Keep the `Concrete Next Step` block compact.

Do not repeat the full review, PRD, architecture, ADR, roadmap, or plan content inside `suggested_prompt`. Include only:

- target artifact/action
- relevant constraint references
- the immediate objective
- the blocking condition if important

