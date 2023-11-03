from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: bool

class TaskSchema(BaseModel):
    title: str
    description: str
    status: bool
    time_created: str 
    time_update: str
