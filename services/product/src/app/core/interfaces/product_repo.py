from abc import ABC, abstractmethod
from typing import Dict, List
from src.app.infrastructure.models import ProductModel


class IProductRepository(ABC):
    @abstractmethod
    async def find_product(self, product_id: str) -> ProductModel:
        pass

    @abstractmethod
    async def get_products(self, **params) -> List[ProductModel]:
        pass

    @abstractmethod
    async def create_product(self, data: Dict) -> ProductModel:
        pass

    @abstractmethod
    async def update_product(self, product_id: str, data: Dict) -> ProductModel:
        pass

    @abstractmethod
    async def delete_product(self, product_id: str) -> None:
        pass
