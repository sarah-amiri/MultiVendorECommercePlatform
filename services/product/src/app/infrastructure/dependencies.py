from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from src.app.core.database import get_database
from src.app.infrastructure.repositories import CategoryRepo
from src.app.services.categories import CategoryService, ICategoryService


def get_async_db():
    return get_database()


def get_category_service(db: AsyncIOMotorDatabase = Depends(get_async_db)) -> ICategoryService:
    repo = CategoryRepo(db)
    return CategoryService(repo)
