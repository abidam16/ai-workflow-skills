---
name: adr-writer
description: Create, supersede, or update Architecture Decision Records (ADRs) for one meaningful technical or architectural decision. Use when architecture, planning, implementation, or review exposes a lasting choice with real alternatives, trade-offs, consequences, or architecture impact. Do not use for broad system design, PRD/product scope, roadmap sequencing, one-task implementation planning, implementation, or review.
---

# ADR Writer

## Shared workflow docs

Use these shared repo docs as cross-skill sources of truth:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md` for artifact routing, create-vs-update decisions, and authority boundaries across phases.
- `docs/workflow/HANDOFF_CONTRACTS.md` for required input/output fields between brainstorm, PRD, architecture, ADR, roadmap, plan, implementation, and review.

Do not duplicate those shared rules here. Apply them, then focus this skill on one durable decision record.

Validate that the incoming artifact choice matches the decision matrix. If the request should go to PRD, architecture, roadmap, plan, implementation, or review instead, do not write ADR content; route explicitly.

## Purpose

Use this skill to record one important technical or architectural decision so future readers and AI agents understand:

- what decision was needed
- what boundary the decision covers
- which source artifacts created the need for the decision
- what decision drivers mattered
- which credible alternatives were considered
- what option was chosen
- why that option fits the drivers
- what consequences, constraints, and follow-up artifacts result
- how the decision links back to `ARCHITECTURE.md` or an initiative architecture document

An ADR is a durable decision log entry. It is not a PRD, not a broad architecture document, not a roadmap, not a task plan, not an implementation note, and not a review report.

## Authority model

Use this authority model:

| Artifact | Authority |
|---|---|
| `BRAINSTORM.md` | Exploration, uncertainty, discarded options, and artifact-routing rationale |
| `PRD.md` | Product behavior, goals, non-goals, user/business rules, product constraints, and success criteria |
| `ARCHITECTURE.md` | System shape, component boundaries, data ownership, runtime flows, integration rules, and cross-cutting constraints |
| `docs/architecture/<initiative>-architecture.md` | Deep system design for one large active initiative |
| ADRs | One accepted technical decision and rationale |
| `ROADMAP.md` | Delivery sequencing, phase boundaries, dependencies, and readiness gates |
| `PLAN.md` | One executable implementation contract |
| Review report | Conformance findings and concrete next action |

ADR authority is narrow but strong: an accepted ADR is the source of truth for the specific decision it records. It does not replace `ARCHITECTURE.md`; it explains why a decision exists. Architecture should link to accepted ADRs and reflect their stable constraints.

## Use this skill when

Use this skill when one or more of the following is true:

- brainstorm selected `NEW_ADR` or `ADR_UPDATE`
- architecture identified an ADR candidate
- PRD requirements imply a technical choice with meaningful alternatives
- roadmap sequencing is blocked by an unresolved technical decision
- plan-writing is blocked by unresolved technical strategy
- implementation or review reveals an unrecorded architectural decision
- an existing ADR must be superseded by a newer accepted decision
- a decision changes or constrains component boundaries, data ownership, runtime flow, integration pattern, consistency model, authorization model, deployment model, reliability pattern, or operational strategy
- the decision is likely to be revisited, questioned, or reused by future tasks

## Do not use this skill when

Do not use this skill when:

- the issue is product behavior, user need, business rule, or success criteria -> route to `prd-writer`
- the issue is broad system shape, component map, data ownership model, runtime flow, or integration design -> route to `architecture-writer`
- the issue is delivery sequencing, phase order, dependency order, or rollout structure -> route to `roadmap-planner`
- the issue is exactly one implementation task -> route to `plan-writer`
- the task is implementation -> route to `implement-task`
- the task is conformance checking -> route to `review-phase`
- the decision is a minor local code preference with no lasting consequence
- the decision has no credible alternative
- the decision is already fully covered by an accepted ADR and no supersession is needed

## Inputs expected

Prefer these inputs when available:

- brainstorm output and artifact decision
- relevant `PRD.md` sections that create product constraints
- relevant root `ARCHITECTURE.md` sections
- relevant initiative architecture document, if the decision belongs to a large initiative
- related ADRs, including accepted, proposed, superseded, or conflicting ADRs
- relevant roadmap phase or dependency context
- relevant `PLAN.md` or review report if the decision was discovered during planning, implementation, or review
- codebase evidence, existing patterns, constraints, or production/runtime observations when available

If inputs are missing, infer conservatively. Do not invent false certainty. Put unresolved items in `Open Questions` and route to the correct next artifact.

## Output contract

Produce one of:

1. a new ADR using `assets/ADR_TEMPLATE.md`
2. an ADR supersession or update summary using `assets/ADR_DELTA_TEMPLATE.md`
3. an architecture ADR-index update note using `assets/ARCHITECTURE_ADR_INDEX_UPDATE_TEMPLATE.md`
4. a routing/blocker response when ADR is not the correct next artifact

Every run must end with `## Concrete Next Step`.

## ADR output requirements

Every ADR must include:

- decision title
- status
- decision date
- decision boundary
- source artifacts
- context/problem
- decision drivers
- considered options
- chosen option and rationale
- consequences
- architecture linkage
- implementation constraints
- review implications
- non-goals / not addressed
- supersedes / superseded by, when relevant
- related artifacts
- open questions, if any
- concrete next step

Use `assets/ADR_TEMPLATE.md` for new ADRs unless the repository already has a compatible ADR style.

For ADR updates, prefer append-only supersession over rewriting accepted decision history. Use `assets/ADR_DELTA_TEMPLATE.md` unless the repo has a different accepted convention.

## One decision rule

One ADR must record exactly one decision.

Do not combine unrelated decisions such as:

