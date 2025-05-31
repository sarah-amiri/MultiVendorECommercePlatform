from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock
from src.app.domain.entities import EmailAddress, MobileNumber, UserEntity
from src.app.services import UserService


async def test_update_user():
    entity_to_update = UserEntity(
        email=EmailAddress('johndoe@test.com'),
        mobile=MobileNumber('09909990999'),
        first_name='john',
        last_name='doe',
        date_of_birth='2000-01-01',
    )
    orm_mock_user_before_update = SimpleNamespace(
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
    orm_mock_user_after_update = SimpleNamespace(
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
    mock_session = AsyncMock()

    mock_repo.get_by_id.return_value = orm_mock_user_before_update
    mock_repo.update.return_value = orm_mock_user_after_update

    service = UserService(mock_repo)
    result = await service.update(user_id=1, session=mock_session, body=entity_to_update)

    assert isinstance(result, UserEntity)
    assert result.id == orm_mock_user_after_update.id
    assert result.username == orm_mock_user_after_update.username
    assert result.email == entity_to_update.email
    assert result.mobile == entity_to_update.mobile
    assert result.first_name == entity_to_update.first_name
    assert result.last_name == entity_to_update.last_name
    assert result.date_of_birth == entity_to_update.date_of_birth
    assert result.status == orm_mock_user_after_update.status
    assert result.user_type == orm_mock_user_after_update.user_type
    # mock_repo.get_by_id.assert_awaited_once_with(1)
    mock_repo.update.assert_awaited_once()
