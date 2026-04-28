# Scope and Split Rules

## Scope lock must include

- changed areas
- unchanged areas
- assumptions
- source artifacts checked
- validation path

## Split required when implementation requires

- multiple independent objectives
- separate schema foundation and behavior implementation
- backend and frontend changes that can be validated independently
- multiple unrelated modules/components
- multiple unrelated ADR outcomes
- multiple architecture boundary changes
- migration plus feature plus cleanup in one task
- broad refactor not required by the task objective

## Stop conditions

Stop with `BLOCKED_REQUIRES_PLAN_SPLIT` if the current plan cannot be executed as one independently reviewable task.

Stop with `BLOCKED_REQUIRES_PLAN_CLARIFICATION` if the plan is one task but lacks enough concrete detail.

Stop with `BLOCKED_REQUIRES_ARCHITECTURE_CLARIFICATION` if a boundary/source-of-truth/runtime-flow rule is needed before coding safely.

## Not a split

Do not split just because the implementation touches multiple files. A single task may touch multiple files when they are required for one coherent objective and one review path.
