# HANDOFF_CONTRACTS.md

Purpose: define minimum required input/output fields between workflow phases so each skill can hand off cleanly with low ambiguity, controlled token usage, and correct source-of-truth authority.

This file defines the shape of workflow handoffs. It should be used together with:

- `docs/workflow/ARTIFACT_DECISION_MATRIX.md`
- `docs/workflow/CONCRETE_NEXT_STEP_CONTRACT.md`
- `docs/workflow/NEXT_STEP_TYPES.md`

---

## 1. Core Rule

Each phase should pass forward only the minimum structured payload the next phase needs.

Do not pass the entire brainstorm/history if a compact handoff is enough.

Every handoff must include:

- `artifact_type`
- `artifact_status`
- `decision`
- `core_rationale`
- references to upstream artifacts
- constraints that materially affect the next phase
- open issues that materially affect the next phase
- exactly one `## Concrete Next Step` block

Do not use loose terminal fields such as:

- `next_step`
- `follow_up`
- `Immediate Next Step`
- `Continuation Prompt`

Use the required block from `CONCRETE_NEXT_STEP_CONTRACT.md`.

---

## 2. Standard Artifact Types

Common values:

```text
BRAINSTORM_OUTPUT
PRD
PRD_DELTA
ARCHITECTURE
ARCHITECTURE_DELTA
INITIATIVE_ARCHITECTURE
INITIATIVE_ARCHITECTURE_DELTA
ADR
ADR_DELTA
ROADMAP
ROADMAP_DELTA
PLAN
PLAN_DELTA
LIGHTWEIGHT_PLAN
IMPLEMENTATION_SUMMARY
LIGHTWEIGHT_IMPLEMENTATION_SUMMARY
TASK_REVIEW_REPORT
LIGHTWEIGHT_TASK_REVIEW_REPORT
ARTIFACT_CONSISTENCY_REVIEW_REPORT
ROADMAP_REVIEW_REPORT
```

---

## 3. Required Concrete Next Step

Every handoff must end with this exact block:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Rules:

1. `next_step_type` must use a canonical value from `NEXT_STEP_TYPES.md`.
2. `target` must be a concrete artifact/action target.
3. `action` must be executable.
4. `why_this_is_next` must explain why this route follows from the current output.
5. `blocking_condition` must identify what would stop or alter the next step.
6. `suggested_prompt` must be ready to copy into the next agent invocation.

---

## 4. Brainstorm → PRD

Use when product intent, user behavior, business rules, or success criteria are unclear or changed.

Required handoff payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: READY_FOR_PRD
decision: CREATE_PRD | UPDATE_PRD
core_rationale:
source_context:
  idea_summary:
  problem_statement:
  target_users_or_roles:
  business_value:
  known_constraints:
product_questions_to_resolve:
  -
out_of_scope:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_PRD` or `UPDATE_PRD`
- `target`: `PRD.md` or target PRD path
- `action`: create/update PRD from the brainstorm handoff
- `blocking_condition`: unresolved idea viability or missing product context

---

## 5. Brainstorm → Architecture

Use when system shape, boundaries, data ownership, runtime flows, integration boundaries, or cross-cutting constraints are the next blocking uncertainty.

Required handoff payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: READY_FOR_ARCHITECTURE
decision: CREATE_ARCHITECTURE | UPDATE_ARCHITECTURE
core_rationale:
source_context:
  idea_summary:
  known_product_intent:
  architecture_questions:
    -
  affected_components_or_domains:
    -
  known_constraints:
    -
architecture_scope:
  root_or_initiative:
  target_path:
out_of_scope:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE`
- `target`: `ARCHITECTURE.md` or `docs/architecture/<initiative>-architecture.md`
- `action`: create/update architecture from the brainstorm handoff
- `blocking_condition`: product intent is too unclear to design system shape safely

---

## 6. Brainstorm → ADR

Use when the next blocking uncertainty is one meaningful technical or architectural decision.

