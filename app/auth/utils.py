import datetime
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from app.config import settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

SECRET_KEY = settings.CLIENT_SECRET
ALGORITHM = "HS256"


def authenticate_client(client_id: str, client_secret: str):
    if client_id == settings.CLIENT_ID and client_secret == settings.CLIENT_SECRET:
        return True
    return False


def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.timezone.utc) + (
        expires_delta or datetime.timedelta(minutes=15)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_client(token: str = Depends(oauth2_scheme)):
    return verify_token(token)
