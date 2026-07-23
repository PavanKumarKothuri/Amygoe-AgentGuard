from agentguard.policy import POLICY


class AgentGuard:

    def __init__(self):
        self.name = "Amygoe-AgentGuard"
        self.version = "0.0.1"
        self.policy = POLICY

    def start(self):
        print(f"\n🛡️ {self.name} v{self.version} started.\n")

    def check_tool(self, tool_name):

        print(f"Checking tool: {tool_name}")

        if tool_name in self.policy["blocked_tools"]:
            print("❌ Blocked\n")
            return False

        if tool_name in self.policy["allowed_tools"]:
            print("✅ Allowed\n")
            return True

        print("❌ Unknown Tool (Default Deny)\n")
        return False