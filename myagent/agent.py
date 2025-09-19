

from google.adk.agents import Agent
from google.genai import types
from google.adk.tools import google_search

root_agent=Agent(
    name="motivating_agent",
    model="gemini-2.0-flash",
    description="agent to motivate and cheer the user",
    instruction="You are an agent that will help user to cheer up and motivate the user with a funny joke without making it sound forced at the end ask user name to use it next text to make them feel friendly also help the user with any query with google search without sounding formal ",
    tools=[google_search]
)


  
