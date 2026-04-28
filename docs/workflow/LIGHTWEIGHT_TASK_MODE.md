# LIGHTWEIGHT_TASK_MODE.md

Purpose: define the fast lane for small, local, low-risk work so the workflow remains efficient without weakening safety for architecture-sensitive changes.

---

## 1. Definition

Lightweight task mode is a shortened workflow for work that is already clear enough to plan, implement, and review without creating or updating PRD, Architecture, ADR, or Roadmap artifacts.

Default lightweight path:

```text
Issue / request / brainstorm summary
-> Lightweight PLAN
-> Implementation
-> Lightweight Review
```

This mode is allowed only when product intent, architecture constraints, and technical decisions are already clear or not materially relevant.

---

## 2. Core Rule

Use lightweight mode only when all of these are true:

1. The task has one primary objective.
2. The affected area is local and easy to identify.
3. No user-facing product behavior needs clarification.
4. No component/module/service boundary is being changed.
5. No data ownership or source-of-truth rule is being changed.
6. No integration, async, transaction, authorization, security, observability, deployment, or performance constraint is being introduced or changed.
7. No ADR-worthy decision is required.
8. No staged roadmap is needed.
9. The change can be validated with a small, explicit validation path.
10. Review can judge the result against one bounded task.

If any condition is false, do not use lightweight mode. Route to the full artifact workflow.

---

## 3. Allowed Lightweight Work

Good candidates:

- small bug fix with clear expected behavior
- typo or documentation correction
- local refactor that preserves behavior and boundaries
- small validation rule already implied by existing PRD or code convention
- minor UI copy/layout adjustment that does not alter product flow
- test addition for existing behavior
- small configuration cleanup
- simple endpoint/controller/service fix that preserves architecture

---

## 4. Disallowed Lightweight Work

Do not use lightweight mode for:

- new product capability
- unclear product behavior
- new user flow
- new persistence model or table ownership
- new service/module/package boundary
- changed authorization or role behavior
- new async/event-driven flow
- new integration with external/internal systems
- transaction, consistency, retry, idempotency, or failure behavior change
- migration or staged rollout
- architecture-sensitive refactor
- decision with credible alternatives and long-term consequences
- change spanning multiple unrelated objectives
- change requiring multiple independent validation paths

Route these through PRD, Architecture, ADR, Roadmap, or full Plan as appropriate.

---

## 5. Lightweight Classification

Every lightweight path must state:

```md
## Lightweight Classification

- `mode`: LIGHTWEIGHT_TASK
- `reason`: 
- `scope`: 
- `why_prd_not_needed`: 
- `why_architecture_not_needed`: 
- `why_adr_not_needed`: 
- `why_roadmap_not_needed`: 
- `validation_path`: 
- `escalation_trigger`: 
```

The classification is mandatory. A lightweight task without this section is not valid.

---

## 6. Escalation Triggers

Escalate out of lightweight mode when any of these appear:

- implementation requires changing architecture-sensitive boundaries
- the task expands beyond one objective
- source-of-truth ownership becomes unclear
- tests reveal behavior ambiguity
- product behavior is not obvious from existing artifacts or code
- multiple implementation approaches imply a durable decision
- validation cannot be kept local and explicit
- the reviewer cannot determine correctness from the lightweight plan

Escalation target:

| Trigger | Route to |
|---|---|
| Product behavior unclear | PRD |
| System shape/boundary unclear | Architecture |
| One durable technical decision needed | ADR |
| Multi-phase sequencing needed | Roadmap |
| Task too broad but intent is clear | Split into multiple Plans |
| Implementation already changed scope | Review / Plan update |

---

## 7. Lightweight PLAN Requirements

A lightweight plan is still a plan. It must include:

- objective
- in scope
- out of scope
- affected files/components if known
- existing behavior
- target behavior
- implementation approach
- validation checklist
- risk check
- escalation trigger
- Concrete Next Step

It may omit broad artifact summaries, roadmap lineage, and extensive architecture context when explicitly not relevant.

---

## 8. Lightweight Implementation Requirements

Implementation must:

- follow the lightweight plan
- avoid scope expansion
- preserve existing architecture and ADR constraints
- stop if an escalation trigger appears
- produce a compact implementation summary
- route to review

Implementation must not silently convert a lightweight task into a full feature/refactor.

---

## 9. Lightweight Review Requirements

Review must verify:

- the work stayed lightweight
- scope remained one task
- no hidden product/architecture/ADR/roadmap decision was introduced
- validation evidence is enough
- implementation matches the lightweight plan
- the next step is concrete

If lightweight assumptions are broken, review must route to the correct full artifact instead of approving by convenience.

---

## 10. Concrete Next Step

Every lightweight output must end with the shared Concrete Next Step block:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Common `next_step_type` values:

- `CREATE_PLAN`
- `IMPLEMENT_PLAN`
- `RUN_REVIEW`
- `UPDATE_PLAN`
- `UPDATE_ARCHITECTURE`
- `CREATE_ADR`
- `UPDATE_PRD`
- `STOP_AND_ESCALATE`
