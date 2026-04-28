# roadmap-planner

Architecture-aware roadmap planning skill for Codex.

Use this skill to create or update product and initiative roadmaps after product intent, architecture constraints, and relevant ADR decisions are clear enough to sequence delivery.

## Install

Copy this folder to one of these locations:

```text
<repo>/.agents/skills/roadmap-planner
$HOME/.agents/skills/roadmap-planner
```

## Main behavior

The skill creates or updates:

- product roadmaps
- initiative roadmaps
- roadmap deltas
- plan handoff candidates

It refuses to produce roadmap phases when product intent, architecture, or ADR decisions are still unresolved.

## Key change in this refactor

`ARCHITECTURE.md` and initiative architecture documents are now first-class roadmap inputs. Roadmap sequencing must respect architecture constraints instead of inventing system design inside the roadmap.

## Validation helper

Run:

```bash
python scripts/check_roadmap_doc.py path/to/ROADMAP.md
```

The script checks for core roadmap sections and the mandatory `Concrete Next Step` block.
