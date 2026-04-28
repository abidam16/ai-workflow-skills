# <Initiative Name> Architecture

## 1. Document Status

- Status: Proposed
- Last updated: YYYY-MM-DD
- Owner:
- Related PRD:
- Related root architecture: `ARCHITECTURE.md`
- Related roadmap:
- Related ADRs:

## 2. Related Artifacts

| Artifact | Path | Role |
|---|---|---|
| Brainstorm |  | Original routing/context |
| PRD |  | Product intent |
| Root architecture | `ARCHITECTURE.md` | Canonical system context |
| Roadmap |  | Delivery sequencing |
| ADR |  | Decision record |

## 3. Problem Context

Explain why this initiative needs architecture documentation.

## 4. Target Architecture

Summarize the intended target system shape.

- 
- 
- 

## 5. Scope and Non-Goals

### In Scope

- 

### Out of Scope

- 

## 6. Component Boundaries

| Component | Responsibility | Owns | Does Not Own | Communicates With |
|---|---|---|---|---|
|  |  |  |  |  |

## 7. Data Ownership

| Concept / Entity | Source of Truth | Read Model / Derived Data | Ownership Rule |
|---|---|---|---|
|  |  |  |  |

## 8. Runtime Flows

### Flow: <Name>

1. Trigger:
2. Validation:
3. Transactional changes:
4. Events / async side effects:
5. Result visible to user/system:
6. Failure behavior:

## 9. Integration Boundaries

### Internal Boundaries

- 

### External Boundaries

- 

### Events / Messaging

- 

### Contract Ownership

- 

## 10. Transaction and Consistency Rules

- 

## 11. Security and Authorization

- Authentication:
- Authorization source of truth:
- Role / permission checks:
- Sensitive data handling:
- Audit requirements:

## 12. Failure Handling and Reliability

- Retryable failures:
- Non-retryable failures:
- Fallback behavior:
- Recovery / dead-letter handling:
- User-visible error behavior:

## 13. Observability and Operations

- Logs:
- Metrics:
- Tracing:
- Audit events:
- Dashboards / alerts:
- Debugging expectations:

## 14. Deployment and Runtime Assumptions

- Deployment unit:
- Environment assumptions:
- Configuration:
- Infrastructure dependencies:
- Scheduler / worker assumptions:

## 15. Performance and Scalability

- Expected load:
- Known bottlenecks:
- Pagination rules:
- Indexing assumptions:
- Async processing needs:
- Known limits:

## 16. Migration / Transition Model

### Current State

- 

### Transitional State

- 

### Target State

- 

### Rollback / Recovery Considerations

- 

## 17. ADRs Required or Linked

| Topic | Decision Needed / Made | ADR | Status |
|---|---|---|---|
|  |  |  |  |

## 18. Roadmap Implications

- 

## 19. Implementation Rules

- 
- 
- 

## 20. Review Checklist

- [ ] Implementation preserves initiative boundaries.
- [ ] Implementation does not contradict root `ARCHITECTURE.md`.
- [ ] Implementation follows source-of-truth rules.
- [ ] Implementation follows transaction and consistency rules.
- [ ] Implementation follows integration boundaries.
- [ ] Implementation has required observability.
- [ ] Missing ADRs are created before implementation relies on the decision.

## 21. Open Questions

| Question | Why It Matters | Current Assumption | Expected Next Artifact |
|---|---|---|---|
|  |  |  |  |
