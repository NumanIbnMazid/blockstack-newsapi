import pytest


@pytest.mark.asyncio
async def test_get_news(async_client):
    response = await async_client.get("/news")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_headlines_by_country(async_client):
    response = await async_client.get("/news/headlines/country/us")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_headlines_by_source(async_client):
    response = await async_client.get("/news/headlines/source/cnn")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_filter_headlines(async_client):
    response = await async_client.get("/news/headlines/filter?country=us&source=cnn")
    assert response.status_code in [200, 400]  # 400 if both can't be used
    if response.status_code == 200:
        assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_save_latest(async_client):
    response = await async_client.post("/news/save-latest")
    assert response.status_code == 200
    assert "saved_count" in response.json()
