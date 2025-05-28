from enum import Enum


class VendorStatus(str, Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    INACTIVE = 'inactive'
    REJECTED = 'rejected'
