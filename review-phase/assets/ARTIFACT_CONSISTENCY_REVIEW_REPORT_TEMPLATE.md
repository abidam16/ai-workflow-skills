# Artifact Consistency Review Report

## 1. Review Metadata

- Review mode: `ARTIFACT_CONSISTENCY_REVIEW`
- Review target:
- Artifact chain reviewed:
- Reviewer:
- Date:

## 2. Source Artifacts Used

| Artifact | Path / Reference | Status | Used For |
|---|---|---|---|
| Workflow Docs | | | artifact authority, handoff contract, next-step rules |
| Brainstorm / Handoff | | | historical routing context only |
| PRD | | | product behavior, scope, business rules, success criteria |
| Architecture | | | system shape, boundaries, data ownership, runtime/integration constraints |
| ADRs | | | accepted technical decisions and consequences |
| Roadmap | | | delivery sequence, phase boundaries, dependencies |
| PLAN files / candidates | | | one-task execution contracts |
| Implementation summaries, if any | | | evidence of drift or downstream conflict |

## 3. Source Artifact Readiness

- Missing artifacts:
- Stale or weak artifacts:
- Conflicting artifacts:
- Review impact:

## 4. Executive Verdict

- Final status: `CONSISTENT | CONSISTENT_WITH_MINOR_GAPS | NEEDS_ARTIFACT_REVISION | BLOCKED`
- Summary:
- Blocking issue count:
- Non-blocking issue count:
- Main reason for status:

## 5. Authority Chain Check

| Authority Layer | Assessment | Evidence | Gaps |
|---|---|---|---|
| PRD as product truth | `PASS | PARTIAL | FAIL | NOT_APPLICABLE` | | |
| Architecture as system-shape truth | `PASS | PARTIAL | FAIL | NOT_APPLICABLE` | | |
| ADRs as decision truth | `PASS | PARTIAL | FAIL | NOT_APPLICABLE` | | |
| Roadmap as sequencing truth | `PASS | PARTIAL | FAIL | NOT_APPLICABLE` | | |
| PLAN as one-task execution truth | `PASS | PARTIAL | FAIL | NOT_APPLICABLE` | | |

## 6. PRD ↔ Architecture Consistency

- Assessment: `PASS | PARTIAL | FAIL | NOT_APPLICABLE`
- Product behaviors that require architecture support:
- Architecture constraints that support PRD behavior:
- Conflicts or missing architecture coverage:
- Recommended artifact owner for fix:

## 7. Architecture ↔ ADR Consistency

- Assessment: `PASS | PARTIAL | FAIL | NOT_APPLICABLE`
- ADRs reviewed:
- Architecture decisions reflected correctly:
- Missing ADRs:
- Conflicting or stale ADR references:
- Recommended artifact owner for fix:

## 8. Architecture / ADR ↔ Roadmap Consistency

- Assessment: `PASS | PARTIAL | FAIL | NOT_APPLICABLE`
- Architecture dependencies reflected in roadmap:
- ADR consequences reflected in sequencing:
- Unsafe or premature sequencing:
- Missing roadmap phases or exit criteria:
- Recommended artifact owner for fix:

## 9. Roadmap / Source Artifacts ↔ PLAN Consistency

- Assessment: `PASS | PARTIAL | FAIL | NOT_APPLICABLE`
- Plans reviewed:
- Plan scope matches roadmap slice:
- Plan preserves PRD behavior:
- Plan preserves architecture constraints:
- Plan preserves ADR decisions:
- Plan is small enough for one implementation task: `YES | NO | NOT_APPLICABLE`
- Recommended artifact owner for fix:

## 10. Handoff Contract Check

- Assessment: `PASS | PARTIAL | FAIL | NOT_APPLICABLE`
- Missing handoff fields:
- Ambiguous next step:
- Missing concrete target:
- Downstream risk:

## 11. Token Efficiency and Agent-Readiness Check

- Assessment: `PASS | PARTIAL | FAIL | NOT_APPLICABLE`
- Duplicated truth across artifacts:
- Overly long or noisy sections:
- Missing compact handoff summaries:
- Risk of agent confusion:

## 12. Findings

| Severity | Category | Title | Description | Why It Matters | Recommended Action |
|---|---|---|---|---|---|
| `HIGH_URGENCY | MEDIUM_URGENCY | LOW_URGENCY | FUTURE_IMPROVEMENT` | | | | | |

## 13. Risk Assessment

- Implementation-readiness risk:
- Architecture drift risk:
- Rework risk:
- Reviewability risk:
- Token/context risk:

## 14. Recommended Next Actions

List supporting actions here, ordered by importance. This section may contain multiple recommendations, but the final `Concrete Next Step` section must choose exactly one immediate action.

1.
2.
3.

## 15. Concrete Next Step

- `next_step_type`: `CREATE_PLAN | UPDATE_PLAN | CREATE_ARCHITECTURE | UPDATE_ARCHITECTURE | CREATE_ADR | UPDATE_ADR | UPDATE_ROADMAP | UPDATE_PRD | REQUEST_MISSING_SOURCE_ARTIFACT | IMPLEMENT_PLAN | RUN_ARTIFACT_CONSISTENCY_REVIEW | STOP_AND_ESCALATE`
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
