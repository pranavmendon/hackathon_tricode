# agent.py

from google.adk.agents import Agent
from google.genai import types

# Create a basic agent class
class GreetingAgent(Agent):
    model = "gemini-2.0-flash"  # Underlying model used by this agent
    description = "Greeting Agent"  # Brief description of the agent
    instruction = "You are a helpful assistant that greets the user."

    # Configuration for how the model should generate responses
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,          # Lower = more deterministic responses
        max_output_tokens=250     # Controls response length
    )

    # Optional: you can override handle_request if you want custom logic
    async def handle_request(self, request):
        """Handle incoming requests to the agent."""
        return await self.generate_content(request.input)

# Entry point for running the agent
if __name__ == "__main__":
    agent = GreetingA
