from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict
from .enums import LoginMethodType


class LoginMethod(ABC):
    @abstractmethod
    def to_dict(self) -> Dict:
        pass

    @property
    def method(self) -> str:
        return ''


@dataclass
class UsernamePasswordLoginMethod(LoginMethod):
    username: str
    password: str

    def __post_init__(self):
        assert self.username, 'Username is required'
        assert self.password, 'Password is required'

    def to_dict(self) -> Dict:
        return {
            'username': self.username,
            'password': self.password,
        }

    @property
    def method(self):
        return LoginMethodType.USERNAME_PASSWORD
