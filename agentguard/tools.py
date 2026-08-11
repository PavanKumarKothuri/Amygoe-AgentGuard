"""
Utility tools for Amygoe-AgentGuard.
"""


def search(query):
    """Simulate a search tool."""
    print(f"🔍 Searching for: {query}")


def send_email():
    """Simulate an email tool."""
    print("📧 Sending email...")


def database():
    """Simulate a database tool."""
    print("🗄️ Reading customer database...")

def broken_tool():
    """Simulate a tool failure."""
    raise RuntimeError("Database connection failed")