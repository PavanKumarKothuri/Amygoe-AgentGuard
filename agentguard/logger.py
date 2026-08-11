# """Logging helpers for AgentGuard."""


# class Logger:
#     """Placeholder logger."""

#     def log(self, message: str) -> None:
#         print(message)


import logging


logging.basicConfig(
    filename="agentguard.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("AgentGuard")