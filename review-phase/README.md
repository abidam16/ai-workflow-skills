# review-phase skill

Architecture-aware review skill for the AI-driven development workflow.

Use this skill after implementation to produce a decision-ready review report. The skill reviews implementation against the correct source-of-truth chain:

1. PRD for product truth
2. Architecture for system-shape truth
3. ADRs for decision truth
4. Roadmap for sequencing truth
5. PLAN for one-task execution truth
6. Implementation summary, diffs, tests, and validation evidence for actual delivery

## Main improvement

The skill now treats `ARCHITECTURE.md` and initiative architecture documents as first-class review authorities. It also requires every report to end with exactly one concrete next step.

## Install

Copy this folder to one of these locations:

```text
<repo>/.agents/skills/review-phase
$HOME/.agents/skills/review-phase
```

Restart Codex if the updated skill is not detected.

## Expected shared workflow docs

This skill expects these docs when available:

```text
docs/workflow/ARTIFACT_DECISION_MATRIX.md
docs/workflow/HANDOFF_CONTRACTS.md
```

If the docs are absent, the skill still works from its local instructions, but the review report should mention that shared workflow docs were not found.
