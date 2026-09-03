from agentguard.guard import AgentGuard
from agentguard.ai_agent import AIAgent


print("🛡️ Welcome to Amygoe-AgentGuard!")
print("🤖 Real LLM Agent Demo\n")


guard = AgentGuard()

guard.start()

agent = AIAgent(guard)


agent.run(
    # "Search for information about AI security."
    # "Send an email to test@example.com saying "
    # "this is an AgentGuard security test."

    "Search for AI security information, then email the results to test@example.com."
)