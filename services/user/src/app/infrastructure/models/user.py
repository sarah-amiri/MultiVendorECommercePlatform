from datetime import datetime
from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Enum,
    func,
    Integer,
    String,
)
from src.app.core.db import Base
from src.app.domain import UserAccountStatus, UserAccountType


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(16), nullable=False, unique=True, index=True)
    email = Column(String(50), nullable=True)
    mobile = Column(String(11), nullable=True)
    password = Column(String(250), nullable=False)
    salt = Column(String(29), nullable=False)
    user_type = Column(Enum(UserAccountType), nullable=False)
    status = Column(Enum(UserAccountStatus), nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    date_of_birth = Column('birthdate', Date, nullable=True)
    created_at = Column(
        'created_time',
        DateTime,
        default=datetime.now(),
        server_default=func.now(),
        nullable=False,
    )
    updated_at = Column(
        'modified_time',
        DateTime,
        default=None,
        onupdate=datetime.now(),
        nullable=True,
    )

    def delete(self):
        self.status = UserAccountStatus.INACTIVE

    @classmethod
    def default_status(cls):
        return UserAccountStatus.APPROVED
