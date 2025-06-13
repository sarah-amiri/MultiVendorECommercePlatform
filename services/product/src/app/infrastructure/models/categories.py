from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field, model_validator
from slugify import slugify


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, info):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class CategoryBaseModel(BaseModel):
    name: str
    description: str | None = None


class CategoryCreateModel(CategoryBaseModel):
    is_active: bool = True
    slug: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)

    @model_validator(mode='after')
    def generate_slug(self) -> 'CategoryCreateModel':
        if self.slug is None:
            self.slug = slugify(self.name)
        return self


class CategoryModel(CategoryBaseModel):
    is_active: bool = True
    slug: str
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {PyObjectId: str}


class CategoryUpdateModel(CategoryBaseModel):
    pass
