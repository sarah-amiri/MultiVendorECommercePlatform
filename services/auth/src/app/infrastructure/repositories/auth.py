from typing import Dict
from src.app.core.interfaces import IAuthRepository
from src.app.infrastructure.apis import UserAPI
from src.app.infrastructure.registry import register_login_method
from src.app.domain import LoginMethodType


@register_login_method(LoginMethodType.USERNAME_PASSWORD)
class UserPasswordAuthRepository(IAuthRepository):
    async def authenticate(self, **kwargs) -> Dict:
        response = await UserAPI.login(self.login_data)
        return response.content
