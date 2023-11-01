from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    balance: float = 0.0  # Default value for balance
