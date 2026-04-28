# review-phase skill

Architecture-aware review skill for the AI-driven development workflow.

Use this skill after implementation to produce a decision-ready implementation review report, or before implementation to check whether durable artifacts are mutually consistent enough for safe execution.

## Review modes

- `TASK_REVIEW`: review one implementation against one approved `PLAN.md`.
- `ROADMAP_IMPLEMENTATION_REVIEW`: review multiple completed tasks against one roadmap or roadmap slice.
- `ARTIFACT_CONSISTENCY_REVIEW`: review PRD, architecture, ADRs, roadmap, and plans before implementation or before continuing execution.

## Main improvement

This version adds `ARTIFACT_CONSISTENCY_REVIEW`, a pre-implementation consistency mode for catching PRD / architecture / ADR / roadmap / plan contradictions before Codex writes code.

The skill still treats `ARCHITECTURE.md` and initiative architecture documents as first-class review authorities and requires every report to end with exactly one `Concrete Next Step`.

## Expected shared workflow docs

This skill expects these docs when available:

```text
docs/workflow/ARTIFACT_DECISION_MATRIX.md
docs/workflow/HANDOFF_CONTRACTS.md
docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md
docs/workflow/NEXT_STEP_TYPES.md
```

If the docs are absent, the skill still works from its local instructions, but the review report should mention that shared workflow docs were not found.

## Install

Copy this folder to one of these locations:

```text
<repo>/.agents/skills/review-phase
$HOME/.agents/skills/review-phase
```

Restart Codex if the updated skill is not detected.
