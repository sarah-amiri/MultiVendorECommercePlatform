from types import SimpleNamespace
from unittest.mock import AsyncMock
from src.app.domain import UserEntity
from src.app.services import UserService


async def test_get_all_users():
    mock_orm_users = [
        SimpleNamespace(
            id=1,
            username='johndoe1',
            password='password1',
            salt='salt1',
            email='johndoe1@test.com',
            mobile='09909990991',
            first_name='john1',
            last_name='doe1',
            created_at='2025-01-01',
            status='approved',
            user_type='customer',
            date_of_birth='2000-01-01',
        ),
        SimpleNamespace(
            id=2,
            username='johndoe2',
            password='password2',
            salt='salt2',
            email='johndoe2@test.com',
            mobile='09909990992',
            first_name='john2',
            last_name='doe2',
            created_at='2025-01-01',
            status='approved',
            user_type='customer',
            date_of_birth='2000-01-01',
        ),
        SimpleNamespace(
            id=3,
            username='johndoe3',
            password='password3',
            salt='salt3',
            email='johndoe3@test.com',
            mobile='09909990993',
            first_name='john3',
            last_name='doe3',
            created_at='2025-01-01',
            status='approved',
            user_type='customer',
            date_of_birth='2000-01-01',
        )
    ]
    mock_repo = AsyncMock()
    mock_repo.list.return_value = mock_orm_users

    service = UserService(mock_repo)
    result = await service.get_all()

    assert isinstance(result, list)
    assert len(result) == len(mock_orm_users)
    for r in result:
        assert isinstance(r, UserEntity)

    mock_repo.list.assert_awaited_once()
