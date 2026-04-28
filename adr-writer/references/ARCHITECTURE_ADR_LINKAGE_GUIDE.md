# Architecture-ADR Linkage Guide

## Purpose

ADRs and architecture must remain connected without duplicating each other.

- `ARCHITECTURE.md` tells agents what system shape to obey.
- ADRs tell agents why a specific decision exists.

## Linkage classifications

### `NONE`

Use when the decision is technical but does not affect architecture documents.

Example: choosing a local test fixture style for one small module.

### `ARCHITECTURE_CONTEXT_ONLY`

Use when architecture provides context, but the ADR does not change architecture.

Example: deciding a small implementation strategy within an already-defined architecture rule.

### `ADD_ADR_INDEX_ENTRY`

Use when architecture already says the right thing but should link to the new ADR for rationale.

Architecture update needed: add an ADR index row only.

### `UPDATE_ROOT_ARCHITECTURE`

Use when the ADR changes stable repo/product-level architecture.

Examples:

- new source-of-truth rule
- new cross-cutting consistency rule
- new integration pattern
- changed module/service ownership

### `UPDATE_INITIATIVE_ARCHITECTURE`

Use when the decision affects only an active initiative document under `docs/architecture/`.

### `UPDATE_ROOT_AND_INITIATIVE_ARCHITECTURE`

Use when an initiative decision also changes stable root architecture rules.

### `ARCHITECTURE_CONFLICT_FOUND`

Use when the chosen decision contradicts current architecture. The next step should usually be `UPDATE_ARCHITECTURE` or `RETURN_TO_ARCHITECTURE`.

### `ARCHITECTURE_MISSING`

Use when a valid ADR cannot be written safely because the broad architecture context is missing.

The next step should usually be `RETURN_TO_ARCHITECTURE`.

## What to include in the ADR

Include:

- affected architecture document path
- affected architecture section names
- the exact constraint the ADR establishes
- whether architecture must be updated before roadmap or plan

Do not include:

- full component maps
- long runtime-flow design
- complete data architecture
- roadmap phases
- task implementation steps

## Preferred loop

```text
Architecture identifies ADR candidate
-> ADR records one decision
-> Architecture links ADR and reflects stable constraint
-> Roadmap/Plan consume architecture constraint
```
