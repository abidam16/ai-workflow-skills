# Decision Rules

Use these rules in order.

## Rule 1: Reject or defer first

Choose `REJECT_OR_DEFER` if any of these are true:

- the problem is weak, unclear, or low-value
- the idea solves little meaningful pain
- the signal is too speculative to justify documentation
- the current information is insufficient for a responsible next artifact

When rejecting or deferring, still state exactly what evidence or clarification would reopen the idea.

The final output must still end with a `Concrete Next Step` block.

## Rule 2: PRD takes priority when product truth is missing or changing

Choose `NEW_PRD` when:

- the idea is new and product intent is not yet defined in a PRD
- the problem, users, goals, scope, flows, or rules must be established

Choose `PRD_UPDATE` when:

- an existing PRD already exists
- the change affects product intent, user-facing behavior, scope, goals, rules, or success criteria

If `NEW_PRD` or `PRD_UPDATE` is chosen, do **not** also choose architecture, ADR, roadmap, or document plan in the same final decision.

The correct next step is the PRD phase. After PRD, architecture, ADR, roadmap, or plan may follow if needed.

## Rule 3: Architecture is for shared system shape

Choose `NEW_ARCHITECTURE` when:

- product or technical intent is stable enough to define system shape
- multiple future decisions or tasks need shared system-level context
- component boundaries, data ownership, runtime flows, integration boundaries, security, consistency, deployment, or observability rules must be made durable
- implementation would likely drift without a system-shape source of truth

Choose `ARCHITECTURE_UPDATE` when:

- an existing `ARCHITECTURE.md` or initiative architecture document exists
- the accepted system shape, component boundaries, data ownership, runtime flow, integration model, deployment assumptions, or cross-cutting rules changed

Do not choose Architecture when:

- the unresolved issue is one bounded technical choice with alternatives and consequences; choose ADR instead
- product truth is missing; choose PRD instead
- delivery sequencing is the only unresolved issue; choose roadmap instead
- one executable task is already clear; choose plan instead

## Rule 4: ADR is for one lasting technical decision

Choose `NEW_ADR` when:

- the immediate need is to record one meaningful technical or architectural decision
- alternatives exist and trade-offs matter
- the decision will constrain later implementation
- the broader architecture context already exists or is not needed for this one bounded decision

Choose `ADR_UPDATE` only when:

- your workflow intentionally maintains an existing ADR record in-place
- the change is truly an update to the same decision rather than a superseding decision

If your ADR practice prefers superseding instead of updating, note that clearly.

## Rule 5: Roadmap is for sequencing already-accepted intent

Choose `NEW_PRODUCT_ROADMAP` when:

- the product direction is already accepted
- there is no suitable strategic roadmap yet
- the next need is phased product sequencing

Choose `PRODUCT_ROADMAP_UPDATE` when:

- a product-level roadmap already exists
- strategic themes, phases, or sequencing changed

Choose `NEW_INITIATIVE_ROADMAP` when:

- the product or technical intent is already sufficiently clear
- architecture and relevant ADR constraints are sufficient for sequencing, when applicable
- the next need is a focused delivery sequence for one feature, refactor, migration, or initiative
- there is no suitable existing initiative roadmap

Choose `INITIATIVE_ROADMAP_UPDATE` when:

- the initiative already has a roadmap
- the scope, sequencing, dependencies, risks, or exit criteria changed

## Rule 6: Document plan is for bounded documentation work

Choose `NEW_DOCUMENT_PLAN` when:

- the accepted need is to produce or refactor a bounded documentation artifact or artifact set
- the next problem is documentation production planning, not product, architecture, ADR, roadmap, implementation, or review

Choose `DOCUMENT_PLAN_UPDATE` when:

- an existing document plan exists
- the source artifacts, target artifacts, sequence, acceptance criteria, or constraints changed

## Rule 7: One final decision only

At the end of the brainstorm, choose exactly one final decision.

If multiple artifacts seem relevant, choose the immediate next artifact/action, not the full downstream chain.

## Mandatory Concrete Next Step

The final output must end with this exact block:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use the old terminal fields as the final output contract:

- `Immediate next step`
- `Continuation prompt`

Those concepts now belong inside the normalized `Concrete Next Step` block.

## Recommended Next Step Mapping

| Decision | Recommended `next_step_type` | Target |
|---|---|---|
| `NEW_PRD` | `CREATE_PRD` | `PRD.md` |
| `PRD_UPDATE` | `UPDATE_PRD` | existing `PRD.md` |
| `NEW_ARCHITECTURE` | `CREATE_ARCHITECTURE` | `ARCHITECTURE.md` or initiative architecture doc |
| `ARCHITECTURE_UPDATE` | `UPDATE_ARCHITECTURE` | existing architecture document |
| `NEW_ADR` | `CREATE_ADR` | `docs/adr/<number>-<decision>.md` |
| `ADR_UPDATE` | `UPDATE_ADR` | existing ADR |
| `NEW_PRODUCT_ROADMAP` | `CREATE_PRODUCT_ROADMAP` | product `ROADMAP.md` |
| `PRODUCT_ROADMAP_UPDATE` | `UPDATE_PRODUCT_ROADMAP` | product `ROADMAP.md` |
| `NEW_INITIATIVE_ROADMAP` | `CREATE_INITIATIVE_ROADMAP` | initiative roadmap |
| `INITIATIVE_ROADMAP_UPDATE` | `UPDATE_INITIATIVE_ROADMAP` | existing initiative roadmap |
| `NEW_DOCUMENT_PLAN` | `CREATE_DOCUMENT_PLAN` | document plan |
| `DOCUMENT_PLAN_UPDATE` | `UPDATE_DOCUMENT_PLAN` | existing document plan |
| `REJECT_OR_DEFER` | `REJECT_OR_DEFER` or `STOP` | no downstream artifact |

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
