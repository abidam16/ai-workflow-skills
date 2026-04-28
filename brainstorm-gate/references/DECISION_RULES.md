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
- roadmap, architecture, ADR, implementation, or review learning changes the product truth

If `NEW_PRD` or `PRD_UPDATE` is chosen, do not also choose architecture, ADR, roadmap, or document plan in the same final decision.

The correct next step is the PRD phase. Architecture, ADR, roadmap, and document plan may follow after PRD if needed.

## Rule 3: Architecture Is for Durable System Structure

Choose `NEW_ARCHITECTURE` when:

- no durable architecture document exists and future work would depend on system-level context
- the idea requires system structure before roadmap, ADR, document plan, or implementation
- module boundaries, layers, integrations, runtime model, deployment shape, data flow, ownership boundaries, or dependency rules are unclear
- multiple future tasks or decisions need the same system-level context
- the next skill needs a durable system map, not one decision record

Choose `ARCHITECTURE_UPDATE` when:

- an architecture document already exists
- system structure changed materially
- module boundaries, integration patterns, runtime model, deployment shape, dependency rules, or cross-cutting conventions need revision
- existing architecture guidance would mislead future implementation
- the change is broader than one ADR but does not change core product truth

Do not choose Architecture when:

- the problem is product intent or user-facing behavior; choose PRD
- the question is one bounded technical decision with clear options; choose ADR
- the question is delivery sequencing; choose roadmap
- the question is planning one bounded document-writing task; choose document plan
- the question is one implementation task; use an execution/implementation planning skill instead

Hard threshold:

```text
Choose Architecture only when multiple future decisions or tasks need the same system-level context.
```

## Rule 4: ADR Is for One Lasting Technical Decision

Choose `NEW_ADR` when:

- the immediate need is to record one meaningful technical or architectural decision
- alternatives exist and trade-offs matter
- the decision will constrain later implementation
- the decision affects reliability, scalability, integration style, persistence, security, deployment, observability, maintainability, or developer workflow
- product intent is already clear enough for this technical decision
- architecture context is already clear enough, or the decision boundary is narrow enough to stand alone

Choose `ADR_UPDATE` only when:

- the workflow intentionally maintains an existing ADR in place
- the change is truly a correction or update to the same decision
- the repo's ADR practice allows mutation of existing ADRs

Preferred default:

- create a new ADR and mark older ADRs as superseded when the decision materially changes

Do not choose ADR when the real gap is broad system structure. Choose Architecture first.

## Rule 5: Roadmap Is for Sequencing Already-Accepted Intent

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

Do not choose roadmap when broad system structure is missing or stale. Choose Architecture first.

Do not choose roadmap when the only unresolved issue is a technical decision. Choose ADR first.

## Rule 6: Document Plan Is for Planning Artifact Production or Refactor

Choose `NEW_DOCUMENT_PLAN` when:

- the product/technical intent is already accepted
- the user wants to produce one or more durable documents but the document-production scope must be planned first
- the next need is defining which documents to create, how they relate, what order to produce them in, or what context each document must consume
- a documentation refactor is needed, but there is no existing document plan

Choose `DOCUMENT_PLAN_UPDATE` when:

- an existing document plan exists
- the set of documents, order, source artifacts, acceptance criteria, or handoff assumptions changed
- the plan needs refactor rather than a new plan

Do not choose document plan when:

- the next artifact is already obvious and bounded; route directly to that artifact
- product truth is missing; choose PRD
- system structure is missing; choose Architecture
- the issue is one technical decision; choose ADR
- the issue is phased delivery sequencing; choose Roadmap

## Rule 7: One Final Decision Only

If multiple artifacts seem relevant, choose the immediate next artifact, not the full downstream chain.

Examples:

- Product idea is unclear and also needs architecture later: choose `NEW_PRD`, not Architecture.
- System boundaries are unclear and several ADRs may follow: choose `NEW_ARCHITECTURE`, not ADR.
- Technical choice is blocking implementation and alternatives matter: choose `NEW_ADR`, not document plan.
- Product intent and ADR are accepted but delivery order is unclear: choose roadmap.
- The user needs to organize several documentation outputs after intent is accepted: choose document plan.
- Idea is weak or under-evidenced: choose `REJECT_OR_DEFER`.

## Rule 8: Artifact Action Must Match Workflow Need

Choose `CREATE_DURABLE_BRAINSTORM_ARTIFACT` when the brainstorm output will feed another skill or later workflow phase.

Choose `UPDATE_EXISTING_BRAINSTORM_ARTIFACT` when the user is revising a prior brainstorm artifact.

Choose `CHAT_ONLY_NO_ARTIFACT` when the brainstorm is lightweight and no stable handoff is needed.

## Mandatory Next-Step Wording

Use one of these patterns:

```text
Immediate next step: Proceed to NEW_PRD.
Immediate next step: Proceed to PRD_UPDATE.
Immediate next step: Proceed to NEW_ARCHITECTURE.
Immediate next step: Proceed to ARCHITECTURE_UPDATE.
Immediate next step: Proceed to NEW_ADR.
Immediate next step: Proceed to ADR_UPDATE.
Immediate next step: Proceed to NEW_PRODUCT_ROADMAP.
Immediate next step: Proceed to PRODUCT_ROADMAP_UPDATE.
Immediate next step: Proceed to NEW_INITIATIVE_ROADMAP.
Immediate next step: Proceed to INITIATIVE_ROADMAP_UPDATE.
Immediate next step: Proceed to NEW_DOCUMENT_PLAN.
Immediate next step: Proceed to DOCUMENT_PLAN_UPDATE.
Immediate next step: Stop here. Do not proceed until stronger evidence exists.
```

## Mandatory Continuation Prompt Wording

Use one of these patterns:

```text
Proceed to create the PRD based on <brainstorm artifact path>.
Proceed to update the PRD based on <brainstorm artifact path>.
Proceed to create the architecture document based on <brainstorm artifact path>.
Proceed to update the architecture document based on <brainstorm artifact path>.
Proceed to create the ADR based on <brainstorm artifact path>.
Proceed to update the ADR based on <brainstorm artifact path>.
Proceed to create the product roadmap based on <brainstorm artifact path>.
Proceed to update the product roadmap based on <brainstorm artifact path>.
Proceed to create the initiative roadmap based on <brainstorm artifact path>.
Proceed to update the initiative roadmap based on <brainstorm artifact path>.
Proceed to create the document plan based on <brainstorm artifact path>.
Proceed to update the document plan based on <brainstorm artifact path>.
Stop here and revisit after gathering stronger evidence.
```

For chat-only output, use "this brainstorm output" instead of an artifact path.
