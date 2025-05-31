import pytest
from types import SimpleNamespace
from unittest.mock import AsyncMock
from src.app.core.exceptions import NotFoundException
from src.app.domain import UserEntity
from src.app.services import UserService


async def test_user_not_found():
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = None

    with pytest.raises(NotFoundException) as exc:
        service = UserService(mock_repo)
        await service.get_user_by_id(1)

    assert exc.value.args[0] == 'user not found'


async def test_get_user_by_id():
    orm_mock_user = SimpleNamespace(
        id=1,
        username='johndoe',
        password='password',
        salt='salt',
        email='johndoe@test.com',
        mobile='09909990999',
        first_name='john',
        last_name='doe',
        created_at='2025-01-01',
        status='approved',
        user_type='customer',
        date_of_birth='2000-01-01',
    )
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = orm_mock_user

    service = UserService(mock_repo)
    result = await service.get_user_by_id(1)

    assert isinstance(result, UserEntity)
    assert result.id == orm_mock_user.id
    assert result.username == orm_mock_user.username
    assert result.email.value == orm_mock_user.email
    assert result.mobile.value == orm_mock_user.mobile
    assert result.first_name == orm_mock_user.first_name
    assert result.last_name == orm_mock_user.last_name
    assert result.date_of_birth == orm_mock_user.date_of_birth
    assert result.status == orm_mock_user.status
    assert result.user_type == orm_mock_user.user_type
