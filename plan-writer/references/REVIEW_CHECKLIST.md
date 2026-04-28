# Review Checklist Guide

A plan's review checklist should let `review-phase` evaluate the implementation without guessing.

## Include checks for

- objective completion
- product behavior alignment
- architecture boundary compliance
- data ownership/source-of-truth compliance
- ADR compliance
- roadmap phase/scope compliance
- validation/test adequacy
- out-of-scope protection
- error handling and edge cases
- observability/audit requirements when relevant

## Architecture checks examples

- Implementation does not use read models as authorization source of truth.
- Domain service does not call infrastructure concerns directly if architecture forbids it.
- Event publishing follows the approved outbox/eventing rule.
- Transaction boundaries match the architecture.
- New API fields do not bypass the approved contract boundary.

## Bad checks

Avoid:

- “Code is good.”
- “Tests pass.”
- “No bugs.”
- “Implementation is clean.”

These are too vague to enforce.
