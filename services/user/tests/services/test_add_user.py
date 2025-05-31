import pytest
from types import SimpleNamespace
from unittest.mock import AsyncMock

from src.app.core.exceptions import NotAcceptableException
from src.app.domain import UserAccountStatus, UserAccountType, UserEntity
from src.app.services import UserService


async def test_add_user():
    mock_orm_user = SimpleNamespace(
        id=1,
        username='johndoe',
        email=None,
        mobile=None,
        status=UserAccountStatus.APPROVED.value,
        user_type=UserAccountType.CUSTOMER.value,
        first_name=None,
        last_name=None,
        date_of_birth=None,
        created_at=None,
    )
    mock_repo = AsyncMock()
    mock_repo.get_by_username.return_value = None
    mock_repo.insert.return_value = mock_orm_user

    service = UserService(mock_repo)
    entity = UserEntity(
        username='johndoe',
        email=None,
        mobile=None,
        status=UserAccountStatus.default(),
        user_type=UserAccountType.CUSTOMER,
        password='password',
    )

    result = await service.add_user(entity)

    mock_repo.get_by_username.assert_awaited_once_with('johndoe')
    mock_repo.insert.assert_awaited_once()

    assert isinstance(result, UserEntity)
    assert result.username == 'johndoe'


async def test_add_duplicate_username_not_allowed():
    mock_duplicate_user = SimpleNamespace(
        id=1,
        username='johndoe',
        email=None,
        mobile=None,
    )
    mock_repo = AsyncMock()
    mock_repo.get_by_username.return_value = mock_duplicate_user

    service = UserService(mock_repo)
    entity = UserEntity(
        username='johndoe',
        email=None,
        mobile=None,
        status=UserAccountStatus.default(),
        user_type=UserAccountType.CUSTOMER,
        password='password',
    )

    with pytest.raises(NotAcceptableException) as exc:
        await service.add_user(entity)

    assert exc.value.args[0] == 'username is taken'
    mock_repo.get_by_username.assert_awaited_once_with('johndoe')
    mock_repo.add_user.assert_not_awaited()
