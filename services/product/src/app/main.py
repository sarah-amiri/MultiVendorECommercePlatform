from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.api.router import router
from src.app.core.database import close_mongo_connection, init_mongo_connection
from src.app.infrastructure.http_client import init_http_client, close_http_client


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_http_client()
    await init_mongo_connection()
    yield
    await close_mongo_connection()
    await close_http_client()


def create_application() -> FastAPI:
    _app = FastAPI(lifespan=lifespan)
    _app.include_router(router)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = create_application()
