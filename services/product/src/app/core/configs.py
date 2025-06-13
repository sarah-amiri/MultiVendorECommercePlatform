import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME', default='Product')
    APP_VERSION: str = os.getenv('APP_VERSION', default='1.0.0')
    APP_DESCRIPTION: str = os.getenv(
        'APP_DESCRIPTION',
        default='Product microservice for Multi - Vendor E - Commerce Platform app'
    )
    APP_HOST: str = os.getenv('APP_HOST', default='localhost')
    APP_PORT: int = os.getenv('APP_PORT', default=8003)
    APP_PORT_EXPOSE: int = os.getenv('APP_PORT_EXPOSE', default=8003)


class MicroserviceSettings(BaseSettings):
    # USER_API_SCHEMA: str = os.getenv('USER_API_SCHEMA', default='http')
    # USER_API_HOST: str =os.getenv('USER_API_HOST')
    # USER_API_PORT: str = os.getenv('USER_API_PORT')
    #
    # @property
    # def user_api_url(self) -> str:
    #     return f'{self.USER_API_SCHEMA}://{self.USER_API_HOST}:{self.USER_API_PORT}'
    pass


class MongoDBSettings(BaseSettings):
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_NAME: str
    MONGODB_USER: str
    MONGODB_PASS: str

    @property
    def mongodb_url(self) -> str:
        return (f'mongodb://{self.MONGODB_USER}:{self.MONGODB_PASS}'
                f'@{self.MONGODB_HOST}:{self.MONGODB_PORT}'
                f'/{self.MONGODB_NAME}'
                f'?authSource=admin')


class Settings(
    AppSettings,
    MicroserviceSettings,
    MongoDBSettings,
):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
