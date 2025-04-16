from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from datetime import timedelta
from app.auth.utils import authenticate_client, create_access_token
from app.config import settings

router = APIRouter()


@router.post("/token")
def get_token(client_id: str = Form(...), client_secret: str = Form(...)):
    if not authenticate_client(client_id, client_secret):
        raise HTTPException(status_code=401, detail="Invalid client credentials")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": client_id}, expires_delta=access_token_expires
    )

    return JSONResponse({"access_token": access_token, "token_type": "bearer"})
