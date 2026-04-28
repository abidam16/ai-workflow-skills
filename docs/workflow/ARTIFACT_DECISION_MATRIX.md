# ARTIFACT_DECISION_MATRIX.md

Purpose: define the routing rules between workflow artifacts so each phase ends with one clear next step, minimal ambiguity, and correct source-of-truth authority.

---

## 1. Core Rule

At any point in the workflow, choose the **single next artifact** that best resolves the current uncertainty or execution need.

Do not create multiple new artifacts in one step unless explicitly required.

Preferred workflow:

1. Brainstorm
2. PRD if product intent is unclear or changed
3. Architecture if system shape, boundaries, ownership, runtime flows, or cross-cutting constraints are unclear or changed
4. ADR if one important technical/architectural decision must be recorded
5. Roadmap if staged delivery structure is needed
6. Plan for one bounded implementation task
7. Implementation
8. Review

Architecture is optional to create, but authoritative when present and relevant.

---

## 2. Artifact Roles

### Brainstorm Output

Used to:

- clarify the problem or opportunity
- test whether the idea is worth pursuing
- decide the next artifact
- preserve only the context needed for the next artifact

Brainstorm should not automatically generate every downstream artifact.

### PRD

Used to define product truth:

- product intent
- goals
- non-goals
- users/roles
- flows
- product rules
- current vs target behavior
- success criteria

PRD should not define system structure, implementation sequence, or one-task execution details.

### Architecture

Used to define system-shape truth:

- canonical repo/product architecture
- initiative-level architecture for large changes
- component/module/service boundaries
- data ownership and source-of-truth rules
- runtime flows
- integration boundaries
- sync vs async boundaries
- transaction, consistency, idempotency, retry, and failure rules
- authorization, observability, deployment, and performance constraints
- architecture rules that future plans and implementations must obey
- links to relevant ADRs

Architecture should not define product scope, delivery phases, task steps, or full ADR decision history.

Default paths:

- `ARCHITECTURE.md` for canonical repo/product architecture
- `docs/architecture/<initiative-slug>-architecture.md` for large initiative architecture
- `docs/architecture/archive/<initiative-slug>-architecture.md` for archived initiative architecture

### ADR

Used to define decision truth:

- one meaningful technical or architectural decision
- options considered
- chosen option
- rationale
- consequences
- supersession relationship, if applicable

An ADR is not a broad architecture document. Architecture may identify ADR candidates; ADRs record the final decision and should be linked back from architecture when relevant.

### Roadmap

Used to define sequencing truth:

- staged delivery structure
- phases or milestones
- dependencies
- risks
- exit criteria
- plan handoff candidates

Roadmap sequences delivery. It must not invent missing product intent, architecture, or ADRs.

### Plan

Used to define one task execution truth:

- one bounded task only
- exact implementation scope
- detailed spec
- expected files/components
- validation/tests
- review expectations
- relevant constraints from PRD, architecture, ADRs, and roadmap

One plan document must cover one task only.

### Implementation

Used to:

- execute one approved plan
- stay within scope
- obey architecture and ADR constraints carried by the plan
- report deviations and blockers

Implementation should not silently override PRD, architecture, ADR, roadmap, or plan constraints.

### Review

Used to:

- judge product/business alignment
- judge architecture alignment
- judge ADR/decision alignment
- judge roadmap alignment, if relevant
- judge plan alignment
- judge technical quality
- judge validation/test evidence
- decide acceptance / revision / blockage

Review is the enforcement layer for all relevant approved artifacts.

---

## 3. Authority Model

Each artifact owns a different kind of truth.

| Artifact | Authority |
|---|---|
| PRD | Product behavior, user value, product rules, success criteria |
| Architecture | System shape, boundaries, ownership, runtime flows, cross-cutting constraints |
| ADR | One recorded technical decision and its rationale/consequences |
| Roadmap | Delivery sequence, phases, dependency ordering |
| Plan | Scope and execution contract for one bounded task |
| Implementation Summary | What actually changed, what was validated, what deviated |
| Review Report | Acceptance decision and findings |

Conflict rules:

1. Do not silently resolve conflicts between artifacts.
2. PRD governs product behavior.
3. Architecture governs system structure and implementation constraints.
4. ADR governs the specific decision it records and may supersede earlier architecture text for that decision only.
5. Roadmap governs sequencing but cannot redefine product or architecture truth.
6. PLAN governs one task scope but cannot override PRD, architecture, or ADRs.
7. If a downstream artifact conflicts with an upstream authority, stop and route to the correct update artifact.

---

## 4. Top-Level Routing Order

When deciding the next artifact, use this order:

1. Reject / defer?
2. Need product intent clarified or changed?
3. Need system shape, boundaries, ownership, runtime flow, or cross-cutting constraints documented?
4. Need one technical/architectural decision recorded?
5. Need staged delivery structure?
6. Need one-task execution contract?
7. Need implementation?
8. Need review?

