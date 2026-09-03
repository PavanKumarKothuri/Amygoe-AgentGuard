import json

from openai import OpenAI
from agentguard.exceptions import ToolBlockedError

from agentguard.tools import (
    search,
    send_email,
    database
)


class AIAgent:

    def __init__(self, guard):

        self.guard = guard
        self.client = OpenAI()

        # --------------------------------
        # Available Python tools
        # --------------------------------

        self.tool_functions = {
            "search": search,
            "send_email": send_email,
            "database": database
        }

    def get_tool_definitions(self):

        return [

            # -----------------------------
            # Search
            # -----------------------------

            {
                "type": "function",
                "function": {
                    "name": "search",
                    "description": (
                        "Search for information."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": (
                                    "What to search for."
                                )
                            }
                        },
                        "required": ["query"]
                    }
                }
            },

            # -----------------------------
            # Send Email
            # -----------------------------

            {
                "type": "function",
                "function": {
                    "name": "send_email",
                    "description": (
                        "Send an email."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "recipient": {
                                "type": "string"
                            },
                            "message": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "recipient",
                            "message"
                        ]
                    }
                }
            },

            # -----------------------------
            # Database
            # -----------------------------

            {
                "type": "function",
                "function": {
                    "name": "database",
                    "description": (
                        "Read information from "
                        "the customer database."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        ]

    def run(self, task):

        print("\n🤖 AI Agent received:")
        print(f"   {task}")

        # --------------------------------
        # Conversation history
        # --------------------------------

        messages = [

            {
                "role": "system",
                "content": (
                    "You are an AI agent. "
                    "Use the available tools when "
                    "they are appropriate."
                )
            },

            {
                "role": "user",
                "content": task
            }
        ]

        # --------------------------------
        # Agent loop
        # --------------------------------

        for step in range(10):

            print(
                f"\n🔄 Agent step {step + 1}"
            )

            response = self.client.chat.completions.create(

                model="gpt-4o-mini",

                messages=messages,

                tools=self.get_tool_definitions()
            )

            message = response.choices[0].message

            # --------------------------------
            # No tool call = final answer
            # --------------------------------

            if not message.tool_calls:

                print("\n🧠 Final AI response:")
                print(message.content)

                return message.content

            # --------------------------------
            # Add assistant message
            # --------------------------------

            messages.append(message)

            # --------------------------------
            # Process tool calls
            # --------------------------------

            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name

                arguments = json.loads(
                    tool_call.function.arguments
                )

                print(
                    f"\n🧠 ChatGPT requested: "
                    f"{tool_name}"
                )

                print(
                    f"📦 Arguments: {arguments}"
                )

                # --------------------------------
                # Find Python function
                # --------------------------------

                tool_function = (
                    self.tool_functions.get(
                        tool_name
                    )
                )

                if tool_function is None:

                    result = (
                        f"Unknown tool: "
                        f"{tool_name}"
                    )

                else:

                    # --------------------------------
                    # 🛡️ AgentGuard
                    # --------------------------------

                    print(
                        "\n🛡️ AgentGuard intercepting..."
                    )


                    try:

                        result = self.guard.execute(
                            tool_name,
                            tool_function,
                            **arguments
                        )

                    except ToolBlockedError as error:

                        result = (
                            f"SECURITY BLOCK: {error}"
                )

                # --------------------------------
                # Return tool result to ChatGPT
                # --------------------------------

                messages.append(

                    {
                        "role": "tool",
                        "tool_call_id": (
                            tool_call.id
                        ),
                        "content": str(result)
                    }
                )

        print(
            "\n⚠️ Agent stopped after "
            "maximum steps."
        )