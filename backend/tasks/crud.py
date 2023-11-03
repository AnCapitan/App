from tasks.schemas import TaskCreate, TaskSchema, TaskUpdate
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from .models import Task
from fastapi import HTTPException


async def list_task_in_db(db:Session):
    tasks = select(Task)
    tasks_db = await db.execute(tasks)
    tasks = tasks_db.scalars().all()
    return tasks


async def get_task_in_db(db: Session, task_id: int):
    stmt = select(Task).where(Task.id == task_id)
    result = await db.execute(stmt)
    task = result.scalars(stmt).one()
    return task

async def delete_task_in_db(db: Session, task_id: int):
    stmt = select(Task).where(Task.id == task_id)
    result = await db.execute(stmt)
    task = result.scalars(stmt).one_or_none()
    if task is not None:
        await db.delete(task)
        await db.commit()
        return {"message": "Task deleted"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

async def create_task_in_db(db: Session, task_create: TaskCreate):
    new_task = Task(**task_create.model_dump())
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def update_task_in_db(db: Session, task_id: int, task_update: TaskUpdate):
    stmt = select(Task).where(Task.id == task_id)
    result = await db.execute(stmt)
    task = result.scalars(stmt).one_or_none()
    if task is not None:
        task.title = task_update.title
        task.description = task_update.description
        task.status = task_update.status
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")