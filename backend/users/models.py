from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, name="ID")
    username = Column(String, default=None, unique=True, name="Никнейм")
    email = Column(String, unique=True, name="Эл. почта")
    password = Column(String, name="пароль")
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    balance = Column(Float, default=0, name="Баланс")
