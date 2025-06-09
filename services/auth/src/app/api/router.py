from fastapi import APIRouter
from .routes.auth import router as auth_router
from .routes.health import router as health_router

router = APIRouter(prefix='/api')
router.include_router(health_router)
router.include_router(auth_router)
