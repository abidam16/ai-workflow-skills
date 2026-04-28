# LIGHTWEIGHT_IMPLEMENTATION_GUIDE.md

Lightweight implementation is allowed only against an approved lightweight plan.

## Allowed

- small local code edits
- small tests
- local documentation/config/copy cleanup
- behavior-preserving refactor

## Not Allowed

- changing product scope
- changing architecture boundaries
- changing data ownership/source-of-truth
- introducing new integration/async/transaction/security/deployment behavior
- making a durable technical decision without ADR
- expanding into multiple objectives

## Stop Conditions

Stop and route back when implementation reveals missing product truth, architecture constraints, ADR decision, roadmap need, plan ambiguity, or scope expansion.
