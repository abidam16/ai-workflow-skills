---
name: adr-writer
description: Create or update Architecture Decision Records (ADRs) for meaningful technical or architectural decisions. Use when a technical choice has lasting impact, significant trade-offs, cross-cutting implications, or is likely to be revisited later. Do not use for product scope decisions, roadmap sequencing, or single-task implementation details.
metadata:
  author: OpenAI
  version: "1.0"
  workflow_stage: adr
---

# ADR Writer

This skill creates or updates a single ADR for one meaningful technical decision.

## Purpose

Use this skill to record one important technical or architectural decision so future readers can understand:
- what problem required a decision
- what options were seriously considered
- what was chosen
- why it was chosen
- what consequences follow from that choice

An ADR is a durable decision log entry, not a PRD, roadmap, task plan, meeting note, or broad architecture document.

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Validate that the incoming artifact choice matches the decision matrix. Produce outputs that satisfy the shared handoff contract for the next phase.

## Core Rules

1. **One ADR = one decision.** Do not combine unrelated decisions into one record.
2. **Default to a new ADR for a new decision.** If a previous ADR is changed by a later decision, create a new ADR that supersedes the old one instead of rewriting history.
3. **Keep it lightweight.** Be concise, but do not omit context, real alternatives, or trade-offs.
4. **State the decision boundary explicitly.** Clarify what this ADR decides and what it does not decide.
5. **Make trade-offs honest.** Record positive and negative consequences, not just benefits.
6. **Route correctly.** If the issue is product scope/behavior, use PRD. If it is delivery sequencing, use roadmap. If it is one task implementation detail, use a plan or implementation note.

## Use This Skill When

Use this skill when the decision:
- changes or constrains system structure
- affects multiple modules, teams, or future tasks
- has meaningful trade-offs
- has credible alternatives
- will likely be questioned later
- would be costly to reverse
- creates a lasting technical rule or pattern

Common examples:
- choose messaging or integration pattern
- choose persistence or consistency strategy
- choose authorization model
- choose caching approach
- choose event/outbox architecture
- choose monolith vs service boundary split

## Do Not Use This Skill When

Do not use this skill for:
- feature or product scope definition
- milestone sequencing or phasing
- one-task implementation details
- routine bug fixes
- minor local refactors without broader impact
- low-importance library usage with no lasting consequences

## Workflow

### Step 1: Confirm ADR-worthiness
Check whether the issue is a meaningful technical decision with lasting impact. If not, recommend the correct artifact instead.

### Step 2: Define the decision boundary
State exactly what is being decided and what is not being decided.

### Step 3: Identify decision drivers
List the criteria that matter most, such as reliability, performance, operability, delivery speed, cost, consistency, team capability, compliance, or maintainability.

### Step 4: Identify credible options
List the serious alternatives. Avoid strawman options.

### Step 5: Choose and justify
State the selected option clearly and explain why it best fits the decision drivers.

### Step 6: Record consequences
Document positive, negative, and follow-up consequences.

### Step 7: Connect downstream impact
State whether this decision affects PRD assumptions, roadmap sequencing, plan documents, implementation constraints, or review criteria.

## Create vs Update Rules

See `references/CREATE_VS_UPDATE.md`.

## Structure Guide

See `references/STRUCTURE_GUIDE.md`.

## Quality Bar

See `references/QUALITY_BAR.md`.

## Review Checklist

See `references/REVIEW_CHECKLIST.md`.

## Output Contract

When producing an ADR, output one of the following:
- a **new ADR** using `assets/ADR_TEMPLATE.md`
- an **ADR update/supersession summary** using `assets/ADR_DELTA_TEMPLATE.md`
- an **artifact routing note** if ADR is not the correct artifact

Each ADR or ADR delta should explicitly include:
- decision title
- status
- decision boundary
- context/problem
- decision drivers
- considered options
- chosen option and rationale
- consequences
- scope/impact
- non-goals / not addressed
- related artifacts

## Style

- Prefer direct, technical language.
- Keep the ADR concise and decision-oriented.
- Do not duplicate broad architecture docs.
- Do not hide trade-offs.
- Do not turn the ADR into a plan or roadmap.
