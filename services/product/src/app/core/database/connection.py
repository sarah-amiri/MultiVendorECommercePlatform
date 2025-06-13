from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.app.core.configs import settings

client: AsyncIOMotorClient | None = None
database: AsyncIOMotorDatabase | None = None


async def init_mongo_connection():
    global client, database
    client = AsyncIOMotorClient(settings.mongodb_url)
    database = client[settings.MONGODB_NAME]


async def close_mongo_connection():
    global client
    if client:
        client.close()


def get_database() -> AsyncIOMotorDatabase:
    global database
    return database
