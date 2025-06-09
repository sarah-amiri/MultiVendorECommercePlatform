from typing import Dict
from .registry_utils import login_repository_registry
from src.app.core.interfaces import IAuthRepository
from src.app.domain import LoginMethodType


class LoginRepositoryFactory:
    @classmethod
    def get_auth_repository(
        cls,
        login_type: LoginMethodType,
        login_data: Dict
    ) -> IAuthRepository:
        repo_cls = login_repository_registry.get(login_type)
        if repo_cls is None:
            raise NotImplementedError(f'No repository implement for {login_type}')
        return repo_cls(login_data)


def get_auth_repo(login_type: LoginMethodType, login_data: Dict) -> IAuthRepository:
    return LoginRepositoryFactory.get_auth_repository(login_type, login_data)
