from abc import ABC, abstractmethod
from typing import Dict


class IAuthRepository(ABC):
    def __init__(self, login_data: Dict):
        self.login_data = login_data

    @abstractmethod
    async def authenticate(self, **kwargs):
        pass
