---
name: brainstorm-gate
description: "Use this skill to run the first gate of the workflow for new ideas, feature additions, user-reported problems, technical concerns, roadmap shifts, and product changes. This skill pressure-tests the problem, value, trade-offs, and alternatives, then routes explicitly to exactly one next artifact: PRD creation/update, roadmap creation/update, ADR creation/update, or reject/defer. Use it when the main need is deciding what the next artifact should be and why. Do not use it to write full PRDs, roadmaps, ADRs, or plans directly."
---

# Brainstorm Gate

## Purpose

This skill is the first decision gate of the workflow.

It exists to:
- clarify the real problem or opportunity
- identify business value and user impact
- evaluate alternatives and trade-offs
- determine whether the idea is strong enough to proceed
- route to the correct next artifact with no ambiguity

This skill does **not** write the full downstream artifact. It decides and prepares the next artifact.

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:
- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing and create-vs-update decisions across phases
- `docs/workflow/HANDOFF_CONTRACTS.md` for the minimum required input/output fields between phases

Do not duplicate those shared rules here. Apply them, then focus this skill on its own phase-specific job.

Use the decision matrix to choose the single next artifact. Use the handoff contracts to define the minimum carry-forward payload for that next phase.

## Operating rule

Every brainstorm run must end with **exactly one** explicit outcome:
- `NEW_PRD`
- `PRD_UPDATE`
- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`
- `NEW_ADR`
- `ADR_UPDATE`
- `REJECT_OR_DEFER`

Do not end with a vague summary.
Do not end with multiple competing next steps.
Do not leave the user to infer what happens next.

## Mandatory closing behavior

At the end of every brainstorm run, output all of the following:

1. `Decision`
   - exactly one outcome from the list above

2. `Why this decision`
   - short rationale for why this is the correct artifact

3. `What will be carried forward`
   - the minimum required context for the next phase

4. `What is explicitly not needed next`
   - state which nearby artifacts are not the correct immediate next step

5. `Immediate next step`
   - name the exact next artifact action
   - example: `Proceed to NEW_PRD`
   - example: `Proceed to NEW_INITIATIVE_ROADMAP`
   - example: `Proceed to NEW_ADR`

6. `User prompt for continuation`
   - a direct continuation prompt with no ambiguity
   - example: `Proceed to create the PRD based on this brainstorm output.`
   - example: `Proceed to create the initiative roadmap based on this brainstorm output.`

If the user asked only for brainstorming, stop after giving the explicit continuation prompt.
If the user explicitly asked to continue immediately, hand off to the next skill/artifact without waiting.

## Workflow

1. Classify the request mode using `references/MODES.md`.
2. Analyze the problem, value, users, alternatives, and trade-offs.
3. Decide whether the idea is worth acting on.
4. Route to exactly one next artifact using `references/DECISION_RULES.md`.
5. Produce the output using `assets/BRAINSTORM_OUTPUT_TEMPLATE.md`.

## Routing discipline

Use PRD when product intent or behavior must be defined or changed.
Use roadmap when intent is already clear and the next need is sequencing delivery.
Use ADR when the main result is a lasting technical decision.
Use reject/defer when the signal is too weak.

If PRD is required, do not also route directly to roadmap in the same closing decision.
If roadmap is required, specify whether it is product roadmap or initiative roadmap.
If ADR is required, specify whether it is new or update.

## Output quality bar

A good brainstorm output must be:
- problem-valid
- value-aware
- trade-off-aware
- artifact-explicit
- next-step-explicit
- concise enough for the next skill to consume directly

Read before use:
- `references/MODES.md`
- `references/DECISION_RULES.md`
- `assets/BRAINSTORM_OUTPUT_TEMPLATE.md`