This ordering prevents jumping into roadmap, plan, or implementation when product intent, architecture, or decisions are still unclear.

Architecture vs ADR shortcut:

- Use architecture when the question is about **system shape or shared implementation constraints**.
- Use ADR when the question is about **one important decision among credible options**.
- Use both when architecture exposes a decision that must be recorded, but do not produce both in one step unless explicitly requested.

---

## 5. Brainstorm Routing Rules

### Choose `REJECT_OR_DEFER` when:

- the problem is weak or unclear
- the value is too low
- the signal is too speculative
- the idea does not justify immediate action
- required evidence is missing

### Choose `NEW_PRD` when:

- product intent does not yet exist in durable form
- the idea defines a new product or major new capability
- user-facing behavior, goals, or scope must be established

### Choose `PRD_UPDATE` when:

- product intent exists, but parts of it changed
- goals, non-goals, flows, roles, rules, or success criteria need adjustment
- the change affects product behavior or business intent

### Choose `NEW_ARCHITECTURE` when:

- product intent is stable enough to design against
- no suitable architecture document exists for the relevant scope
- future implementation would drift without shared system-shape guidance
- component, module, service, package, layer, or repository boundaries must be defined
- data ownership or source-of-truth rules must be made durable
- runtime flows, sync/async boundaries, integration boundaries, or deployment/runtime assumptions must be documented
- transaction, consistency, idempotency, retry, security, observability, or performance rules must guide multiple future tasks

The architecture writer decides whether the correct path is root `ARCHITECTURE.md` or `docs/architecture/<initiative>-architecture.md`.

### Choose `ARCHITECTURE_UPDATE` when:

- an architecture document already exists for the same scope
- the system shape, boundaries, ownership, runtime flow, integration model, or cross-cutting constraints changed
- a PRD, ADR, roadmap, implementation, or review result exposes an architecture gap or contradiction
- an initiative architecture has become stable enough to fold permanent rules into root `ARCHITECTURE.md`

### Choose `NEW_ADR` when:

- the next blocking question is one significant technical/architectural decision
- multiple credible options exist
- the decision has lasting downstream impact
- future readers will need the rationale

### Choose `ADR_UPDATE` only when:

- your ADR practice explicitly allows updates in place for non-historic corrections
- otherwise prefer a new ADR that supersedes the old one

Preferred default:

- create a **new ADR** and mark older ADRs as superseded instead of rewriting history

### Choose `NEW_PRODUCT_ROADMAP` when:

- strategic product direction is already clear enough
- relevant architecture and ADR concerns are either stable enough or intentionally not needed
- the next need is high-level staged product evolution
- no suitable product roadmap exists yet

### Choose `PRODUCT_ROADMAP_UPDATE` when:

- a product-level roadmap already exists
- strategic sequencing, priorities, or major phases changed
- architecture or ADR changes affect sequencing

### Choose `NEW_INITIATIVE_ROADMAP` when:

- the work is a distinct initiative
- product intent is already clear enough
- architecture and ADR concerns are stable enough for sequencing, or explicitly out of scope
- the next need is phased delivery for one feature/refactor/migration/capability
- no suitable initiative roadmap exists yet

### Choose `INITIATIVE_ROADMAP_UPDATE` when:

- an initiative roadmap already exists
- phase structure, sequencing, dependencies, risks, or exit criteria changed
- PRD, architecture, ADR, implementation, or review findings change delivery order

### Brainstorm constraint

Brainstorm must end with **exactly one** final routing decision.

---

## 6. PRD Routing Rules

### Create a PRD when:

- the problem, users, goals, or behavior must be defined for the first time
- the work changes product truth materially

### Update a PRD when:

- product truth already exists
- only part of the product truth changed
- the document remains fundamentally valid

### Do not use PRD when:

- the issue is only system architecture
- the issue is only one technical decision
- the issue is only delivery sequencing
- the issue is only one-task implementation detail

### After PRD, the next step is usually:

- architecture creation/update, if system shape, boundaries, ownership, runtime flow, or cross-cutting constraints must be defined
- ADR, if one major technical choice is still unresolved before architecture or delivery sequencing
- roadmap creation/update, if delivery sequencing is needed and architecture/ADR concerns are stable enough or not relevant
- plan, only if the task is small, bounded, and does not need roadmap or architecture work
- stop, if the PRD is being refined but execution should not proceed yet

PRD should expose architecture impact, but not write architecture detail.

---

## 7. Architecture Routing Rules

### Create root `ARCHITECTURE.md` when:

- no canonical repo/product architecture exists
- the architecture applies broadly across the repo/product
- many future tasks need the same system-shape context
- the stable rules belong at the repo/product level

