# HANDOFF_CONTRACTS.md

Purpose: define the minimum required input/output fields between workflow phases so each skill can hand off cleanly to the next phase with low ambiguity, controlled token usage, and correct source-of-truth authority.

---

## 1. Core Rule

Each phase should pass forward only the **minimum structured payload** the next phase needs.

Do not pass the entire history if a compact handoff is enough.

Every handoff must include:

- artifact type
- artifact status
- decision/routing
- core rationale
- references to upstream artifacts
- constraints that materially affect the next phase
- open issues that materially affect the next phase
- exactly one next step

Architecture is now a first-class handoff artifact. When relevant, downstream phases must receive architecture constraints instead of re-inferring system shape from prose, code, or assumptions.

---

## 2. Standard Field Conventions

Use these field meanings consistently.

### `artifact_type`

Examples:

- `BRAINSTORM_OUTPUT`
- `PRD`
- `PRD_DELTA`
- `ARCHITECTURE`
- `ARCHITECTURE_DELTA`
- `INITIATIVE_ARCHITECTURE`
- `INITIATIVE_ARCHITECTURE_DELTA`
- `ADR`
- `ADR_DELTA`
- `ROADMAP`
- `ROADMAP_DELTA`
- `PLAN`
- `PLAN_DELTA`
- `IMPLEMENTATION_SUMMARY`
- `TASK_REVIEW_REPORT`
- `ROADMAP_REVIEW_REPORT`

### `artifact_status`

Examples:

- `DRAFT`
- `APPROVED`
- `UPDATED`
- `REJECTED`
- `DEFERRED`
- `SUPERSEDED`
- `ARCHIVED`
- `BLOCKED`

### `decision`

The explicit routing, acceptance, or stop decision for that phase.

### `source_artifacts`

List of upstream artifacts used as source of truth.

### `architecture_scope`

The architecture scope affected by the handoff.

Common values:

- `ROOT`
- `INITIATIVE`
- `BOTH`
- `NONE`

### `architecture_path`

The relevant architecture document path.

Examples:

- `ARCHITECTURE.md`
- `docs/architecture/notification-system-architecture.md`
- `none`

### `open_questions`

Only unresolved questions that materially affect the next phase.

### `constraints`

Only constraints that materially affect the next phase.

### `architecture_constraints`

The subset of constraints coming from root or initiative architecture.

Examples:

- component/module/service boundaries
- data ownership/source-of-truth rules
- runtime flow constraints
- sync/async boundaries
- transaction/consistency/idempotency/retry rules
- authorization/security constraints
- observability/deployment/performance constraints

### `next_step`

Exactly one immediate next step.

---

## 3. Global Handoff Policy

### Required in every handoff

- `artifact_type`
- `artifact_status`
- `decision`
- `why`
- `source_artifacts`
- `next_step`

### Required when architecture is relevant

- `architecture_scope`
- `architecture_path`
- `architecture_constraints`
- `architecture_open_questions`
- `architecture_impact`

### Optional

- `open_questions`
- `constraints`
- `risks`
- `deferred_items`
- `follow_up_needed`

### Do not pass forward unless needed

- full exploratory narrative
- duplicated product background
- repeated roadmap prose
- repeated architecture prose when a compact constraint list is enough
- repeated implementation detail already captured in plan
- low-importance observations

---

## 4. Brainstorm → PRD

Use when brainstorm decides:

- `NEW_PRD`
- `PRD_UPDATE`

### Required output from brainstorm

- `artifact_type: BRAINSTORM_OUTPUT`
- `decision: NEW_PRD | PRD_UPDATE`
- `problem_statement`
- `target_users_or_actors`
- `business_need`
- `product_intent_summary`
- `goals`
- `non_goals`
- `key_flows_or_domains`
- `known_constraints`
- `known_architecture_signals`
- `reason_prd_is_needed`
- `source_artifacts`
- `next_step`

### Consumed by PRD writer

- problem and user context
- product intent
- goals / non-goals
- affected flows/domains
- constraints
- architecture signals that may become PRD handoff impact
- why create vs update

### Not required

- roadmap phases
- plan-level detail
- implementation file lists
- full architecture design

---

## 5. Brainstorm → Architecture

Use when brainstorm decides:

- `NEW_ARCHITECTURE`
- `ARCHITECTURE_UPDATE`

### Required output from brainstorm

