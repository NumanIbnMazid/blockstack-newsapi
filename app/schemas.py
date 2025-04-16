from datetime import datetime
from pydantic import BaseModel

class NewsOut(BaseModel):
    title: str
    description: str | None = None
    url: str
    published_at: datetime

    class Config:
        orm_mode = True
