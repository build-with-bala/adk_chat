
from .agents.commander import commander
from .agents.discusser import discusser
from .agents.validator import validator
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.agents.llm_agent import LlmAgent
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAC45ypPWsLTlAutQfWNUBHrOo2jEP3yk8"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"
print(f"Google API Key set: {'Yes' if os.environ.get('GOOGLE_API_KEY') and os.environ['GOOGLE_API_KEY'] != 'YOUR_GOOGLE_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")




# Create a sequential pipeline: Commander → Discusser → Validator
chat_agent = LlmAgent(
    name="Ultimate_researcher",
    model = "gemini-2.5-pro-exp-03-25",
    description="You are a multi-agent system. Collaborate to solve complex tasks. especially research",
    instruction="You the main research and u have three agents to help you, the commander, discusser and validator. The commander will propose a solution, the discusser will review it and the validator will give the final recommendation. make it a long interaction between the three agents once all 4 of you are convinced then producte me the final answer. only if the validator accepst it come to me with the final answer. if the validator rejects it then ask the commander",
    sub_agents=[commander, discusser, validator]
)


# Create session
root_agent = chat_agent
session_service = InMemorySessionService()
