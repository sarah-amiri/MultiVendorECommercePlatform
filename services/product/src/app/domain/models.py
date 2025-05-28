from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID
from .enums import Color
from .value_objects import Price


@dataclass
class Category:
    id: UUID
    name: str
    parent_id: UUID | None


@dataclass
class Product:
    id: UUID
    name: str
    category_id: UUID
    price: Price
    is_active: bool
    created_at: datetime
    variants: List["ProductVariant"]


@dataclass
class ProductVariant:
    id: UUID
    product_id: UUID
    subname: str
    size: int | None
    color: Color | None


@dataclass
class VendorProduct:
    product_id: UUID
    vendor_id: UUID
