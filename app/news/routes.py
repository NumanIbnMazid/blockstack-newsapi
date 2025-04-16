from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.auth.utils import get_current_client
from app.database import get_db
from app.schemas import NewsOut
from app.news.service import fetch_top_headlines, fetch_everything, fetch_latest_news
from app.news.crud import save_news_items

router = APIRouter(prefix="/news", tags=["News"])


@router.get("", response_model=list[NewsOut])
async def get_news(
    page: int = 1,
    query: str = "technology",
    token=Depends(get_current_client),
):
    data = await fetch_everything(query=query, page=page)
    return [
        {
            "title": a["title"],
            "description": a["description"],
            "url": a["url"],
            "published_at": a["publishedAt"],
        }
        for a in data.get("articles", [])
    ]


@router.post("/save-latest")
async def save_latest_news(
    db: Session = Depends(get_db), 
    token=Depends(get_current_client)
):
    data = await fetch_latest_news()
    top_3_articles = data.get("articles", [])[:3]
    
    if not top_3_articles:
        raise HTTPException(status_code=404, detail="No articles found to save.")
    
    saved = save_news_items(top_3_articles, db)
    return {
        "saved_count": len(saved),
        "saved_titles": [item.title for item in saved],
    }


@router.get("/headlines/country/{country_code}", response_model=list[NewsOut])
async def get_news_by_country(country_code: str, token=Depends(get_current_client)):
    data = await fetch_top_headlines(country=country_code)
    return [
        {
            "title": a["title"],
            "description": a["description"],
            "url": a["url"],
            "published_at": a["publishedAt"],
        }
        for a in data.get("articles", [])
    ]


@router.get("/headlines/source/{source_id}", response_model=list[NewsOut])
async def get_news_by_source(source_id: str, token=Depends(get_current_client)):
    data = await fetch_top_headlines(source=source_id)
    return [
        {
            "title": a["title"],
            "description": a["description"],
            "url": a["url"],
            "published_at": a["publishedAt"],
        }
        for a in data.get("articles", [])
    ]


@router.get("/headlines/filter", response_model=list[NewsOut])
async def filter_headlines(
    country: str = Query(None),
    source: str = Query(None),
    token=Depends(get_current_client),
):
    if country and source:
        # NOTE: As per documentation, only one of 'country' or 'source' can be provided.
        # Prioritize source over country (since it's more specific).
        # Note: you can't mix this param with the sources param.
        # https://newsapi.org/docs/endpoints/top-headlines
        print("Both 'country' and 'source' provided. 'source' will be used.")
    
    # source takes priority if both are provided
    data = await fetch_top_headlines(country=None if source else country, source=source)
    return [
        {
            "title": a["title"],
            "description": a["description"],
            "url": a["url"],
            "published_at": a["publishedAt"],
        }
        for a in data.get("articles", [])
    ]
