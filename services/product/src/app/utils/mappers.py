from src.app.api.schemas import CategoryDetailSchema, CategoryCreateSchema
from src.app.domain import Category, CategoryCreate
from src.app.infrastructure.models import CategoryModel, CategoryCreateModel


def map_model_to_entity(model: CategoryModel) -> Category:
    return Category(
        id=str(model.id),
        slug=model.slug,
        name=model.name,
        description=model.description,
        is_active=model.is_active,
    )


def map_entity_to_schema(entity: Category) -> CategoryDetailSchema:
    return CategoryDetailSchema(
        id=entity.id,
        slug=entity.slug,
        name=entity.name,
        description=entity.description,
        is_active=entity.is_active,
    )


def map_entity_to_create_model(entity: CategoryCreate) -> CategoryCreateModel:
    return CategoryCreateModel(
        name=entity.name,
        description=entity.description,
    )


def map_schema_to_create_domain(schema: CategoryCreateSchema) -> CategoryCreate:
    return CategoryCreate(
        name=schema.name,
        description=schema.description,
    )
