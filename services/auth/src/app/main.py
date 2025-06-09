from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.app.api.router import router
from src.app.infrastructure.cache import redis_cache
from src.app.infrastructure.http_client import init_http_client, close_http_client

# force import to execute decorator to register class
import src.app.infrastructure.repositories.auth


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_http_client()
    await redis_cache.connect()
    yield
    await redis_cache.disconnect()
    await close_http_client()


def create_application() -> FastAPI:
    _app = FastAPI(lifespan=lifespan)
    _app.include_router(router)
    return _app

app = create_application()
