from typing import Tuple
from .bcrypt import BCryptSHA25PasswordHasher


def get_new_hashed_password(raw_password: str, salt: str) -> str:
    hasher = BCryptSHA25PasswordHasher(raw_password, salt)
    return hasher.make_password()


def make_hash_password(raw_password: str) -> Tuple[str, str]:
    hasher = BCryptSHA25PasswordHasher(raw_password)
    hashed_password = hasher.make_password()
    return hashed_password, hasher.salt.decode()


def verify_password(password: str, user_password: str, user_salt: str) -> bool:
    hasher = BCryptSHA25PasswordHasher(password, user_salt)
    return hasher.verify(user_password)
