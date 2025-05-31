from dataclasses import asdict, dataclass
from datetime import date, datetime
from .enums import UserAccountStatus, UserAccountType
from .value_objects import EmailAddress, MobileNumber


@dataclass
class UserEntity:
    username: str | None = None
    email: EmailAddress | None = None
    mobile: MobileNumber | None = None
    user_type: UserAccountType | None = None
    status: UserAccountStatus | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None
    created_at: datetime | None = None
    id: int | None = None

    def dict(self):
        _tmp = asdict(self)
        _tmp['email'] = _tmp['email'].value if _tmp['email'] else None
        _tmp['mobile'] = _tmp['mobile'].value if _tmp['mobile'] else None
        return _tmp

    def update_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email.value if self.email else None,
            'mobile': self.mobile.value if self.mobile else None,
            'date_of_birth': self.date_of_birth,
        }
