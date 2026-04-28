# Architecture Boundary Guide

## Architecture vs PRD

Use PRD when the question is:

> What should the product do, for whom, and why?

Use architecture when the question is:

> How should the system be shaped to support approved product intent?

PRD owns:

- product goals
- non-goals
- users and roles
- user-facing behavior
- business rules
- success criteria
- product constraints

Architecture owns:

- component boundaries
- data ownership
- runtime flows
- integration boundaries
- consistency and transaction rules
- security and authorization source-of-truth rules
- observability and deployment assumptions

If product behavior is still unclear, route to PRD before architecture.

## Architecture vs ADR

Use ADR when the question is:

> Which one technical option should we choose, and why?

Use architecture when the question is:

> What is the current or target system shape that future work must obey?

Architecture is broader and living.

ADR is narrower and historical.

Architecture may link many ADRs. Do not copy full ADR contents into architecture.

Create an ADR when a section of architecture depends on a meaningful decision with alternatives, trade-offs, and long-term consequences.

## Architecture vs Roadmap

Use roadmap when the question is:

> In what sequence should we deliver the work?

Use architecture when the question is:

> What structural rules must the delivered work obey?

Architecture may mention roadmap implications, but it must not become a phase plan.

Roadmap may reference architecture dependencies, but it must not redefine architecture.

## Architecture vs PLAN

Use PLAN when the question is:

> What exactly should be implemented now as one bounded task?

Use architecture when the question is:

> What system-level constraints should many tasks obey?

Architecture can guide many plans. A plan should not create new architecture unless explicitly scoped as an architecture update.

## Architecture vs Implementation

Use implementation workflow when the approved plan exists and code should be changed.

Architecture does not contain detailed code patches, migration scripts, class-by-class designs, or full endpoint implementation steps.

## Architecture vs Review

Use review when completed work must be compared against the approved artifacts.

Review should check whether implementation obeys architecture, ADRs, roadmap, PRD, and plan.

## Common Misrouting Corrections

| User asks for | Correct route |
|---|---|
| "Define exactly how users accept invitations" | PRD first, unless product behavior is already approved |
| "Should we use Kafka or direct API call?" | ADR |
| "Where should notification state live and how should invitation, membership, and notification interact?" | Architecture |
| "Split this into MVP and phase 2" | Roadmap |
| "Write the task for repository method and service changes" | PLAN |
| "Implement the repository method" | Implementation |
| "Check whether code follows the design" | Review |
