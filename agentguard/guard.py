class AgentGuard:

    def __init__(self):
        self.name = "Amygoe-AgentGuard"
        self.version = "0.0.1"

    def start(self):
        print(f"{self.name} v{self.version} started.")

    def check_tool(self, tool_name):

        print(f"Checking tool: {tool_name}")

        if tool_name == "send_email":
            print("❌ Blocked")
        else:
            print("✅ Allowed")