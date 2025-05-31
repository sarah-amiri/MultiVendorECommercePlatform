from abc import ABC, abstractmethod


class AbstractPasswordHasher(ABC):
    algorithm: str

    def __init__(self, raw_password: str, salt: bytes | None = None):
        self._raw_password = raw_password
        self._salt = salt.encode() if salt else None

    @abstractmethod
    def _create_salt(self) -> str:
        pass

    @abstractmethod
    def make_password(self) -> str:
        pass

    @abstractmethod
    def verify(self, hashed_password: str) -> bool:
        pass

    @abstractmethod
    def _compare_passwords(self, password1: str, password2: str) -> bool:
        pass
