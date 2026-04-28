# Brainstorm Modes

Use these modes to classify the request before routing to a final decision.

The mode is not the final decision. The mode helps identify the dominant kind of uncertainty.

## 1. New Product / New Opportunity

Use when the user is exploring a new app, product, SaaS, internal tool, or major business capability.

Common final decisions:

- `NEW_PRD`
- `NEW_ARCHITECTURE`
- `NEW_ADR`
- `NEW_DOCUMENT_PLAN`
- `REJECT_OR_DEFER`

Bias toward `NEW_PRD` when product intent is not yet durable.

Choose Architecture only if the product intent is already clear enough and the missing artifact is system structure.

## 2. Feature Addition

Use when the product already exists and the user wants to add or expand a capability.

Common final decisions:

- `PRD_UPDATE`
- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`
- `NEW_ADR`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_DOCUMENT_PLAN`
- `REJECT_OR_DEFER`

Choose PRD update when user behavior, scope, goals, product rules, or success criteria change.

Choose Architecture when system structure or repo-level rules must become durable before later work.

Choose initiative roadmap when product/technical intent is already sufficiently clear and the next problem is sequencing.

## 3. User Report / Feedback / Problem Signal

Use when the trigger is user pain, bug patterns, workflow friction, operational incidents, or recurring complaints.

Common final decisions:

- `PRD_UPDATE`
- `ARCHITECTURE_UPDATE`
- `NEW_ADR`
- `NEW_INITIATIVE_ROADMAP`
- `NEW_DOCUMENT_PLAN`
- `REJECT_OR_DEFER`

Reject/defer if the signal is weak, anecdotal, or not yet connected to a meaningful product or technical problem.

## 4. Technical / Architecture Concern

Use when the main question is architecture, integration style, reliability, persistence, migration, messaging, deployment, observability, security posture, maintainability, or another durable technical concern.

Common final decisions:

- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`
- `NEW_ADR`
- `ADR_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `REJECT_OR_DEFER`

Bias toward Architecture when the missing context is broad system structure, boundaries, flows, runtime model, or repo conventions.

Bias toward ADR when alternatives exist and one bounded decision will constrain future implementation.

Do not choose ADR when the real gap is product intent or broad system structure.

## 5. Existing Product / Scope Change

Use when priorities, assumptions, user behavior, product boundaries, domain rules, architecture assumptions, or success criteria changed.

Common final decisions:

- `PRD_UPDATE`
- `ARCHITECTURE_UPDATE`
- `PRODUCT_ROADMAP_UPDATE`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_ADR`
- `DOCUMENT_PLAN_UPDATE`
- `REJECT_OR_DEFER`

Choose PRD update if product truth changed.

Choose Architecture update if system structure or durable technical context changed.

Choose roadmap update if product and architecture truth remain valid but sequencing changed.

## 6. Roadmap Shift / Delivery Reshaping

Use when the product or technical intent is already accepted and the main need is changing phase boundaries, sequencing, dependencies, risks, milestones, or exit criteria.

Common final decisions:

- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `REJECT_OR_DEFER`

Bias toward roadmap only when the intent is already clear enough.

If broad system structure is not durable enough to sequence work safely, choose Architecture before roadmap.

## 7. Documentation / Artifact Planning

Use when the main issue is deciding how to create, update, refactor, or sequence durable documents or artifact sets.

Common final decisions:

- `NEW_DOCUMENT_PLAN`
- `DOCUMENT_PLAN_UPDATE`
- `NEW_PRD`
- `PRD_UPDATE`
- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`
- `NEW_ADR`
- `REJECT_OR_DEFER`

Bias toward Document Plan when the product/technical direction is accepted and the remaining uncertainty is document production order, source artifacts, output artifacts, or acceptance criteria.

Do not choose Document Plan when the correct next artifact is already obvious and bounded.

## 8. Revisit / Deferred Idea

Use when the user returns to an old idea that was previously rejected, deferred, or unresolved.

Common final decisions:

- `NEW_PRD`
- `PRD_UPDATE`
- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`
- `NEW_ADR`
- `NEW_INITIATIVE_ROADMAP`
- `NEW_DOCUMENT_PLAN`
- `REJECT_OR_DEFER`

First check what evidence, constraint, or priority changed since the earlier defer decision.
