"""Policy definitions for AgentGuard."""


class Policy:
    """Placeholder policy container."""

    def __init__(self, name: str = "default") -> None:
        self.name = name

POLICY = {
    "allowed_tools": [
        "search",
        "database",
        "calculator"
    ],

    "blocked_tools": [
        "send_email"
    ]
}