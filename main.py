from agentguard.guard import AgentGuard
from agentguard.tools import search, send_email, database

print("🛡️ Welcome to Amygoe-AgentGuard!")
print("Sprint 1 - Day 6\n")

# Create AgentGuard object
guard = AgentGuard()

# Start AgentGuard
guard.start()

# ------------------------------------
# Search Tool
# ------------------------------------
guard.execute(
    "search",
    search,
    "Python security"
)

print()

# ------------------------------------
# Email Tool
# ------------------------------------
guard.execute(
    "send_email",
    send_email
)

print()

# ------------------------------------
# Database Tool
# ------------------------------------
guard.execute(
    "database",
    database
)

print()

# ------------------------------------
# Unknown Tool
# ------------------------------------
guard.execute(
    "weather_api",
    lambda: print("🌦️ Weather API Executed")
)