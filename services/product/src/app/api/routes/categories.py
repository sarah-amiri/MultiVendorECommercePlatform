from fastapi import APIRouter, Depends
from src.app.api.schemas import CategoryCreateSchema, CategoryDetailSchema
from src.app.core.interfaces import ICategoryService
from src.app.infrastructure.dependencies import get_category_service
from src.app.utils.mappers import map_entity_to_schema, map_schema_to_create_domain

router = APIRouter(prefix='/categories', tags=['category'])

@router.get(
    '/{category_id}',
    summary='get category',
    response_model=CategoryDetailSchema,
    responses={400:{}, 404: {}},
)
async def find_category(
    category_id: str,
    category_service: ICategoryService = Depends(get_category_service),
):
    category_entity = await category_service.find_category(_id=category_id)
    return map_entity_to_schema(category_entity)


@router.post(
    '',
    summary='create category',
    response_model=CategoryDetailSchema,
    status_code=201,
    responses={400: {}, 422: {}},
)
async def create_category(
    body: CategoryCreateSchema,
    category_service: ICategoryService = Depends(get_category_service),
):
    entity = map_schema_to_create_domain(body)
    category_entity = await category_service.create(entity)
    return map_entity_to_schema(category_entity)


@router.put(
    '/{category_id}',
    summary='update category',
    status_code=200,
    responses={400: {}, 404: {}, 406: {}, 422: {}},
)
async def update_category(
        category_id: str,
        body: CategoryCreateSchema,
        category_service: ICategoryService = Depends(get_category_service),
):
    entity = map_schema_to_create_domain(body)
    category_entity = await category_service.update(_id=category_id, data=entity)
    return map_entity_to_schema(category_entity)


@router.delete(
    '/{category_id}',
    summary='inactive category',
    status_code=204,
    responses={400: {}, 404: {}, 422:{}},
)
async def inactive_category(
        category_id: str,
        category_service: ICategoryService = Depends(get_category_service),
):
    return await category_service.inactive(_id=category_id)
