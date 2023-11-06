from fastapi import HTTPException
from .schemas import TaskSchemaAdd, TaskSchemaUpdate
from .utils import AbstractRepository, SQLAlchemyRepository
from .models import Task


class TasksRepository(SQLAlchemyRepository):
    model = Task


class TasksService():
    def __init__(self, task_repo: AbstractRepository) -> None:
        self.tasks_repo: AbstractRepository = task_repo()

    async def add_task(self, task: TaskSchemaAdd):
        tasks_dict =task.model_dump()
        task_id = await self.tasks_repo.add(tasks_dict)
        return task_id
    
    async def get_tasks(self):
        tasks = await self.tasks_repo.find_all()
        return tasks
    
    async def get_task(self, task_id: int):
        task = await self.tasks_repo.find_one(task_id)
        return task
    
    async def update_task(self, task_id: int, task: TaskSchemaUpdate):
        task_dict = task.model_dump()
        task_id = await self.tasks_repo.update(task_dict, task_id)
        return task_id
    
    async def delete_task(self, task_id: int):
        task = await self.tasks_repo.delete(task_id)
        if task:
            return {"Message": "Task delete"}
        else:
            raise HTTPException(status_code=404, detail="Task not found")
    