# Architecture Review Checklist

Use this before finalizing an architecture document.

## Artifact Routing

- [ ] Is architecture the correct artifact?
- [ ] If product behavior is unclear, did the result route to PRD?
- [ ] If only one decision is unresolved, did the result route to ADR?
- [ ] If only sequencing is needed, did the result route to roadmap?
- [ ] If only one executable task is needed, did the result route to PLAN?

## Scope

- [ ] Is the document root-level or initiative-level?
- [ ] Is the selected path correct?
- [ ] Does the document avoid unrelated concerns?
- [ ] Are non-goals explicit?

## System Shape

- [ ] Are major components/modules/services identified?
- [ ] Are responsibilities clear?
- [ ] Are "owns" and "does not own" boundaries clear?
- [ ] Are communication paths clear?

## Data Ownership

- [ ] Are source-of-truth models/tables/services identified?
- [ ] Are read models separated from authority models?
- [ ] Are lifecycle rules clear?
- [ ] Are audit or retention concerns addressed if relevant?

## Runtime Flows

- [ ] Do key flows include trigger, validation, transaction, side effects, result, and failure behavior?
- [ ] Are sync vs async boundaries clear?
- [ ] Are retries, idempotency, and failure modes covered when relevant?

## Cross-Cutting Rules

- [ ] Are transaction and consistency rules explicit?
- [ ] Are security and authorization rules explicit?
- [ ] Are observability expectations explicit?
- [ ] Are deployment/runtime assumptions explicit?
- [ ] Are performance/scalability constraints explicit when relevant?

## ADR Discipline

- [ ] Are settled ADRs linked?
- [ ] Are ADR candidates identified?
- [ ] Is ADR content summarized rather than duplicated?

## AI-Agent Usefulness

- [ ] Are implementation rules concrete?
- [ ] Could a coding agent know where to place code?
- [ ] Could a coding agent avoid wrong source-of-truth usage?
- [ ] Could a reviewer identify architecture violations?

## Handoff

- [ ] Does the output end with the mandatory closing format?
- [ ] Is the immediate next step explicit?
- [ ] Is the continuation prompt copy-paste usable?
