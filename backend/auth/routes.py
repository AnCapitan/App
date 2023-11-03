from datetime import timedelta
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from auth.jwt import create_access_token
from .schemas import Token, CreateUser
from .models import User
from config.database import get_async_session
from sqlalchemy.orm import Session

router_auth = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {
    "Alice": {
        "password": password_context.hash("AlicePassword")
    },
    "Bob": {
        "password": password_context.hash("BobPassword")
    }
}

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    print(user)
    if user is None or not verify_password(password, user['password']):
        return False
    return True


@router_auth.post("/register")
async def register_user(new_user: CreateUser, db: Session = Depends(get_async_session)):
    user = User(**new_user.model_dump())
    user.hashed_password = password_context.hash(user.hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router_auth.get("/secure-data")
async def secure_data(current_user: str = Depends(oauth2_scheme)):
    return {"message": "This is secure data!", "user": current_user}

@router_auth.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if authenticate_user(username, password):
        access_token_expires = timedelta(minutes=15)
        access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")
