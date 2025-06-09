from abc import ABC, abstractmethod
from typing import Any


class ICache(ABC):
    @abstractmethod
    async def set(self, key: str, value: Any, expire: int | None = None) -> None:
        pass

    @abstractmethod
    async def get(self, key: str) -> Any:
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        pass
