# Create vs Update Guide

## Create a new PRD when

- no PRD exists for the product/initiative
- brainstorm selected `CREATE_PRD`
- the initiative is product-distinct from existing PRDs
- existing documents are notes, brainstorms, or architecture/roadmap/plan artifacts but no product-truth document exists

## Update an existing PRD when

- product goals changed
- target behavior changed
- user roles or permissions changed
- business/product rules changed
- success criteria changed
- open questions were resolved
- architecture, roadmap, implementation, or review exposed stale product truth

## Create only a delta when

- the user asks only for a change summary
- the repository prefers patch notes before editing the actual PRD
- the change is small and the target PRD section is obvious

## Route elsewhere when

- product truth is already stable and the next gap is architecture
- one technical decision needs ADR
- sequencing needs roadmap
- one implementation task needs plan
- implementation or review is requested

## Update discipline

Do not rewrite the whole PRD when a targeted update is enough.

When updating, preserve:

- existing stable product definitions
- accepted non-goals
- settled rules
- existing section style if it is clear

Only change what the new evidence requires.
