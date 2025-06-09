import redis.asyncio
from typing import Any
from src.app.core.configs import settings
from src.app.core.interfaces import ICache


class RedisCache(ICache):
    _client: None

    async def connect(self):
        connection_pool = redis.asyncio.ConnectionPool.from_url(settings.redis_url)
        self._client = redis.asyncio.Redis.from_pool(connection_pool)

    async def disconnect(self):
        await self._client.close()

    async def set(self, key: str, value: Any, expire: int | None = None) -> None:
        await self._client.set(key, value, ex=expire)

    async def get(self, key: str) -> Any:
        value = await self._client.get(key)
        return value.decode() if value else None

    async def delete(self, key: str) -> None:
        await self._client.delete(key)


redis_cache = RedisCache()
