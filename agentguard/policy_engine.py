from agentguard.policy import POLICY
from agentguard.decision import Decision


class PolicyEngine:

    def __init__(self, policy=None):
        self.policy = policy or POLICY

    def check(self, tool_name):

        if tool_name in self.policy["blocked_tools"]:
            return Decision(
                allowed=False,
                reason="Tool is blocked by policy"
            )

        if tool_name in self.policy["allowed_tools"]:
            return Decision(
                allowed=True,
                reason="Tool is allowed"
            )

        return Decision(
            allowed=False,
            reason="Unknown tool (Default Deny)"
        )