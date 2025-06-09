from typing import Dict
from .base import MakeRequestMixin
from src.app.core.configs import settings
from src.app.core.exceptions import UnauthorizedException


class UserAPI(MakeRequestMixin):
    BASE_URL: str = settings.user_api_url

    @classmethod
    async def login(cls, payload: Dict):
        url = cls.BASE_URL + '/api/users/authenticate'
        return await cls._make_request('post', url, json=payload)

    @classmethod
    def handle_404_error(cls, detail: str):
        raise UnauthorizedException(detail)
