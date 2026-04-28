# ARTIFACT_DECISION_MATRIX.md

Purpose: define routing rules between workflow artifacts so each phase ends with one clear next step, minimal ambiguity, and correct source-of-truth authority.

---

## 1. Core Rule

At any point in the workflow, choose the **single next artifact or action** that best resolves the current uncertainty or execution need.

Preferred full workflow:

```text
Brainstorm
-> PRD if product intent is unclear or changed
-> Architecture if system shape, boundaries, ownership, runtime flows, or cross-cutting constraints are unclear or changed
-> ADR if one important technical/architectural decision must be recorded
-> Roadmap if staged delivery structure is needed
-> Plan for one bounded implementation task
-> Implementation
-> Review
```

Lightweight workflow for small, local, low-risk tasks:

```text
Issue / request / brainstorm summary
-> Lightweight Plan
-> Implementation
-> Lightweight Review
```

Do not create every artifact every time. Create or update exactly the artifact/action that resolves the current uncertainty.

Architecture is optional to create, but authoritative when present and relevant.

---

## 2. Artifact Roles

### Brainstorm Output

Used to clarify an idea, assess value, compare options, and route to exactly one next artifact/action. Brainstorm is historical routing context, not long-term product or architecture truth once downstream artifacts supersede it.

### PRD

Product truth: product intent, goals, non-goals, users/roles, flows, product rules, current vs target behavior, and success criteria.

### Architecture

System-shape truth: repo/product architecture, initiative architecture, component/module/service boundaries, data ownership, runtime flows, integration boundaries, consistency/security/observability/deployment/performance constraints, and ADR links.

### ADR

Decision truth: one meaningful technical or architectural decision, options considered, chosen option, rationale, consequences, and supersession relationship.

### Roadmap

Sequencing truth: staged delivery structure, phases, dependencies, risks, exit criteria, and plan handoff candidates.

### Plan

Execution truth for one bounded task: scope, files/components, implementation approach, validation, review expectations, and constraints from relevant upstream artifacts.

### Lightweight Plan

A compressed plan for one small, local, low-risk task. It is allowed only when PRD, architecture, ADR, and roadmap work are not needed.

### Implementation

Executes one approved plan or lightweight plan. It must not silently override PRD, architecture, ADR, roadmap, or plan constraints.

### Review

Enforcement layer. Judges implementation and/or artifact consistency against the relevant approved sources of truth.

---

## 3. Authority Model

| Artifact | Authority |
|---|---|
| PRD | Product behavior, user value, product rules, success criteria |
| Architecture | System shape, boundaries, ownership, runtime flows, cross-cutting constraints |
| ADR | One recorded technical decision and its rationale/consequences |
| Roadmap | Delivery sequence, phases, dependency ordering |
| Plan | Scope and execution contract for one bounded task |
| Lightweight Plan | Scope and execution contract for one small, local, low-risk task |
| Implementation Summary | What changed, what was validated, what deviated |
| Review Report | Acceptance decision, findings, and next action |

Conflict rules:

1. Do not silently resolve conflicts between artifacts.
2. PRD governs product behavior.
3. Architecture governs system structure and implementation constraints.
4. ADR governs the specific decision it records.
5. Roadmap governs sequencing but cannot redefine product or architecture truth.
6. PLAN governs one task scope but cannot override PRD, architecture, or ADRs.
7. Lightweight PLAN is valid only while lightweight assumptions remain true.
8. If a downstream artifact conflicts with an upstream authority, stop and route to the correct update artifact.

---

## 4. Top-Level Routing Order

When deciding the next artifact/action, use this order:

1. Reject / defer?
2. Is this eligible for lightweight mode?
3. Need product intent clarified or changed?
4. Need system shape, boundaries, ownership, runtime flow, or cross-cutting constraints documented?
5. Need one technical/architectural decision recorded?
6. Need staged delivery structure?
7. Need one-task execution contract?
8. Need implementation?
9. Need review?

This ordering allows efficient small-task execution without letting architecture-sensitive work bypass durable artifacts.

---

## 5. Lightweight Mode Routing Rules

Use lightweight mode only when all of these are true:

- one primary objective
- small/local change
- product behavior is already clear or unaffected
- architecture boundaries are already clear or unaffected
- no ADR-worthy decision is needed
- no roadmap sequencing is needed
- validation is small and explicit
- review can judge the result against one bounded task

Choose lightweight mode for:

- local bug fix
- small test addition
- documentation typo or small clarification
- local behavior-preserving refactor
- small validation/copy/config cleanup

Do not choose lightweight mode for:

- new feature/capability
- behavior ambiguity
- boundary/data ownership/integration changes
- async, transaction, security, authorization, deployment, observability, or performance changes
- large refactor/migration
- multi-task work
- decisions with meaningful alternatives

Lightweight route:

```text
CREATE_PLAN -> IMPLEMENT_PLAN -> RUN_REVIEW
```

If lightweight eligibility is uncertain, do not use lightweight mode. Route to the full artifact workflow.

---

## 6. Full Workflow Routing Rules

### Choose PRD when

- product intent does not exist or changed
- user-facing behavior, product goals, roles, flows, rules, or success criteria must be defined

### Choose Architecture when

- system shape, component/module/service boundaries, data ownership, runtime flow, integration model, or cross-cutting constraints must be durable before later work proceeds

### Choose ADR when

- the next blocking question is one important technical/architectural decision with credible options and lasting consequences

### Choose Roadmap when

- intent and relevant architecture/ADR constraints are stable enough and the next need is staged delivery structure

### Choose Plan when

- exactly one bounded task is ready for execution and relevant constraints are clear enough

### Choose Implementation when

- one approved plan exists, scope is bounded, and validation/test expectations are clear

### Choose Review when

- implementation or artifact-chain consistency must be judged against approved sources of truth

---

## 7. Default Workflow Patterns

### Pattern A: New product or major feature

Brainstorm → PRD → Architecture → ADR if needed → Roadmap → Plan → Implementation → Review

### Pattern B: Existing product behavior change

Brainstorm → PRD Update → Architecture Update if needed → Roadmap Update or Plan → Implementation → Review

### Pattern C: Broad technical architecture change

Brainstorm → Architecture → ADR if needed → Roadmap or Plan → Implementation → Review

### Pattern D: One significant technical decision

Brainstorm → ADR → Architecture Update if needed → Roadmap or Plan → Implementation → Review

### Pattern E: Existing initiative change

Brainstorm → PRD/Architecture/Roadmap Update, whichever resolves current uncertainty → Plan → Implementation → Review

### Pattern F: Small local implementation task

Issue/request/brainstorm summary → Lightweight Plan → Implementation → Lightweight Review

Use Pattern F only when product intent, architecture constraints, ADRs, and roadmap sequencing are clear or not relevant.

### Pattern G: Weak or premature idea

Brainstorm → Reject / Defer

---

## 8. Minimum Next-Step Requirement

Every phase must end with the shared `Concrete Next Step` block.

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

No phase should end with only analysis and no routing.

---

## 9. Portability Rule

This matrix is workflow-generic. Domain-specific rules should be layered through `AGENTS.md`, nested `AGENTS.md`, domain-specific checklists, or domain-specific skills. Do not overload this matrix with domain-specific regulations.
