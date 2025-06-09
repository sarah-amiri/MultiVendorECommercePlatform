from datetime import date, datetime
from pydantic import BaseModel, Field
from src.app.domain import UserAccountStatus, UserAccountType


class UserDetailModel(BaseModel):
    id: int
    username: str
    email: str | None
    mobile: str | None
    user_type: UserAccountType
    status: UserAccountStatus
    first_name: str | None
    last_name: str | None
    birthdate: date | None = Field(..., alias='date_of_birth')
    created_at: datetime


class UserAuthenticatedModel(BaseModel):
    id: int
    user_type: str
    status: str
    