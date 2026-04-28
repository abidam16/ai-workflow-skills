# Architecture Handoff Guide

Architecture-writer must hand off architecture work in a compact, structured way.

## Required handoff shape

Use two final sections:

1. `Architecture Handoff Summary`
2. `Concrete Next Step`

## Architecture Handoff Summary

```md
## Architecture Handoff Summary

- `decision`:
- `architecture_scope`:
- `architecture_path`:
- `why_this_decision`:
- `sections_created_or_changed`:
- `adr_impact`:
- `roadmap_impact`:
- `plan_readiness`:
```

This section records architecture-specific context.

## Concrete Next Step

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

This section routes the workflow to one concrete next action.

## Separation rule

Do not combine the two sections.

The handoff summary explains the architecture result.

The concrete next step tells the user or agent exactly what to do next.
