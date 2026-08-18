# """Policy definitions for AgentGuard."""


# class Policy:
#     """Placeholder policy container."""

#     def __init__(self, name: str = "default") -> None:
#         self.name = name

# POLICY = {
#     "allowed_tools": [
#         "search",
#         "database",
#         "calculator"
#     ],

#     "blocked_tools": [
#         "send_email"
#     ]
# }

# import json


# with open("policy.json", "r") as file:
#     POLICY = json.load(file)

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
POLICY_FILE = BASE_DIR / "config" / "policy.json"


def load_policy():
    """Load AgentGuard policy from the configuration file."""

    with open(POLICY_FILE, "r") as file:
        return json.load(file)


POLICY = load_policy()