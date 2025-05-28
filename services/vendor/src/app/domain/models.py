from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from .enums import VendorStatus


@dataclass
class Vendor:
    id: UUID
    user_id: UUID
    status: VendorStatus
    ecode: str
    created_at: datetime
