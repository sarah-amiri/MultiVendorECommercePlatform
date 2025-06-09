import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME')
    APP_VERSION: str = os.getenv('APP_VERSION')
    APP_DESCRIPTION: str = os.getenv('APP_DESCRIPTION')
    APP_HOST: str = os.getenv('APP_HOST', default='localhost')
    APP_PORT: int = os.getenv('APP_PORT', default=8001)
    APP_PORT_EXPOSE: int = os.getenv('APP_PORT_EXPOSE', default=8001)


class MicroserviceSettings(BaseSettings):
    USER_API_SCHEMA: str = os.getenv('USER_API_SCHEMA', default='http')
    USER_API_HOST: str =os.getenv('USER_API_HOST')
    USER_API_PORT: str = os.getenv('USER_API_PORT')

    @property
    def user_api_url(self) -> str:
        return f'{self.USER_API_SCHEMA}://{self.USER_API_HOST}:{self.USER_API_PORT}'


class AuthTokenSettings(BaseSettings):
    ACCESS_TOKEN_SECRET_KEY: str = os.getenv('ACCESS_TOKEN_SECRET_KEY')
    REFRESH_TOKEN_SECRET_KEY: str = os.getenv('REFRESH_TOKEN_SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60 # 7 days
    ACCESS_TOKEN_CACHE_PREFIX: str = 'AccessToken_'
    REFRESH_TOKEN_CACHE_PREFIX: str = 'RefreshToken_'


class RedisSettings(BaseSettings):
    REDIS_HOST: str = os.getenv('REDIS_HOST')
    REDIS_PORT: int = os.getenv('REDIS_PORT')
    REDIS_DB: int = os.getenv('REDIS_DB', default=0)

    @property
    def redis_url(self) -> str:
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}'


class Settings(
    AppSettings,
    AuthTokenSettings,
    MicroserviceSettings,
    RedisSettings,
):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
