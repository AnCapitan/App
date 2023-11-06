from typing import Annotated
from fastapi import APIRouter, Depends
from .schemas import TaskSchemaAdd, TaskSchemaUpdate
from .dependencies import tasks_service
from .service import TasksService

router_task = APIRouter(prefix='/tasks', tags=["Tasks"])

@router_task.get("")
async def tasks(tasks_service: Annotated[TasksService, Depends(tasks_service)]):
    tasks = await tasks_service.get_tasks()
    return tasks

@router_task.get("/{task_id}")
async def get_task(task_id: int, tasks_service: Annotated[TasksService, Depends(tasks_service)]):
    task = await tasks_service.get_task(task_id)
    return task

@router_task.post("")
async def add_task(task: TaskSchemaAdd, tasks_service: Annotated[TasksService, Depends(tasks_service)]):
    task_id = await tasks_service.add_task(task)
    return {"task id": task_id}

@router_task.put("/{task_id}")
async def update_task(task: TaskSchemaUpdate, task_id: int, tasks_service: Annotated[TasksService, Depends(tasks_service)]):
    task = await tasks_service.update_task(task_id, task)
    return task

@router_task.delete("/{task_id}")
async def delete_task(task_id: int, tasks_service: Annotated[TasksService, Depends(tasks_service)]):
    task = await tasks_service.delete_task(task_id)
    return task
                   