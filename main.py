from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
#from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
#from tools import search_tool, wiki_tool, save_tool

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini")
response = llm.invoke("What team does LeBron James play for?")
print(response)