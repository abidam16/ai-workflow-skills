# ADR Routing Rules

Choose ADR when the issue is primarily a **technical decision with lasting impact**.

Choose PRD instead when the main question is:
- what user or business behavior should exist
- what problem the product solves
- what scope is in or out

Choose ROADMAP instead when the main question is:
- how work should be sequenced or phased
- what milestones exist
- what should be delivered first or later

Choose PLAN instead when the main question is:
- how to execute one bounded task
- which files to change
- how to validate one implementation unit

Examples of good ADR candidates:
- adopt outbox pattern for reliable event publishing
- choose Kafka over RabbitMQ for cross-service event distribution
- choose optimistic locking for invitation updates
- choose push unread-count + pull detail strategy for notifications
