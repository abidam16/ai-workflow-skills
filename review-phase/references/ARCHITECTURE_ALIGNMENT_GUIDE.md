# Architecture Alignment Guide

Review architecture alignment whenever the implementation touches system-shape concerns.

## Checkpoints

### Component and module boundaries

- Was new code placed in the right component/module/layer?
- Did the implementation bypass intended boundaries?
- Did it introduce coupling that architecture disallows?

### Data ownership and source of truth

- Is each business concept read from and written to the correct owner?
- Did the implementation use a read model as a write authority?
- Did it duplicate truth across tables/services without an accepted decision?

### Runtime flows and integration boundaries

- Does the implementation follow approved sync/async boundaries?
- Are events, queues, workers, or schedulers used according to architecture?
- Did the implementation add a new integration path without architecture approval?

### Transaction and consistency rules

- Are transaction boundaries preserved?
- Are consistency expectations honored?
- Are idempotency, retry, and failure behavior implemented where required?

### Security and authorization

- Is authorization based on the approved source of truth?
- Are sensitive fields protected according to architecture?
- Are audit/logging requirements preserved?

### Observability and operations

- Are logs, metrics, tracing, or audit events present where required?
- Is operational debugging possible for the implemented flow?
- Did the implementation create hidden runtime risk?

## Architecture finding categories

Use these categories when relevant:

- `ARCHITECTURE_VIOLATION`
- `SOURCE_OF_TRUTH_VIOLATION`
- `BOUNDARY_VIOLATION`
- `RUNTIME_FLOW_VIOLATION`
- `TRANSACTION_CONSISTENCY_GAP`
- `SECURITY_AUTHORIZATION_GAP`
- `MISSING_ARCHITECTURE_UPDATE`

## Review stance

Do not require architecture for tiny local changes that do not affect system shape. But when architecture exists and is relevant, treat it as binding.
