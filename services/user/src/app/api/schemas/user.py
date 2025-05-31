from datetime import date
from pydantic import BaseModel, field_validator
from src.app.domain import EmailAddress, MobileNumber, UserAccountType


class UserCreateModel(BaseModel):
    username: str
    email: str | None
    mobile: str | None
    password: str
    user_type: UserAccountType
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v is not None:
            EmailAddress(v)
        return v

    @field_validator('mobile')
    @classmethod
    def validate_mobile(cls, v):
        if v is not None:
            MobileNumber(v)
        return v


class UserUpdateModel(BaseModel):
    email: str | None
    mobile: str | None
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None


class UserChangePasswordModel(BaseModel):
    old_password: str
    new_password: str
