from typing import Callable, Dict

from src.app.core.exceptions import UnauthorizedException, InvalidRefreshToken
from src.app.core.interfaces import IAuthRepository, IAuthService, ICache
from src.app.services.tokens import (
    create_access_token,
    create_refresh_token,
    invalidate_token,
    verify_refresh_token,
)
from src.app.domain import (
    AuthenticatedUserEntity,
    LoginMethod,
    LoginMethodType,
    TokenEntity,
)


class AuthService(IAuthService):
    def __init__(self, cache: ICache, repo: Callable[[LoginMethodType, Dict], IAuthRepository]):
        self._cache = cache
        self._repo_getter = repo

    async def authenticate(self, data: LoginMethod):
        repo = self._repo_getter(data.method, data.to_dict())
        user = await repo.authenticate()
        return AuthenticatedUserEntity(
            user_id=user['id'],
            user_type=user['user_type'],
            user_status=user['status'],
        )

    async def login(self, data: LoginMethod) -> TokenEntity:
        user = await self.authenticate(data)
        return TokenEntity(
            access_token=await create_access_token(user.sub, user.data, self._cache),
            refresh_token=await create_refresh_token(user.sub, user.data, self._cache),
        )

    async def refresh_token(self, token: str) -> TokenEntity:
        payload = await verify_refresh_token(token, self._cache)
        if payload is None:
            raise InvalidRefreshToken()
        sub = payload.pop('sub')
        new_access_token = await create_access_token(sub, payload, self._cache)
        new_refresh_token = await create_refresh_token(sub, payload, self._cache)
        return TokenEntity(access_token=new_access_token, refresh_token=new_refresh_token)

    async def logout(self, token: str | None) -> None:
        if token is None:
            raise UnauthorizedException()
        token_parts = token.split(' ')
        if len(token_parts) != 2 or token_parts[0].lower() != 'bearer':
            raise UnauthorizedException()
        if await invalidate_token(token_parts[1], self._cache) is None:
            raise UnauthorizedException()
