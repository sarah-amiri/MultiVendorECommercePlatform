from pydantic import BaseModel


class LoginUsernamePasswordSchema(BaseModel):
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
