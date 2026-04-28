# plan-writer

Architecture-aware Codex skill for creating or updating one single-task `PLAN.md`.

## Purpose

This skill converts approved upstream intent into one bounded implementation contract. It is designed for workflows that use durable artifacts:

```text
BRAINSTORM.md -> PRD.md -> ARCHITECTURE.md -> ADRs -> ROADMAP.md -> PLAN.md -> IMPLEMENT -> REVIEW
```

## Key behavior

- Creates or updates exactly one task plan.
- Extracts binding constraints from source artifacts.
- Treats architecture as binding when present and relevant.
- Blocks planning when architecture/ADR/product decisions are missing or conflicting.
- Forces exactly one normalized `Concrete Next Step` block after every run.

## Normalized terminal contract

Every generated plan, plan delta, split response, or blocker response must end with:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use `Immediate Next Step`, `Continuation Prompt`, loose `next_step`, or loose `follow_up` fields.

## Install

Copy this folder to either:

```text
<repo>/.agents/skills/plan-writer
```

or:

```text
$HOME/.agents/skills/plan-writer
```

## Optional validation

Run:

```bash
python scripts/check_plan_doc.py PLAN.md
```

The script checks required plan sections and validates that exactly one normalized `Concrete Next Step` block is present.
