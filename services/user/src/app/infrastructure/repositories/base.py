from abc import ABC, abstractmethod
from typing import Dict

from src.app.domain import UserEntity
from src.app.infrastructure.models import User


class BaseUserRepository(ABC):
    @abstractmethod
    async def insert(self, user: UserEntity) -> User:
        pass

    @abstractmethod
    async def update(self, instance: User, new_data: Dict) -> User:
        pass

    @abstractmethod
    async def list(self) -> Dict:
        pass

    @abstractmethod
    async def delete(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, _id: int) -> User | None:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    async def change_password(self, user: User, new_password: str) -> User:
        pass
