# Source-of-Truth Guide

Use this guide when the review target involves multiple artifacts.

## Authority model

| Artifact | Owns | Does not own |
|---|---|---|
| PRD | product behavior, user intent, product rules, success criteria | system structure, implementation steps |
| Architecture | system shape, boundaries, data ownership, runtime flows, cross-cutting constraints | product scope, delivery sequence, individual task steps |
| ADR | one accepted technical decision and its rationale | full architecture, roadmap, task list |
| Roadmap | delivery sequencing and phase/slice exit criteria | product truth, architecture truth, code details |
| PLAN | one-task execution contract | product truth, architecture truth, roadmap sequencing |
| Implementation Summary | delivered changes and deviations | approval decision |
| Review Report | acceptance decision and findings | creating upstream artifact truth |

## Conflict handling

Do not silently resolve artifact conflicts.

Route conflicts by highest impacted authority:

- product behavior conflict -> update PRD
- system-shape conflict -> update architecture
- one technical decision conflict -> create/update ADR
- delivery sequence conflict -> update roadmap
- task execution contract conflict -> update plan
- evidence gap -> request missing evidence

## Examples

### PLAN conflicts with architecture

If the plan says to store authorization state in a notification table, but architecture says membership is the authorization source of truth, the review must not approve. Route to `UPDATE_PLAN` or `UPDATE_ARCHITECTURE`, depending on which artifact is wrong.

### Implementation follows plan but violates ADR

If implementation follows the plan but contradicts an accepted ADR, the review must classify it as `ADR_CONFLICT`. Route to `RETURN_TO_IMPLEMENTATION`, `UPDATE_PLAN`, or `CREATE_OR_UPDATE_ADR` depending on whether the ADR remains valid.