- `artifact_type: BRAINSTORM_OUTPUT`
- `decision: NEW_ARCHITECTURE | ARCHITECTURE_UPDATE`
- `architecture_problem_statement`
- `why_architecture_is_needed`
- `known_product_context`
- `affected_components_or_domains`
- `known_boundaries_or_boundary_gaps`
- `known_data_ownership_or_source_of_truth_issues`
- `known_runtime_flows_or_integration_points`
- `known_cross_cutting_constraints`
- `architecture_scope_hint: ROOT | INITIATIVE | UNKNOWN`
- `related_prd_if_any`
- `related_adrs_if_any`
- `related_roadmap_if_any`
- `source_artifacts`
- `next_step`

### Consumed by architecture writer

- architecture problem boundary
- product context that is stable enough to design against
- affected system areas
- boundary/data/flow/constraint signals
- root vs initiative hints
- create vs update basis

### Not required

- full PRD structure
- final ADR decisions
- roadmap phases
- plan/task detail
- implementation file lists

---

## 6. Brainstorm → ADR

Use when brainstorm decides:

- `NEW_ADR`
- `ADR_UPDATE` if your practice allows it

### Required output from brainstorm

- `artifact_type: BRAINSTORM_OUTPUT`
- `decision: NEW_ADR | ADR_UPDATE`
- `decision_scope`
- `technical_problem_statement`
- `why_this_is_technical_not_product`
- `why_this_is_adr_not_architecture`
- `decision_drivers`
- `credible_options_if_known`
- `known_constraints`
- `related_architecture_if_any`
- `source_artifacts`
- `next_step`

### Consumed by ADR writer

- decision boundary
- technical context
- drivers
- constraints
- architecture context, if any
- why ADR is the correct artifact

### Not required

- full PRD structure
- full architecture structure
- full roadmap structure
- plan/task detail

---

## 7. Brainstorm → Roadmap

Use when brainstorm decides:

- `NEW_PRODUCT_ROADMAP`
- `PRODUCT_ROADMAP_UPDATE`
- `NEW_INITIATIVE_ROADMAP`
- `INITIATIVE_ROADMAP_UPDATE`

### Required output from brainstorm

- `artifact_type: BRAINSTORM_OUTPUT`
- `decision`
- `initiative_or_product_scope`
- `delivery_objective`
- `why_roadmap_is_needed_now`
- `known_dependencies`
- `known_risks`
- `known_constraints`
- `whether_prd_is_already_sufficient`
- `whether_architecture_is_already_sufficient`
- `whether_blocking_adrs_are_resolved`
- `source_artifacts`
- `next_step`

### Consumed by roadmap planner

- scope of roadmap
- delivery objective
- dependency/risk signals
- architecture readiness signal
- ADR readiness signal
- create vs update basis
- product vs initiative roadmap mode

### Not required

- single-task detail
- code file expectations
- full implementation behavior

---

## 8. PRD → Architecture

Use when PRD is complete enough and the next need is system-shape guidance.

### Required output from PRD writer

- `artifact_type: PRD | PRD_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_ARCHITECTURE | HOLD`
- `product_overview_summary`
- `current_goals`
- `current_non_goals`
- `key_roles_and_flows`
- `product_rules`
- `current_behavior_summary`
- `target_behavior_summary`
- `success_criteria`
- `architecture_impact`
- `architecture_questions`
- `known_constraints`
- `source_artifacts`
- `next_step`

### `architecture_impact` format

- `impact_type: none | create root architecture | update root architecture | create initiative architecture | update initiative architecture | unknown`
- `why_architecture_is_or_is_not_needed`
- `affected_components_or_domains`
- `data_ownership_signals`
- `integration_or_runtime_flow_signals`
- `cross_cutting_constraint_signals`

### Consumed by architecture writer

- stable product behavior
- product rules that architecture must preserve
- architecture-impacting flows/domains
- source-of-truth or integration signals
- open questions that block architecture

### Not required

- delivery phases
- ADR rationale
- implementation steps
- file-level changes

---

## 9. PRD → Roadmap

Use when PRD is complete enough, architecture is not needed or already sufficient, and the next need is delivery sequencing.

### Required output from PRD writer

- `artifact_type: PRD | PRD_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_ROADMAP | HOLD`
- `product_overview_summary`
- `current_goals`
- `current_non_goals`
- `key_roles_and_flows`
- `product_rules`
- `current_behavior_summary`
- `target_behavior_summary`
- `success_criteria`
- `important_open_questions`
- `architecture_impact`
- `architecture_readiness: not needed | sufficient | insufficient | unknown`
- `roadmap_implications`
- `source_artifacts`
- `next_step`

### Consumed by roadmap planner

- product truth
- delivery implications
- architecture readiness
- areas requiring staged work
- open questions that may affect sequencing