- choosing Kafka and choosing the database schema
- choosing outbox and choosing notification UI behavior
- choosing service boundary and choosing deployment topology
- choosing optimistic locking and choosing pagination strategy

If multiple decisions are present, split them into multiple ADRs or route back to architecture if the issue is still broad system design.

## Architecture linkage rule

Every ADR run must classify architecture linkage.

Allowed values:

- `NONE`
- `ARCHITECTURE_CONTEXT_ONLY`
- `ADD_ADR_INDEX_ENTRY`
- `UPDATE_ROOT_ARCHITECTURE`
- `UPDATE_INITIATIVE_ARCHITECTURE`
- `UPDATE_ROOT_AND_INITIATIVE_ARCHITECTURE`
- `ARCHITECTURE_CONFLICT_FOUND`
- `ARCHITECTURE_MISSING`

Use these rules:

- `NONE`: decision has no meaningful architecture relevance.
- `ARCHITECTURE_CONTEXT_ONLY`: architecture provided context, but no architecture update is needed.
- `ADD_ADR_INDEX_ENTRY`: architecture only needs a decision-index/link update.
- `UPDATE_ROOT_ARCHITECTURE`: the decision changes stable repo/product-level architecture rules.
- `UPDATE_INITIATIVE_ARCHITECTURE`: the decision changes one active initiative architecture document.
- `UPDATE_ROOT_AND_INITIATIVE_ARCHITECTURE`: both stable root rules and active initiative design must change.
- `ARCHITECTURE_CONFLICT_FOUND`: existing architecture contradicts the chosen decision.
- `ARCHITECTURE_MISSING`: the decision cannot be safely recorded because architecture context is required but absent.

Do not copy broad architecture content into the ADR. Instead, record the decision and state the precise architecture sections that must be linked or updated.

## ADR-worthiness gate

Before writing an ADR, classify readiness:

- `ADR_READY`: one meaningful decision with context, drivers, alternatives, and consequences is clear enough.
- `BLOCKED_BY_PRD`: product truth is unclear.
- `BLOCKED_BY_ARCHITECTURE`: system shape or boundary context is unclear.
- `BLOCKED_BY_MISSING_OPTIONS`: credible alternatives have not been explored.
- `BLOCKED_BY_CONFLICTING_SOURCES`: PRD, architecture, roadmap, plan, or existing ADRs conflict.
- `NOT_ADR_WORTHY`: issue is too small, too local, or already decided.
- `ROUTE_TO_ARCHITECTURE`: the request is broad design, not one decision.

If status is not `ADR_READY`, do not force an ADR. Produce a routing/blocker response with a concrete next step.

## Create vs supersede vs update

Default behavior:

- new decision -> create new ADR
- decision replacing an accepted ADR -> create new ADR that supersedes the old ADR
- typo/format/link correction -> update existing ADR
- status transition from Proposed to Accepted/Rejected -> update existing ADR if repo convention allows
- expanded consequences after implementation learning -> append a consequences note or create a superseding ADR if the decision changed

Do not silently rewrite accepted decision history.

## Decision boundary rule

State explicitly:

- what this ADR decides
- what this ADR does not decide
- which architecture boundary, runtime behavior, integration pattern, data rule, or cross-cutting constraint is affected
- which future plans or implementations must obey it

If the boundary is too broad, route to `architecture-writer`.

## Options rule

Include credible options only.

For each option, capture:

- summary
- benefits
- costs/risks
- fit against decision drivers
- why it was selected or rejected

Avoid strawman alternatives.

## Consequences rule

Consequences must be honest and useful for future agents.

Include:

- positive consequences
- negative consequences
- implementation constraints
- migration or compatibility implications
- operational implications
- review implications
- follow-up artifacts required

## Downstream handoff rule

ADR output must explicitly state downstream impact:

- Architecture Impact
- Roadmap Impact
- Plan Impact
- Review Impact

If the ADR changes architecture, the next step should usually be `UPDATE_ARCHITECTURE` before roadmap or plan.

If the ADR unblocks sequencing, route to roadmap.

If the ADR unblocks exactly one task and roadmap is already ready or irrelevant, route to plan.

## Concrete next step rule

Every output must end with this exact section:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Allowed `next_step_type` values:

- `UPDATE_ARCHITECTURE`
- `CREATE_OR_UPDATE_ROADMAP`
- `CREATE_OR_UPDATE_PLAN`
- `RETURN_TO_PRD`
- `RETURN_TO_ARCHITECTURE`
- `REVISE_ADR`
- `CREATE_SUPERSEDING_ADR`
- `REQUEST_MISSING_SOURCE_ARTIFACT`
- `REQUEST_DECISION_INPUT`
- `RETURN_TO_REVIEW`
- `START_IMPLEMENTATION`
- `STOP_AND_ESCALATE`

The next step must be concrete. Do not write vague actions like “continue,” “review later,” “fix issues,” or “proceed as needed.”

## Style

- Prefer direct technical language.
- Keep the ADR concise and decision-oriented.
- Be explicit about uncertainty.
- Do not duplicate broad architecture docs.
- Do not hide trade-offs.
- Do not turn the ADR into a roadmap or plan.
- Use tables when they make options or impacts easier to compare.
- Preserve existing repo ADR numbering and naming conventions.

## References

Use these references when needed:

- `references/SOURCE_OF_TRUTH_GUIDE.md`
- `references/ARCHITECTURE_ADR_LINKAGE_GUIDE.md`
- `references/ADR_WORTHINESS_GUIDE.md`
- `references/DECISION_BOUNDARY_GUIDE.md`
- `references/CREATE_VS_UPDATE.md`
- `references/QUALITY_BAR.md`
- `references/NEXT_STEP_ROUTING_GUIDE.md`
- `references/REVIEW_CHECKLIST.md`
