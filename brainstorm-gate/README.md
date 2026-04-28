# brainstorm-gate — Concrete Next Step normalization patch

This patch normalizes `brainstorm-gate` so every chat-only or durable brainstorm output ends with the shared `## Concrete Next Step` block.

## Updated files

```text
brainstorm-gate/
├── SKILL.md
├── assets/
│   ├── BRAINSTORM_OUTPUT_TEMPLATE.md
│   ├── BRAINSTORM_RESPONSE_TEMPLATE.md
│   └── NEXT_STEP_BLOCK_TEMPLATE.md
├── references/
│   ├── DECISION_RULES.md
│   ├── DURABLE_ARTIFACT_RULES.md
│   ├── HANDOFF_PAYLOADS.md
│   └── MODES.md
└── scripts/
    └── check_brainstorm_output.py
```

## Canonical final block

```md
## Concrete Next Step

- `next_step_type`:
- `target`:
- `action`:
- `why_this_is_next`:
- `blocking_condition`:
- `suggested_prompt`:
```

## Main behavioral change

The old final fields are no longer the terminal output contract:

- `Immediate next step`
- `Continuation prompt`

Their meaning is preserved inside the normalized `Concrete Next Step` block.
