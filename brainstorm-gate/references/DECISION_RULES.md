# Decision Rules

Use these rules in order.

## Rule 1: Reject or defer first
Choose `REJECT_OR_DEFER` if any of these are true:
- the problem is weak, unclear, or low-value
- the idea solves little meaningful pain
- the signal is too speculative to justify documentation
- the current information is insufficient for a responsible next artifact

When rejecting or deferring, still state exactly what evidence or clarification would reopen the idea.

## Rule 2: PRD takes priority when product truth is missing or changing
Choose `NEW_PRD` when:
- the idea is new and product intent is not yet defined in a PRD
- the problem, users, goals, scope, flows, or rules must be established

Choose `PRD_UPDATE` when:
- an existing PRD already exists
- the change affects product intent, user-facing behavior, scope, goals, rules, or success criteria

If `NEW_PRD` or `PRD_UPDATE` is chosen, do **not** also choose roadmap in the same final decision.
The correct next step is the PRD phase.
After PRD, roadmap may follow if needed.

## Rule 3: ADR is for lasting technical decisions
Choose `NEW_ADR` when:
- the immediate need is to record one meaningful technical or architectural decision
- alternatives exist and trade-offs matter
- the decision will constrain later implementation

Choose `ADR_UPDATE` only when:
- your workflow intentionally maintains an existing ADR record in-place
- the change is truly an update to the same decision rather than a superseding decision

If your ADR practice prefers superseding instead of updating, note that clearly.

## Rule 4: Roadmap is for sequencing already-accepted intent
Choose `NEW_PRODUCT_ROADMAP` when:
- the product direction is already accepted
- there is no suitable strategic roadmap yet
- the next need is phased product sequencing

Choose `PRODUCT_ROADMAP_UPDATE` when:
- a product-level roadmap already exists
- strategic themes, phases, or sequencing changed

Choose `NEW_INITIATIVE_ROADMAP` when:
- the product or technical intent is already sufficiently clear
- the next need is a focused delivery sequence for one feature, refactor, migration, or initiative
- there is no suitable existing initiative roadmap

Choose `INITIATIVE_ROADMAP_UPDATE` when:
- the initiative already has a roadmap
- the scope, sequencing, dependencies, risks, or exit criteria changed

## Rule 5: One final decision only
At the end of the brainstorm, choose exactly one final decision.
If multiple artifacts seem relevant, choose the immediate next artifact, not the full downstream chain.

## Mandatory next-step wording
The final output must include an explicit line in this pattern:
- `Immediate next step: Proceed to NEW_PRD.`
- `Immediate next step: Proceed to PRD_UPDATE.`
- `Immediate next step: Proceed to NEW_INITIATIVE_ROADMAP.`
- `Immediate next step: Proceed to NEW_ADR.`
- `Immediate next step: Stop here. Do not proceed until stronger evidence exists.`

The final output must also include a direct continuation prompt in this pattern:
- `Proceed to create the PRD based on this brainstorm output.`
- `Proceed to update the PRD based on this brainstorm output.`
- `Proceed to create the initiative roadmap based on this brainstorm output.`
- `Proceed to create the ADR based on this brainstorm output.`
- `Stop here and revisit after gathering stronger evidence.`
