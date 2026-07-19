print("🛡️ Welcome to Amygoe AgentGuard!")
print("Sprint 1 - Day 1")
print("Project setup completed successfully.")


from agentguard.guard import AgentGuard

# Create an AgentGuard object
guard = AgentGuard()

# Start the application
guard.start()

# Test some tools
guard.check_tool("search")
guard.check_tool("send_email")
guard.check_tool("database")