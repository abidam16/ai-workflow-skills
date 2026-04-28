---
name: brainstorm-gate
description: |
  Use this skill as the first decision gate for new ideas, feature additions,
  user-reported problems, technical concerns, roadmap shifts, and product changes.
  The skill pressure-tests the problem, value, alternatives, risks, and trade-offs,
  then routes to exactly one next artifact: PRD creation/update, roadmap
  creation/update, ADR creation/update, or reject/defer.

  This skill can produce either a lightweight chat-only brainstorm conclusion or
  a durable BRAINSTORM artifact that becomes the source-of-truth handoff for the
  next workflow phase.

  Do not use this skill to write full PRDs, roadmaps, ADRs, execution plans, or
  implementation tasks directly.
---

# Brainstorm Gate

## 1. Purpose

This skill is the first decision gate of the workflow.

It exists to:

- clarify the real problem or opportunity
- test whether the idea is worth pursuing
- identify business value and user impact
- evaluate alternatives and trade-offs
- identify meaningful constraints, risks, and open questions
- route to exactly one correct next artifact
- create a compact durable handoff when later phases need stable context

This skill does **not** write the full downstream artifact.

It decides what should happen next and preserves only the minimum context needed by the next phase.

## 2. Shared Workflow Sources of Truth

Use these shared workflow docs when they exist in the target repo:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/HANDOFF_CONTRACTS.md`

Do not duplicate the full shared workflow rules inside this skill.

Apply those documents as the higher-level workflow policy, then use this skill for the brainstorm-specific phase behavior.

If those shared workflow docs are not present, use this skill's local references:

- `references/MODES.md`
- `references/DECISION_RULES.md`
- `references/DURABLE_ARTIFACT_RULES.md`
- `references/HANDOFF_PAYLOADS.md`

## 3. When to Use This Skill

Use this skill when the user is exploring or evaluating:

- a new product idea
- a new capability or feature addition
- a user-reported problem or recurring pain point
- a technical concern that may require an ADR
- a scope change in an existing product
- a roadmap or delivery sequencing change
- whether an idea should proceed, stop, or be deferred

Use this skill when the main question is:

> What should this idea become next, and why?

## 4. When Not to Use This Skill

Do not use this skill when the correct artifact is already explicitly selected and no brainstorm/routing decision is needed.

Examples:

- The user asks directly to write a PRD from already-approved context.
- The user asks directly to write an ADR for a clearly bounded technical decision.
- The user asks directly to write an execution plan from an approved roadmap slice.
- The user asks to implement code.
- The user asks to review completed work.

In those cases, use the corresponding downstream skill directly.

## 5. Core Invariant

Every brainstorm run must end with exactly one explicit decision:

- `NEW_PRD`
- `PRD_UPDATE`
- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_ADR`
- `ADR_UPDATE`
- `REJECT_OR_DEFER`

Do not end with:

- multiple competing next steps
- a vague recommendation
- a list of possible artifacts without choosing one
- a full downstream artifact
- an implementation plan

If multiple artifacts seem useful, choose the **single immediate next artifact** that resolves the current uncertainty.

## 6. Output Modes

This skill has two output modes.

### 6.1 `CHAT_ONLY_BRAINSTORM`

Use this mode when:

- the user is casually exploring an idea
- no downstream workflow phase is expected yet
- the decision does not need to be referenced later
- the idea is weak and not worth preserving

Output a concise brainstorm conclusion using `assets/BRAINSTORM_RESPONSE_TEMPLATE.md`.

### 6.2 `DURABLE_BRAINSTORM_OUTPUT`

Use this mode when:

- the brainstorm result will feed a PRD, ADR, roadmap, plan, implementation, or review phase
- the user wants a durable document
- the decision rationale must be preserved
- another AI agent or future session must consume the result
- the idea is deferred but likely to be revisited
- the idea affects product direction, architecture, roadmap sequencing, or implementation scope

Output a durable artifact using `assets/BRAINSTORM_OUTPUT_TEMPLATE.md`.

Default durable path:

```text
/docs/brainstorm/BRAINSTORM-<sequence>-<short-slug>.md
```

If the next sequence number cannot be safely determined, use:

```text
/docs/brainstorm/BRAINSTORM-XXX-<short-slug>.md
```

The slug must be lowercase, short, and hyphen-separated.

Examples:

```text
/docs/brainstorm/BRAINSTORM-001-notification-inbox.md
/docs/brainstorm/BRAINSTORM-002-ai-report-template-builder.md
/docs/brainstorm/BRAINSTORM-XXX-payment-reconciliation.md
```

## 7. Durable Artifact Rule

A durable brainstorm artifact is not a PRD, ADR, roadmap, or plan.

It is:

```text
idea conclusion + decision rationale + compact handoff payload
```

It must include:

- artifact metadata
- request classification
- problem/opportunity summary
- value assessment
- users or actors affected
- options considered
- trade-offs
- constraints
- risks
- material open questions
- final decision
- why this decision
- what will be carried forward
- what is explicitly not needed next
- next artifact handoff payload
- immediate next step
- continuation prompt

