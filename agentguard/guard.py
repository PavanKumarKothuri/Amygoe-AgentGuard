from curses import error

from agentguard.policy import POLICY
from agentguard.interceptor import Interceptor
from agentguard.logger import logger
from agentguard.exceptions import ToolBlockedError

class AgentGuard:

    def __init__(self):
        self.interceptor = Interceptor()
        self.name = "Amygoe-AgentGuard"
        self.version = "0.0.1"
        self.policy = POLICY

    def start(self):
        logger.info("AgentGuard Started")

        print(f"\n🛡️ {self.name} v{self.version} started.")
        print(f"📜 Policy : {self.policy['policy_name']}")
        print(f"🛡️ Security Level : {self.policy['security_level']}\n")

    # def execute(self, tool_name, tool_function, *args):

    #     # Intercept the tool request
    #     self.interceptor.intercept(tool_name)

    #     # Check the security policy
    #     decision = self.check_tool(tool_name)

    #     print(f"Decision : {decision['reason']}")

    #     # Execute only if allowed
    #     if decision["allowed"]:

    #         tool_function(*args)

    #         logger.info(f"Executed : {tool_name}")

    #     else:

    #         print(f"🚫 '{tool_name}' execution denied.")

    #         logger.warning(
    #             f"Execution Denied : {tool_name}"
    #         )

    def execute(self, tool_name, tool_function, *args):

        # Intercept the tool request
        self.interceptor.intercept(tool_name)

        # Check the security policy
        decision = self.check_tool(tool_name)

        print(f"Decision : {decision['reason']}")

        if not decision["allowed"]:

            print(f"🚫 '{tool_name}' execution denied.")

            logger.warning(
                f"Execution Denied : {tool_name}"
            )

            raise ToolBlockedError(
                f"Tool '{tool_name}' was blocked by AgentGuard."
            )

        try:

            tool_function(*args)

            logger.info(
                f"Executed : {tool_name}"
            )

        except Exception as error:

            logger.exception(
                f"Tool Execution Failed : {tool_name} | Error : {error}"
            )

            print(
                f"⚠️ Tool '{tool_name}' failed: {error}"
            )

    def check_tool(self, tool_name):

        print(f"Checking tool: {tool_name}")

        # Log every tool request
        logger.info(
            f"Tool Requested : {tool_name}"
        )

        # Explicitly blocked tool
        if tool_name in self.policy["blocked_tools"]:

            logger.warning(
                f"Decision : BLOCKED | Tool : {tool_name}"
            )

            return {
                "allowed": False,
                "reason": "Tool is blocked by policy"
            }

        # Explicitly allowed tool
        if tool_name in self.policy["allowed_tools"]:

            logger.info(
                f"Decision : ALLOWED | Tool : {tool_name}"
            )

            return {
                "allowed": True,
                "reason": "Tool is allowed"
            }

        # Unknown tool = Default Deny
        logger.warning(
            f"Decision : UNKNOWN TOOL | Tool : {tool_name}"
        )

        return {
            "allowed": False,
            "reason": "Unknown tool (Default Deny)"
        }