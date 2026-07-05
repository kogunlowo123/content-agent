"""Content Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_content():
    """Test Generate marketing content for a specified format and topic."""
    tools = AgentTools()
    result = await tools.generate_content(topic="test", format="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_for_seo():
    """Test Optimize content for target keywords and search intent."""
    tools = AgentTools()
    result = await tools.optimize_for_seo(content="test", target_keywords="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_brand_voice():
    """Test Check content alignment with brand voice guidelines."""
    tools = AgentTools()
    result = await tools.check_brand_voice(content="test", brand_guidelines="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_schedule_publish():
    """Test Schedule content publication on content calendar."""
    tools = AgentTools()
    result = await tools.schedule_publish(content_id="test", publish_date="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.content_agent_agent import ContentAgentAgent
    agent = ContentAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
