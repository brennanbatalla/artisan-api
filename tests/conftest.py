import tests.env
import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from app.main import app


@pytest.fixture
async def client_test():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test", follow_redirects=True) as ac:
            yield ac