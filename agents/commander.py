from google.adk.agents.llm_agent import LlmAgent

import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAC45ypPWsLTlAutQfWNUBHrOo2jEP3yk8"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

import subprocess
from google.adk.tools.function_tool import FunctionTool

def terminal_executor(command: str) -> str:
    if any(bad in command for bad in ["rm", "shutdown", "reboot"]):
        return "🚫 Command blocked for safety."
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=8
        )
        return result.stdout or result.stderr
    except Exception as e:
        return f"❌ Error: {str(e)}"

commander = LlmAgent(
    name="Commander",
    model="gemini-2.5-pro-exp-03-25",  # Thinking model
    
    instruction="you are a ultimate biotech researcher. you will propose a solution, you can also google search for the solution"
)