It must not include:

- full exploratory chat transcript
- full PRD sections
- full ADR sections
- full roadmap phases
- implementation task breakdown
- file lists
- class names, endpoint lists, or table schemas unless they are necessary to explain a technical decision boundary
- low-importance observations

## 8. Handoff Discipline

Use `references/HANDOFF_PAYLOADS.md` to choose the correct handoff payload shape for the selected decision.

The brainstorm output must have a generic section named:

```text
Next Artifact Handoff Payload
```

Do not create special sections such as:

- `PRD Section`
- `ADR Section`
- `Roadmap Section`

The selected downstream skill owns the downstream artifact format.

This skill only passes the minimum structured input required for that next skill.

## 9. Workflow

Follow this sequence:

1. Classify the request mode using `references/MODES.md`.
2. Identify known source artifacts, if any.
3. Restate the problem or opportunity in one clear sentence.
4. Identify affected users, actors, systems, or stakeholders.
5. Assess value, urgency, and evidence strength.
6. Identify current alternatives or workarounds.
7. Compare at least two plausible options when trade-offs matter.
8. Capture constraints, risks, and material open questions.
9. Select exactly one final decision using `references/DECISION_RULES.md`.
10. Select output mode using `references/DURABLE_ARTIFACT_RULES.md`.
11. Produce the output using the correct asset template.
12. End with one immediate next step and one continuation prompt.

## 10. Routing Discipline

Use PRD when product intent, user-facing behavior, goals, non-goals, scope, product rules, or success criteria must be defined or changed.

Use ADR when the main unresolved issue is a lasting technical or architectural decision with meaningful alternatives and trade-offs.

Use roadmap when the intent is already accepted and the next need is staged delivery structure, sequencing, dependencies, risks, and exit criteria.

Use reject/defer when the idea is weak, low-value, under-evidenced, premature, or missing material constraints.

If PRD is required, do not also route directly to roadmap in the same final decision.

If roadmap is required, specify whether it is a product roadmap or initiative roadmap.

If ADR is required, specify whether it is a new ADR or an update.

If reject/defer is selected, state what evidence or clarification would reopen the idea.

## 11. Mandatory Closing Behavior

Every output must end with all of the following:

1. `Decision` — exactly one decision from the allowed list
2. `Artifact action` — one of:
   - `CREATE_DURABLE_BRAINSTORM_ARTIFACT`
   - `UPDATE_EXISTING_BRAINSTORM_ARTIFACT`
   - `CHAT_ONLY_NO_ARTIFACT`
3. `Durable artifact path` — required if artifact action creates or updates a durable brainstorm artifact
4. `Why this decision` — short rationale for why this is the correct immediate artifact
5. `What will be carried forward` — minimum context for the next phase
6. `What is explicitly not needed next` — nearby artifacts that should not happen immediately
7. `Immediate next step` — exact next artifact action
8. `Continuation prompt` — direct prompt that can be copied into the next skill/session

Examples:

```text
Decision: NEW_PRD
Artifact action: CREATE_DURABLE_BRAINSTORM_ARTIFACT
Durable artifact path: docs/brainstorm/BRAINSTORM-001-notification-inbox.md
Immediate next step: Proceed to NEW_PRD.
Continuation prompt: Proceed to create the PRD based on docs/brainstorm/BRAINSTORM-001-notification-inbox.md.
```

```text
Decision: REJECT_OR_DEFER
Artifact action: CHAT_ONLY_NO_ARTIFACT
Immediate next step: Stop here. Do not proceed until stronger evidence exists.
Continuation prompt: Stop here and revisit after gathering stronger evidence.
```

## 12. Stop Condition

When the final decision is `REJECT_OR_DEFER`, do not create a downstream artifact.

State:

- why forward progress should stop
- what is missing or conflicting
- what evidence, constraint, or decision would reopen the idea
- whether a durable brainstorm artifact is still worth keeping

Use a durable artifact for `REJECT_OR_DEFER` only when the idea is likely to be revisited or the rationale is important to preserve.

## 13. Output Quality Bar

A good brainstorm output must be:

- decision-explicit
- artifact-explicit
- problem-valid
- value-aware
- evidence-aware
- trade-off-aware
- constraint-aware
- concise enough for the next skill to consume
- durable only when durability helps future workflow
- free from downstream artifact duplication

Before finalizing, check:

- Is there exactly one decision?
- Is the output mode correct?
- Is the durable artifact path present when needed?
- Is the handoff payload compatible with the selected decision?
- Are non-next artifacts explicitly excluded?
- Is the continuation prompt copy-paste usable?

## 14. Read Before Use

Read these local files before using the skill:

- `references/MODES.md`
- `references/DECISION_RULES.md`
- `references/DURABLE_ARTIFACT_RULES.md`
- `references/HANDOFF_PAYLOADS.md`
- `assets/BRAINSTORM_OUTPUT_TEMPLATE.md`
- `assets/BRAINSTORM_RESPONSE_TEMPLATE.md`
