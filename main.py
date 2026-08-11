from agentguard.guard import AgentGuard

from agentguard.tools import (
    search,
    send_email,
    database,
    broken_tool
)

from agentguard.exceptions import ToolBlockedError


print("🛡️ Welcome to Amygoe-AgentGuard!")
print("Sprint 1 - Day 8\n")


# Create AgentGuard object
guard = AgentGuard()


# Start AgentGuard
guard.start()


# ------------------------------------
# 1. Allowed Tool
# ------------------------------------

guard.execute(
    "search",
    search,
    "Python security"
)

print()


# ------------------------------------
# 2. Blocked Tool
# ------------------------------------

try:

    guard.execute(
        "send_email",
        send_email
    )

except ToolBlockedError as error:

    print(f"🛡️ Security Event: {error}")

print()


# ------------------------------------
# 3. Allowed Database Tool
# ------------------------------------

guard.execute(
    "database",
    database
)

print()


# ------------------------------------
# 4. Unknown Tool
# ------------------------------------

try:

    guard.execute(
        "weather_api",
        lambda: print("🌦️ Weather API Executed")
    )

except ToolBlockedError as error:

    print(f"🛡️ Security Event: {error}")

print()


# ------------------------------------
# 5. Broken Tool
# ------------------------------------

try:

    guard.execute(
        "broken_tool",
        broken_tool
    )

except ToolBlockedError as error:

    print(f"🛡️ Security Event: {error}")