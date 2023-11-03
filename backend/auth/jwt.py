from datetime import datetime, timedelta
import jwt

# Секретный ключ для подписи токена
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


