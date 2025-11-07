from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from react_template import get_react_prompt_template
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.mytools import *
import os

# Load environment variables
load_dotenv()

# Configure the API key directly
api_key = os.environ["GEMINI_API_KEY"]

# Choose the LLM to use with the API key
llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-001", google_api_key=api_key)

# Set the tools
tools = [add, subtract, multiply, divide, power, search, repl_tool, get_historical_price, get_current_price, get_company_info, check_system_time]

# Get the react prompt template
prompt_template = get_react_prompt_template()

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Test the agent with a stock price query
print("Testing agent with stock price query...")
try:
    response = agent_executor.invoke({"input": "what is the stock price of Adani green"})
    print("Response:", response["output"])
except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()