from datetime import datetime
from pydantic import BaseModel


class NewsOut(BaseModel):
    title: str
    description: str | None = None
    url: str
    published_at: datetime

    model_config = {"from_attributes": True}