Required handoff payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: READY_FOR_ADR
decision: CREATE_ADR | UPDATE_ADR
core_rationale:
decision_topic:
options_identified:
  -
decision_pressure:
  why_now:
  consequences_if_unrecorded:
related_artifacts:
  prd:
  architecture:
  roadmap:
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ADR` or `UPDATE_ADR`
- `target`: `docs/adr/<decision>.md`
- `action`: create/update one ADR for the decision topic
- `blocking_condition`: decision topic is too broad and must be split or routed to architecture first

---

## 7. Brainstorm → Roadmap

Use when intent and relevant constraints are stable enough and the next need is staged delivery sequencing.

Required handoff payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: READY_FOR_ROADMAP
decision: CREATE_ROADMAP | UPDATE_ROADMAP
core_rationale:
delivery_goal:
known_scope:
known_dependencies:
  -
known_risks:
  -
source_artifacts:
  prd:
  architecture:
  adrs:
    -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ROADMAP` or `UPDATE_ROADMAP`
- `target`: `ROADMAP.md` or target roadmap path
- `action`: create/update roadmap using stable product and architecture constraints
- `blocking_condition`: missing PRD/architecture/ADR truth needed for sequencing

---

## 8. Brainstorm → Lightweight Plan

Use only when the task is small, local, low-risk, and does not need PRD, architecture, ADR, or roadmap work.

Required handoff payload:

```yaml
artifact_type: LIGHTWEIGHT_MODE_CLASSIFICATION
artifact_status: APPROVED | REJECTED | BLOCKED
decision: USE_LIGHTWEIGHT_MODE | ESCALATE_TO_FULL_WORKFLOW
core_rationale:
lightweight_classification:
  mode: LIGHTWEIGHT_TASK
  objective:
  scope:
  why_prd_not_needed:
  why_architecture_not_needed:
  why_adr_not_needed:
  why_roadmap_not_needed:
  validation_path:
  escalation_trigger:
```

Required `Concrete Next Step` when approved:

- `next_step_type`: `CREATE_LIGHTWEIGHT_PLAN`
- `target`: lightweight plan output
- `action`: create a lightweight implementation plan
- `blocking_condition`: any discovered product, architecture, ADR, or roadmap uncertainty

If rejected or blocked, route to the appropriate full workflow artifact.

---

## 9. PRD → Architecture

Use when product behavior introduces or changes system shape, boundaries, ownership, runtime flow, integration, consistency, or security constraints.

Required handoff payload:

```yaml
artifact_type: PRD | PRD_DELTA
artifact_status: APPROVED | DRAFT | BLOCKED
decision: CREATE_ARCHITECTURE | UPDATE_ARCHITECTURE
core_rationale:
product_scope:
  goals:
  non_goals:
  user_roles:
  key_flows:
  business_rules:
architecture_impact:
  affected_domains:
    -
  affected_data:
    -
  affected_integrations:
    -
  affected_cross_cutting_constraints:
    -
open_product_questions:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE`
- `target`: `ARCHITECTURE.md` or target initiative architecture
- `action`: translate approved product intent into architecture constraints
- `blocking_condition`: PRD still has unresolved product behavior or acceptance criteria

---

## 10. PRD → Roadmap or Plan

Use when product truth is stable and architecture work is not required or already complete.

Required handoff payload:

```yaml
artifact_type: PRD | PRD_DELTA
artifact_status: APPROVED
decision: CREATE_ROADMAP | UPDATE_ROADMAP | CREATE_PLAN | UPDATE_PLAN
core_rationale:
stable_product_requirements:
  -
architecture_relevance:
  status: NOT_RELEVANT | ALREADY_COVERED
  architecture_refs:
    -
constraints:
  -
open_issues:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ROADMAP`, `UPDATE_ROADMAP`, `CREATE_PLAN`, or `UPDATE_PLAN`
- `target`: roadmap or plan artifact
- `action`: create/update the next artifact
- `blocking_condition`: missing architecture or ADR constraint discovered during handoff

