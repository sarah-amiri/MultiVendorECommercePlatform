from httpx import ConnectError, HTTPStatusError, Response
from typing import Dict
from starlette import status

from ..http_client import get_http_client
from src.app.core.exceptions import (
    InternalServerError,
    UserServiceUnavailableException,
)


class MakeRequest:
    def __init__(self, method: str, url: str, **kwargs):
        self._method = method
        self._url = url
        self._kwargs = kwargs
        self._content = None
        self._response = None

    async def request(self):
        http_client = get_http_client()
        self._response = await http_client.request(self._method, self._url, **self._kwargs)
        self._content = self._response.json()
        self._response.raise_for_status()

    @property
    def content(self) -> Dict | None:
        return self._content

    @property
    def response(self) -> Response | None:
        return self._response


class MakeRequestMixin:
    @classmethod
    async def _make_request(cls, method: str, url: str, **kwargs):
        try:
            make_request = MakeRequest(method, url, **kwargs)
            await make_request.request()
        except ConnectError as err:
            cls.handle_connect_error()
        except HTTPStatusError as err:
            response = make_request.response
            if response.status_code == status.HTTP_404_NOT_FOUND:
                cls.handle_404_error(make_request.content['detail'])
            cls.handle_http_status_error()
        except Exception as err:
            cls.handle_exception()
        return make_request

    @classmethod
    def handle_connect_error(cls):
        raise UserServiceUnavailableException()

    @classmethod
    def handle_404_error(cls, detail: str):
        pass

    @classmethod
    def handle_http_status_error(cls):
        raise UserServiceUnavailableException()

    @classmethod
    def handle_exception(cls):
        raise InternalServerError()
