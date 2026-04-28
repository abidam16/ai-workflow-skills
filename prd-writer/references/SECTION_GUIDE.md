# Section Guide

## Product Summary

State the product/feature in one paragraph. Avoid implementation nouns unless product-facing.

## Problem Statement

Describe who has the problem, what the current pain is, and why it matters.

## Goals

Goals are desired product outcomes. They should be stable enough to guide architecture and roadmap.

## Non-Goals

Non-goals prevent scope creep. Include exclusions that downstream agents might otherwise implement.

## Users, Actors, and Roles

Define each actor and what they are allowed or expected to do. This is important for architecture and authorization planning.

## Current Behavior

Describe current behavior from the product/user perspective. Avoid code-level diagnosis unless needed to explain product behavior.

## Target Behavior

Describe the desired behavior. This should be concrete enough that a reviewer can identify product drift.

## Core User Flows

Use numbered steps. Keep flows product-level. Do not specify classes, tables, endpoints, or package names.

## Product Rules

Rules should be testable.

Good:

```text
A user can accept only invitations targeted to their account.
```

Bad:

```text
Call InvitationService.acceptInvitation() and update status = 2.
```

## Product Constraints

Include constraints that affect product behavior, compliance, operations, compatibility, or user experience.

## Success Criteria

Use observable outcomes. Include both functional and product-quality criteria when relevant.

## Architecture Impact

Classify impact and list architecture questions/constraints. Do not design architecture.

## ADR Impact

Identify candidate technical decisions only. Do not select the option.

## Roadmap Impact

Identify whether sequencing needs to change. Do not create phases.

## Implementation Plan Readiness

State the next planning layer that is ready or blocked.

## Open Product Questions

Questions must be actionable and routed.

Each question should include why it matters and which next artifact it blocks.
