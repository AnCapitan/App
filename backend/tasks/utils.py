from abc import ABC, abstractmethod
from fastapi import HTTPException
from sqlalchemy import insert, select
from config.database import async_session_maker
from .models import Task

class AbstractRepository(ABC):
    
    @abstractmethod
    async def add():
        raise NotImplemented
    
    @abstractmethod
    async def find_all():
        raise NotImplemented
    
    @abstractmethod
    async def find_one():
        raise NotImplemented
    
    @abstractmethod
    async def delete():
        raise NotImplemented
    
    async def update():
        raise NotImplemented
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()
        
    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            result = await session.execute(stmt)
            result = result.scalars().all()
            return result    
    
    async def find_one(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == id)
            result = await session.execute(stmt)
            task = result.scalars(stmt).one()
            return task
        
    async def delete(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == id)
            result = await session.execute(stmt)
            result = result.scalars(stmt).one_or_none()
            if result is not None:
                await session.delete(result)
                await session.commit()
                return True
            else:
                return False
            
    async def update(self, data: dict, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == id)
            result = await session.execute(stmt)
            result = result.scalars(stmt).one_or_none()
            if result is not None:
                result.title = data['title']
                result.description = data['description']
                result.status = data['status']
                session.add(result)
                await session.commit()
                await session.refresh(result)
                return result
            else:
                raise HTTPException(status_code=404, detail="Task not found")
            


