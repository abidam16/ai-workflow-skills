# Changelog

## 2026-04-28 — Durable Brainstorm Handoff Refactor

### Added

- Durable brainstorm artifact mode.
- Chat-only brainstorm mode.
- Default durable artifact path convention:
  - `docs/brainstorm/BRAINSTORM-<sequence>-<short-slug>.md`
- Generic `Next Artifact Handoff Payload` section.
- Handoff payload mapping for PRD, ADR, roadmap, and reject/defer.
- Explicit artifact actions:
  - `CREATE_DURABLE_BRAINSTORM_ARTIFACT`
  - `UPDATE_EXISTING_BRAINSTORM_ARTIFACT`
  - `CHAT_ONLY_NO_ARTIFACT`
- Dedicated durable artifact rules reference.
- Minimal durable artifact template.
- Example brainstorm artifact.

### Changed

- Reframed brainstorm output as a routing record and handoff packet, not a mini downstream document.
- Strengthened rule that brainstorm must end with exactly one decision.
- Strengthened anti-overlap rules with PRD/ADR/roadmap skills.
- Made output mode an explicit decision separate from artifact routing.

### Removed / Avoided

- No special PRD section inside brainstorm output.
- No full ADR or roadmap structure inside brainstorm output.
- No plan-level or implementation-level detail inside brainstorm output.
