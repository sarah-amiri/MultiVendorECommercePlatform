from abc import ABC, abstractmethod
from src.app.domain import LoginMethod, TokenEntity


class IAuthService(ABC):
    @abstractmethod
    async def login(cls, data: LoginMethod) -> TokenEntity:
        pass

    @abstractmethod
    async def authenticate(cls, data: LoginMethod):
        pass

    @abstractmethod
    async def refresh_token(cls, token: str) -> TokenEntity:
        pass

    @abstractmethod
    async def logout(cls, token: str | None) -> None:
        pass
