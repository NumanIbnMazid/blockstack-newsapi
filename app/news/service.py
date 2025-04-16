import httpx
from typing import Optional
from app.config import settings
import datetime

NEWS_API_BASE_URL = "https://newsapi.org/v2"
API_KEY = settings.NEWS_API_KEY

async def fetch_top_headlines(country: Optional[str] = None, source: Optional[str] = None, page: int = 1):
    url = f"{NEWS_API_BASE_URL}/top-headlines"
    params = {
        "apiKey": API_KEY,
        "page": page,
        "pageSize": 10,
    }
    if country:
        params["country"] = country
    if source:
        params["sources"] = source

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()

async def fetch_everything(query: str, page: int = 1):
    url = f"{NEWS_API_BASE_URL}/everything"
    params = {
        "q": query,
        "apiKey": API_KEY,
        "page": page,
        "pageSize": 10,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()


async def fetch_latest_news(q="general", sort_by="publishedAt", page_size=10):
    today = datetime.datetime.now(datetime.timezone.utc).date()
    yesterday = today - datetime.timedelta(days=1)

    params = {
        "apiKey": settings.NEWS_API_KEY,
        "q": q,
        "from": yesterday.isoformat(),
        "to": today.isoformat(),
        "sortBy": sort_by,
        "pageSize": page_size,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{NEWS_API_BASE_URL}/everything", params=params)
        response.raise_for_status()
        return response.json()