---

## 11. Architecture → ADR

Use when architecture exposes one meaningful decision that must be recorded separately.

Required handoff payload:

```yaml
artifact_type: ARCHITECTURE | ARCHITECTURE_DELTA | INITIATIVE_ARCHITECTURE | INITIATIVE_ARCHITECTURE_DELTA
artifact_status: APPROVED | DRAFT | BLOCKED
decision: CREATE_ADR | UPDATE_ADR
core_rationale:
decision_topic:
architecture_context:
  affected_sections:
    -
  affected_components:
    -
  affected_data_or_flow:
    -
options_or_tradeoffs:
  -
why_adr_is_required:
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ADR` or `UPDATE_ADR`
- `target`: `docs/adr/<decision>.md`
- `action`: record the specific decision and consequences
- `blocking_condition`: decision is too broad and must be split or returned to architecture

---

## 12. Architecture → Roadmap

Use when architecture constraints are stable and delivery sequencing is now the next problem.

Required handoff payload:

```yaml
artifact_type: ARCHITECTURE | ARCHITECTURE_DELTA | INITIATIVE_ARCHITECTURE | INITIATIVE_ARCHITECTURE_DELTA
artifact_status: APPROVED
decision: CREATE_ROADMAP | UPDATE_ROADMAP
core_rationale:
architecture_constraints:
  component_boundaries:
    -
  data_ownership:
    -
  runtime_flows:
    -
  integration_boundaries:
    -
  sequencing_implications:
    -
required_or_linked_adrs:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ROADMAP` or `UPDATE_ROADMAP`
- `target`: roadmap artifact
- `action`: sequence delivery according to architecture constraints
- `blocking_condition`: required ADRs are missing or architecture remains unstable

---

## 13. Architecture → Plan

Use when exactly one bounded implementation task is ready after architecture constraints are defined.

Required handoff payload:

```yaml
artifact_type: ARCHITECTURE | ARCHITECTURE_DELTA | INITIATIVE_ARCHITECTURE | INITIATIVE_ARCHITECTURE_DELTA
artifact_status: APPROVED
decision: CREATE_PLAN | UPDATE_PLAN
core_rationale:
plan_candidate:
  objective:
  affected_components:
    -
  required_constraints:
    -
  validation_expectations:
    -
source_refs:
  architecture_sections:
    -
  adrs:
    -
  prd:
  roadmap:
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_PLAN` or `UPDATE_PLAN`
- `target`: `PLAN.md` or target plan artifact
- `action`: create/update one bounded implementation plan
- `blocking_condition`: task is too broad, dependencies are missing, or source artifacts conflict

---

## 14. ADR → Architecture

Use when an ADR decision affects architecture constraints or must be indexed from architecture.

Required handoff payload:

```yaml
artifact_type: ADR | ADR_DELTA
artifact_status: ACCEPTED | SUPERSEDED | PROPOSED | REJECTED
decision: UPDATE_ARCHITECTURE | RETURN_TO_ARCHITECTURE
core_rationale:
adr_path:
decision_summary:
architecture_impact:
  root_architecture_update_needed: true | false
  initiative_architecture_update_needed: true | false
  affected_sections:
    -
  constraints_to_reflect:
    -
```

Required `Concrete Next Step`:

- `next_step_type`: `UPDATE_ARCHITECTURE` or `RETURN_TO_ARCHITECTURE`
- `target`: `ARCHITECTURE.md` or target initiative architecture
- `action`: add ADR link and reflect accepted architectural constraint
- `blocking_condition`: ADR status is not accepted or conflicts with existing architecture

---

## 15. ADR → Roadmap or Plan

Use when the ADR is accepted and architecture is already updated or unaffected.

Required handoff payload:

