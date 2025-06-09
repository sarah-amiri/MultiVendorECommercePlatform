from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.app.core.exceptions import UnauthorizedException
from src.app.core.interfaces import IAuthService
from src.app.infrastructure import get_auth_repo
from src.app.infrastructure.dependencies.cache import get_cache
from src.app.services.tokens import verify_access_token
from src.app.services import AuthService

oauth2_scheme = HTTPBearer(auto_error=False)


def get_auth_service() -> IAuthService:
    return AuthService(get_cache(), get_auth_repo)


async def is_authenticated(
    token: HTTPAuthorizationCredentials | None = Depends(oauth2_scheme),
    cache = Depends(get_cache),
):
    payload = await verify_access_token(token.credentials, cache)
    if payload is None:
        raise UnauthorizedException()
