from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    password: str

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str



class Token(BaseModel):
    access_token: str