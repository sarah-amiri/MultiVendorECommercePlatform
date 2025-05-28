from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from .value_objects import Password


@dataclass
class UserCredential:
    id: UUID
    user_id: UUID
    password: Password
    last_password_changed_at: datetime


@dataclass
class Role:
    id: UUID
    name: str


@dataclass
class UserRole:
    id: UUID
    user_id: UUID
    role_id: UUID
