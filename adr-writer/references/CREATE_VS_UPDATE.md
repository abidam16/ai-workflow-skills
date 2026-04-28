# Create vs Update

## Create a new ADR when

- this is a new decision
- the decision has not been recorded before
- the decision supersedes an accepted ADR
- implementation or review exposed an unrecorded lasting technical choice
- architecture identifies a new ADR candidate

## Supersede an ADR when

- an accepted decision is replaced by a newer decision
- constraints changed enough that the old rationale is no longer valid
- production or implementation learning invalidates the old decision

Preferred approach:

1. Create a new ADR.
2. Mark the old ADR as superseded.
3. Link both ADRs.
4. Update architecture if the stable system constraint changed.

## Update an existing ADR when

- fixing typos or broken links
- adding missing related-artifact links
- changing status from Proposed to Accepted/Rejected if the decision itself did not change
- adding implementation outcome notes that do not alter the decision

## Do not rewrite accepted history

Do not silently edit an accepted ADR to make it look like the new decision was always true.

Historical decision records must remain auditable.
