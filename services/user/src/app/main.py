from fastapi import FastAPI
from src.app.api.router import router


def create_application() -> FastAPI:
    _app = FastAPI()
    _app.include_router(router)
    return _app

app = create_application()
