# Quality Bar

A PRD is good enough when it is useful as product truth for architecture, ADRs, roadmap, plan, implementation, and review.

## Required qualities

- Product-level, not implementation-level
- Concrete enough to test and review
- Concise enough to reload often
- Explicit goals and non-goals
- Clear users, actors, and role semantics
- Current and target behavior separated
- Business/product rules are testable
- Architecture impact is classified
- ADR impact is classified
- Roadmap impact is classified
- Plan readiness is classified
- Open questions are explicit and routed
- Concrete next step is mandatory

## Red flags

- PRD contains class names, table schemas, implementation steps, package paths, or migration details without product necessity
- PRD chooses a technical option that belongs in ADR
- PRD designs component boundaries that belong in architecture
- PRD sequences delivery phases that belong in roadmap
- PRD creates task instructions that belong in PLAN.md
- PRD leaves “next step” vague
- PRD says “TBD” without explaining what it blocks
- PRD repeats brainstorm uncertainty after decisions are settled

## Token efficiency

Use dense, navigable sections. Avoid generic textbook explanation.

Prefer:

```text
Rule: A pending invitation expires after its configured expiry time and can no longer be accepted.
```

Avoid:

```text
Invitations are a common product mechanism used in many collaborative applications...
```
