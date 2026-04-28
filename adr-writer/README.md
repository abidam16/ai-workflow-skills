# adr-writer skill

Architecture-aware ADR writer for Codex.

Use this skill to create, supersede, or update one Architecture Decision Record when a technical or architectural choice has lasting impact, credible alternatives, and meaningful trade-offs.

## What this refactor adds

- Treats `ARCHITECTURE.md` as a first-class source artifact.
- Preserves the rule that one ADR records one decision only.
- Adds mandatory `Architecture Linkage` and `Architecture Follow-up` sections.
- Adds explicit ADR-worthiness and architecture-readiness gates.
- Adds mandatory `Concrete Next Step` output.
- Prevents ADRs from becoming broad architecture documents.

## Install

Copy this folder to either:

```text
<repo>/.agents/skills/adr-writer
```

or:

```text
$HOME/.agents/skills/adr-writer
```

## Validate an ADR

```bash
python scripts/check_adr_doc.py docs/adr/0001-example.md
```
