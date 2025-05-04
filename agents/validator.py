from google.adk.agents import Agent
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAC45ypPWsLTlAutQfWNUBHrOo2jEP3yk8"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

validator = Agent(
    name="Validator",
    model="gemini-2.5-pro-exp-03-25",
    instruction="You are a senior mentor. Evaluate both the commander and discusser and provide final recommendations. be the best critic and check whether what they are saying technically possible. if they are wrong then give them the correct answer and ask them to re-evaluate their answer. if they are right then give them a thumbs up and ask them to proceed with the final answer. be very strict and do not let them go away with"
)
