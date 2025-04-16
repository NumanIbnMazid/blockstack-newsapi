import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

from app.main import app
from app.database import get_db
from app.database import Base
from app.auth.utils import get_current_client

# Use in-memory SQLite for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test DB
Base.metadata.create_all(bind=engine)


# Dependency override for DB
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency override for OAuth2
def override_get_current_client():
    return {"client_id": "test-client"}


# Apply overrides
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_client] = override_get_current_client


@pytest.fixture(scope="module")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
