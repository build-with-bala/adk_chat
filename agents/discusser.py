from google.adk.agents import Agent
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAC45ypPWsLTlAutQfWNUBHrOo2jEP3yk8"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

discusser = Agent(
    name="Discusser",
    model="gemini-2.0-flash",
    instruction="You are a thoughtful collaborator. Review and critique the commander's decisions."
)
