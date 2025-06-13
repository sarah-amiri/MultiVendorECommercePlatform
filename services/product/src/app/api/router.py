from fastapi import APIRouter
from .routes.categories import router as category_router
from .routes.health import router as health_router

router = APIRouter(prefix='/api')
router.include_router(health_router)
router.include_router(category_router)
