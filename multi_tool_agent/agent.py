

from google.adk.agents import Agent
from google.genai import types
root_agent=Agent(
    name="motivating_agent",
    model="gemini-2.0-flash",
    description="agent to motivate and cheer the user",
    instruction="You are an agent that will help user to cheer up and motivate the user!"
)

  
