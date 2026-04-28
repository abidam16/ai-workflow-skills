# brainstorm-gate

Drop-in refactor of the `brainstorm-gate` skill.

## Purpose

This skill is the first gate for idea evaluation.

It converts raw brainstorming into one clear decision:

- create/update PRD
- create/update ADR
- create/update roadmap
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
- stop/defer handling
- stronger anti-overlap rules against PRD/ADR/roadmap writers

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
git commit -m "Refactor brainstorm-gate durable handoff output"
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

For continuing to PRD/ADR/roadmap:

```text
Proceed to create the PRD based on docs/brainstorm/BRAINSTORM-001-example.md.
```

## Boundary

This skill must not write full PRDs, ADRs, roadmaps, plans, or implementation tasks.

It only produces:

```text
idea conclusion + decision rationale + compact handoff payload
```
