from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    url = Column(String, nullable=False)
    published_at = Column(DateTime)
