from fastapi import APIRouter
from src.app.core.configs import settings

router = APIRouter(prefix='/health', tags=['health'])

@router.get('/health')
async def health_check():
    return {
        'name': settings.APP_NAME,
        'description': settings.APP_DESCRIPTION,
        'version': settings.APP_VERSION,
    }
