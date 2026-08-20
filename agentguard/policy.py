import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

POLICY_FILE = BASE_DIR / "config" / "policy.json"


def load_policy():
    """Load and validate AgentGuard policy from JSON."""

    if not POLICY_FILE.exists():

        raise FileNotFoundError(
            f"Policy file not found: {POLICY_FILE}"
        )

    try:

        with open(POLICY_FILE, "r") as file:
            policy = json.load(file)

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Invalid JSON policy file: {error}"
        )

    # ------------------------------------
    # Validate required fields
    # ------------------------------------

    required_fields = [
        "policy_name",
        "version",
        "security_level",
        "allowed_tools",
        "blocked_tools"
    ]

    for field in required_fields:

        if field not in policy:

            raise ValueError(
                f"Missing required policy field: {field}"
            )

    # ------------------------------------
    # Validate conflicting rules
    # ------------------------------------

    allowed = set(policy["allowed_tools"])
    blocked = set(policy["blocked_tools"])

    conflicts = allowed.intersection(blocked)

    if conflicts:

        raise ValueError(
            f"Policy conflict. "
            f"Tools cannot be both allowed and blocked: "
            f"{sorted(conflicts)}"
        )

    return policy


POLICY = load_policy()