### Not required

- task-level implementation detail
- low-level design alternatives

---

## 10. Architecture → ADR

Use when architecture exposes one important decision that must be recorded separately.

### Required output from architecture writer

- `artifact_type: ARCHITECTURE | ARCHITECTURE_DELTA | INITIATIVE_ARCHITECTURE | INITIATIVE_ARCHITECTURE_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_ADR | HOLD`
- `architecture_scope`
- `architecture_path`
- `architecture_summary`
- `decision_candidate_title`
- `decision_scope`
- `why_adr_is_needed`
- `decision_drivers`
- `credible_options_if_known`
- `constraints_from_architecture`
- `affected_architecture_sections`
- `source_artifacts`
- `next_step`

### Consumed by ADR writer

- decision boundary
- architecture context
- drivers and constraints
- affected sections that may need ADR link-back

### Not required

- full architecture document
- roadmap phase detail
- plan task detail

---

## 11. Architecture → Roadmap

Use when architecture is stable enough and staged delivery is needed.

### Required output from architecture writer

- `artifact_type: ARCHITECTURE | ARCHITECTURE_DELTA | INITIATIVE_ARCHITECTURE | INITIATIVE_ARCHITECTURE_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_ROADMAP | HOLD`
- `architecture_scope`
- `architecture_path`
- `architecture_summary`
- `relevant_components_or_layers`
- `data_ownership_rules`
- `runtime_flows`
- `integration_boundaries`
- `cross_cutting_constraints`
- `architecture_dependencies`
- `architecture_risks`
- `adr_status_summary`
- `roadmap_implications`
- `source_artifacts`
- `next_step`

### Consumed by roadmap planner

- stable architecture constraints
- sequencing dependencies from architecture
- architectural risks that affect phases
- ADR readiness
- plan candidate boundaries

### Not required

- full architecture document if a compact summary and file reference are enough
- task-level steps
- implementation file lists

---

## 12. Architecture → Plan

Use when architecture is stable enough and exactly one bounded task is ready without needing roadmap first.

### Required output from architecture writer

- `artifact_type: ARCHITECTURE | ARCHITECTURE_DELTA | INITIATIVE_ARCHITECTURE | INITIATIVE_ARCHITECTURE_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_PLAN | HOLD`
- `architecture_scope`
- `architecture_path`
- `selected_task_candidate`
- `why_roadmap_is_not_needed`
- `task_objective`
- `scope_boundary`
- `relevant_components_or_layers`
- `architecture_constraints`
- `data_ownership_rules`
- `runtime_or_integration_flow_constraints`
- `transaction_consistency_or_idempotency_rules`
- `security_observability_or_deployment_rules`
- `validation_direction`
- `source_artifacts`
- `next_step`

### Consumed by plan writer

- one bounded task candidate
- architecture constraints for that task
- scope boundary
- validation direction

### Not required

- full roadmap structure
- full implementation algorithm
- detailed file-by-file edits

---

## 13. ADR → Architecture

Use when an accepted ADR changes architecture constraints or should be linked from architecture.

### Required output from ADR writer

- `artifact_type: ADR | ADR_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_ARCHITECTURE_UPDATE | NO_ARCHITECTURE_UPDATE_NEEDED | HOLD`
- `decision_title`
- `context_summary`
- `chosen_option`
- `key_consequences`
- `architecture_impact`
- `affected_architecture_path`
- `affected_architecture_sections`
- `required_architecture_updates`
- `source_artifacts`
- `next_step`

### Consumed by architecture writer

- accepted decision
- consequences to reflect in architecture
- sections needing link/update
- supersession impact, if any

### Not required

- full ADR body if decision/consequences are summarized and path is provided
- roadmap phase detail
- plan task detail

---

## 14. ADR → Roadmap

Use when a technical decision is accepted and staged delivery is needed.

### Required output from ADR writer

- `artifact_type: ADR | ADR_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_ROADMAP | PROCEED_TO_PLAN | PROCEED_TO_ARCHITECTURE_UPDATE | HOLD`
- `decision_title`
- `context_summary`
- `decision_drivers`
- `chosen_option`
- `key_consequences`
- `scope_and_impact`
- `architecture_impact`
- `architecture_readiness`
- `non_goals_or_not_addressed`
- `downstream_delivery_implications`
- `source_artifacts`
- `next_step`

### Consumed by roadmap planner

- decision and consequences
- scope/impact
- architecture readiness
- constraints that shape sequencing
- whether roadmap should exist at all

---

## 15. Roadmap → Plan

