# Quality Bar

A good implementation is:

- exactly one task
- plan-compliant
- architecture-aware when relevant
- ADR-compliant when relevant
- minimal
- validated
- deviation-transparent
- review-ready

## Must pass

The implementation must answer:

1. Which plan was implemented?
2. Was this exactly one task?
3. Which source artifacts were checked?
4. Was the task architecture-sensitive?
5. Which architecture constraints were enforced?
6. Which ADR constraints were enforced?
7. What files changed and why?
8. What validation was run?
9. Were there deviations?
10. What is the concrete next step?

## Fail conditions

Implementation is not acceptable if it:

- expands scope without reporting a deviation
- ignores relevant architecture constraints
- ignores ADR decisions
- performs unrelated refactors
- changes product behavior not approved by PRD/plan
- crosses component boundaries without approved architecture
- changes data source-of-truth behavior without approved architecture/ADR
- claims completion without validation or validation-gap reporting
- ends without a concrete next step
