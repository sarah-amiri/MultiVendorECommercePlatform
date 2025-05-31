from enum import Enum


class UserAccountType(str, Enum):
    CUSTOMER = 'customer'
    CRM = 'crm'
    ADMIN = 'admin'
    REPORTER = 'reporter'
    VENDOR = 'vendor'


class UserAccountStatus(str, Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    INACTIVE = 'inactive'

    @classmethod
    def default(cls):
        return cls.APPROVED