Use when one roadmap phase or slice is ready to become an executable task.

### Required output from roadmap planner

- `artifact_type: ROADMAP | ROADMAP_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_PLAN`
- `roadmap_mode: PRODUCT | INITIATIVE`
- `selected_phase_or_slice`
- `phase_objective`
- `why_this_slice_is_next`
- `in_scope_for_this_slice`
- `out_of_scope_for_this_slice`
- `dependencies`
- `risks`
- `exit_criteria`
- `architecture_scope`
- `architecture_path`
- `architecture_constraints`
- `adr_constraints`
- `plan_handoff_candidates`

### `plan_handoff_candidates` format

For each candidate task:

- `task_name`
- `task_objective`
- `why_it_is_one_task`
- `scope_boundary`
- `expected_components_or_layers`
- `architecture_constraints`
- `adr_constraints`
- `validation_direction`

### Consumed by plan writer

- one selected roadmap slice
- one candidate task
- scope boundary
- architecture/ADR constraints
- validation direction

### Not required

- full roadmap history
- all phases if only one task is being planned
- full architecture prose if compact constraints are enough

---

## 16. Plan → Implementation

Use when one single-task plan is approved.

### Required output from plan writer

- `artifact_type: PLAN | PLAN_DELTA`
- `artifact_status`
- `decision: PROCEED_TO_IMPLEMENTATION | SPLIT_REQUIRED | HOLD`
- `task_summary`
- `objective`
- `in_scope`
- `out_of_scope`
- `detailed_spec`
- `expected_changes`
- `must_not_change`
- `architecture_scope`
- `architecture_path`
- `architecture_constraints`
- `adr_constraints`
- `validation_requirements`
- `test_requirements`
- `review_checkpoints`
- `tradeoffs_and_risks`
- `future_improvements`
- `source_artifacts`
- `next_step`

### Consumed by implement-task

- complete single-task execution contract
- exact scope boundaries
- validation/test obligations
- file/component boundaries
- architecture and ADR constraints

### Hard rule

If `decision != PROCEED_TO_IMPLEMENTATION`, implementation must not start.

If `architecture_constraints` are required but missing, implementation must not infer them silently; it must stop or report the missing upstream artifact.

---

## 17. Implementation → Review

Use when one approved task has been implemented or implementation was blocked.

### Required output from implement-task

- `artifact_type: IMPLEMENTATION_SUMMARY`
- `artifact_status: COMPLETED | BLOCKED | PARTIAL`
- `decision: READY_FOR_REVIEW | BLOCKED`
- `plan_reference`
- `objective_restatement`
- `scope_followed_summary`
- `architecture_constraints_followed_summary`
- `adr_constraints_followed_summary`
- `files_changed`
- `files_not_changed`
- `implementation_summary`
- `validation_done`
- `tests_run_or_updated`
- `deviations`
- `architecture_deviations`
- `blockers`
- `remaining_gaps`
- `self_check_result`
- `next_step`

### `deviations` format

For each deviation:

- `severity: HIGH | MEDIUM | LOW`
- `what_changed_from_plan`
- `why`
- `impact`
- `whether_plan_update_is_needed`

### `architecture_deviations` format

For each architecture deviation:

- `severity: HIGH | MEDIUM | LOW`
- `violated_architecture_reference`
- `what_changed_from_architecture`
- `why`
- `impact`
- `whether_architecture_update_is_needed`
- `whether_adr_is_needed`

### Consumed by review phase

- implementation summary
- deviations/blockers
- architecture deviations
- self-check result
- plan reference
- evidence of validation/tests

---

## 18. Plan → Review (Task Review Inputs)

Task review should not rely on implementation summary alone.

### Required review inputs

- `PLAN`
- `IMPLEMENTATION_SUMMARY`
- relevant code/diff/tests
- relevant `ARCHITECTURE.md` or initiative architecture when task is architecture-sensitive
- relevant ADRs when decisions constrain implementation
- relevant roadmap slice if needed
- relevant PRD context if needed

### Required source-of-truth handling

Use each artifact for its authority:

1. `PLAN` controls task scope and explicit implementation obligations.
2. `PRD` controls product behavior and acceptance intent.
3. `ARCHITECTURE.md` / initiative architecture controls system-shape constraints.
4. ADRs control specific recorded technical decisions.
5. Roadmap controls sequencing and phase/slice intent.
6. Implementation output states what changed.
7. Validation evidence supports or weakens the implementation claim.

Conflict rule:

- If `PLAN` conflicts with PRD, architecture, or ADRs, do not approve silently. Report the conflict and route to the correct artifact update or plan revision.

