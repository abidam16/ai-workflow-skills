# Decision Rules

Use these rules in order. The selected decision should normally be the same value used in the final `next_step_type`.

## Rule 1: Reject or defer first

Choose `REJECT_OR_DEFER` when the problem is weak, unclear, low-value, too speculative, or missing material context. State what evidence or clarification would reopen the idea.

## Rule 2: Use lightweight mode before durable artifacts

Choose `CREATE_LIGHTWEIGHT_PLAN` only when the request satisfies `docs/workflow/LIGHTWEIGHT_TASK_MODE.md`.

If any lightweight condition is uncertain, route to the full artifact workflow.

## Rule 3: PRD owns product truth

Choose:

- `CREATE_PRD` when product intent is not yet durably defined.
- `UPDATE_PRD` when an existing PRD must change because product intent, behavior, scope, goals, rules, or success criteria changed.

Do not also route to architecture, ADR, roadmap, or plan in the same final decision.

## Rule 4: Architecture owns system shape

Choose:

- `CREATE_ARCHITECTURE` when product or technical intent is stable enough to define system shape, boundaries, ownership, flows, integrations, or cross-cutting constraints.
- `UPDATE_ARCHITECTURE` when an existing architecture document no longer reflects accepted system shape.

Do not choose architecture when product truth is missing, one narrow decision is the real blocker, delivery sequencing is the only uncertainty, or one executable task is already clear.

## Rule 5: ADR owns one durable decision

Choose:

- `CREATE_ADR` when the next blocker is one meaningful technical or architectural decision with credible alternatives and lasting consequences.
- `UPDATE_ADR` when an existing ADR must be updated or superseded according to the repo's ADR practice.

If the decision is broad system design, route to architecture instead.

## Rule 6: Roadmap owns sequencing

Choose:

- `CREATE_ROADMAP` when accepted product and technical intent are stable enough and staged delivery structure is missing.
- `UPDATE_ROADMAP` when an existing roadmap's phases, dependencies, risks, or exit criteria changed.

Do not use roadmap to redefine product behavior or architecture constraints.

## Rule 7: Plan owns one bounded task

Choose:

- `CREATE_PLAN` when one bounded implementation task is ready for a full plan.
- `UPDATE_PLAN` when an existing plan no longer matches the approved source artifacts or task scope.

Do not plan broad multi-task work. Use `SPLIT_INTO_PLANS` downstream when work must be split.

## Rule 8: Clarify or stop when routing is unsafe

Choose:

- `REQUEST_CLARIFICATION` when essential input is missing but can be asked directly.
- `STOP_AND_ESCALATE` when no safe workflow continuation exists without a human or upstream decision.

## Mandatory Concrete Next Step

Every final output must end with exactly one:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Use canonical `next_step_type` values from `docs/workflow/NEXT_STEP_TYPES.md`.

## Prompt Quality Rule

`suggested_prompt` must be directly copy-pasteable.

Good:

```text
Use `architecture-writer` to create `ARCHITECTURE.md` based on `docs/brainstorm/BRAINSTORM-002-modular-backend-architecture.md`.
```

Bad:

```text
Continue with the next step.
```
