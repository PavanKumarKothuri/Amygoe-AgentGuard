from agentguard.interceptor import Interceptor
from agentguard.policy import POLICY
from agentguard.policy_engine import PolicyEngine
from agentguard.logger import logger
from agentguard.exceptions import ToolBlockedError


class AgentGuard:

    def __init__(self):

        self.name = "Amygoe-AgentGuard"
        self.version = "0.0.1"

        self.policy = POLICY

        self.interceptor = Interceptor()

        self.policy_engine = PolicyEngine(
            self.policy
        )

    def start(self):

        logger.info("AgentGuard Started")

        print(
            f"\n🛡️ {self.name} "
            f"v{self.version} started."
        )

        print(
            f"📜 Policy : "
            f"{self.policy['policy_name']}"
        )

        print(
            f"🛡️ Security Level : "
            f"{self.policy.get('security_level', 'Unknown')}\n"
        )

    def execute(
        self,
        tool_name,
        tool_function,
        *args,
        **kwargs
    ):

        # ------------------------------------
        # 1. Intercept the tool request
        # ------------------------------------

        self.interceptor.intercept(tool_name)

        logger.info(
            f"Tool Requested : {tool_name}"
        )

        # ------------------------------------
        # 2. Check security policy
        # ------------------------------------

        decision = self.policy_engine.check(
            tool_name
        )

        print(
            f"Decision : {decision.reason}"
        )

        logger.info(
            f"Decision : {decision.reason} "
            f"| Tool : {tool_name}"
        )

        # ------------------------------------
        # 3. Block denied requests
        # ------------------------------------

        if not decision.allowed:

            logger.warning(
                f"Execution Denied : {tool_name}"
            )

            print(
                f"🚫 '{tool_name}' "
                f"execution denied."
            )

            raise ToolBlockedError(
                f"Tool '{tool_name}' "
                f"was blocked by AgentGuard."
            )

        # ------------------------------------
        # 4. Execute allowed tool
        # ------------------------------------

        try:

            result = tool_function(
                *args,
                **kwargs
            )

            logger.info(
                f"Executed : {tool_name}"
            )

            return result

        # ------------------------------------
        # 5. Handle tool failure
        # ------------------------------------

        except Exception as error:

            logger.exception(
                f"Tool Execution Failed : "
                f"{tool_name} | Error : {error}"
            )

            print(
                f"⚠️ Tool '{tool_name}' "
                f"failed: {error}"
            )

            return (
                f"Tool '{tool_name}' "
                f"failed: {error}"
            )