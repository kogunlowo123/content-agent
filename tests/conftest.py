"""Test configuration for Content Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "content-agent", "category": "Marketing"}
