from typing import Dict
from fastapi.exceptions import HTTPException
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)


class BadRequestException(HTTPException):
    def __init__(self, detail: str = 'Bad Request', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_400_BAD_REQUEST, detail, headers)


class UnauthorizedException(HTTPException):
    def __init__(self, detail: str = 'not authenticated', headers: Dict[str, str] | None = None):
        super().__init__(HTTP_401_UNAUTHORIZED, detail, headers)


class InvalidRefreshToken(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None):
        super().__init__(HTTP_401_UNAUTHORIZED, 'expired or invalid refresh token', headers)


class NotFoundException(HTTPException):
    def __init__(self, detail: str = 'Not Found', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_404_NOT_FOUND, detail, headers)


class InternalServerError(HTTPException):
    def __init__(self, detail: str = 'An unexpected error occurred', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_500_INTERNAL_SERVER_ERROR, detail, headers)


class ServiceUnavailableErrorException(HTTPException):
    def __init__(self, detail: str = 'Service Unavailable Error', headers: Dict[str, str] | None = None):
        super().__init__(HTTP_503_SERVICE_UNAVAILABLE, detail, headers)


class UserServiceUnavailableException(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None):
        super().__init__(HTTP_503_SERVICE_UNAVAILABLE, 'user service is not available', headers)
