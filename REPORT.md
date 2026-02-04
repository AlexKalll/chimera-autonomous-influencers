# TRP 1 - MCP Setup Challenge Report

Related: see `REPORT_CHIMERA.md` for the Agentic Infrastructure Challenge submission.

## What I did
- Created and populated [mcp.json](.vscode/mcp.json) with the Tenx MCP server configuration for Windows.
- Authored agent rules in [.github/copilot-instructions.md](.github/copilot-instructions.md).

## What worked
- The MCP configuration format with `servers` and `inputs` was accepted by VS Code.
- Clear, stepwise rules improved instruction-following and reduced back-and-forth.

## What didn't work
- Initial attempt to create files with `touch` failed on Windows PowerShell (command not available).

## Insights gained
- Small, explicit rules produce more predictable agent behavior.
- Keeping changes incremental makes it easier to validate outcomes.
