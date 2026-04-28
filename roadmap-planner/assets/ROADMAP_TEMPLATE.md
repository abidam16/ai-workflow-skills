# <Initiative or Product> Roadmap

## 1. Metadata

- `artifact_type`: ROADMAP
- `artifact_status`: DRAFT | APPROVED | UPDATED | BLOCKED
- `roadmap_mode`: PRODUCT | INITIATIVE
- `decision`: CREATE_ROADMAP | UPDATE_ROADMAP
- `owner`:
- `last_updated`:

## 2. Source Artifacts

| Artifact | Path | Status | Used For |
|---|---|---|---|
| PRD | `<path>` | `<status>` | Product truth |
| Architecture | `<path>` | `<status>` | System-shape constraints |
| ADR | `<path>` | `<status>` | Decision constraints |
| Existing Roadmap | `<path>` | `<status>` | Previous sequencing |

## 3. Delivery Objective

State the delivery outcome this roadmap exists to sequence.

## 4. Scope

### In Scope

- ...

### Out of Scope

- ...

## 5. Architecture Constraints Used

List only constraints that shape sequencing.

| Constraint | Source | Roadmap Impact |
|---|---|---|
| `<constraint>` | `<ARCHITECTURE.md section>` | `<phase/order/dependency impact>` |

## 6. ADR Constraints Used

| Decision | ADR | Roadmap Impact |
|---|---|---|
| `<decision>` | `<ADR path>` | `<phase/order/dependency impact>` |

## 7. Sequencing Strategy

- `primary_strategy`: VALUE_FIRST | DEPENDENCY_FIRST | RISK_FIRST | ARCHITECTURE_FOUNDATION_FIRST | MIGRATION_FIRST | ROLLOUT_FIRST | OPERABILITY_FIRST | MIXED
- `why_this_strategy`:

## 8. Roadmap Phases

### Phase 1 — <Type>: <Meaningful Title>

- `objective`:
- `why_this_phase_exists_now`:
- `product_outcome`:
- `architecture_constraints_used`:
- `adr_constraints_used`:
- `key_outcomes`:
  - ...
- `in_scope`:
  - ...
- `out_of_scope`:
  - ...
- `dependencies`:
  - ...
- `risks`:
  - ...
- `exit_criteria`:
  - ...
- `plan_handoff_candidates`:
  - `task_name`:
    - `task_objective`:
    - `why_it_is_one_task`:
    - `scope_boundary`:
    - `expected_components_or_layers`:
    - `validation_direction`:

### Phase 2 — <Type>: <Meaningful Title>

- `objective`:
- `why_this_phase_exists_now`:
- `product_outcome`:
- `architecture_constraints_used`:
- `adr_constraints_used`:
- `key_outcomes`:
  - ...
- `in_scope`:
  - ...
- `out_of_scope`:
  - ...
- `dependencies`:
  - ...
- `risks`:
  - ...
- `exit_criteria`:
  - ...
- `plan_handoff_candidates`:
  - ...

## 9. Cross-Cutting Concerns

Capture concerns that apply across multiple phases without turning them into implementation tasks.

- Security / authorization:
- Observability / logging:
- Data migration / compatibility:
- Reliability / recovery:
- Performance / scalability:
- UX / documentation / support:

## 10. Deferred / Not Next

List work intentionally deferred from the next plan.

| Item | Reason Deferred | Revisit Trigger |
|---|---|---|
| ... | ... | ... |

## 11. Open Delivery Questions

Only include unresolved questions that affect sequencing or plan readiness.

| Question | Impact | Required Next Artifact |
|---|---|---|
| ... | ... | PRD | ARCHITECTURE | ADR | PLAN |

## 12. Plan Handoff Candidates

Recommend the next single-task plan candidate first.

### Recommended Next Plan Candidate

- `task_name`:
- `task_objective`:
- `why_it_is_one_task`:
- `scope_boundary`:
- `expected_components_or_layers`:
- `architecture_constraints_to_include`:
- `adr_constraints_to_include`:
- `validation_direction`:

### Later Plan Candidates

- ...

## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
