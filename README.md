# Content Agent

[![CI](https://github.com/kogunlowo123/content-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/content-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Content creation agent that generates blog posts, whitepapers, social media posts, and marketing copy aligned with brand voice, SEO best practices, and content calendar schedules.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_content` | Generate marketing content for a specified format and topic |
| `optimize_for_seo` | Optimize content for target keywords and search intent |
| `check_brand_voice` | Check content alignment with brand voice guidelines |
| `schedule_publish` | Schedule content publication on content calendar |
| `repurpose_content` | Repurpose content into multiple formats |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/content/create` | Create or generate |
| `POST` | `/api/v1/content/analyze` | Analyze performance |
| `POST` | `/api/v1/content/optimize` | Optimize |
| `POST` | `/api/v1/content/schedule` | Schedule |
| `POST` | `/api/v1/content/report` | Generate report |

## Features

- Content
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
content-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── content_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
