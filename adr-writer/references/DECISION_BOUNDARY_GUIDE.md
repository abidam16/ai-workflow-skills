# Decision Boundary Guide

A good ADR boundary is narrow enough to decide and broad enough to matter.

## Boundary questions

Before writing an ADR, answer:

- What exact choice is being made?
- What alternatives are in scope?
- What is explicitly out of scope?
- Which source artifact created the need for this decision?
- Which architecture section is affected?
- Which future implementation tasks must obey this decision?

## Good boundaries

Good:

- "Use transactional outbox for reliable event publishing from the invitation service."
- "Use `user_product_membership` as the authorization source of truth for product access."
- "Use cursor-based pagination for notification inbox reads."

Bad:

- "Design the notification system."
- "Improve backend architecture."
- "Implement invitations."
- "Make the app scalable."

Bad boundaries should route to architecture, roadmap, or plan instead of ADR.

## Boundary format

Use:

```md
## Decision Boundary

### Decides

- ...

### Does Not Decide

- ...
```

## Red flags

Split or reroute if the ADR tries to decide:

- multiple unrelated patterns
- product scope and technical strategy together
- roadmap phase order
- detailed task implementation
- broad module/service design without prior architecture
