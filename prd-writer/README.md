# prd-writer

Architecture-aware PRD writer skill for Codex.

This skill creates or updates `PRD.md` as the product-truth artifact in an AI-driven development workflow. It is designed to sit before architecture, ADR, roadmap, plan, implementation, and review.

## Core responsibility

`prd-writer` defines product intent:

- problem and value
- goals and non-goals
- users, actors, and roles
- current and target behavior
- product rules
- success criteria
- product constraints
- open product questions

It does not design architecture, choose ADR options, sequence roadmap phases, or plan implementation tasks.

## Architecture-aware behavior

Every run classifies architecture impact:

- `NONE`
- `CREATE_ARCHITECTURE`
- `UPDATE_ARCHITECTURE`
- `CHECK_EXISTING_ARCHITECTURE`
- `ARCHITECTURE_BLOCKED_BY_PRODUCT_QUESTIONS`

This lets PRD hand off cleanly to `architecture-writer` when product behavior implies system-shape decisions.

## Required final output

Every response must end with exactly one block:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use `Immediate Next Step`, `Continuation Prompt`, or a loose `next_step` field.

## Install

Copy this folder to one of:

```text
<repo>/.agents/skills/prd-writer
$HOME/.agents/skills/prd-writer
```
