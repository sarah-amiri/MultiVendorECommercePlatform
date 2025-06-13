from bson import ObjectId

from src.app.core.exceptions import BadRequestException
from src.app.core.interfaces import ICategoryRepo, ICategoryService
from src.app.domain import Category, CategoryCreate
from src.app.utils.decorators import check_id_is_valid_object_id
from src.app.utils.mappers import map_model_to_entity, map_entity_to_create_model


class CategoryService(ICategoryService):
    def __init__(self, repository: ICategoryRepo):
        self._repo = repository

    @check_id_is_valid_object_id
    async def find_category(self, category_id: ObjectId) -> Category:
        category = await self._repo.find_category(category_id)
        return map_model_to_entity(category)

    async def create(self, data: CategoryCreate) -> Category:
        model_data = map_entity_to_create_model(data)
        if await self._repo.find_by_slug(model_data.slug):
            raise BadRequestException('category is already exists')
        new_category = await self._repo.create_category(model_data)
        return map_model_to_entity(new_category)

    @check_id_is_valid_object_id
    async def inactive(self, category_id: ObjectId) -> None:
        return await self._repo.inactive_category(category_id)

    @check_id_is_valid_object_id
    async def update(self, category_id: ObjectId, data: CategoryCreate):
        model_data = map_entity_to_create_model(data)
        updated_category = await self._repo.update_category(category_id, model_data)
        return map_model_to_entity(updated_category)
