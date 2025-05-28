from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID
from .enums import UserAccountStatus, UserAccountType
from .value_objects import EmailAddress, MobileNumber


@dataclass
class UserAccount:
    id: UUID
    username: str | None
    email: EmailAddress | None
    mobile: MobileNumber | None
    user_type: UserAccountType
    status: UserAccountStatus
    created_at: datetime
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None
