print("🛡️ Welcome to Amygoe-AgentGuard!")
print("Sprint 1 - Day 3\n")

from agentguard.guard import AgentGuard

# Create AgentGuard object
guard = AgentGuard()

# Start AgentGuard
guard.start()

# List of tools to test
tools = [
    "search",
    "send_email",
    "delete_database",
    "calculator",
    "format_disk",
    "weather_api"
]

# Check every tool
for tool in tools:

    if guard.check_tool(tool):
        print(f"➡️ {tool} executed successfully.\n")
    else:
        print(f"🚫 {tool} execution denied.\n")