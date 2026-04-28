# Handoff Payloads

This file defines the minimum structured payload that brainstorm should pass to the next artifact phase.

The payload belongs in the `Next Artifact Handoff Payload` section of the brainstorm output.

Do not write full PRD, Architecture, ADR, roadmap, document plan, or implementation content here.

## Common Handoff Fields

Every handoff payload must include:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: <DRAFT | APPROVED | UPDATED | DEFERRED | REJECTED | BLOCKED>
decision: <final decision>
why: <compact rationale>
source_artifacts:
  - <brainstorm artifact path or source document path>
next_step: <exact next step>
```

Optional fields:

```yaml
open_questions:
  - <only material questions>
constraints:
  - <only material constraints>
risks:
  - <only material risks>
deferred_items:
  - <only if relevant>
follow_up_needed:
  - <only if relevant>
```

## Brainstorm → PRD

Use when final decision is:

- `NEW_PRD`
- `PRD_UPDATE`

Required payload:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: <status>
decision: <NEW_PRD | PRD_UPDATE>
problem_statement: <one clear sentence>
target_users_or_actors:
  - <user or actor>
business_need: <why this matters>
product_intent_summary: <compact product direction>
goals:
  - <goal>
non_goals:
  - <non-goal>
key_flows_or_domains:
  - <flow or domain>
known_constraints:
  - <constraint>
reason_prd_is_needed: <why PRD is the correct immediate artifact>
source_artifacts:
  - <brainstorm artifact path>
next_step: <Proceed to NEW_PRD or PRD_UPDATE>
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
artifact_status: <status>
decision: <NEW_ARCHITECTURE | ARCHITECTURE_UPDATE>
architecture_scope: <system, repo, product area, or initiative scope>
system_or_repo_context: <compact context for the architecture writer>
why_architecture_is_needed_now: <why system structure is the correct immediate artifact>
known_modules_or_boundaries:
  - <module, layer, bounded context, or ownership boundary>
known_data_flows:
  - <data flow if known>
known_integration_points:
  - <integration point if known>
known_runtime_or_deployment_context:
  - <runtime/deployment fact if known>
known_cross_cutting_concerns:
  - <security, observability, performance, reliability, maintainability, etc.>
known_constraints:
  - <constraint>
known_risks:
  - <risk>
open_questions:
  - <material question>
source_artifacts:
  - <brainstorm artifact path>
next_step: <Proceed to NEW_ARCHITECTURE or ARCHITECTURE_UPDATE>
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
artifact_status: <status>
decision: <NEW_ADR | ADR_UPDATE>
decision_scope: <one bounded technical decision>
technical_problem_statement: <technical problem to decide>
why_this_is_technical_not_product: <reason>
why_adr_not_architecture: <why this is one decision rather than broad system structure>
decision_drivers:
  - <driver>
credible_options_if_known:
  - <option>
known_constraints:
  - <constraint>
source_artifacts:
  - <brainstorm artifact path>
next_step: <Proceed to NEW_ADR or ADR_UPDATE>
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
artifact_status: <status>
decision: <roadmap decision>
initiative_or_product_scope: <scope>
delivery_objective: <what delivery should accomplish>
why_roadmap_is_needed_now: <why sequencing is the immediate need>
known_dependencies:
  - <dependency>
known_risks:
  - <risk>
known_constraints:
  - <constraint>
whether_prd_is_already_sufficient: <yes | no | unknown, with reason>
whether_architecture_is_already_sufficient: <yes | no | unknown, with reason>
source_artifacts:
  - <brainstorm artifact path>
next_step: <Proceed to roadmap action>
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
artifact_status: <status>
decision: <NEW_DOCUMENT_PLAN | DOCUMENT_PLAN_UPDATE>
document_plan_scope: <which document or document set needs planning>
why_document_plan_is_needed_now: <why planning documentation production/refactor is the immediate need>
known_source_artifacts:
  - <source artifact>
intended_output_artifacts:
  - <target document or document family>
known_dependencies:
  - <dependency>
known_constraints:
  - <constraint>
known_risks:
  - <risk>
acceptance_criteria_signals:
  - <quality or completion signal>
source_artifacts:
  - <brainstorm artifact path>
next_step: <Proceed to NEW_DOCUMENT_PLAN or DOCUMENT_PLAN_UPDATE>
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
artifact_status: <DEFERRED | REJECTED | BLOCKED>
decision: REJECT_OR_DEFER
why_forward_progress_should_stop: <reason>
what_is_missing_or_conflicting:
  - <missing evidence, unresolved conflict, or unclear constraint>
recommended_resolution:
  - <what to do before reopening>
reopen_when:
  - <condition>
source_artifacts:
  - <brainstorm artifact path if durable, otherwise source inputs>
next_step: Stop here. Do not proceed until stronger evidence exists.
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
