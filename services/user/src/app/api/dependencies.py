from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.core.db import get_db
from src.app.infrastructure.repositories import UserRepository
from src.app.services import UserService


def get_user_service(session: AsyncSession = Depends(get_db)) -> UserService:
    repo = UserRepository(session)
    return UserService(repo)
