# DEVIATION_PROTOCOL

A deviation is a difference between the implemented result and the approved plan.

## Allowed deviations

A deviation may be allowed only when it is minimal and necessary for one of these reasons:
- the plan is contradictory
- the plan is incomplete in a blocking way
- repository constraints prevent literal implementation
- a minimal change is required for correctness or safety

## Required reporting

When a deviation occurs, report:
1. the original plan expectation
2. the implemented difference
3. why the difference was necessary
4. impact on behavior, tests, or follow-up work
5. whether the plan should be updated

## Forbidden behavior

Do not:
- silently improve the plan during coding
- broaden scope under the label of cleanup
- hide design changes in implementation notes
- claim strict plan fidelity when a material deviation happened
