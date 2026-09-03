from agentguard.guard import AgentGuard
from agentguard.exceptions import ToolBlockedError
from agent import DemoAgent


print("🛡️ Welcome to Amygoe-AgentGuard!")
print("Sprint 1 - Day 12")
print("🤖 AI Agent Security Demo\n")


# ------------------------------------
# Create AgentGuard
# ------------------------------------

guard = AgentGuard()

guard.start()


# ------------------------------------
# Create AI Agent
# ------------------------------------

agent = DemoAgent(guard)


# ------------------------------------
# Agent Task 1
# ------------------------------------

try:

    agent.run(
        "Search for information about AI security"
    )

except ToolBlockedError as error:

    print(
        f"\n🛡️ Security Event: {error}"
    )


# ------------------------------------
# Agent Task 2
# ------------------------------------

try:

    agent.run(
        "Send an email containing the results"
    )

except ToolBlockedError as error:

    print(
        f"\n🛡️ Security Event: {error}"
    )


# ------------------------------------
# Agent Task 3
# ------------------------------------

try:

    agent.run(
        "Access the customer database"
    )

except ToolBlockedError as error:

    print(
        f"\n🛡️ Security Event: {error}"
    )