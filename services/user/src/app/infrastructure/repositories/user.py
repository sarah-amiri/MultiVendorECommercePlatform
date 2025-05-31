from typing import Dict

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseUserRepository
from src.app.core.hashers import get_new_hashed_password, make_hash_password
from src.app.infrastructure.models import User


class UserRepository(BaseUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, user: User) -> User | None:
        if not await self.get_by_username(user.username):
            hashed_password, salt = make_hash_password(user.password)
            user.password = hashed_password
            user.salt = salt
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)
            return user
        return None
    
    async def update(self, instance: User, new_data: Dict) -> User:
        for attr, val in new_data.items():
            setattr(instance, attr, val)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def list(self) -> Dict:
        stmt = select(User)
        return (await self.session.execute(stmt)).scalars().all()

    async def delete(self, user: User) -> None:
        user.delete()
        await self.session.commit()

    async def get_by_id(self, _id: int) -> User | None:
        stmt = select(User).filter_by(id=_id)
        return (await self.session.execute(stmt)).scalar_one_or_none()

    async def get_by_username(self, username: str) -> User | None:
        stmt = select(User).filter_by(username=username)
        return (await self.session.execute(stmt)).scalar_one_or_none()

    async def change_password(self, user: User, new_password: str) -> User:
        user.password = get_new_hashed_password(new_password, user.salt)
        await self.session.commit()
        await self.session.refresh(user)
        return user
