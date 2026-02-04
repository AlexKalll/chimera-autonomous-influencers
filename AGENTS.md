# AGENTS.md — Fleet-Wide Governance (BoardKit-style)

This file defines fleet-wide operating rules for Project Chimera agents.

## Prime Directives
- Specs are the source of truth: consult `specs/` before making changes.
- External side-effects must occur via MCP tools (no direct API calls in core logic).
- Maintain traceability: plans first, incremental diffs, and tests for new behavior.

## Safety & HITL
- Route content to HITL review when confidence is below threshold or when sensitive topics are detected.
- Sensitive domains requiring mandatory HITL: politics, legal claims, medical advice, financial advice.

## Transparency
- All published content must include AI disclosure mechanisms where supported by the platform.
- If asked directly whether the agent is AI, respond with clear, truthful disclosure.

## Economic Agency Controls
- Wallet operations require budget checks (daily limits) and allowlists where appropriate.
- Secrets must never be committed. Use environment variables and secret managers in deployment.

## Data & Privacy
- Enforce tenant isolation; never mix memories or credentials across agents/tenants.
- Avoid storing secrets or PII in semantic memory.