```yaml
artifact_type: ADR | ADR_DELTA
artifact_status: ACCEPTED
decision: CREATE_ROADMAP | UPDATE_ROADMAP | CREATE_PLAN | UPDATE_PLAN
core_rationale:
decision_summary:
implementation_constraints:
  -
architecture_refs:
  -
roadmap_or_plan_implications:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_ROADMAP`, `UPDATE_ROADMAP`, `CREATE_PLAN`, or `UPDATE_PLAN`
- `target`: roadmap or plan artifact
- `action`: continue sequencing or planning with ADR constraints
- `blocking_condition`: architecture has not yet reflected the accepted ADR where required

---

## 16. Roadmap → Plan

Use when a roadmap phase or slice is ready to become one bounded implementation task.

Required handoff payload:

```yaml
artifact_type: ROADMAP | ROADMAP_DELTA
artifact_status: APPROVED
decision: CREATE_PLAN | UPDATE_PLAN | SPLIT_INTO_PLANS
core_rationale:
roadmap_slice:
  phase:
  outcome:
  exit_criteria:
  dependencies:
    -
source_constraints:
  prd:
  architecture:
  adrs:
    -
plan_candidates:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `CREATE_PLAN`, `UPDATE_PLAN`, or `SPLIT_INTO_PLANS`
- `target`: target `PLAN.md` or plan set
- `action`: create/update one bounded implementation plan
- `blocking_condition`: selected roadmap slice is too broad or source constraints conflict

---

## 17. Plan → Implementation

Use when one full plan is approved.

Required handoff payload:

```yaml
artifact_type: PLAN | PLAN_DELTA
artifact_status: APPROVED
decision: IMPLEMENT_PLAN
core_rationale:
plan_path:
objective:
in_scope:
  -
out_of_scope:
  -
affected_files_or_components:
  -
architecture_constraints:
  -
adr_constraints:
  -
validation_checklist:
  -
deviation_rules:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `IMPLEMENT_PLAN`
- `target`: approved plan
- `action`: implement the plan exactly within scope
- `blocking_condition`: source artifact conflict, scope expansion, or missing validation path

---

## 18. Lightweight Plan → Implementation

Use when one lightweight plan is approved.

Required handoff payload:

```yaml
artifact_type: LIGHTWEIGHT_PLAN
artifact_status: APPROVED | DRAFT | BLOCKED
decision: IMPLEMENT_LIGHTWEIGHT_PLAN
core_rationale:
objective:
in_scope:
  -
out_of_scope:
  -
affected_files_or_components:
  -
existing_behavior:
target_behavior:
implementation_approach:
validation_checklist:
  -
risk_check:
  product_risk: none | low | blocked
  architecture_risk: none | low | blocked
  adr_risk: none | low | blocked
  roadmap_risk: none | low | blocked
escalation_trigger:
```

Required `Concrete Next Step`:

- `next_step_type`: `IMPLEMENT_LIGHTWEIGHT_PLAN`
- `target`: approved lightweight plan
- `action`: implement the lightweight plan within its local scope
- `blocking_condition`: any escalation trigger invalidates lightweight mode

---

## 19. Implementation → Review

Use when implementation is complete or blocked and must be judged.

Required handoff payload:

```yaml
artifact_type: IMPLEMENTATION_SUMMARY
artifact_status: COMPLETED | BLOCKED | DEVIATED
decision: RUN_REVIEW | UPDATE_PLAN | RESOLVE_SOURCE_CONFLICT
core_rationale:
plan_path:
changes_made:
  -
files_changed:
  -
validation_performed:
  -
source_constraints_preserved:
  prd: true | false | not_relevant
  architecture: true | false | not_relevant
  adr: true | false | not_relevant
  roadmap: true | false | not_relevant
deviations:
  -
blockers:
  -
```

Required `Concrete Next Step`:

- `next_step_type`: `RUN_REVIEW`, `UPDATE_PLAN`, or `RESOLVE_SOURCE_CONFLICT`
- `target`: implementation summary and changed files
- `action`: review or resolve blocker based on implementation result
- `blocking_condition`: missing validation evidence or unresolved source conflict

