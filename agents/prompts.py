def planner_prompt(user_prompt:str)->str:
    prompt=f'''you are a Planner agent convert the user prmpt into a complete engineering project plan
    user request={user_prompt}'''
    return prompt