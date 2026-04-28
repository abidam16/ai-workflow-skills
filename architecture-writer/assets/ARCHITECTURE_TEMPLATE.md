# ARCHITECTURE.md

## 1. Document Status

- Status: Draft
- Last updated: YYYY-MM-DD
- Owner:
- Related PRD:
- Related roadmap:
- Related ADRs:

## 2. Purpose

This document defines the canonical architecture for this repo/product. It describes system shape, component boundaries, data ownership, runtime flows, integration boundaries, and cross-cutting implementation rules.

## 3. Current Architecture Summary

- 
- 
- 

## 4. Scope and Non-Goals

### In Scope

- 

### Out of Scope

- 

## 5. Source Artifacts

| Artifact | Path | Role |
|---|---|---|
| PRD |  | Product intent |
| Roadmap |  | Delivery sequencing |
| ADR |  | Technical decision record |

## 6. System Context

### Users / Actors

- 

### Internal Systems

- 

### External Systems

- 

### Upstream Dependencies

- 

### Downstream Dependencies

- 

## 7. Component / Module / Service Boundaries

| Component | Responsibility | Owns | Does Not Own | Communicates With |
|---|---|---|---|---|
|  |  |  |  |  |

## 8. Data Architecture and Ownership

| Concept / Entity | Source of Truth | Read Model / Derived Data | Ownership Rule |
|---|---|---|---|
|  |  |  |  |

### Lifecycle Rules

- 

### Audit / Retention Rules

- 

## 9. Runtime Flows

### Flow: <Name>

1. Trigger:
2. Validation:
3. Transactional changes:
4. Events / async side effects:
5. Result visible to user/system:
6. Failure behavior:

## 10. Integration and API Boundaries

### Internal APIs

- 

### External APIs

- 

### Events / Messaging

- 

### Sync vs Async Rules

- 

### Contract Ownership

- 

## 11. Consistency, Transaction, and Concurrency Rules

- 

## 12. Security and Authorization

- Authentication:
- Authorization source of truth:
- Role / permission checks:
- Sensitive data handling:
- Audit requirements:

## 13. Error Handling and Reliability

- Retryable failures:
- Non-retryable failures:
- Fallback behavior:
- Recovery / dead-letter handling:
- User-visible error behavior:

## 14. Observability and Operations

- Logs:
- Metrics:
- Tracing:
- Audit events:
- Dashboards / alerts:
- Debugging expectations:

## 15. Deployment and Runtime Assumptions

- Deployment unit:
- Environment assumptions:
- Configuration:
- Infrastructure dependencies:
- Scheduler / worker assumptions:

## 16. Performance and Scalability

- Expected load:
- Known bottlenecks:
- Pagination rules:
- Indexing assumptions:
- Async processing needs:
- Known limits:

## 17. Active Initiative Architectures

| Initiative | Document | Status | Notes |
|---|---|---|---|
|  |  |  |  |

## 18. Architectural Decisions

| Topic | Decision | ADR | Status |
|---|---|---|---|
|  |  |  |  |

## 19. Implementation Rules for AI Agents

- 
- 
- 

## 20. Review Checklist

- [ ] Implementation preserves component boundaries.
- [ ] Implementation uses the correct source of truth.
- [ ] Implementation follows transaction and consistency rules.
- [ ] Implementation respects sync/async boundaries.
- [ ] Implementation follows security and authorization rules.
- [ ] Implementation has required observability.
- [ ] Implementation does not require a missing ADR.
- [ ] Implementation does not require an architecture update.

## 21. Open Architecture Questions

| Question | Why It Matters | Current Assumption | Expected Next Artifact |
|---|---|---|---|
|  |  |  |  |