---

## 20. Lightweight Implementation → Review

Use when lightweight implementation is complete or blocked.

Required handoff payload:

```yaml
artifact_type: LIGHTWEIGHT_IMPLEMENTATION_SUMMARY
artifact_status: COMPLETED | BLOCKED | DEVIATED
decision: RUN_LIGHTWEIGHT_REVIEW | UPDATE_LIGHTWEIGHT_PLAN | ESCALATE_TO_FULL_WORKFLOW
core_rationale:
plan_path:
changes_made:
  -
files_changed:
  -
validation_performed:
  -
lightweight_assumptions_preserved:
  product_behavior_unchanged_or_clear: true | false
  architecture_unchanged: true | false
  no_adr_decision_introduced: true | false
  no_roadmap_need_introduced: true | false
deviations:
  -
escalation_trigger_hit: true | false
```

Required `Concrete Next Step`:

- `next_step_type`: `RUN_LIGHTWEIGHT_REVIEW`, `UPDATE_LIGHTWEIGHT_PLAN`, or `ESCALATE_TO_FULL_WORKFLOW`
- `target`: lightweight implementation summary and changed files
- `action`: review lightweight implementation or escalate to full workflow
- `blocking_condition`: lightweight assumptions were not preserved

---

## 21. Review Output

Use when review produces an approval, revision, or escalation decision.

Required handoff payload:

```yaml
artifact_type: TASK_REVIEW_REPORT | LIGHTWEIGHT_TASK_REVIEW_REPORT | ROADMAP_REVIEW_REPORT | ARTIFACT_CONSISTENCY_REVIEW_REPORT
artifact_status: APPROVED | APPROVED_WITH_MINOR_IMPROVEMENTS | NEEDS_REVISION | BLOCKED
decision:
reviewed_sources:
  -
findings:
  - severity: BLOCKER | MAJOR | MINOR | NOTE
    type:
    description:
    required_action:
acceptance_decision:
```

Required `Concrete Next Step`:

- `next_step_type`: one canonical review next-step value from `NEXT_STEP_TYPES.md`
- `target`: the artifact/action that must happen next
- `action`: execute the acceptance, correction, evidence request, or escalation
- `blocking_condition`: unresolved blocker, missing evidence, or conflicting source artifact

If review finds architecture, ADR, PRD, roadmap, or plan drift, it must route to the correct artifact update instead of approving silently.

---

## 22. Artifact Consistency Review Output

Use before implementation when durable artifacts may contradict each other.

Required handoff payload:

```yaml
artifact_type: ARTIFACT_CONSISTENCY_REVIEW_REPORT
artifact_status: CONSISTENT | CONSISTENT_WITH_MINOR_GAPS | NEEDS_ARTIFACT_REVISION | BLOCKED
decision:
reviewed_artifacts:
  prd:
  architecture:
  adrs:
    -
  roadmap:
  plan:
consistency_findings:
  - source:
    target:
    issue:
    severity:
    required_action:
implementation_readiness:
```

Required `Concrete Next Step`:

- `next_step_type`: `IMPLEMENT_PLAN`, `UPDATE_PRD`, `UPDATE_ARCHITECTURE`, `UPDATE_ADR`, `UPDATE_ROADMAP`, `UPDATE_PLAN`, or `STOP_AND_ESCALATE`
- `target`: the artifact/action that resolves the inconsistency or starts implementation
- `action`: execute the next consistency or implementation step
- `blocking_condition`: unresolved artifact contradiction or missing source evidence

---

## 23. Portability Rule

These handoff contracts are workflow-generic.

Domain-specific constraints should be layered through:

- project-level `AGENTS.md`
- nested `AGENTS.md`
- domain-specific checklists
- domain-specific skills

Do not overload this file with project-specific business rules.
