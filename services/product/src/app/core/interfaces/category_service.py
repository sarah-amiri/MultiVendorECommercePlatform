from abc import ABC, abstractmethod
from bson import ObjectId
from src.app.domain import Category, CategoryCreate


class ICategoryService(ABC):
    @abstractmethod
    async def find_category(self, category_id: ObjectId) -> Category:
        pass

    @abstractmethod
    async def create(self, data: CategoryCreate) -> Category:
        pass

    @abstractmethod
    async def inactive(self, category_id: ObjectId) -> None:
        pass

    @abstractmethod
    async def update(self, category_id: ObjectId, data: CategoryCreate):
        pass
