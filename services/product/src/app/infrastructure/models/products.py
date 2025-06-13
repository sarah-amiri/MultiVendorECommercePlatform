from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field, model_validator
from typing import Dict, List

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


class ProductVariantModel(BaseModel):
    color: str | None
    size: str | None
    sku: str
    price: float
    currency: str
    is_active: bool = True


class ProductBaseModel(BaseModel):
    name: str
    categories: List[str]
    variants: List[ProductVariantModel]
    vendor_id: int
    attributes: Dict | None = Field(default_factory=dict)
    description: str | None = None
    is_active: bool = True


class ProductCreateModel(ProductBaseModel):
    slug: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)

    @model_validator(mode='after')
    def generate_slug(self) -> 'ProductCreateModel':
        if self.slug is None:
            self.slug = slugify(self.name)
        return self


class ProductUpdateModel(ProductBaseModel):
    updated_at: datetime = Field(default_factory=datetime.now)


class ProductModel(ProductBaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    slug: str

    class config:
        json_encoders = {PyObjectId: str}
        allow_population_by_field_name = True
