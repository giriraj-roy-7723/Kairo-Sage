from pydantic import BaseModel , Field ,ConfigDict

class File(BaseModel):
    path:str=Field(description="the path to the file to be created or modified")
    purpose:str=Field(description="The purpose of the file,e.g. 'main application logic','data processing module',etc.")
class Plan(BaseModel):
    name:str=Field(description="The name of the app to be built")
    description:str=Field(description="A online description of the app to be built,e.g.'A web applicaiton for managing personal expenses'")
    techstack:str=Field(description="The tech stack to be used for the app , e.g. 'python','javascript','react','flask'")
    features:list[str]=Field(description="List of features the app should have ,e.g.'user suthentication','data analysis'")
    files:list[File]=Field(description="A list of files to be created each with a 'path' and a 'purpose'")

class ImplementationTask(BaseModel):
    filepath:str=Field(description="The path to the file to be modified")
    task_description:str=Field(description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc.")
class TaskPlan(BaseModel):
    implementation_Steps:list[ImplementationTask]=Field(description="The plan for the task to be implemented")
    model_config = ConfigDict(extra="allow")