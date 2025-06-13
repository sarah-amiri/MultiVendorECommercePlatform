from abc import ABC, abstractmethod
from bson import ObjectId
from typing import List
from src.app.infrastructure.models import (
    CategoryModel, CategoryCreateModel, CategoryUpdateModel,
)


class ICategoryRepo(ABC):
    @abstractmethod
    async def find_category(self, category_id: ObjectId) -> CategoryModel:
        pass

    @abstractmethod
    async def get_categories(self, **params) -> List[CategoryModel]:
        pass

    @abstractmethod
    async def create_category(self, data: CategoryCreateModel) -> CategoryModel:
        pass

    @abstractmethod
    async def update_category(self, category_id: ObjectId, data: CategoryUpdateModel) -> CategoryModel:
        pass

    @abstractmethod
    async def inactive_category(self, category_id: ObjectId) -> None:
        pass

    @abstractmethod
    async def find_by_slug(self, slug: str) -> CategoryModel | None:
        pass
