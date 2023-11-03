from tasks.schemas import TaskCreate,  TaskUpdate
from fastapi import APIRouter, Depends
from config.database import get_async_session
from sqlalchemy.orm import Session
from .crud import update_task_in_db, create_task_in_db, list_task_in_db, get_task_in_db, delete_task_in_db


router_task = APIRouter()


@router_task.get("/tasks/")
async def list_task(db: Session = Depends(get_async_session)):
    return await list_task_in_db(db)

@router_task.get("/tasks/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_async_session)):
    return await get_task_in_db(db, task_id)

@router_task.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_async_session)):
    return await delete_task_in_db(db, task_id)
    
@router_task.put("/tasks/{task_id}")
async def update_task(task_update: TaskUpdate, task_id: int, db: Session = Depends(get_async_session)):
    return await update_task_in_db(db, task_id, task_update)

@router_task.post("/tasks/")
async def create_task(task_create: TaskCreate, db: Session = Depends(get_async_session)):
    return await create_task_in_db(db, task_create)

