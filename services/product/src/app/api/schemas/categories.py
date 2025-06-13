from pydantic import BaseModel, Field


class CategoryBaseSchema(BaseModel):
    name: str
    description: str | None = None


class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategoryDetailSchema(CategoryBaseSchema):
    slug: str
    id: str
    is_active: bool = True


class CategoryUpdateSchema(CategoryBaseSchema):
    pass


class CategoryListParams(BaseModel):
    pass
