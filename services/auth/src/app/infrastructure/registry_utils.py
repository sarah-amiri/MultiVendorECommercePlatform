from typing import Dict
from src.app.core.interfaces import IAuthRepository
from src.app.domain import LoginMethodType

login_repository_registry: Dict[LoginMethodType, IAuthRepository] = {}
