# BRAINSTORM-001: Notification Inbox

```yaml
artifact_id: BRAINSTORM-001
artifact_type: BRAINSTORM_OUTPUT
artifact_status: DRAFT
source_skill: brainstorm-gate
created_at: 2026-04-28
updated_at: 2026-04-28
decision: CREATE_PRD
output_mode: DURABLE_BRAINSTORM_OUTPUT
durable_artifact_path: docs/brainstorm/BRAINSTORM-001-notification-inbox.md
source_artifacts: []
```

## 1. Request Classification

- Mode: Feature Addition
- Trigger: Need to design notification/invitation behavior for users.
- Primary problem/opportunity: Users need a reliable way to see, understand, and act on product invitations and other system events.
- Existing product/artifact context: Product exists, but notification behavior is not yet durable as product truth.
- Source artifacts used: None.

## 2. Problem / Opportunity

- Problem statement: Users need a clear notification inbox that shows actionable invitations and relevant status changes without requiring heavy joins or ambiguous UI logic.
- Who is affected: Invited users, inviters, product administrators, and downstream services that need notification state.
- Why it matters: Without a durable notification model, invitation visibility, unread count, and action availability may become inconsistent.
- Current workaround or alternative: Query invitation records directly and infer display state at read time.
- Evidence strength: Medium; the need is structurally clear, but exact UX rules still need PRD-level definition.

## 3. Value Assessment

- Expected value if solved: Clear user-facing inbox behavior, better read/unread semantics, and reusable notification patterns for future event types.
- Cost of doing nothing: Increased coupling between invitation tables and UI rendering, inconsistent badge behavior, and harder future notification expansion.
- Urgency: Medium.
- Confidence level: Medium.
- Why this is worth pursuing now: The feature affects product behavior and needs a stable product-level source of truth before roadmap or implementation.

## 4. Options Considered

### Option A: Render directly from invitation tables

- Summary: Use `product_invitation` as the primary notification source.
- Benefits: Simpler initial implementation.
- Costs / risks: Tight coupling, harder support for future notification types, heavier reads, and weaker snapshot behavior.
- When this option makes sense: Only if invitation notification is the only foreseeable notification type.

### Option B: Separate notification feed with snapshot payload

- Summary: Store notification display records separately from invitation source records.
- Benefits: More flexible feed, easier unread/read logic, supports multiple notification types, and reduces UI dependency on domain joins.
- Costs / risks: Requires synchronization and lifecycle rules.
- When this option makes sense: When notification feed is intended to become a general product capability.

### Recommended Direction

- Recommended option: Option B.
- Reason: The concept affects product behavior and needs clear PRD-level rules before technical design and implementation.
- Main trade-offs accepted: More upfront design in exchange for cleaner future extensibility.

## 5. Constraints, Risks, and Open Questions

### Constraints

- Notification feed should not become a second source of truth for membership.
- Invitation acceptance/rejection should remain authoritative in the invitation or membership domain.
- UI should not need heavy joins to render normal feed items.

### Risks

- Snapshot payload may become stale if lifecycle rules are unclear.
- Read/unread semantics may be confused with actionable/non-actionable semantics.
- Updating versus appending notifications may affect audit expectations.

### Open Questions That Matter Now

- Should accepted/rejected invitations update the existing feed item or append a new status item?
- What exactly changes the unread badge count?
- Which notification types are in MVP?

## 6. Final Decision

Decision: `CREATE_PRD`

## 7. Why This Decision

- The main unresolved issue is product behavior, not implementation.
- Notification semantics affect users, flows, rules, and success criteria.
- A PRD is needed before ADR or roadmap can be reliable.

## 8. What Will Be Carried Forward

- Business/product/technical intent: Create a user-facing notification inbox that can support invitations and future event types.
- Scope boundary: Define product behavior and notification lifecycle, not implementation tables or Kafka design yet.
- Important constraints: Notification display must not become the authority for membership.
- Important risks: Confusing unread/actionable/status semantics.
- Open questions for the next phase: Lifecycle behavior, read/unread semantics, MVP notification types.

## 9. What Is Explicitly Not Needed Next

- Not ADR because the product behavior is not defined clearly enough yet.
- Not roadmap because delivery sequencing depends on the PRD.
- Not implementation plan because task boundaries are premature.

## 10. Next Artifact Handoff Payload

```yaml
artifact_type: BRAINSTORM_OUTPUT
artifact_status: DRAFT
decision: CREATE_PRD
problem_statement: Users need a clear notification inbox that shows actionable invitations and relevant status changes without ambiguous UI logic.
target_users_or_actors:
  - invited users
  - inviters
  - product administrators
business_need: Improve reliability and clarity of invitation and notification handling.
product_intent_summary: Define a notification inbox that separates display/feed behavior from authoritative domain records.
goals:
  - Define notification inbox behavior.
  - Define unread/read semantics.
  - Define actionable invitation behavior.
  - Define MVP notification types.
non_goals:
  - Do not define Kafka/outbox implementation yet.
  - Do not define database schema yet.
  - Do not define frontend component structure yet.
key_flows_or_domains:
  - invitation received
  - invitation accepted
  - invitation rejected
  - notification read/unread
  - notification feed rendering
known_constraints:
  - Membership authority must remain outside the notification feed.
  - Feed rendering should not require heavy domain joins for normal display.
reason_prd_is_needed: Product behavior, user-facing rules, and lifecycle semantics must be established before ADR, roadmap, or implementation.
source_artifacts:
  - docs/brainstorm/BRAINSTORM-001-notification-inbox.md
concrete_next_step:
  next_step_type: CREATE_PRD
  target: PRD.md
  action: Create the initial notification inbox PRD from this brainstorm handoff.
  why_this_is_next: Product behavior, user-facing rules, and lifecycle semantics must be established before architecture, ADR, roadmap, or implementation.
  blocking_condition: Stop if notification lifecycle, unread semantics, or MVP notification types cannot be resolved enough for PRD drafting.
  suggested_prompt: Use `prd-writer` to create `PRD.md` for the notification inbox from `docs/brainstorm/BRAINSTORM-001-notification-inbox.md`.
```

## 11. Stop Condition

Not applicable. The idea should proceed to PRD.

## Concrete Next Step

- `next_step_type`: CREATE_PRD
- `target`: `PRD.md`
- `action`: Create the initial notification inbox PRD from this brainstorm handoff.
- `why_this_is_next`: Product behavior, user-facing rules, and lifecycle semantics must be established before architecture, ADR, roadmap, or implementation.
- `blocking_condition`: Stop if notification lifecycle, unread semantics, or MVP notification types cannot be resolved enough for PRD drafting.
- `suggested_prompt`: Use `prd-writer` to create `PRD.md` for the notification inbox from `docs/brainstorm/BRAINSTORM-001-notification-inbox.md`.
