# Split Rules

## Split required when

Split into multiple plans when the requested work has:

- multiple primary objectives
- unrelated validation paths
- unrelated file/component clusters
- mixed feature + refactor + migration scope
- separate frontend and backend tasks that can be validated independently
- separate schema foundation and behavior implementation tasks
- multiple independent ADR outcomes
- multiple architecture boundaries changed at once
- different review criteria for different pieces of work

## Split output format

When splitting is required, do not write a giant plan. Output:

```md
## Split Required

### Reason

### Proposed Plan 1
- `title`:
- `objective`:
- `source_artifacts`:
- `architecture_constraints`:
- `validation`:

### Proposed Plan 2
...

## Concrete Next Step

- `next_step_type`: SPLIT_INTO_PLANS
- `target`: proposed plan 1
- `action`: Create the first single-task plan before implementation.
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

## Split ordering

Prefer this order:

1. schema/data foundation
2. domain/service behavior
3. API boundary
4. async/event side effect
5. UI/client behavior
6. observability/operational hardening
7. cleanup/refactor

Use roadmap order when it already exists and does not conflict with architecture.
