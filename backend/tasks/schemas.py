from pydantic import BaseModel


class TaskSchemaAdd(BaseModel):
    title: str
    description: str

class TaskSchemaUpdate(BaseModel):
    title: str
    description: str
    status: bool

class TaskSchema(BaseModel):
    title: str
    description: str
    status: bool
    time_created: str 
    time_update: str
