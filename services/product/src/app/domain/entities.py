from dataclasses import dataclass
from datetime import datetime
from typing import List
from .enums import Color, Currency
from .value_objects import Price


@dataclass
class Category:
    id: str | None
    slug: str
    name: str
    description: str | None = None
    is_active: bool = True


@dataclass
class CategoryCreate:
    name: str
    description: str | None


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: int
    price: Price
    currency: Currency
    is_active: bool
    created_at: datetime
    variants: List["ProductVariant"]


@dataclass
class ProductVariant:
    id: int
    product_id: int
    subname: str | None = None
    size: int | None = None
    color: Color | None = None


@dataclass
class VendorProduct:
    product_id: int
    vendor_id: int
