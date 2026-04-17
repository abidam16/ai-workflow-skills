# Quality Bar

A good `PLAN.md` is a concise, single-task implementation contract.

It is good when it is:
- focused on exactly one task
- specific enough to implement without inventing missing logic
- bounded enough to prevent scope drift
- explicit enough to review objectively
- short enough to scan quickly

## Required qualities

### 1. Single-task only
There must be one primary objective and one coherent deliverable.

### 2. Sharp boundaries
In-scope and out-of-scope must be explicit.

### 3. Concrete specification
The plan must say what behavior or implementation result must exist, not just vague aspirations.

### 4. Validation-ready
It must be possible to tell whether the task is done.

### 5. Review-ready
A reviewer should be able to compare implementation against the plan without guessing.

### 6. Portable
The structure should work across frontend, backend, platform, internal tools, finance, healthcare, and general software projects.

## Anti-patterns

Reject or split the plan if it:
- includes multiple independent objectives
- contains a full milestone instead of one task
- duplicates roadmap or PRD content
- has vague scope
- lacks validation or tests
- hides risk or trade-offs
- cannot identify expected files/components to change
