import asyncio
import pytest
from httpx import AsyncClient
from unittest.mock import AsyncMock, patch

from src.app.main import app
from src.app.services import AuthService


# @pytest.fixture
# def event_loop():
#     loop = asyncio().new_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture
def auth_service_setup():
    mock_repo = AsyncMock()
    mock_cache = AsyncMock()
    mock_repo_getter = lambda method, data: mock_repo
    return AuthService(mock_cache, mock_repo_getter), mock_repo


# @pytest.fixture
# async def async_client(event_loop):
#     async with AsyncClient(app=app, base_url='http://test') as client:
#         yield client


@pytest.fixture
def mock_redis():
    mock_client = AsyncMock()
    with patch('src.app.infrastructure.dependencies.cache.get_cache') as mock_get_cache:
        mock_cache = mock_get_cache.return_value
        mock_cache._client = mock_client
        yield mock_cache


@pytest.fixture(scope='function')
def mock_user_api():
    with patch('src.app.infrastructure.apis.user.UserAPI.login', new_callable=AsyncMock) as mock:
        yield mock
