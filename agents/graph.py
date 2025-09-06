from dotenv import load_dotenv
load_dotenv()

from langchain.globals import set_debug,set_verbose
set_debug(True)
set_verbose(True)
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
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Defining hte planner agent
def planner_agent(state:dict)->dict:
    user_prompt=state["user_prompt"]
    resp=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    return ({"plan":resp})
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Defining the architect agent
def architect_agent(state:dict)->str:
    plan:Plan=state["plan"]
    resp=llm.with_structured_output(TaskPlan).invoke(architect_prompt(plan))
    if resp is None:
        raise ValueError("The planner didnot return a valid response")
    resp.plan=plan
    return {"task_plan":resp}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Defining a coder agent
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_edge("planner","architect")
graph.set_entry_point("planner")
agent=graph.compile()
resp=agent.invoke({"user_prompt":user_prompt})
print(resp)
