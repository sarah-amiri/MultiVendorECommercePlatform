from dataclasses import dataclass


@dataclass
class TokenEntity:
    access_token: str
    refresh_token: str
    token_type: str = 'Bearer'


@dataclass
class AuthenticatedUserEntity:
    user_id: int
    user_type: str
    user_status: str

    @property
    def sub(self):
        return self.user_id

    @property
    def data(self):
        return {
            'user_type': self.user_type,
            'status': self.user_status,
        }
