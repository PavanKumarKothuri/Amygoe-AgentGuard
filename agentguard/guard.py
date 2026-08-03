from agentguard.policy import POLICY
from agentguard.interceptor import Interceptor

class AgentGuard:

    def __init__(self):
        self.interceptor = Interceptor()
        self.name = "Amygoe-AgentGuard"
        self.version = "0.0.1"
        self.policy = POLICY

    def start(self):
        print(f"\n🛡️ {self.name} v{self.version} started.\n")

    def execute(self, tool_name, tool_function, *args):

        self.interceptor.intercept(tool_name)

        if self.check_tool(tool_name):

            tool_function(*args)

        else:

            print(f"🚫 '{tool_name}' execution denied.")

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