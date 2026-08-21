import pytest

from agentguard.guard import AgentGuard
from agentguard.exceptions import ToolBlockedError


def test_allowed_tool():

    guard = AgentGuard()

    result = guard.policy_engine.check("search")

    assert result.allowed is True


def test_blocked_tool():

    guard = AgentGuard()

    result = guard.policy_engine.check("send_email")

    assert result.allowed is False


def test_unknown_tool():

    guard = AgentGuard()

    result = guard.policy_engine.check("weather_api")

    assert result.allowed is False

    assert result.reason == "Unknown tool (Default Deny)"


def test_allowed_tool_executes():

    guard = AgentGuard()

    executed = []

    def fake_tool():
        executed.append(True)

    guard.execute(
        "search",
        fake_tool
    )

    assert executed == [True]


def test_blocked_tool_does_not_execute():

    guard = AgentGuard()

    executed = []

    def fake_tool():
        executed.append(True)

    with pytest.raises(ToolBlockedError):

        guard.execute(
            "send_email",
            fake_tool
        )

    assert executed == []


def test_broken_tool_does_not_crash_agentguard():

    guard = AgentGuard()

    def broken_tool():

        raise RuntimeError(
            "Database connection failed"
        )

    guard.execute(
        "broken_tool",
        broken_tool
    )