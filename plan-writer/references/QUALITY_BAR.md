# Quality Bar

A good plan is:

- single-task only
- architecture-aware when relevant
- bounded
- executable
- testable
- reviewable
- explicit about what must not change
- clear about the immediate next action

## Must pass

The plan must answer:

1. What exactly is being implemented?
2. Why is this one task?
3. Which upstream artifacts constrain it?
4. Is architecture relevant, ready, missing, or conflicting?
5. What architecture constraints must implementation obey?
6. What is in scope?
7. What is out of scope?
8. What files/components are expected to change?
9. What must not change?
10. How will correctness be validated?
11. What should review check?
12. What is the concrete next step?

## Fail conditions

The plan is not acceptable if it:

- bundles multiple independent tasks
- invents product or architecture decisions
- omits relevant architecture constraints
- ignores ADR constraints
- uses vague validation criteria
- has no explicit next step
- says “continue implementation” without target/action
- cannot be reviewed against source artifacts
