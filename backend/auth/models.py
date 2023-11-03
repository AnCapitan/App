from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, func, DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    email = Column(String(30), unique=True)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
