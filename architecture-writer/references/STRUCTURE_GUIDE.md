# Architecture Structure Guide

## Root `ARCHITECTURE.md` Structure

Use this for the canonical repo/product architecture.

```md
# ARCHITECTURE.md

## 1. Document Status

- Status:
- Last updated:
- Owner:
- Related PRD:
- Related roadmap:
- Related ADRs:

## 2. Purpose

## 3. Current Architecture Summary

## 4. Scope and Non-Goals

## 5. Source Artifacts

## 6. System Context

## 7. Component / Module / Service Boundaries

## 8. Data Architecture and Ownership

## 9. Runtime Flows

## 10. Integration and API Boundaries

## 11. Consistency, Transaction, and Concurrency Rules

## 12. Security and Authorization

## 13. Error Handling and Reliability

## 14. Observability and Operations

## 15. Deployment and Runtime Assumptions

## 16. Performance and Scalability

## 17. Active Initiative Architectures

## 18. Architectural Decisions

## 19. Implementation Rules for AI Agents

## 20. Review Checklist

## 21. Open Architecture Questions
```

## Minimum Viable Root Architecture

For small repos or early-stage products, use this shorter shape:

```md
# ARCHITECTURE.md

## 1. Purpose

## 2. Architecture Summary

## 3. Scope and Non-Goals

## 4. Component Boundaries

## 5. Data Ownership

## 6. Key Runtime Flows

## 7. Integration Boundaries

## 8. Transaction / Consistency Rules

## 9. Security / Authorization Rules

## 10. ADR Links

## 11. Implementation Rules for AI Agents

## 12. Open Questions
```

## Initiative Architecture Structure

Use this for substantial initiatives.

```md
# <Initiative Name> Architecture

## 1. Document Status

## 2. Related Artifacts

## 3. Problem Context

## 4. Target Architecture

## 5. Scope and Non-Goals

## 6. Component Boundaries

## 7. Data Ownership

## 8. Runtime Flows

## 9. Integration Boundaries

## 10. Transaction and Consistency Rules

## 11. Security and Authorization

## 12. Failure Handling and Reliability

## 13. Observability and Operations

## 14. Deployment and Runtime Assumptions

## 15. Performance and Scalability

## 16. Migration / Transition Model

## 17. ADRs Required or Linked

## 18. Roadmap Implications

## 19. Implementation Rules

## 20. Review Checklist

## 21. Open Questions
```

## Section Guidance

### Purpose

State what the architecture document defines and what decisions it guides.

Keep it short.

### Architecture Summary

Use 5-10 bullets.

Summarize the accepted system shape, not the product pitch.

### Scope and Non-Goals

Clarify the document boundary.

This prevents architecture docs from becoming PRDs, roadmaps, or plans.

### System Context

Mention users, internal systems, external systems, upstream dependencies, and downstream dependencies.

Do not over-describe product behavior.

### Component Boundaries

For each major component:

- responsibility
- owns
- does not own
- communicates with
- important constraints

### Data Architecture and Ownership

Define:

- main entities/models/tables
- source-of-truth ownership
- read models
- lifecycle rules
- audit/retention concerns when relevant

### Runtime Flows

Use flow format:

1. Trigger
2. Validation
3. Transactional changes
4. Events or async side effects
5. Result visible to user/system
6. Failure behavior

### Integration and API Boundaries

Define:

- internal APIs
- external APIs
- messaging/events
- sync vs async boundaries
- contract ownership

Do not include a full endpoint catalog unless the endpoints are architecture-critical.

### Consistency, Transaction, and Concurrency Rules

Define:

- transaction boundaries
- optimistic locking
- idempotency
- retries
- eventual consistency
- conflict handling

### Security and Authorization

Define:

- authentication assumptions
- authorization source of truth
- role/permission checks
- sensitive data handling
- audit requirements

### Error Handling and Reliability

Define:

- expected failure modes
- retryable vs non-retryable errors
- fallback behavior
- dead-letter/recovery strategy
- user-visible error behavior

### Observability and Operations

Define:

- logs
- metrics
- traces
- audit events
- dashboard/alert expectations
- operational debugging needs

### Deployment and Runtime Assumptions

Define:

- deployment unit
- environment assumptions
- configuration rules
- infrastructure dependencies
- scheduler/worker/runtime concerns

### Performance and Scalability

Define:

- expected load
- known bottlenecks
- pagination rules
- indexing assumptions
- async processing needs
- known limits

### Architectural Decisions

Link ADRs. Do not duplicate ADR content.

### Implementation Rules for AI Agents

Write concrete rules.

Good:

- Do not use `notification` as the source of truth for authorization.
- Do not create membership outside the invitation acceptance transaction.
- Do not publish integration events directly if the outbox rule applies.

Weak:

- Follow best practices.
- Keep the code clean.
- Make it scalable.

### Open Architecture Questions

Each open question should include:

- question
- why it matters
- current assumption
- expected next artifact: PRD / ADR / roadmap / PLAN
