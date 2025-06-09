from src.app.core.interfaces import ICache
from src.app.infrastructure.cache import redis_cache


def get_cache() -> ICache:
    return redis_cache
