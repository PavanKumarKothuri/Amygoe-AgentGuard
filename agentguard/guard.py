from agentguard.policy import POLICY
from agentguard.interceptor import Interceptor

class AgentGuard:

    def __init__(self):
        self.interceptor = Interceptor()
        self.name = "Amygoe-AgentGuard"
        self.version = "0.0.1"
        self.policy = POLICY
    
    def start(self):
        print(f"\n🛡️ {self.name} v{self.version} started.")
        print(f"📜 Policy : {self.policy['policy_name']}")
        print(f"🛡️ Security Level : {self.policy['security_level']}\n")

    def execute(self, tool_name, tool_function, *args):

        self.interceptor.intercept(tool_name)

        decision = self.check_tool(tool_name)

        print(f"Decision : {decision['reason']}")

        if decision["allowed"]:

            tool_function(*args)

        else:

            print(f"🚫 '{tool_name}' execution denied.")

    def check_tool(self, tool_name):

        print(f"Checking tool: {tool_name}")

        if tool_name in self.policy["blocked_tools"]:

            return {
            "allowed": False,
            "reason": "Tool is blocked by policy"
            }

        if tool_name in self.policy["allowed_tools"]:

            return {
            "allowed": True,
            "reason": "Tool is allowed"
            }

        return {
        "allowed": False,
        "reason": "Unknown tool (Default Deny)"
        }
    

    