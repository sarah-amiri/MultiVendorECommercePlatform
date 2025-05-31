import pytest
from types import SimpleNamespace
from unittest.mock import AsyncMock
from src.app.core.exceptions import NotFoundException
from src.app.services import UserService


async def test_delete_with_user_not_found():
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = None

    with pytest.raises(NotFoundException) as exc:
        service = UserService(mock_repo)
        await service.delete(1)

    assert exc.value.args[0] == 'user not found'


async def test_delete_user():
    orm_mock_user = SimpleNamespace(
        id=1,
        username='johndoe',
        password='password',
        salt='salt',
        email=None,
        mobile=None,
        first_name=None,
        last_name=None,
        created_at='2025-01-01',
        status='approved',
        user_type='customer',
        date_of_birth=None,
    )
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = orm_mock_user
    mock_repo.delete.return_value = None

    service = UserService(mock_repo)
    result = await service.delete(1)
    # original_func = service.delete.__closure__[0].cell_contents
    # result = await original_func(service, user=orm_mock_user)
    assert result is None
