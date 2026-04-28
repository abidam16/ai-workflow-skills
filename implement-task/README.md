# implement-task

Architecture-aware Codex skill for executing one approved `PLAN.md` with strict plan fidelity.

## Purpose

This skill implements exactly one bounded task from an approved plan while preserving upstream durable artifacts:

```text
BRAINSTORM.md -> PRD.md -> ARCHITECTURE.md -> ADRs -> ROADMAP.md -> PLAN.md -> IMPLEMENT -> REVIEW
```

## Key behavior

- Executes one plan only.
- Checks relevant architecture/ADR constraints before coding.
- Preserves scope and avoids opportunistic refactors.
- Reports plan, architecture, ADR, roadmap, or validation blockers explicitly.
- Produces an implementation summary ready for `review-phase`.
- Forces a concrete next step after every run.

## Install

Copy this folder to either:

```text
<repo>/.agents/skills/implement-task
```

or:

```text
$HOME/.agents/skills/implement-task
```

## Optional validation

Run:

```bash
python scripts/check_implementation_report.py IMPLEMENTATION_SUMMARY.md
```

The script checks for required reporting sections and a concrete next-step block.
