from dotenv import load_dotenv
load_dotenv()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from langchain_groq import ChatGroq
from pydantic import BaseModel

llm = ChatGroq(model="gemma2-9b-it")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
user_prompt="Design a complete  calculator web app"

from prompts import *
prompt=planner_prompt(user_prompt)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from states import *
# ans = llm.with_structured_output(Plan).invoke(prompt)
# print(ans)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from langgraph.constants import END
from langgraph.graph import StateGraph
graph=StateGraph(dict)
def planner_agent(state:dict)->dict:
    user_prompt=state["user_prompt"]
    resp=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    return ({"plan":resp})
graph.add_node("planner",planner_agent)
graph.set_entry_point("planner")
agent=graph.compile()
resp=agent.invoke({"user_prompt":user_prompt})
print(resp)
