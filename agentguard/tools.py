"""Demo tools used by the AgentGuard MVP."""


def search(query):

    print(
        f"🔍 Searching for: {query}"
    )

    return (
        f"Search completed for '{query}'. "
        "Found information about AI security, "
        "prompt injection, agent permissions, "
        "and runtime monitoring."
    )


def send_email(recipient, message):

    print(
        f"📧 Sending email to: {recipient}"
    )

    print(
        f"📝 Message: {message}"
    )

    return (
        f"Email successfully sent to "
        f"{recipient}."
    )


def database(query):

    print(
        f"🗄️ Database query: {query}"
    )

    return (
        "Database returned 3 customer records."
    )


def broken_tool():

    raise RuntimeError(
        "Database connection failed"
    )