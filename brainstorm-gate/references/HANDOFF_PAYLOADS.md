# Handoff Payloads

This file defines the minimum structured payload that brainstorm should pass to the next artifact phase.

The payload belongs in the `Next Artifact Handoff Payload` section of the brainstorm output.

Do not write full PRD, Architecture, ADR, roadmap, document plan, or implementation content here.

## Common Handoff Fields

Every handoff payload must include:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
why:
source_artifacts:
  -
concrete_next_step:
  next_step_type:
  target:
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Optional fields:

```yaml
open_questions:
  -
constraints:
  -
risks:
  -
deferred_items:
  -
follow_up_needed:
  -
```

Do not use the old `next_step` field as the only next-step contract. Use `concrete_next_step` inside the payload and the full `## Concrete Next Step` block at the end of the output.

## Brainstorm → PRD

Use when final decision is:

- `NEW_PRD`
- `PRD_UPDATE`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
problem_statement:
target_users_or_actors:
  -
business_need:
product_intent_summary:
goals:
  -
non_goals:
  -
key_flows_or_domains:
  -
known_constraints:
  -
reason_prd_is_needed:
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_PRD # or UPDATE_PRD
  target: PRD.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Consumed by PRD writer:

- problem and user context
- product intent
- goals and non-goals
- affected flows or domains
- constraints
- create-vs-update rationale

Not required:

- PRD section drafts
- architecture section drafts
- roadmap phases
- plan-level detail
- implementation file lists
- technical design unless it directly constrains product behavior

## Brainstorm → Architecture

Use when final decision is:

- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
architecture_scope:
system_or_repo_context:
why_architecture_is_needed_now:
known_modules_or_boundaries:
  -
known_data_flows:
  -
known_integration_points:
  -
known_runtime_or_deployment_context:
  -
known_cross_cutting_concerns:
  -
known_constraints:
  -
known_risks:
  -
open_questions:
  -
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_ARCHITECTURE # or UPDATE_ARCHITECTURE
  target: ARCHITECTURE.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Consumed by Architecture writer:

- architecture scope
- system or repo context
- boundaries and layers needing clarification
- integrations and data flow signals
- runtime/deployment constraints
- cross-cutting concerns
- known risks and unresolved questions
- create-vs-update basis

Not required:

- full Architecture document sections
- full PRD structure
- full ADR rationale
- roadmap phases
- task-level implementation detail
- file-by-file implementation plan

## Brainstorm → ADR

Use when final decision is:

- `NEW_ADR`
- `ADR_UPDATE`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
decision_scope:
technical_problem_statement:
why_this_is_technical_not_product:
why_adr_not_architecture:
decision_drivers:
  -
credible_options_if_known:
  -
known_constraints:
  -
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_ADR # or UPDATE_ADR
  target: docs/adr/<number>-<decision>.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Consumed by ADR writer:

- decision boundary
- technical context
- drivers
- constraints
- why ADR is correct
- why Architecture is not the immediate next artifact

Not required:

- full PRD structure
- full Architecture document structure
- full roadmap structure
- implementation plan
- code-level pseudocode unless needed to explain an architectural option

## Brainstorm → Roadmap

Use when final decision is:

- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
initiative_or_product_scope:
delivery_objective:
why_roadmap_is_needed_now:
known_dependencies:
  -
known_risks:
  -
known_constraints:
  -
whether_prd_is_already_sufficient:
whether_architecture_is_already_sufficient:
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_INITIATIVE_ROADMAP # or another roadmap route
  target: ROADMAP.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Consumed by roadmap planner:

- scope of roadmap
- delivery objective
- dependency/risk signals
- create-vs-update basis
- product vs initiative roadmap mode
- whether PRD/Architecture should block roadmap creation

Not required:

- single-task detail
- code file expectations
- full implementation behavior
- full PRD, Architecture, or ADR content

## Brainstorm → Document Plan

Use when final decision is:

- `NEW_DOCUMENT_PLAN`
- `DOCUMENT_PLAN_UPDATE`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
document_plan_scope:
why_document_plan_is_needed_now:
known_source_artifacts:
  -
intended_output_artifacts:
  -
known_dependencies:
  -
known_constraints:
  -
known_risks:
  -
acceptance_criteria_signals:
  -
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_DOCUMENT_PLAN # or UPDATE_DOCUMENT_PLAN
  target:
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Consumed by Document Plan writer:

- scope of planned documentation work
- source artifacts and target artifacts
- sequencing/dependency signals
- constraints and risks
- create-vs-update basis

Not required:

- full PRD content
- full Architecture content
- full ADR content
- full roadmap phases
- implementation task list

## Brainstorm → Stop / Escalation

Use when final decision is:

- `REJECT_OR_DEFER`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision: REJECT_OR_DEFER
why_forward_progress_should_stop:
what_is_missing_or_conflicting:
  -
recommended_resolution:
  -
reopen_when:
  -
source_artifacts:
  -
concrete_next_step:
  next_step_type: REJECT_OR_DEFER
  target: No downstream artifact.
  action: Stop the workflow for now.
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

No downstream artifact should be created from this decision.

## Payload Selection Rule

Map the decision to exactly one payload shape:

| Decision | Payload |
|---|---|
| `NEW_PRD` | Brainstorm → PRD |
| `PRD_UPDATE` | Brainstorm → PRD |
| `NEW_ARCHITECTURE` | Brainstorm → Architecture |
| `ARCHITECTURE_UPDATE` | Brainstorm → Architecture |
| `NEW_ADR` | Brainstorm → ADR |
| `ADR_UPDATE` | Brainstorm → ADR |
| `NEW_PRODUCT_ROADMAP` | Brainstorm → Roadmap |
| `PRODUCT_ROADMAP_UPDATE` | Brainstorm → Roadmap |
| `NEW_INITIATIVE_ROADMAP` | Brainstorm → Roadmap |
| `INITIATIVE_ROADMAP_UPDATE` | Brainstorm → Roadmap |
| `NEW_DOCUMENT_PLAN` | Brainstorm → Document Plan |
| `DOCUMENT_PLAN_UPDATE` | Brainstorm → Document Plan |
| `REJECT_OR_DEFER` | Brainstorm → Stop / Escalation |

If the chosen payload feels insufficient, add only fields that are necessary for the next skill.

Do not copy the entire brainstorm narrative into the payload.
