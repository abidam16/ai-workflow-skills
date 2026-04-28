# Create vs Update

## Create a new plan

Create a new plan when:

- no plan exists for this task
- task identity is new
- implementation can be reviewed independently
- upstream roadmap/architecture/ADR creates a new work item
- review finding requires a distinct corrective task
- previous plan should remain historical

## Update an existing plan

Update an existing plan when:

- task identity remains the same
- objective remains the same
- upstream source artifact changed only to clarify constraints
- architecture constraints must be added to an otherwise valid plan
- review feedback only tightens scope/validation

## Do not update

Do not update when:

- the plan would become multi-task
- the objective changed materially
- the existing plan was already implemented/reviewed and should remain historical
- a new ADR superseded the basis of the old plan
- roadmap sequencing changed enough that the task identity changed