---

## 19. Roadmap → Review (Roadmap Implementation Review Inputs)

Use for cross-task or initiative-level review.

### Required inputs

- `ROADMAP`
- relevant root or initiative architecture documents
- relevant ADRs
- relevant PRD context
- set of relevant `PLAN` artifacts
- set of relevant `IMPLEMENTATION_SUMMARY` artifacts
- integration evidence if available

### Required review focus

- roadmap fulfillment
- architecture alignment across tasks
- cross-task gaps
- integration risk
- business fulfillment across the initiative
- sequencing or dependency issues
- follow-up tasks needed
- architecture or ADR updates needed

---

## 20. Review Outputs

### Task Review output

Required fields:

- `artifact_type: TASK_REVIEW_REPORT`
- `artifact_status`
- `decision: APPROVED | APPROVED_WITH_MINOR_IMPROVEMENTS | NEEDS_REVISION | BLOCKED`
- `review_scope`
- `source_artifacts`
- `business_alignment_assessment`
- `architecture_alignment_assessment`
- `adr_alignment_assessment`
- `plan_alignment_assessment`
- `technical_quality_assessment`
- `validation_and_test_assessment`
- `findings`
- `risk_assessment`
- `recommended_next_actions`
- `next_step`

### Roadmap Review output

Required fields:

- `artifact_type: ROADMAP_REVIEW_REPORT`
- `artifact_status`
- `decision: APPROVED | APPROVED_WITH_MINOR_IMPROVEMENTS | NEEDS_REVISION | BLOCKED`
- `review_scope`
- `source_artifacts`
- `roadmap_fulfillment_assessment`
- `business_alignment_assessment`
- `architecture_alignment_assessment`
- `cross_task_alignment_assessment`
- `technical_quality_summary`
- `findings`
- `risk_assessment`
- `recommended_next_actions`
- `next_step`

### `findings` format

For each finding:

- `severity: HIGH | MEDIUM | LOW`
- `category`
- `title`
- `description`
- `why_it_matters`
- `recommended_action`

Common architecture-related categories:

- `ARCHITECTURE_VIOLATION`
- `SOURCE_OF_TRUTH_VIOLATION`
- `BOUNDARY_VIOLATION`
- `ADR_CONFLICT`
- `PLAN_ARCHITECTURE_CONFLICT`
- `MISSING_ARCHITECTURE_UPDATE`
- `MISSING_ADR`

---

## 21. Minimal Carry-Forward Rules

To control token usage, pass only:

### From brainstorm

- decision
- rationale
- key problem/intent/constraints
- architecture signals if relevant

### From PRD

- product truth summary
- architecture impact
- roadmap implications
- open questions that materially matter

### From architecture

- architecture path
- scope
- compact system-shape summary
- constraints relevant to the next phase
- ADR impact
- roadmap impact
- plan readiness
- open architecture questions

### From ADR

- chosen decision
- drivers
- consequences
- architecture impact
- downstream impact

### From roadmap

- selected phase/slice
- why it is next
- task candidate boundary
- architecture/ADR constraints relevant to the selected slice

### From plan

- exact task execution contract
- architecture/ADR constraints relevant to the task

### From implementation

- what changed
- what deviated
- what was validated
- architecture/ADR deviations
- blockers/gaps

### From review

- verdict
- major findings
- architecture/ADR conflicts
- next actions

---

## 22. Stop / Escalation Contract

Any phase may stop and escalate instead of handing off forward.

### Required stop fields

- `artifact_type`
- `artifact_status: BLOCKED | DEFERRED`
- `decision`
- `why_forward_progress_should_stop`
- `what_is_missing_or_conflicting`
- `recommended_resolution`
- `next_step`

### Stop examples

- PRD is insufficient for architecture.
- Architecture is required before roadmap.
- ADR is required before architecture can be finalized.
- Roadmap cannot sequence work because architecture dependencies are unclear.
- PLAN cannot proceed because architecture constraints are missing.
- Implementation found a plan/architecture conflict.
- Review found an architecture violation or missing ADR.

No stop condition should end without a recommended resolution.

---

## 23. Portability Rule

These handoff contracts are workflow-generic.

They are intended to work across:

- frontend
- backend
- platform/infrastructure
- internal tools
- healthcare systems
- finance systems
- general product applications

Domain-specific additions should be layered separately through:

- `AGENTS.md`
- nested `AGENTS.md`
- domain-specific review checklists
- domain-specific skills

Do not overload these generic handoff contracts with domain-specific regulation content.
