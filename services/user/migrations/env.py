from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from src.app.core.db import Base, DATABASE_URL

config = context.config

target_metadata = Base.metadata
config.set_main_option(
    'sqlalchemy.url',
    DATABASE_URL,
)


def run_migrations_online():
    engine = create_async_engine(
        context.config.get_main_option("sqlalchemy.url")
    )

    async def run_migrations():
        async with engine.connect() as conn:
            await conn.run_sync(do_run_migrations)

    import asyncio
    asyncio.run(run_migrations())

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )
    with context.begin_transaction():
        context.run_migrations()

run_migrations_online()
