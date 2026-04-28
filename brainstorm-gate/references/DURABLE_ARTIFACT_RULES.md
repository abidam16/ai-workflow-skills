# Durable Artifact Rules

Use this file to decide whether brainstorm output should be chat-only or durable.

## Core Rule

Do not create a durable brainstorm artifact merely because the discussion was interesting.

Create a durable brainstorm artifact when the brainstorm result must become a stable input for another workflow phase.

## Use `CHAT_ONLY_BRAINSTORM` When

- the user is exploring casually
- the idea is not expected to continue into another workflow phase
- the conclusion is simple enough to remain in chat
- the idea is weak and not likely to be revisited
- no later AI agent needs to consume the result

A chat-only result must still end with the normalized `Concrete Next Step` block.

## Use `DURABLE_BRAINSTORM_OUTPUT` When

- the brainstorm will feed PRD, Architecture, ADR, roadmap, document plan, implementation, or review
- the user explicitly asks for a durable document
- the decision rationale matters later
- the idea is deferred but likely to be revisited
- another session or AI agent must consume the result
- the idea affects product direction, architecture direction, delivery sequencing, documentation workflow, or implementation scope
- the brainstorm resolves ambiguity that would otherwise be lost in chat history

## Artifact Path

Default path:

```text
docs/brainstorm/BRAINSTORM-<sequence>-<slug>.md
```

Examples:

```text
docs/brainstorm/BRAINSTORM-001-notification-inbox.md
docs/brainstorm/BRAINSTORM-002-modular-backend-architecture.md
docs/brainstorm/BRAINSTORM-003-roadmap-scope-split.md
```

Use `BRAINSTORM-XXX` when the sequence number cannot be safely determined.

## Artifact Status

Use one of:

- `DRAFT`
- `APPROVED`
- `UPDATED`
- `DEFERRED`
- `REJECTED`
- `BLOCKED`

Default to `DRAFT` unless the user explicitly approves the conclusion or the decision is reject/defer.

## Durable Artifact Must Include

- metadata
- final decision
- artifact action
- decision rationale
- compact carry-forward context
- explicit non-next artifacts
- next artifact handoff payload
- `Concrete Next Step` block

## Durable Artifact Must Not Include

- full chat transcript
- full downstream document content
- full PRD sections
- full Architecture sections
- full ADR sections
- full roadmap phases
- full document plan sections
- implementation task breakdown
- speculative detail not needed by the next skill

## Reject / Defer Handling

A rejected or deferred idea can still have a durable brainstorm artifact when:

- the rationale must be preserved
- the idea may return later
- stakeholders may ask why it was not pursued
- there are clear reopen conditions

For lightweight rejection, use chat-only output.

## Terminal Contract

Both chat-only and durable outputs must end with:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not end with only `Immediate next step` or `Continuation prompt`.
