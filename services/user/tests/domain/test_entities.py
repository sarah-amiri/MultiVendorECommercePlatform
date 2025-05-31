import pytest
from datetime import date
from src.app.domain.enums import UserAccountType, UserAccountStatus
from src.app.domain.entities import UserEntity
from src.app.domain.value_objects import EmailAddress, MobileNumber


def test_create_user():
    user = UserEntity(
        username='test',
        email=EmailAddress('test@test.com'),
        mobile=MobileNumber('09332641071'),
        password='password',
        user_type=UserAccountType.CUSTOMER,
        status=UserAccountStatus.APPROVED,
        first_name='test name',
        last_name='test family',
        date_of_birth=date(2000, 1, 1),
    )
    assert user
    assert user.username == 'test'
    assert user.email == EmailAddress('test@test.com')
    assert user.mobile == MobileNumber('09332641071')
    assert user.first_name == 'test name'
    assert user.last_name == 'test family'
    assert user.user_type == UserAccountType.CUSTOMER
    assert user.status == UserAccountStatus.APPROVED
    assert user.date_of_birth == date(2000, 1, 1)


def test_create_with_null_values():
    user = UserEntity(
        username='test',
        email='test@test.com',
        mobile='09332641071',
        password='password',
        user_type=UserAccountType.CUSTOMER,
        status=UserAccountStatus.APPROVED,
    )
    assert user
    assert user.username == 'test'
    assert user.email == 'test@test.com'
    assert user.mobile == '09332641071'
    assert user.first_name is None
    assert user.last_name is None
    assert user.user_type == UserAccountType.CUSTOMER
    assert user.status == UserAccountStatus.APPROVED
    assert user.date_of_birth is None


def test_email_pattern_is_incorrect():
    with pytest.raises(ValueError) as exc:
        _ = UserEntity(
            username='test',
            email=EmailAddress('test'),
            mobile='09332641071',
            password='password',
            user_type=UserAccountType.CUSTOMER,
            status=UserAccountStatus.APPROVED,
        )
    assert exc.value.args[0] == 'Incorrect email address'


def test_mobile_pattern_is_incorrect():
    with pytest.raises(ValueError) as exc:
        _ = UserEntity(
            username='test',
            email=EmailAddress('test@test.com'),
            mobile=MobileNumber('9332641071'),
            password='password',
            user_type=UserAccountType.CUSTOMER,
            status=UserAccountStatus.APPROVED,
        )
    assert exc.value.args[0] == 'Incorrect mobile number'
