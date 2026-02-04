As a **Forward Deployed Engineer (FDE) Trainee**, your goal is to architect the "Factory" for autonomous influencers using **Spec-Driven Development (SDD)**. Since you prefer using **pip**, we will set up a professional environment that mirrors the "Golden Environment" requirements while using standard Python tooling.

Ensure your **Tenx MCP Sense** server is active in VS Code throughout this process; it acts as your "flight recorder" for assessment.

### **Phase 1: Research & Strategy (`research/`)**

#### **1. `research/summary.md`**
This document captures your high-level insights into the agentic ecosystem.
```markdown
# Project Chimera Research Summary

## OpenClaw Integration
Project Chimera functions as an infrastructure provider where agents publish their **Availability** and **Status** to the OpenClaw network. 

## Social Protocols
Agents will utilize **Agentic Commerce Protocols (ACP)** to communicate with other agents. This allows for autonomous negotiation, purchasing digital assets, and paying for computational resources without human intervention.
```

#### **2. `research/architecture_strategy.md`**
Based on the **FastRender Swarm** pattern.
```markdown
# Domain Architecture Strategy

## Agent Pattern: FastRender Swarm
We utilize a hierarchical swarm consisting of:
- **Planner:** Decomposes goals into a task DAG.
- **Worker:** Stateless agents executing atomic tasks via MCP tools.
- **Judge:** Quality gatekeeper using Optimistic Concurrency Control (OCC).

## Human-in-the-Loop (HITL)
Safety Layer: Content is routed to the Orchestrator Dashboard for human review based on confidence scores:
- < 0.70: Automatic Reject/Retry.
- 0.70 - 0.90: Async Approval required.
- > 0.90: Auto-Approve.

## Database Strategy
- **Transactional (PostgreSQL):** For user data and video metadata.
- **Semantic (Weaviate):** For long-term agent memory and RAG.
```

---

### **Phase 2: Master Specifications (`specs/`)**

#### **3. `specs/_meta.md`**
```markdown
# Project Meta Specification
**Vision:** A scalable fleet of 1,000+ autonomous influencers.
**Constraints:** 
- Decouple reasoning from APIs via **Model Context Protocol (MCP)**.
- Use **Coinbase AgentKit** for economic agency.
```

#### **4. `specs/technical.md`**
Define the "contracts" for your agents.
```markdown
# Technical Specification

## Agent Task Schema (JSON)
Tasks passed between Planner and Worker must follow this structure:
- `task_id`: uuid-v4
- `task_type`: generate_content | execute_transaction
- `context`: { goal_description, persona_constraints, required_resources }

## Database Schema
- **Video Metadata:** id, agent_id, platform, media_url, timestamp, engagement_metrics.
- **Wallet Ledger:** on-chain storage for immutable financial records.
```

---

### **Phase 3: Context Engineering & Environment**

#### **5. `CLAUDE.md`**
This file is the "Brain" for your VS Code AI agent.
```markdown
# Chimera Agent Rules

## Project Context
This is Project Chimera, an autonomous influencer system built on MCP and Swarm architecture.

## The Prime Directive
- NEVER generate code without checking `specs/` first.
- All external interactions MUST go through MCP Tools.

## Traceability
- Explain your plan before writing code.
- Ensure all content includes automated AI disclosure.
```

#### **6. `requirements.txt`**
Since you are using **pip**, create this file to manage your "Golden Environment".
```text
pydantic-ai
mcp
weaviate-client
redis
coinbase-agentkit
langchain
cdp-sdk
pytest
```

---

### **Phase 4: Governance & Skills (`skills/` & `tests/`)**

#### **7. `skills/README.md`**
Define your agent's capabilities.
```markdown
# Agent Skills Structure

## Skill A: skill_download_youtube
- **Input:** youtube_url (string)
- **Output:** local_file_path (string)

## Skill B: skill_trend_analyzer
- **Input:** news_resource (mcp_resource)
- **Output:** trend_cluster (json)
```

#### **8. `tests/test_trend_fetcher.py`**
Create **failing tests** to define the "Empty Slot" for the AI to fill.
```python
import pytest

def test_trend_data_schema():
    # This test asserts that trend data matches the API contract in technical.md
    # It will fail initially because the fetcher is not implemented.
    from src.perception import fetch_trends
    data = fetch_trends("mcp://news/trends")
    assert "trending_topics" in data
    assert isinstance(data["trending_topics"], list)
```

---

### **Phase 5: Automation (`Dockerfile` & `Makefile`)**

#### **9. `Makefile`**
Standardize your VS Code terminal commands.
```makefile
setup:
	pip install -r requirements.txt

test:
	pytest tests/

spec-check:
	# Script to verify code aligns with specs/ directory
	python scripts/verify_specs.py
```

#### **10. `Dockerfile`**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["make", "test"]
```

### **Next Steps**
1. **Initialize Git:** Run `git init` and link your origin.
2. **Setup Pip:** Run `make setup` in your VS Code terminal.
3. **Connect MCP:** Verify your **Tenx MCP Sense** connection logs.
4. **Task 1 Submission:** By the end of today (Feb 4th), submit your **Research & Architecture Report** (PDF) to the designated Google Drive.
