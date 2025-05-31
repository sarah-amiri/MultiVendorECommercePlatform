from fastapi import APIRouter
from .routes.health import router as health_router
from .routes.user import router as user_router

router = APIRouter(prefix='/api')
router.include_router(health_router)
router.include_router(user_router)
