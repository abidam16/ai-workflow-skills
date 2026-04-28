# Changelog

## 2026-04-28 — Architecture + ADR Artifact Routing Update

### Added

- `NEW_ARCHITECTURE` and `ARCHITECTURE_UPDATE` as first-class final decisions.
- `NEW_DOCUMENT_PLAN` and `DOCUMENT_PLAN_UPDATE` as first-class final decisions.
- Brainstorm → Architecture handoff payload.
- Brainstorm → Document Plan handoff payload.
- Architecture vs ADR boundary rules.
- Hard threshold for Architecture selection:
  - choose Architecture only when multiple future decisions or tasks need shared system-level context.
- Documentation / Artifact Planning brainstorm mode.
- Architecture example artifact.

### Changed

- Reframed the skill as a router across PRD, Architecture, ADR, roadmap, document plan, or reject/defer.
- Updated mandatory next-step and continuation-prompt wording for Architecture and Document Plan.
- Updated durable artifact rules to explicitly include Architecture and Document Plan.
- Updated handoff payload selection table to cover all supported final decisions.

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
- Strengthened anti-overlap rules with downstream writer skills.
- Made output mode an explicit decision separate from artifact routing.

### Removed / Avoided

- No special PRD section inside brainstorm output.
- No full Architecture, ADR, roadmap, or document plan structure inside brainstorm output.
- No plan-level or implementation-level detail inside brainstorm output.
