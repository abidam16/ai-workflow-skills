# PRD Review Checklist

Use this checklist before finalizing PRD output.

## Artifact fit

- Is PRD the correct artifact?
- Is the request actually architecture, ADR, roadmap, plan, implementation, or review?

## Product clarity

- Are goals and non-goals explicit?
- Are users/actors/roles defined?
- Are current and target behavior separated?
- Are product rules testable?
- Are success criteria observable?

## Architecture boundary

- Does the PRD classify architecture impact?
- Does it avoid designing component boundaries, schemas, runtime flows, or transaction rules?
- Does it route to architecture when product behavior requires system-shape decisions?

## ADR boundary

- Does the PRD identify candidate decisions without choosing technical options?
- Does it avoid replacing an ADR?

## Roadmap boundary

- Does the PRD identify sequencing impact without creating phases?
- Does it avoid replacing a roadmap?

## Plan boundary

- Does the PRD avoid implementation task lists?
- Does it classify plan readiness accurately?

## Handoff

- Is `PRD Handoff Summary` present?
- Is `Concrete Next Step` present?
- Is the next step specific, routed, and actionable?
