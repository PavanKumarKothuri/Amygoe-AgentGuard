from agentguard.guard import AgentGuard
from agentguard.ai_agent import AIAgent


def main():

    print("🛡️ Amygoe-AgentGuard")
    print("🤖 OpenAI Agent + AgentGuard Demo\n")

    # Start AgentGuard
    guard = AgentGuard()
    guard.start()

    # Create AI agent protected by AgentGuard
    agent = AIAgent(guard)

    # Run a realistic multi-step agent task
    agent.run(
        "Search for AI security information, "
        "then email the results to test@example.com."
    )


if __name__ == "__main__":
    main()

