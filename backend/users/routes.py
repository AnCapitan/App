from fastapi import APIRouter, Depends
from .models import User
from .schemes import UserCreate
from config.database import get_async_session
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import Session

router_user = APIRouter()

@router_user.get("/users/")
async def list_users(db: Session = Depends(get_async_session)):
    stmt = select(User)
    result = await db.execute(stmt)
    users = result.scalars().all()
    return users

@router_user.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_async_session)):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalars(stmt).one()
    return user

@router_user.post("/users/")
async def create_user(user_create: UserCreate, db: Session = Depends(get_async_session)):
    new_user = User(**user_create.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user