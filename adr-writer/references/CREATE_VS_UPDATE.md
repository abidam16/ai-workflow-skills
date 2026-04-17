# Create vs Update ADR

## Default Rule

Default to **creating a new ADR** for a new decision.

## Create a New ADR When

Create a new ADR when:
- the team is making a new technical or architectural decision
- a previous ADR is being replaced by a new decision
- the new decision could stand on its own as a separate log entry
- the decision may later be superseded independently of other decisions

## Update an Existing ADR Only When

Only update an existing ADR for:
- typo or wording corrections
- adding missing references or metadata
- clarifying wording without changing the actual decision

## Supersession Rule

If the decision has changed materially:
- create a new ADR
- mark the previous ADR as `Superseded`
- reference the previous ADR in the new one

## Merge Rule

Do **not** merge unrelated decisions into one ADR.

Grouping is acceptable only when the items are inseparable parts of the same architectural choice. If the document starts reading like multiple debates, split it.

## Route Away from ADR When

Use another artifact instead if the issue is primarily:
- **PRD**: product behavior, scope, user-facing rules, business goals
- **ROADMAP**: phased delivery sequencing, milestones, prioritization
- **PLAN**: one bounded implementation task
