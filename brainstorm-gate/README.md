# brainstorm-gate

Drop-in refactor of the `brainstorm-gate` skill.

## Purpose

This skill is the first gate for idea evaluation.

It converts raw brainstorming into one clear decision:

- create/update PRD
- create/update Architecture
- create/update ADR
- create/update roadmap
- create/update document plan
- reject/defer

It can also produce a durable brainstorm artifact:

```text
docs/brainstorm/BRAINSTORM-<sequence>-<short-slug>.md
```

That artifact becomes the source-of-truth handoff for later phases.

## Main Design Change

The previous skill produced a clear brainstorm conclusion, but the result was mostly chat-shaped.

This refactor adds:

- output mode selection
- durable artifact rules
- artifact naming convention
- generic handoff payloads
- Architecture and ADR as first-class next-artifact targets
- Document Plan as a first-class next-artifact target
- stop/defer handling
- stronger anti-overlap rules against PRD/Architecture/ADR/roadmap/document-plan writers

## Installation

Replace the existing folder:

```text
ai-workflow-skills/brainstorm-gate
```

with this folder:

```text
brainstorm-gate
```

Suggested command from repo root:

```bash
rm -rf brainstorm-gate
cp -R /path/to/refactored/brainstorm-gate ./brainstorm-gate
```

Then commit:

```bash
git add brainstorm-gate
git commit -m "Refactor brainstorm-gate artifact routing"
```

## Files

```text
brainstorm-gate/
  SKILL.md
  README.md
  CHANGELOG.md
  agents/
    openai.yaml
  assets/
    BRAINSTORM_OUTPUT_TEMPLATE.md
    BRAINSTORM_RESPONSE_TEMPLATE.md
    BRAINSTORM_ARTIFACT_MINIMAL_TEMPLATE.md
  references/
    DECISION_RULES.md
    MODES.md
    DURABLE_ARTIFACT_RULES.md
    HANDOFF_PAYLOADS.md
  examples/
    BRAINSTORM-001-example-notification-inbox.md
    BRAINSTORM-002-example-modular-backend-architecture.md
```

## Usage Pattern

For lightweight brainstorming:

```text
Use brainstorm-gate to evaluate this idea, but keep it chat-only unless it clearly needs a durable artifact: <idea>
```

For durable workflow handoff:

```text
Use brainstorm-gate and create a durable brainstorm artifact if the idea should proceed to another workflow phase: <idea>
```

For continuing to a downstream writer:

```text
Proceed to create the architecture document based on docs/brainstorm/BRAINSTORM-002-modular-backend-architecture.md.
```

## Boundary

This skill must not write full PRDs, Architecture documents, ADRs, roadmaps, document plans, execution plans, or implementation tasks.

It only produces:

```text
idea conclusion + decision rationale + compact handoff payload
```
