# Decision Rules

Use these rules in order.

The final output must choose exactly one decision.

## Rule 1: Reject or Defer First

Choose `REJECT_OR_DEFER` when any of these are true:

- the problem is weak, unclear, or low-value
- the idea solves little meaningful pain
- the signal is too speculative
- the idea is premature relative to current priorities
- required evidence is missing
- the user cannot yet define who is affected or why it matters
- the cost/risk is obviously disproportionate to the expected value

When rejecting or deferring, still state what would reopen the idea.

Common reopen conditions:

- stronger user evidence
- clearer business value
- clearer product scope
- clearer technical constraints
- priority change
- recurring operational pain

## Rule 2: PRD Takes Priority When Product Truth Is Missing or Changing

Choose `NEW_PRD` when:

- the idea is new and product intent does not exist in durable form
- the problem, users, goals, non-goals, scope, flows, or rules must be established
- the idea defines a new product, major capability, or meaningful user-facing behavior
- downstream agents would otherwise need to infer product truth from chat history

Choose `PRD_UPDATE` when:

- an existing PRD exists
- the change affects product intent, user-facing behavior, scope, goals, non-goals, product rules, current behavior, target behavior, or success criteria
- roadmap or implementation learning changes the product truth

If `NEW_PRD` or `PRD_UPDATE` is chosen, do not also choose roadmap in the same final decision.

The correct next step is the PRD phase. Roadmap may follow after PRD if needed.

## Rule 3: ADR Is for Lasting Technical Decisions

Choose `NEW_ADR` when:

- the immediate need is to record one meaningful technical or architectural decision
- alternatives exist and trade-offs matter
- the decision will constrain later implementation
- the decision affects reliability, scalability, integration style, persistence, security, deployment, observability, or maintainability
- product intent is already clear enough for this technical decision

Choose `ADR_UPDATE` only when:

- the workflow intentionally maintains an existing ADR in place
- the change is truly a correction or update to the same decision
- the repo's ADR practice allows mutation of existing ADRs

Preferred default:

- create a new ADR and mark older ADRs as superseded when the decision materially changes

## Rule 4: Roadmap Is for Sequencing Already-Accepted Intent

Choose `NEW_PRODUCT_ROADMAP` when:

- the product direction is already accepted
- there is no suitable strategic roadmap yet
- the next need is phased product sequencing across larger product direction

Choose `PRODUCT_ROADMAP_UPDATE` when:

- a product-level roadmap already exists
- strategic themes, phases, priorities, milestones, or sequencing changed

Choose `NEW_INITIATIVE_ROADMAP` when:

- product or technical intent is already sufficiently clear
- the next need is a focused delivery sequence for one feature, refactor, migration, integration, or initiative
- there is no suitable existing initiative roadmap

Choose `INITIATIVE_ROADMAP_UPDATE` when:

- the initiative already has a roadmap
- scope, sequencing, dependencies, risks, milestones, or exit criteria changed

Do not choose roadmap when product truth is missing or changing. Choose PRD first.

Do not choose roadmap when the only unresolved issue is a technical decision. Choose ADR first.

## Rule 5: One Final Decision Only

If multiple artifacts seem relevant, choose the immediate next artifact, not the full downstream chain.

Examples:

- Product idea is unclear and also needs sequencing later: choose `NEW_PRD`, not roadmap.
- Technical choice is blocking implementation and alternatives matter: choose `NEW_ADR`, not plan.
- Product intent and ADR are accepted but delivery order is unclear: choose roadmap.
- Idea is weak or under-evidenced: choose `REJECT_OR_DEFER`.

## Rule 6: Artifact Action Must Match Workflow Need

Choose `CREATE_DURABLE_BRAINSTORM_ARTIFACT` when the brainstorm output will feed another skill or later workflow phase.

Choose `UPDATE_EXISTING_BRAINSTORM_ARTIFACT` when the user is revising a prior brainstorm artifact.

Choose `CHAT_ONLY_NO_ARTIFACT` when the brainstorm is lightweight and no stable handoff is needed.

## Mandatory Next-Step Wording

Use one of these patterns:

```text
Immediate next step: Proceed to NEW_PRD.
Immediate next step: Proceed to PRD_UPDATE.
Immediate next step: Proceed to NEW_PRODUCT_ROADMAP.
Immediate next step: Proceed to PRODUCT_ROADMAP_UPDATE.
Immediate next step: Proceed to NEW_INITIATIVE_ROADMAP.
Immediate next step: Proceed to INITIATIVE_ROADMAP_UPDATE.
Immediate next step: Proceed to NEW_ADR.
Immediate next step: Proceed to ADR_UPDATE.
Immediate next step: Stop here. Do not proceed until stronger evidence exists.
```

## Mandatory Continuation Prompt Wording

Use one of these patterns:

```text
Proceed to create the PRD based on <brainstorm artifact path>.
Proceed to update the PRD based on <brainstorm artifact path>.
Proceed to create the product roadmap based on <brainstorm artifact path>.
Proceed to update the product roadmap based on <brainstorm artifact path>.
Proceed to create the initiative roadmap based on <brainstorm artifact path>.
Proceed to update the initiative roadmap based on <brainstorm artifact path>.
Proceed to create the ADR based on <brainstorm artifact path>.
Proceed to update the ADR based on <brainstorm artifact path>.
Stop here and revisit after gathering stronger evidence.
```

For chat-only output, use "this brainstorm output" instead of an artifact path.
