from src.app.core.exceptions import (
    NotAcceptableException,
    NotFoundException,
)
from src.app.core.hashers import verify_password
from src.app.domain import UserEntity
from src.app.domain.mappers import entity_to_orm, orm_to_entity
from src.app.infrastructure.repositories import BaseUserRepository
from src.app.infrastructure.models import User


class UserService:
    def __init__(self, repository: BaseUserRepository):
        self.repo = repository

    async def get_user_by_id(self, user_id: int) -> UserEntity:
        if not (user := await self.repo.get_by_id(user_id)):
            raise NotFoundException('user not found')
        return orm_to_entity(user)

    async def add_user(self, data: UserEntity) -> UserEntity:
        if await self.repo.get_by_username(data.username):
            raise NotAcceptableException('username is taken')
        user = entity_to_orm(data)
        new_user = await self.repo.insert(user)
        return orm_to_entity(new_user)

    async def update(
        self,
        *,
        user: User,
        body: UserEntity,
    ):
        updated_user = await self.repo.update(user, body.update_dict())
        return orm_to_entity(updated_user)

    async def get_all(self):
        users = await self.repo.list()
        return [orm_to_entity(user) for user in users]

    async def delete(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        if user is None:
            raise NotFoundException('user not found')
        return await self.repo.delete(user)

    async def change_password(
        self,
        user_id: int,
        old_password: str,
        new_password: str,
    ):
        user = await self.repo.get_by_id(user_id)
        if user is None:
            raise NotFoundException('user not found')
        if not verify_password(old_password, user.password, user.salt):
            raise NotAcceptableException('user password is incorrect')
        updated_user = await self.repo.change_password(user, new_password)
        return orm_to_entity(updated_user)

    async def authenticate_username_and_password(
        self,
        username: str,
        password: str,
    ):
        user = await self.repo.get_by_username(username)
        if user is None or not verify_password(password, user.password, user.salt):
            raise NotFoundException('username or password is incorrect')
        return {
            'id': user.id,
            'user_type': user.user_type.value,
            'status': user.status.value,
        }
