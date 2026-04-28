# BRAINSTORM OUTPUT

## 1. Artifact Metadata

- `artifact_type`: BRAINSTORM_OUTPUT
- `artifact_status`:
- `artifact_path`:
- `created_or_updated_at`:
- `source_request`:

## 2. Request Classification

- `mode`:
- `trigger`:
- `primary_problem_or_opportunity`:
- `affected_users_actors_systems_or_stakeholders`:

## 3. Problem and Value Assessment

- `problem_statement`:
- `who_is_affected`:
- `why_it_matters`:
- `current_workaround_or_alternative`:
- `expected_value_if_solved`:
- `evidence_strength`:

## 4. Options and Trade-offs

- `option_a`:
- `option_b`:
- `option_c_if_relevant`:
- `recommended_direction`:
- `main_trade_offs`:

## 5. Key Constraints, Risks, and Open Questions

- `constraints`:
- `risks`:
- `open_questions_that_matter_now`:

## 6. Decision

- `final_decision`: `CHOOSE EXACTLY ONE`
- `artifact_action`: `CREATE_DURABLE_BRAINSTORM_ARTIFACT` / `UPDATE_EXISTING_BRAINSTORM_ARTIFACT` / `CHAT_ONLY_NO_ARTIFACT`
- `durable_artifact_path`:

## 7. Why This Decision

- `reason_1`:
- `reason_2`:
- `reason_3`:

## 8. What Will Be Carried Forward

- `business_or_technical_intent`:
- `scope_boundary`:
- `important_constraints`:
- `risks_or_open_questions_for_next_phase`:

## 9. What Is Explicitly Not Needed Next

- `not_next_artifact`:
- `reason_not_next`:

## 10. Next Artifact Handoff Payload

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status:
decision:
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

Replace the generic payload above with the specific payload shape from `references/HANDOFF_PAYLOADS.md`.

Do not write downstream artifact sections here.

## 11. Stop Condition

If the final decision is `REJECT_OR_DEFER`, say exactly what is missing and state what would reopen the idea.

## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