### Update root `ARCHITECTURE.md` when:

- the canonical repo/product architecture remains the right scope
- stable boundaries, ownership, integration, runtime, or cross-cutting constraints changed
- an initiative architecture has matured and permanent rules should be folded into root
- accepted ADRs need to be indexed or reflected as architecture constraints

### Create initiative architecture when:

- the work is too large, transitional, or multi-component for root `ARCHITECTURE.md`
- the design affects several modules/services/layers
- the design introduces new infrastructure or runtime behavior
- the design changes data ownership, transaction boundaries, authorization, async/event flows, or deployment assumptions
- the initiative will produce multiple plans or ADRs

### Update initiative architecture when:

- the same initiative remains active
- target architecture, flows, boundaries, risks, open questions, or ADR links changed
- review or implementation findings reveal architecture gaps

### Do not use architecture when:

- product intent is still unclear -> use PRD
- the question is one bounded decision with alternatives -> use ADR
- the next need is delivery sequencing -> use roadmap
- the next need is one bounded executable task -> use PLAN
- the change is local, obvious, and does not create durable architecture constraints

### After architecture, the next step is usually:

- ADR, if a specific architectural decision must be recorded
- roadmap, if architecture is stable enough and staged delivery is needed
- plan, if one bounded task is ready and no roadmap is needed
- PRD update, if architecture revealed product ambiguity
- stop, if unresolved architecture questions block execution

Architecture output must state:

- ADR impact
- roadmap impact
- plan readiness
- exactly one immediate next step

---

## 8. ADR Routing Rules

### Create a new ADR when:

- there is one meaningful technical decision
- multiple credible options exist
- the decision has important consequences
- future readers will need the rationale

### Prefer a new ADR over updating an old ADR when:

- the actual decision changed
- the old ADR would become historically misleading if rewritten
- the new decision supersedes the old one

### Do not use ADR when:

- the question is product scope or business behavior
- the question is broad system shape rather than one decision
- the question is milestone sequencing
- the question is one-task implementation detail

### After ADR, the next step is usually:

- architecture update, if the decision changes system shape, constraints, ownership, flows, or ADR index
- roadmap, if the decision enables staged delivery
- plan, if the decision directly unlocks one bounded task
- PRD update, if the decision changes product assumptions materially

---

## 9. Roadmap Routing Rules

### Choose `PRODUCT_ROADMAP` when:

- the document is strategic
- it tracks product evolution across multiple initiatives
- it acts as a lightweight index of active/completed/deferred initiative streams

### Choose `INITIATIVE_ROADMAP` when:

- the roadmap is for one specific feature, refactor, migration, capability, or major improvement
- this roadmap is the main bridge into planning

Preferred default for real execution:

- use **initiative roadmap**

### Create a new roadmap when:

- the work is a new initiative
- the objective is materially different
- the work deserves its own phased delivery structure
- merging into an existing roadmap would reduce clarity
- product intent and relevant architecture/ADR constraints are stable enough for sequencing

### Update an existing roadmap when:

- the work is part of the same initiative
- the same roadmap remains structurally valid
- only phase order, scope, risk, dependency, or exit criteria changed
- PRD, architecture, ADR, implementation, or review findings changed sequencing

### Do not use roadmap when:

- product intent is still unclear
- system architecture is still unclear and materially affects sequencing
- a major technical decision is still unresolved and materially affects sequencing
- the next work is just one bounded task with no need for phased structure

### After roadmap, the next step is:

- generate one or more **single-task plans**

Roadmap must sequence work according to PRD, architecture, and ADR constraints. It must not invent them.

---

## 10. Plan Routing Rules

### Create a new plan when:

- one bounded task is ready for execution
- no suitable plan exists yet
- relevant PRD, architecture, ADR, and roadmap constraints are clear enough for the task

### Update an existing plan when:

- the same task still exists
- only details, scope boundaries, files, tests, validation, or constraints changed
- the plan remains a single coherent task

### Split instead of update when:

- the plan has more than one primary objective
- the scope crosses multiple unrelated behaviors
- the review criteria are not singular
- the work would naturally produce multiple independent commit themes
- the validation paths are separate enough to deserve distinct tasks

### Architecture-sensitive task rule

A plan must include relevant architecture constraints when the task touches:

- module/service/package/layer boundaries
- data ownership or source-of-truth rules
- API/integration boundaries
- messaging/events/async flows
- transaction boundaries
- consistency, idempotency, retry, or failure behavior
- authorization/security
- observability/auditability
- deployment/runtime behavior
- performance/scalability assumptions

### Hard rule

One plan document must cover **one task only**.

### After plan, the next step is:

- implementation of that one task

---

## 11. Implementation Routing Rules

### Proceed to implementation when:

- one approved plan exists
- scope is bounded
- expected files/components are known
- validation/test expectations are clear
- relevant architecture/ADR constraints are either included or explicitly not applicable

