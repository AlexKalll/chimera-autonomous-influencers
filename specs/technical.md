# Technical Specification

## Agent Task Schema (JSON)
Tasks passed between Planner and Worker must follow this structure:
- `task_id`: uuid-v4
- `task_type`: `generate_content` | `execute_transaction`
- `context`: `{ goal_description, persona_constraints, required_resources }`

## Data Model (initial)
### Video Metadata
- `id`
- `agent_id`
- `platform`
- `media_url`
- `timestamp`
- `engagement_metrics`

### Wallet Ledger
- On-chain storage for immutable financial records.
