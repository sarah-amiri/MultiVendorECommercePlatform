import uuid
from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Any, Dict

from src.app.core.configs import settings
from src.app.core.interfaces import ICache

ALGORITHM = 'HS256'
access_expire = settings.ACCESS_TOKEN_EXPIRE_MINUTES
refresh_expire = settings.REFRESH_TOKEN_EXPIRE_MINUTES
at_prefix = settings.ACCESS_TOKEN_CACHE_PREFIX
rt_prefix = settings.REFRESH_TOKEN_CACHE_PREFIX


def get_time(expire: timedelta | None = None):
    if expire:
        _time = datetime.now() + expire
    else:
        _time = datetime.now()
    return int(_time.timestamp())


async def create_access_token(sub: Any, data: Dict, cache: ICache) -> str:
    to_encode = {
        'sub': str(sub),
        'exp': get_time(timedelta(minutes=access_expire)),
        'iat': get_time(),
        'jti': str(uuid.uuid4()),
        'user_type': data['user_type'],
        'status': data['status'],
    }
    await cache.set(f'{at_prefix}{sub}', to_encode['jti'], expire=access_expire * 60)
    return jwt.encode(to_encode, settings.ACCESS_TOKEN_SECRET_KEY, algorithm=ALGORITHM)


async def create_refresh_token(sub: Any, data: Dict, cache: ICache) -> str:
    to_encode = {
        'sub': str(sub),
        'exp': get_time(timedelta(minutes=refresh_expire)),
        'iat': get_time(),
        'jti': str(uuid.uuid4()),
        'user_type': data['user_type'],
        'status': data['status'],
    }
    await cache.set(f'{rt_prefix}{sub}', to_encode['jti'], expire=refresh_expire * 60)
    return jwt.encode(to_encode, settings.REFRESH_TOKEN_SECRET_KEY, algorithm=ALGORITHM)


async def verify_access_token(access_token: str, cache: ICache) -> bool:
    try:
        payload = jwt.decode(access_token, settings.ACCESS_TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        cached_access_token = await cache.get(f'{at_prefix}{payload["sub"]}')
        if cached_access_token != payload['jti']:
            return None
        if payload.get('exp') < datetime.now().timestamp():
            return None
        return payload
    except JWTError as err:
        return None


async def verify_refresh_token(refresh_token: str, cache: ICache) -> bool:
    try:
        payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        cached_refresh_token = await cache.get(f'{rt_prefix}{payload["sub"]}')
        if cached_refresh_token != payload['jti']:
            return None
        if payload.get('exp') < datetime.now().timestamp():
            return None
        return payload
    except JWTError as err:
        return None

async def invalidate_token(access_token: str, cache: ICache) -> None:
    payload = await verify_access_token(access_token, cache)
    if payload is None:
        return None
    sub = payload['sub']
    await cache.delete(f'{rt_prefix}{sub}')
    await cache.delete(f'{at_prefix}{sub}')
    return sub
