from sqlalchemy.orm import Session
from app.models import News
from app.schemas import NewsOut
from datetime import datetime


def save_news_items(news_data: list[dict], db: Session):
    saved_items = []
    for article in news_data[:3]:  # Save only top 3
        news_item = News(
            title=article["title"],
            description=article.get("description"),
            url=article["url"],
            published_at=datetime.fromisoformat(article["publishedAt"].replace("Z", "+00:00"))
        )
        db.add(news_item)
        saved_items.append(news_item)
    db.commit()
    return saved_items
