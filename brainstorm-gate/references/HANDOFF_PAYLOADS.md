# Handoff Payloads

This file defines compact brainstorm handoffs. The shared contract in `docs/workflow/HANDOFF_CONTRACTS.md` is authoritative when there is any conflict.

Every handoff payload must include:

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
core_rationale:
source_artifacts:
  -
constraints:
  -
open_issues:
  -
concrete_next_step:
  next_step_type:
  target:
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

Do not use loose `next_step` or `follow_up` fields as the terminal contract. The output must also end with the full `## Concrete Next Step` block.

## Brainstorm To PRD

Use for `CREATE_PRD` or `UPDATE_PRD`.

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision: CREATE_PRD # or UPDATE_PRD
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
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_PRD
  target: PRD.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

## Brainstorm To Architecture

Use for `CREATE_ARCHITECTURE` or `UPDATE_ARCHITECTURE`.

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision: CREATE_ARCHITECTURE # or UPDATE_ARCHITECTURE
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
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_ARCHITECTURE
  target: ARCHITECTURE.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

## Brainstorm To ADR

Use for `CREATE_ADR` or `UPDATE_ADR`.

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision: CREATE_ADR # or UPDATE_ADR
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
source_artifacts:
  -
concrete_next_step:
  next_step_type: CREATE_ADR
  target: docs/adr/<decision>.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

## Brainstorm To Roadmap

Use for `CREATE_ROADMAP` or `UPDATE_ROADMAP`.

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision: CREATE_ROADMAP # or UPDATE_ROADMAP
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
concrete_next_step:
  next_step_type: CREATE_ROADMAP
  target: ROADMAP.md
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

## Brainstorm To Lightweight Plan

Use for `CREATE_LIGHTWEIGHT_PLAN`.

```yaml
artifact_type: LIGHTWEIGHT_MODE_CLASSIFICATION
artifact_status: APPROVED
decision: CREATE_LIGHTWEIGHT_PLAN
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
concrete_next_step:
  next_step_type: CREATE_LIGHTWEIGHT_PLAN
  target: lightweight plan output
  action:
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```

## Brainstorm To Stop Or Clarification

Use for `REJECT_OR_DEFER`, `REQUEST_CLARIFICATION`, or `STOP_AND_ESCALATE`.

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: BLOCKED
decision: REJECT_OR_DEFER
core_rationale:
what_is_missing_or_conflicting:
  -
recommended_resolution:
  -
reopen_when:
  -
concrete_next_step:
  next_step_type: REJECT_OR_DEFER
  target: No downstream artifact.
  action: Stop the workflow until the missing evidence or decision is supplied.
  why_this_is_next:
  blocking_condition:
  suggested_prompt:
```
