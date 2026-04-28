# Artifact Consistency Review Contract

`ARTIFACT_CONSISTENCY_REVIEW` checks whether durable artifacts are mutually consistent before implementation or before continuing a dependent implementation sequence.

## It answers

```text
Are PRD, architecture, ADRs, roadmap, and PLAN coherent enough for safe implementation?
```

## It does not

- create PRD
- create architecture
- create ADR
- create roadmap
- create plan
- implement code
- approve code changes

It only reviews consistency and routes to exactly one next step.

## Required checks

1. PRD supports the intended product behavior.
2. Architecture supports the PRD and does not invent unsupported product scope.
3. ADRs record important durable decisions and do not contradict architecture.
4. Roadmap sequencing respects PRD, architecture, and ADR dependencies.
5. PLAN is one bounded implementation task and does not override upstream artifacts.
6. Handoffs are complete enough for the next agent.
7. The next action is concrete and executable.
