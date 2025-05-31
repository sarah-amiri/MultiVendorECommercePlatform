from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.app.core.configs import settings

DB_URI = f'{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
DATABASE_URL = f'{settings.DB_ASYNC_PREFIX}{DB_URI}'

async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=False,
    pool_size=30,
    max_overflow=20,
    pool_timeout=30,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)


async def get_db():
    session: AsyncSession = SessionLocal()
    try:
        yield session
    finally:
        await session.close()

class Base(DeclarativeBase):
    pass
