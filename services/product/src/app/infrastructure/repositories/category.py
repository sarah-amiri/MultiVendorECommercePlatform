from bson import ObjectId
from datetime import datetime
from typing import Dict, List

from motor.motor_asyncio import AsyncIOMotorDatabase

from src.app.core.exceptions import NotAcceptableException, NotFoundException
from src.app.core.interfaces import ICategoryRepo
from src.app.infrastructure.models import (
    CategoryModel, CategoryCreateModel, CategoryUpdateModel,
)


class CategoryRepo(ICategoryRepo):
    collection_name: str = 'categories'

    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db[self.collection_name]

    async def find_category(self, category_id: ObjectId) -> CategoryModel:
        category = await self.collection.find_one({'_id': category_id})
        if not category:
            raise NotFoundException('product not found')
        return CategoryModel(**category)

    async def find_by_slug(self, slug: str) -> CategoryModel | None:
        category = await self.collection.find_one({'slug': slug})
        return CategoryModel(**category) if category else None

    async def get_categories(self, **params) -> List[CategoryModel]:
        pass

    async def create_category(self, data: CategoryCreateModel) -> CategoryModel:
        data_dict = data.model_dump()
        result = await self.collection.insert_one(data_dict)
        return await self.find_category(result.inserted_id)

    async def update_category(self, category_id: ObjectId, data: CategoryUpdateModel) -> CategoryModel:
        instance = await self.find_category(category_id)

        update_data = data.model_dump(exclude_unset=True)
        has_changes = any(
            getattr(instance, field) != value
            for field, value in update_data.items()
        )
        if not has_changes:
            raise NotAcceptableException('no changes have been detected')

        _ = await self.collection.update_one(
            {"_id": category_id},
            {"$set": {**update_data, "updated_at": datetime.now()}},
        )
        return await self.find_category(category_id)

    async def inactive_category(self, category_id: ObjectId) -> None:
        result = await self.collection.update_one(
            {"_id": category_id},
            {"$set": {"is_active": False}},
        )
        if result.modified_count == 0:
            raise NotFoundException('category not found or already inactive')
