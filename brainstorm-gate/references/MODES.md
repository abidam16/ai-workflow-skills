# Brainstorm Modes

Use these modes to classify the request before routing to a final decision.

The mode is not the final decision. The mode helps identify the dominant kind of uncertainty.

## 1. New Product / New Opportunity

Use when the user is exploring a new app, product, SaaS, internal tool, or major business capability.

Common final decisions:

- `NEW_PRD`
- `NEW_ADR`
- `REJECT_OR_DEFER`

Bias toward `NEW_PRD` when product intent is not yet durable.

## 2. Feature Addition

Use when the product already exists and the user wants to add or expand a capability.

Common final decisions:

- `PRD_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_ADR`
- `REJECT_OR_DEFER`

Choose PRD update when user behavior, scope, goals, product rules, or success criteria change.

Choose initiative roadmap when product intent is already sufficiently clear and the next problem is sequencing.

## 3. User Report / Feedback / Problem Signal

Use when the trigger is user pain, bug patterns, workflow friction, operational incidents, or recurring complaints.

Common final decisions:

- `PRD_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `NEW_ADR`
- `REJECT_OR_DEFER`

Reject/defer if the signal is weak, anecdotal, or not yet connected to a meaningful product or technical problem.

## 4. Technical / Architecture Concern

Use when the main question is architecture, integration style, reliability, persistence, migration, messaging, deployment, observability, security posture, or another durable technical choice.

Common final decisions:

- `NEW_ADR`
- `ADR_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `REJECT_OR_DEFER`

Bias toward ADR when alternatives exist and the decision will constrain future implementation.

Do not choose ADR when the real gap is product intent.

## 5. Existing Product / Scope Change

Use when priorities, assumptions, user behavior, product boundaries, domain rules, or success criteria changed.

Common final decisions:

- `PRD_UPDATE`
- `PRODUCT_ROADMAP_UPDATE`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_ADR`
- `REJECT_OR_DEFER`

Choose PRD update if product truth changed.

Choose roadmap update if product truth remains valid but sequencing changed.

## 6. Roadmap Shift / Delivery Reshaping

Use when the product or technical intent is already accepted and the main need is changing phase boundaries, sequencing, dependencies, risks, milestones, or exit criteria.

Common final decisions:

- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `REJECT_OR_DEFER`

Bias toward roadmap only when the intent is already clear enough.

## 7. Revisit / Deferred Idea

Use when the user returns to an old idea that was previously rejected, deferred, or unresolved.

Common final decisions:

- `NEW_PRD`
- `PRD_UPDATE`
- `NEW_ADR`
- `NEW_INITIATIVE_ROADMAP`
- `REJECT_OR_DEFER`

First check what evidence, constraint, or priority changed since the earlier defer decision.
