# ADR-NNNN: <Decision Title>

## Status

Proposed / Accepted / Rejected / Superseded

## Date

YYYY-MM-DD

## Decision Owner

<owner or team>

## Source Artifacts

| Artifact | Path / Reference | Relevance |
|---|---|---|
| PRD | `PRD.md` | <product constraint or behavior driving this decision> |
| Architecture | `ARCHITECTURE.md` | <system-shape context> |
| Initiative Architecture | `docs/architecture/<initiative>-architecture.md` | <if relevant> |
| Roadmap | `ROADMAP.md` | <if relevant> |
| Plan / Review | `<path>` | <if decision was discovered downstream> |

## Decision Boundary

### Decides

- <what this ADR decides>

### Does Not Decide

- <related but excluded topics>

## Context / Problem

<Explain the technical or architectural problem that requires a decision.>

## Decision Drivers

- <driver 1: reliability, consistency, operability, delivery speed, cost, maintainability, etc.>
- <driver 2>
- <driver 3>

## Considered Options

| Option | Summary | Benefits | Costs / Risks | Fit |
|---|---|---|---|---|
| Option A | <summary> | <benefits> | <costs> | <fit> |
| Option B | <summary> | <benefits> | <costs> | <fit> |
| Option C | <summary> | <benefits> | <costs> | <fit> |

## Decision

Chosen option: **<Option>**

<Explain why this option best fits the decision drivers.>

## Consequences

### Positive

- <positive consequence>

### Negative / Trade-offs

- <negative consequence or accepted trade-off>

### Implementation Constraints

- <constraint future plans and implementations must obey>

### Operational / Runtime Implications

- <logging, monitoring, deployment, recovery, migration, or support implication>

## Architecture Linkage

- `architecture_linkage`: NONE / ARCHITECTURE_CONTEXT_ONLY / ADD_ADR_INDEX_ENTRY / UPDATE_ROOT_ARCHITECTURE / UPDATE_INITIATIVE_ARCHITECTURE / UPDATE_ROOT_AND_INITIATIVE_ARCHITECTURE / ARCHITECTURE_CONFLICT_FOUND / ARCHITECTURE_MISSING
- Affected architecture document(s): `<path>`
- Affected section(s): `<section names>`
- Required architecture update: <none / add ADR index entry / update constraints / update runtime flow / update component boundary / update data ownership / other>

## Downstream Impact

- PRD Impact: none / check assumptions / update PRD
- Architecture Impact: none / add ADR link / update architecture / resolve conflict
- Roadmap Impact: none / update sequencing / unblock roadmap
- Plan Impact: none / create plan / revise plan constraints
- Review Impact: none / add review criterion / revisit previous review

## Review Criteria

Future review should verify:

- <criterion 1>
- <criterion 2>
- <criterion 3>

## Related Artifacts

- PRD: `<path>`
- Architecture: `<path>`
- Related ADRs: `<paths>`
- Roadmap: `<path>`
- Plan(s): `<paths>`

## Supersession

- Supersedes: `<ADR path or none>`
- Superseded by: `<ADR path or none>`

## Open Questions

- <question, owner/status, expected next artifact>

## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
