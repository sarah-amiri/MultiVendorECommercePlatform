from typing import Dict
from fastapi.exceptions import HTTPException
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)


class BadRequestException(HTTPException):
    def __init__(self, detail: str = 'Bad Request', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_400_BAD_REQUEST, detail, headers)


class NotFoundException(HTTPException):
    def __init__(self, detail: str = 'Not Found', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_404_NOT_FOUND, detail, headers)


class NotAcceptableException(HTTPException):
    def __init__(self, detail: str = 'Not Acceptable', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_406_NOT_ACCEPTABLE, detail, headers)


class InternalServerError(HTTPException):
    def __init__(self, detail: str = 'An unexpected error occurred', headers: Dict[str, str] | None = None) -> None:
        super().__init__(HTTP_500_INTERNAL_SERVER_ERROR, detail, headers)


class ServiceUnavailableErrorException(HTTPException):
    def __init__(self, detail: str = 'Service Unavailable Error', headers: Dict[str, str] | None = None):
        super().__init__(HTTP_503_SERVICE_UNAVAILABLE, detail, headers)
