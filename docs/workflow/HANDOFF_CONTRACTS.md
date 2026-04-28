# HANDOFF_CONTRACTS.md

Purpose: define minimum required input/output fields between workflow phases so each skill can hand off cleanly with low ambiguity, controlled token usage, and correct source-of-truth authority.

---

## 1. Core Rule

Each phase should pass forward only the **minimum structured payload** the next phase needs. Do not pass the entire history if a compact handoff is enough.

Every handoff must include:

- artifact type
- artifact status
- decision/routing
- core rationale
- references to upstream artifacts
- constraints that materially affect the next phase
- open issues that materially affect the next phase
- exactly one `Concrete Next Step`

Architecture is a first-class handoff artifact. Lightweight mode is a first-class shortcut only for small, local, low-risk work.

---

## 2. Standard Artifact Types

Common values:

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
- `LIGHTWEIGHT_PLAN`
- `IMPLEMENTATION_SUMMARY`
- `LIGHTWEIGHT_IMPLEMENTATION_SUMMARY`
- `TASK_REVIEW_REPORT`
- `LIGHTWEIGHT_TASK_REVIEW_REPORT`
- `ARTIFACT_CONSISTENCY_REVIEW_REPORT`
- `ROADMAP_REVIEW_REPORT`

---

## 3. Required Concrete Next Step

Every handoff must end with:

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

Do not use old terminal fields such as `Immediate Next Step`, `Continuation Prompt`, loose `next_step`, or loose `follow_up`.

---

## 4. Lightweight Eligibility Handoff

Use when a phase decides that full PRD/Architecture/ADR/Roadmap work is not needed.

Required fields:

```yaml
artifact_type: LIGHTWEIGHT_MODE_CLASSIFICATION
artifact_status: APPROVED | REJECTED | BLOCKED
decision: USE_LIGHTWEIGHT_MODE | ESCALATE_TO_FULL_WORKFLOW
source_artifacts:
  - <issue/request/brainstorm/doc/code reference>
lightweight_classification:
  mode: LIGHTWEIGHT_TASK
  reason: <why the work is small/local/low-risk>
  scope: <one objective>
  why_prd_not_needed: <product truth already clear/unaffected>
  why_architecture_not_needed: <system shape/boundaries unaffected>
  why_adr_not_needed: <no durable decision required>
  why_roadmap_not_needed: <no staged sequencing required>
  validation_path: <small explicit validation>
  escalation_trigger: <condition that exits lightweight mode>
```

Consumed by:

- `plan-writer` for lightweight plan creation
- `implement-task` for lightweight implementation
- `review-phase` for lightweight review

---

## 5. Lightweight Plan → Implementation

Use when one lightweight plan is approved.

Required output from plan writer:

```yaml
artifact_type: LIGHTWEIGHT_PLAN
artifact_status: APPROVED | DRAFT | BLOCKED
decision: PROCEED_TO_IMPLEMENTATION | HOLD
objective: <one primary objective>
in_scope:
  - <allowed work>
out_of_scope:
  - <excluded work>
affected_files_or_components:
  - <known targets, if known>
existing_behavior: <summary>
target_behavior: <summary>
implementation_approach: <small local approach>
validation_checklist:
  - <validation step>
risk_check:
  product_risk: none | low | blocked
  architecture_risk: none | low | blocked
  adr_risk: none | low | blocked
  roadmap_risk: none | low | blocked
escalation_trigger: <when implementation must stop>
```

Consumed by implement-task:

- objective
- scope boundary
- files/components
- implementation approach
- validation checklist
- escalation trigger

Not required:

- full PRD summary
- full architecture prose
- roadmap phases
- broad alternatives

---

## 6. Lightweight Implementation → Review

Required output from implement-task:

```yaml
artifact_type: LIGHTWEIGHT_IMPLEMENTATION_SUMMARY
artifact_status: COMPLETED | BLOCKED | DEVIATED
decision: PROCEED_TO_REVIEW | ESCALATE_TO_PLAN_UPDATE | ESCALATE_TO_FULL_WORKFLOW
plan_path: <path>
changes_made:
  - <compact change summary>
files_changed:
  - <file path>
validation_performed:
  - <command/check/manual validation>
lightweight_assumptions_preserved:
  product_behavior_unchanged_or_clear: true | false
  architecture_unchanged: true | false
  no_adr_decision_introduced: true | false
  no_roadmap_need_introduced: true | false
deviations:
  - <none or deviation>
escalation_trigger_hit: true | false
```

Consumed by review-phase:

- plan path
- changes made
- validation evidence
- whether lightweight assumptions were preserved
- deviations/escalation triggers

---

## 7. Lightweight Review Output

Required output from review-phase:

```yaml
artifact_type: LIGHTWEIGHT_TASK_REVIEW_REPORT
artifact_status: APPROVED | APPROVED_WITH_MINOR_IMPROVEMENTS | NEEDS_REVISION | BLOCKED
decision: ACCEPT | RETURN_TO_IMPLEMENTATION | UPDATE_PLAN | ESCALATE_TO_FULL_WORKFLOW
reviewed_plan: <path>
reviewed_implementation_summary: <path or summary>
lightweight_eligibility_confirmed: true | false
findings:
  - severity: BLOCKER | MAJOR | MINOR | NOTE
    type: SCOPE | VALIDATION | ARCHITECTURE_ESCALATION | PRODUCT_ESCALATION | ADR_ESCALATION | ROADMAP_ESCALATION | TECHNICAL_QUALITY
    description: <finding>
required_action: <concrete action>
```

If lightweight eligibility is false, review must route to the appropriate full artifact instead of approving.

---

## 8. Full Workflow Handoff Rule

When a task is not lightweight, use the standard full workflow handoffs:

- Brainstorm → PRD / Architecture / ADR / Roadmap
- PRD → Architecture / Roadmap / Plan
- Architecture → ADR / Roadmap / Plan
- ADR → Architecture / Roadmap / Plan
- Roadmap → Plan
- Plan → Implementation
- Implementation → Review
- Review → next correction or approval action

Lightweight mode must not be used as a shortcut around unresolved upstream truth.
