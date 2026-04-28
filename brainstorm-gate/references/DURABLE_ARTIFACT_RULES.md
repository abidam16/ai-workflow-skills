# Durable Artifact Rules

The brainstorm phase can end as chat-only output or as a durable artifact.

The purpose of durable output is to avoid relying on chat history when another skill, phase, or future session needs the conclusion.

## Output Mode Choices

### `CHAT_ONLY_BRAINSTORM`

Use when:

- the user is exploring casually
- no downstream workflow is expected
- the idea is obviously weak and not worth preserving
- the user only needs a recommendation in the current conversation
- the decision does not affect durable product, architecture, roadmap, or implementation context

### `DURABLE_BRAINSTORM_OUTPUT`

Use when:

- the user asks for a durable document
- the brainstorm will feed PRD, ADR, roadmap, plan, implementation, or review
- the decision rationale should be preserved
- the idea may be revisited later
- future AI agents need a compact source of truth
- the conclusion changes product direction, architecture, sequencing, or task scope

## Default File Path

Use:

```text
docs/brainstorm/BRAINSTORM-<sequence>-<short-slug>.md
```

If sequence cannot be known:

```text
docs/brainstorm/BRAINSTORM-XXX-<short-slug>.md
```

## Naming Rules

- Use uppercase `BRAINSTORM` prefix.
- Use a 3-digit sequence when known: `001`, `002`, `003`.
- Use `XXX` only when the agent cannot inspect existing files.
- Use a short lowercase slug.
- Use hyphens, not spaces or underscores.
- Avoid vague slugs like `context`, `idea`, or `notes`.

Good:

```text
BRAINSTORM-001-notification-inbox.md
BRAINSTORM-002-ai-report-template-builder.md
BRAINSTORM-003-kafka-log-monitoring.md
```

Weak:

```text
BRAINSTORM-001-context.md
BRAINSTORM-001-idea.md
brainstorm-notes.md
```

## Artifact Status Rules

Use:

- `DRAFT` when the brainstorm has not been explicitly accepted
- `APPROVED` when the decision is accepted as source of truth
- `UPDATED` when revising an existing brainstorm artifact
- `DEFERRED` when the final decision is `REJECT_OR_DEFER` but the rationale should be preserved
- `REJECTED` when the idea should not be pursued and does not need future revisit
- `BLOCKED` when required information is missing and no responsible decision can be made

## Source Artifact Rule

When a durable brainstorm artifact exists, every downstream artifact should reference it in `source_artifacts`.

Example:

```yaml
source_artifacts:
  - docs/brainstorm/BRAINSTORM-001-notification-inbox.md
```

## Minimality Rule

The durable brainstorm artifact should be compact.

Include only what the next phase needs:

- decision
- rationale
- key problem or intent
- constraints
- risks
- material open questions
- selected next artifact
- handoff payload

Do not include:

- the full chat transcript
- every discarded thought
- downstream artifact templates
- implementation steps
- detailed task decomposition
- low-importance context

## Deferred Idea Rule

A `REJECT_OR_DEFER` decision does not automatically require a durable artifact.

Create a durable artifact for defer/reject only when:

- the idea is likely to be revisited
- the rationale is important to preserve
- the user asks for a record
- the decision prevents repeated re-discussion
- the idea has enough context to make future revisit useful

Otherwise, keep the result chat-only.
