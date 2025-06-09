from httpx import AsyncClient

http_client: AsyncClient | None = None


async def init_http_client():
    global http_client
    if http_client is None:
        http_client = AsyncClient()


async def close_http_client():
    global http_client
    if http_client is not None:
        await http_client.aclose()


def get_http_client():
    return http_client