### Do not proceed to implementation when:

- the plan is internally inconsistent
- the task is too broad
- product intent is still unresolved
- architecture required for safe implementation is missing or contradictory
- a blocking technical decision is still missing
- the plan conflicts with relevant architecture or ADRs

### During implementation:

- follow the plan
- preserve architecture constraints
- preserve ADR decisions
- do not silently expand scope
- do not silently deviate
- report blockers if safe implementation is not possible
- report any architecture-impacting deviation explicitly

### After implementation, the next step is:

- review

---

## 12. Review Routing Rules

### Choose `TASK_REVIEW` when:

- reviewing one implementation against one `PLAN.md`

### Choose `ROADMAP_IMPLEMENTATION_REVIEW` when:

- reviewing the combined implementation status of multiple tasks under one roadmap
- checking cross-task gaps, integration issues, architecture drift, or roadmap fulfillment

### Review must assess:

- business/product alignment
- architecture alignment
- ADR/decision alignment
- roadmap alignment, if relevant
- plan alignment
- technical quality
- tests/validation
- integration impact
- risks
- next actions

### Review output status

Use one:

- `APPROVED`
- `APPROVED_WITH_MINOR_IMPROVEMENTS`
- `NEEDS_REVISION`
- `BLOCKED`

Review must not approve work that violates relevant architecture or ADR constraints unless the decision explicitly states that architecture/ADR updates are required before approval.

---

## 13. Create vs Update Summary

### Create new artifact when:

- there is no suitable existing artifact
- the scope/objective is materially new
- reusing an old artifact would reduce clarity
- historical continuity matters

### Update existing artifact when:

- the existing artifact still represents the same underlying object
- only part of it changed
- updating preserves clarity better than creating a new one

### Prefer new over update when:

- the change would rewrite history in a confusing way
- the objective materially changed
- the old artifact should remain as historical record

### Architecture-specific create/update rule

- Create root architecture when no canonical repo/product architecture exists.
- Update root architecture when stable repo/product rules changed.
- Create initiative architecture when a large initiative needs isolated depth.
- Update initiative architecture while the same initiative remains active.
- Archive initiative architecture after permanent rules are folded into root architecture.

---

## 14. Escalation Rules

Stop and escalate instead of proceeding when:

- the chosen artifact is still unclear after analysis
- two artifact types seem equally necessary but one depends on the other
- product intent and architecture are both unresolved
- architecture and ADR are both unresolved, and the ADR decision is needed before architecture can be written safely
- roadmap sequencing depends on missing architecture or ADRs
- plan scope depends on missing architecture constraints
- implementation would need to invent upstream decisions
- review reveals artifact conflict that cannot be resolved inside review
- the scope is too broad for the target artifact

Use this escalation order:

1. clarify product intent first
2. clarify system shape second
3. record one blocking technical decision third
4. sequence delivery fourth
5. define one-task execution fifth

---

## 15. Minimum Next-Step Requirement

Every phase must end with:

- `Current Decision`
- `Why this is the correct artifact`
- `What is explicitly not next`
- `Immediate Next Step`

Architecture-producing phases must also end with:

- `Architecture Scope`
- `Architecture Path`
- `ADR Impact`
- `Roadmap Impact`
- `Plan Readiness`

No phase should end with only analysis and no routing.

---

## 16. Default Workflow Patterns

### Pattern A: New product or major feature

Brainstorm → PRD → Architecture → ADR if needed → Roadmap → Plan → Implementation → Review

### Pattern B: Existing product change affecting behavior

Brainstorm → PRD Update → Architecture Update if needed → Roadmap Update or New Initiative Roadmap → Plan → Implementation → Review

### Pattern C: Broad technical architecture change

Brainstorm → Architecture → ADR if needed → Roadmap or Plan → Implementation → Review

### Pattern D: One significant technical decision

Brainstorm → ADR → Architecture Update if needed → Roadmap or Plan → Implementation → Review

### Pattern E: Existing initiative change

Brainstorm → PRD/Architecture/Roadmap Update, whichever resolves the current uncertainty → Plan → Implementation → Review

### Pattern F: Small local implementation task

Brainstorm or issue context → Plan → Implementation → Review

Use this only when product intent, architecture constraints, and technical decisions are already clear or not relevant.

### Pattern G: Weak or premature idea

Brainstorm → Reject / Defer

---

## 17. Portability Rule

This matrix is workflow-generic. It should work across:

- frontend
- backend
- platform/infrastructure
- finance systems
- healthcare systems
- internal tools
- general product applications

Domain-specific rules should be layered separately through:

- `AGENTS.md`
- nested `AGENTS.md`
- domain-specific checklists
- domain-specific skills

Do not overload this matrix with domain-specific regulations.
