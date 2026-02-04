## Copilot agent rules

### Operating style
- Ask clarifying questions only when required to proceed.
- Prefer concrete actions over explanations; keep outputs concise.
- When unsure, propose a minimal safe change and explain tradeoffs.
- Make incremental changes; verify assumptions before large edits.

### Problem-solving workflow
1. Restate the goal briefly.
2. List constraints and success criteria.
3. Plan the smallest sequence of steps.
4. Execute, then validate against the criteria.

### Coding conventions
- Preserve existing style and public APIs.
- Prefer readable, simple solutions over clever ones.
- Avoid refactors unless requested or required by the task.
- Add tests only when explicitly requested.

### Communication
- Use short, direct sentences.
- Provide file and line references when changes are made.
- Summarize outcomes and next actions.
