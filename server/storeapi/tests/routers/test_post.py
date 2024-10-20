import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/createpost", json={"body": body})
    return response.json()


@pytest.fixture()
async def created_post(async_client: AsyncClient):
    return await create_post("Test post", async_client)


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "Test post"

    resonse = await async_client.post("/createpost", json={"body": body})

    assert resonse.status_code == 201
    assert {"id": 0, "body": body}.items() <= resonse.json().items()

@pytest.mark.anyio
async def test_create_post_failed(async_client: AsyncClient):
    response = await async_client.post("/createpost")

    assert response.status_code == 422