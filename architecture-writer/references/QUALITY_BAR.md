# Architecture Quality Bar

A good architecture document must pass these checks.

## 1. Boundary Clarity

A reader or coding agent can identify:

- where new code belongs
- where new code must not go
- which component owns which concern
- which data model is authoritative
- which integrations are allowed
- which cross-component calls are forbidden or constrained

## 2. Source-of-Truth Clarity

The document explicitly states source-of-truth ownership for important concepts.

Examples:

- membership authorization source
- invitation lifecycle source
- notification read model source
- audit trail source
- external system state source

Weak architecture leaves this implicit.

## 3. Runtime Flow Clarity

Important flows include:

- trigger
- validation
- transactional changes
- async side effects
- visible result
- failure handling

Do not write vague flow descriptions such as “process request and update data.”

## 4. Constraint Clarity

Constraints are explicit and reviewable.

Good constraints:

- "Invitation acceptance and membership creation must occur in the same database transaction."
- "Notification generation may be eventually consistent."
- "API responses must not expose JPA entities directly."

Weak constraints:

- "Handle consistency well."
- "Use clean architecture."
- "Make it reliable."

## 5. ADR Discipline

The architecture links ADRs for important decisions but does not duplicate full ADRs.

If a major decision lacks an ADR, the architecture marks it as an ADR candidate.

## 6. Roadmap Discipline

The architecture may mention sequencing implications, but does not become a roadmap.

No phase lists unless they describe architectural transition states, not delivery planning.

## 7. Plan Discipline

The architecture must not include one-task implementation steps.

No detailed file modification lists unless they are architecture-critical ownership boundaries.

## 8. Token Efficiency

The document is dense and navigable.

Avoid:

- generic theory
- repeated explanations
- long background history
- copied PRD content
- copied ADR content
- copied roadmap content
- excessive diagrams described in prose

## 9. Reviewability

A reviewer can use the document to say:

- implementation follows the architecture
- implementation violates the architecture
- implementation requires an ADR
- implementation requires architecture update
- architecture is outdated relative to code

## 10. Open Question Hygiene

Open questions are specific and actionable.

Each open question should state:

- what is unknown
- why it matters
- current assumption
- expected next artifact or decision path
