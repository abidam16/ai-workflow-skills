# LIGHTWEIGHT_TASK_MODE.md

Use this local reference only when `docs/workflow/LIGHTWEIGHT_TASK_MODE.md` is not available.

Choose lightweight mode only for small, local, low-risk work with one objective, clear product behavior, no architecture impact, no ADR-worthy decision, no roadmap need, and a small validation path.

Required section:

```md
## Lightweight Classification

- `mode`: LIGHTWEIGHT_TASK
- `reason`:
- `scope`:
- `why_prd_not_needed`:
- `why_architecture_not_needed`:
- `why_adr_not_needed`:
- `why_roadmap_not_needed`:
- `validation_path`:
- `escalation_trigger`:
```

Escalate to the full workflow when product behavior, architecture boundaries, source-of-truth, integration, async, transaction, authorization, security, deployment, performance, or durable decision-making becomes relevant.
