from pydantic import BaseModel


class ProductBaseModel(BaseModel):
    name: str
    description: str
    category_id: int
    price: int
    currency: str


class ProductCreateModel(ProductBaseModel):
    pass


class ProductUpdateModel(BaseModel):
    id: str
    name: str
    description: str
    category_id: int
    price: int
    currency: str
