import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME')
    APP_VERSION: str = os.getenv('APP_VERSION')
    APP_DESCRIPTION: str = os.getenv('APP_DESCRIPTION')
    APP_HOST: str = os.getenv('APP_HOST', default='localhost')
    APP_PORT: int = os.getenv('APP_PORT', default=8001)
    APP_PORT_EXPOSE: int = os.getenv('APP_PORT_EXPOSE', default=8001)


class DatabaseSettings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_PORT_EXPOSE: int = os.getenv('DB_PORT_EXPOSE')
    DB_SYNC_PREFIX: str = 'postgresql://'
    DB_ASYNC_PREFIX: str = 'postgresql+asyncpg://'

    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # DB_URI: str = f'{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class Settings(
    AppSettings,
    DatabaseSettings,
):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
