from agentguard.guard import AgentGuard
from agentguard.tools import search, send_email, database

print("🛡️ Welcome to Amygoe-AgentGuard!")
print("Sprint 1 - Day 4\n")

# Create AgentGuard object
guard = AgentGuard()

# Start AgentGuard
guard.start()


# -----------------------------
# Search Tool
# -----------------------------
if guard.check_tool("search"):
    search("Python security")

print()


# -----------------------------
# Email Tool
# -----------------------------
if guard.check_tool("send_email"):
    send_email()

print()


# -----------------------------
# Database Tool
# -----------------------------
if guard.check_tool("database"):
    database()

print()


# -----------------------------
# Unknown Tool
# -----------------------------
if guard.check_tool("weather_api"):
    print("Weather tool executed.")