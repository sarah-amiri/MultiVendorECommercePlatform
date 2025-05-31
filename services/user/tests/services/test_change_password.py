import pytest
from datetime import datetime
from types import SimpleNamespace
from unittest.mock import AsyncMock
from src.app.core.exceptions import NotAcceptableException, NotFoundException
from src.app.domain import UserEntity
from src.app.services import UserService

user_id = 1
old_password = 'password'
new_password = 'new_password'
password_hash = 'bcrypt_sha256$$2b$12$e.g.Ogv.WNrWHYEc7eXspuSDc6XGFdin2J15ssWzlBInpv4nljuRW'
salt = '$2b$12$e.g.Ogv.WNrWHYEc7eXspu'


async def test_user_not_found():
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = None

    service = UserService(mock_repo)
    with pytest.raises(NotFoundException) as exc:
        await service.change_password(user_id, old_password, new_password)

    assert exc.value.args[0] == 'user not found'
    mock_repo.get_by_id.assert_awaited_once_with(user_id)


async def test_old_password_is_incorrect(monkeypatch):
    orm_mock_user = SimpleNamespace(
        id=1,
        username='johndoe',
        password=password_hash,
        salt=salt,
    )
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = orm_mock_user

    def mock_verify_password(*args):
        return False

    monkeypatch.setattr(
        'src.app.services.user.verify_password',
        mock_verify_password
    )

    service = UserService(mock_repo)
    with pytest.raises(NotAcceptableException) as exc:
        await service.change_password(user_id, old_password, new_password)

    assert exc.value.args[0] == 'user password is incorrect'
    mock_repo.get_by_id.assert_awaited_once_with(user_id)


async def test_change_password(monkeypatch):
    orm_mock_user = SimpleNamespace(
        id=user_id,
        username='johndoe',
        password=password_hash,
        salt=salt,
        email='johndoe@test.com',
        mobile=None,
        first_name='john',
        last_name='doe',
        created_at=datetime.now(),
        status='approved',
        user_type='customer',
        date_of_birth=None,
    )
    mock_repo = AsyncMock()
    mock_repo.get_by_id.return_value = orm_mock_user
    mock_repo.change_password.return_value = orm_mock_user

    def mock_verify_password(*args):
        return True

    monkeypatch.setattr(
        'src.app.services.user.verify_password',
        mock_verify_password
    )

    service = UserService(mock_repo)
    result = await service.change_password(user_id, old_password, new_password)

    assert isinstance(result, UserEntity)
    mock_repo.get_by_id.assert_awaited_once_with(user_id)
    mock_repo.change_password.assert_awaited_once_with(orm_mock_user, new_password)

