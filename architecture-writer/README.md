# architecture-writer skill

This skill creates or updates durable architecture documentation for Codex-style AI-driven development workflows.

## Install

Copy the `architecture-writer/` directory into one of these locations:

```text
<repo>/.agents/skills/architecture-writer
$HOME/.agents/skills/architecture-writer
```

Codex scans `.agents/skills` from the current working directory up to the repo root, and user-level skills from `$HOME/.agents/skills`.

## Primary outputs

- `ARCHITECTURE.md`
- `docs/architecture/<initiative-slug>-architecture.md`
- architecture delta summary
- artifact routing note

## Suggested workflow position

```text
brainstorm-gate
  -> PRD
  -> architecture-writer
  -> ADR
  -> roadmap
  -> PLAN
  -> implementation
  -> review
```

The skill may be invoked explicitly with:

```text
$architecture-writer
```
