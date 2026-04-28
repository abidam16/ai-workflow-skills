# Create vs Update Rules

## Output Modes

Choose exactly one:

- `CREATE_ROOT_ARCHITECTURE`
- `UPDATE_ROOT_ARCHITECTURE`
- `CREATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `ROUTE_TO_PRD`
- `ROUTE_TO_ADR`
- `ROUTE_TO_ROADMAP`
- `ROUTE_TO_PLAN`
- `INSUFFICIENT_INPUT`

## Create Root Architecture

Choose `CREATE_ROOT_ARCHITECTURE` when:

- no canonical repo/product architecture document exists
- future implementation needs a stable system-shape source of truth
- existing docs are scattered, obsolete, or not authoritative
- multiple future tasks need common architectural constraints
- the repo/product lacks clear component, module, service, data, or integration boundaries

Default path:

```text
ARCHITECTURE.md
```

## Update Root Architecture

Choose `UPDATE_ROOT_ARCHITECTURE` when:

- root `ARCHITECTURE.md` exists
- the same product/repo scope remains valid
- stable system shape, boundaries, data ownership, integration rules, or cross-cutting constraints changed
- an initiative has finished and its stable conclusions should be folded into the root file
- root architecture needs links to active initiative architecture documents

Do not update root architecture with temporary delivery sequencing, task lists, or speculative design.

## Create Initiative Architecture

Choose `CREATE_INITIATIVE_ARCHITECTURE` when:

- the initiative is large, transitional, or multi-component
- root `ARCHITECTURE.md` would become too long or noisy if the full design were added there
- several future `PLAN.md` files need the same initiative-level system context
- the initiative affects multiple modules/services, data ownership, integration flows, authorization, consistency, deployment, or observability
- several ADRs may be needed but the broader target system shape must be captured first

Default path:

```text
docs/architecture/<initiative-slug>-architecture.md
```

## Update Initiative Architecture

Choose `UPDATE_INITIATIVE_ARCHITECTURE` when:

- an initiative architecture document already exists
- the initiative scope remains the same
- design boundaries, runtime flows, data ownership, constraints, ADR links, or open questions changed
- implementation learning updates the target architecture without changing the initiative identity

## Route to PRD

Choose `ROUTE_TO_PRD` when:

- product intent is unclear
- user behavior, business rules, scope, or success criteria are unresolved
- architecture would require guessing the product truth
- the requested architecture change is actually a product behavior decision

## Route to ADR

Choose `ROUTE_TO_ADR` when:

- the problem is one bounded technical decision
- the main work is comparing options and recording the chosen option
- the broader architecture context already exists
- the decision should be historical rather than living documentation

## Route to Roadmap

Choose `ROUTE_TO_ROADMAP` when:

- product and architecture intent are stable enough
- the next problem is phased delivery, sequencing, dependencies, risks, and exit criteria
- no new architecture rule is needed before planning delivery

## Route to PLAN

Choose `ROUTE_TO_PLAN` when:

- product and architecture intent are already clear
- the next need is one executable task contract
- no broad architecture update is needed

## Insufficient Input

Choose `INSUFFICIENT_INPUT` only when missing information blocks safe architecture drafting.

Do not overuse this. Prefer conservative assumptions plus `Open Architecture Questions` when progress is possible.

Minimum blocking examples:

- no product intent and no existing PRD
- no codebase or system context for an update that must match reality
- conflicting source artifacts with no clear authority order
- missing decision about whether the architecture is root-level or initiative-level
