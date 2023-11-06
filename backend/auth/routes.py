from datetime import timedelta
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth import authenticate_user, create_access_token, oauth2_scheme, password_context, get_current_active_user
from config.config import ACCESS_TOKEN_EXPIRE_MINUTES
from .schemas import Token, CreateUser, UserSchema
from .models import User
from config.database import get_async_session
from sqlalchemy.orm import Session
from typing import Annotated


router_auth = APIRouter()

@router_auth.get("/secure-data")
async def secure_data(current_user: str = Depends(oauth2_scheme)):
    return {"message": "This is secure data!", "user": current_user}

@router_auth.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_async_session)):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router_auth.post("/register")
async def register_user(new_user: CreateUser, db: Session = Depends(get_async_session)):
    user = User(**new_user.model_dump())
    user.hashed_password = password_context.hash(user.hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router_auth.get("/users/me/", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

