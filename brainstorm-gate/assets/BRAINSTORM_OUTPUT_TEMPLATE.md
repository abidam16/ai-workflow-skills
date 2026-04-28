# BRAINSTORM-XXX: <short-title>

```yaml
artifact_id: BRAINSTORM-XXX
artifact_type: BRAINSTORM_OUTPUT
artifact_status: DRAFT
source_skill: brainstorm-gate
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
decision: <NEW_PRD | PRD_UPDATE | NEW_PRODUCT_ROADMAP | PRODUCT_ROADMAP_UPDATE | NEW_INITIATIVE_ROADMAP | INITIATIVE_ROADMAP_UPDATE | NEW_ADR | ADR_UPDATE | REJECT_OR_DEFER>
output_mode: DURABLE_BRAINSTORM_OUTPUT
durable_artifact_path: docs/brainstorm/BRAINSTORM-XXX-<short-slug>.md
source_artifacts:
  - <path-or-none>
next_step: <exact next step>
```

## 1. Request Classification

- Mode:
- Trigger:
- Primary problem/opportunity:
- Existing product/artifact context:
- Source artifacts used:

## 2. Problem / Opportunity

- Problem statement:
- Who is affected:
- Why it matters:
- Current workaround or alternative:
- Evidence strength:

## 3. Value Assessment

- Expected value if solved:
- Cost of doing nothing:
- Urgency:
- Confidence level:
- Why this is worth or not worth pursuing now:

## 4. Options Considered

### Option A: <name>

- Summary:
- Benefits:
- Costs / risks:
- When this option makes sense:

### Option B: <name>

- Summary:
- Benefits:
- Costs / risks:
- When this option makes sense:

### Recommended Direction

- Recommended option:
- Reason:
- Main trade-offs accepted:

## 5. Constraints, Risks, and Open Questions

### Constraints

- <constraint>

### Risks

- <risk>

### Open Questions That Matter Now

- <question>

## 6. Final Decision

Decision: `<choose exactly one>`

## 7. Why This Decision

- Reason 1:
- Reason 2:
- Reason 3:

## 8. What Will Be Carried Forward

- Business/product/technical intent:
- Scope boundary:
- Important constraints:
- Important risks:
- Open questions for the next phase:

## 9. What Is Explicitly Not Needed Next

- Not `<artifact>` because:
- Not `<artifact>` because:

## 10. Next Artifact Handoff Payload

Use the payload shape from `references/HANDOFF_PAYLOADS.md` that matches the final decision.

Do not include a full PRD, ADR, roadmap, or plan here.

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: DRAFT
decision: <same as final decision>
why: <compact rationale>
source_artifacts:
  - <this brainstorm artifact path>
next_step: <exact next step>
```

## 11. Immediate Next Step

`Proceed to ...`

## 12. Continuation Prompt

`Proceed to ... based on docs/brainstorm/BRAINSTORM-XXX-<short-slug>.md.`

## 13. Stop Condition

If the final decision is `REJECT_OR_DEFER`, state:

```text
Stop here and revisit after stronger evidence or clearer constraints exist.
```

Also state:

- why forward progress should stop
- what is missing or conflicting
- what would reopen the idea
