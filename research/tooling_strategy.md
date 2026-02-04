# Tooling Strategy (Dev MCP vs Runtime Skills)

## Developer Tooling (MCP)
Goal: accelerate development while preserving traceability.

- **Tenx MCP Sense (required):** flight recorder / telemetry for agent work in the IDE.
- Recommended additional dev MCP servers (optional, future):
  - **git-mcp:** structured git operations, safer automation.
  - **filesystem-mcp:** controlled file edits and search.
  - **postgres-mcp / redis-mcp:** integration testing against real services.

## Runtime Skills (Agent Capabilities)
Skills are reusable, testable Python modules the agent calls at runtime.

Initial skills (stubs defined in `skills/`):
- `skill_download_youtube`: fetch media to local storage.
- `skill_transcribe_audio`: produce transcript + timestamps.
- `skill_trend_analyzer`: cluster/score trends for planning.

## Separation Rules
- MCP servers = external bridges (network, DB, wallets).
- Skills = internal code (pure-ish functions) with explicit I/O contracts.
