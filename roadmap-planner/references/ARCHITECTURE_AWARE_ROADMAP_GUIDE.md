# Architecture-Aware Roadmap Guide

Architecture shapes delivery sequence. It does not become the roadmap.

## Use Architecture To Determine

- which foundation must be built first
- which modules or services are affected
- which data ownership changes must precede features
- which migrations or compatibility steps are needed
- which event or integration flows must exist before dependent behavior
- which transaction/consistency rules constrain implementation order
- which security or authorization rules block unsafe sequencing
- which observability or operational needs must be included before scale

## Do Not Put In Roadmap

- detailed component design
- full runtime flow descriptions
- class/package structure
- migration SQL
- event payload schema details
- endpoint-by-endpoint API detail
- ADR rationale

Reference or summarize only the constraints that affect phase order.

## Architecture Readiness Signals

Architecture is ready enough when:

- source-of-truth ownership is clear
- major components and boundaries are defined
- sync/async and integration boundaries are clear
- transaction/consistency expectations are known
- unresolved decisions are either non-blocking or routed to ADR

Architecture is not ready when:

- roadmap would need to invent component boundaries
- roadmap would need to decide source-of-truth ownership
- roadmap would need to decide sync vs async communication
- roadmap would need to choose infrastructure or architecture pattern
- multiple credible technical options still exist and affect sequencing
