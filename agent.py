from agentguard.guard import AgentGuard


class DemoAgent:

    def __init__(self, guard):

        self.guard = guard

    def run(self, task):

        print("\n🤖 AI Agent received task:")
        print(f"   {task}")

        # --------------------------------
        # Simulated agent decision
        # --------------------------------

        if "search" in task.lower():

            self.use_search()

        elif "email" in task.lower():

            self.use_email()

        elif "database" in task.lower():

            self.use_database()

        else:

            print(
                "🤷 Agent does not know "
                "which tool to use."
            )

    # ------------------------------------
    # Search
    # ------------------------------------

    def use_search(self):

        print(
            "\n🤖 Agent decided:"
            " use search"
        )

        def search(query):

            print(
                f"🔍 Searching for: {query}"
            )

        self.guard.execute(
            "search",
            search,
            "AI security"
        )

    # ------------------------------------
    # Email
    # ------------------------------------

    def use_email(self):

        print(
            "\n🤖 Agent decided:"
            " send email"
        )

        def send_email():

            print(
                "📧 Email sent!"
            )

        self.guard.execute(
            "send_email",
            send_email
        )

    # ------------------------------------
    # Database
    # ------------------------------------

    def use_database(self):

        print(
            "\n🤖 Agent decided:"
            " access database"
        )

        def database():

            print(
                "🗄️ Database accessed."
            )

        self.guard.execute(
            "database",
            database
        )