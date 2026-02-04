# Functional Specification

## User Stories (Agent-centric)

### Trend Perception
- As an Agent, I need to fetch platform/news trends so I can decide what content to create.
- As a Planner, I need trend outputs in a consistent JSON schema so I can enqueue tasks deterministically.

### Content Generation
- As a Worker, I need to generate a post (caption + asset pointers) that respects persona constraints.
- As a Judge, I need to verify content against safety and brand rules before publishing.

### Engagement & Operations
- As an Agent, I need to read and respond to engagement events (comments/DMs) according to policy.
- As a Governor, I need an audit trail of actions and spend to enforce budget limits.

## Acceptance Criteria (MVP)
- Trend fetch returns a JSON object with `trending_topics` as a list.
- Each trending topic contains a stable identifier and a short summary.
- Unsafe content is routed to Human-in-the-Loop (HITL) review.
