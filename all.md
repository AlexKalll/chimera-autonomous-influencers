# Project Chimera — Submission Index

This repo is organized for the **Agentic Infrastructure Challenge** (FDE Trainee). Specs are the source of truth; tests and automation form the safety net.

## Research & Strategy (Task 1)
- Research summary: `research/summary.md`
- Domain architecture strategy (with diagram): `research/architecture_strategy.md`
- Tooling strategy (Dev MCP vs Runtime Skills): `research/tooling_strategy.md`

## Master Specifications (Task 2)
- Meta / vision + constraints: `specs/_meta.md`
- Functional / user stories: `specs/functional.md`
- Technical / contracts & schemas: `specs/technical.md`
- OpenClaw integration plan: `specs/openclaw_integration.md`

## Context Engineering
- IDE agent rules: `CLAUDE.md`
- Cursor rules (challenge requirement): `.cursor/rules`

## Skills & Tests (Task 3)
- Skills contracts: `skills/README.md`
- Skills stubs: `skills/skill_download_youtube.py`, `skills/skill_transcribe_audio.py`, `skills/skill_trend_analyzer.py`
- Failing tests:
    - `tests/test_trend_fetcher.py`
    - `tests/test_skills_interface.py`

## Automation & Governance
- Makefile: `Makefile`
- Dockerfile: `Dockerfile`
- CI workflow: `.github/workflows/main.yml`
- AI review policy: `.coderabbit.yaml`

## Reports
- MCP Setup Challenge report: `REPORT.md`
- Chimera Challenge report: `REPORT_CHIMERA.md`

## Original NotebookLM dump
The raw paste you originally placed in this file is preserved in `notebooklm_dump.md`.