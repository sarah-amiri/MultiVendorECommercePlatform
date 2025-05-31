import bcrypt
import binascii
import hashlib
import secrets
from .base import AbstractPasswordHasher


class BCryptSHA25PasswordHasher(AbstractPasswordHasher):
    algorithm = 'bcrypt_sha256'
    rounds = 12

    def _create_salt(self) -> str:
        return bcrypt.gensalt(self.rounds)

    def make_password(self) -> str:
        _password = self._raw_password.encode()
        _password = binascii.hexlify(hashlib.sha256(_password).digest())
        hashed_password = bcrypt.hashpw(_password, self.salt)
        return '{}${}'.format(self.algorithm, hashed_password.decode('ascii'))

    def verify(self, hashed_password: str) -> bool:
        _hash_of_raw_password = self.make_password()
        return self._compare_passwords(hashed_password, _hash_of_raw_password)

    def _compare_passwords(self, password1: str, password2: str) -> bool:
        return secrets.compare_digest(password1, password2)

    @property
    def salt(self) -> str:
        if self._salt is None:
            self._salt = self._create_salt()
        return self._salt

    @property
    def raw_password(self):
        return self._raw_password
