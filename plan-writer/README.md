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
- Forces a concrete next step after every run.

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

The script checks for required sections and a concrete next-step block.
