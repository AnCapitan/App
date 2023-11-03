from datetime import datetime, timedelta
from jose import jwt
from config.config import SECRET_KEY, ALGORITHM
from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from .schemas import TokenData
from .models import User
from sqlalchemy.future import select
from config.database import get_async_session
from sqlalchemy.orm import Session
from typing import Annotated
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





async def verify_password(plain_password, hashed_password):
    result = password_context.verify(plain_password, hashed_password)
    return result

async def authenticate_user(username: str, password: str, db:Session):
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    user = result.scalars(stmt).one_or_none()
    if User is not None:
        verify = await verify_password(password, user.hashed_password)
        return user
    else:
        return None
    


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_async_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    stmt = select(User).where(User.username == token_data.username)
    result = await db.execute(stmt)
    user = result.scalars(stmt).one_or_none()    
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return current_user
