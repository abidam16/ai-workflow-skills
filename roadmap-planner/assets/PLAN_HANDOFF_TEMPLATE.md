# Plan Handoff Candidate

- `task_name`:
- `task_objective`:
- `why_it_is_one_task`:
- `source_roadmap`:
- `selected_phase_or_slice`:
- `scope_boundary`:
- `in_scope_for_this_task`:
- `out_of_scope_for_this_task`:
- `expected_components_or_layers`:
- `architecture_constraints_to_include`:
- `adr_constraints_to_include`:
- `dependencies`:
- `risks`:
- `validation_direction`:
- `review_focus`:

## Concrete Next Step

- `next_step_type`: CREATE_PLAN
- `target`: `<PLAN path or suggested task name>`
- `action`: Create one single-task implementation plan from this handoff candidate.
- `why_this_is_next`: This roadmap slice is sufficiently bounded and has clear architecture/ADR constraints.
- `blocking_condition`: Stop if the task cannot remain one coherent implementation plan.
- `suggested_prompt`: Use `plan-writer` to create a single-task PLAN.md for `<task_name>` using this roadmap handoff and relevant architecture/ADR constraints.
