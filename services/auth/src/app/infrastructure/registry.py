from .registry_utils import login_repository_registry
from src.app.domain import LoginMethodType


def register_login_method(method: LoginMethodType):
    def wrapper(cls):
        login_repository_registry[method] = cls
        return cls
    return wrapper
