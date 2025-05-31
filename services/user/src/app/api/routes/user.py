from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.api.dependencies import get_user_service
from src.app.core.db import get_db
from src.app.domain.mappers import (
    entity_to_schema,
    schema_create_to_entity,
    schema_update_to_entity,
)
from src.app.api.schemas import (
    UserChangePasswordModel,
    UserCreateModel,
    UserDetailModel,
    UserUpdateModel,
)
from src.app.services import UserService

router = APIRouter(prefix='/users', tags=['user'])


@router.get(
    '/{user_id}',
    response_model=UserDetailModel,
    responses={200: {}, 404: {}},
)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    entity = await service.get_user_by_id(user_id)
    return entity_to_schema(entity)


@router.get('', response_model=List[UserDetailModel])
async def get_users_list(
    service: UserService = Depends(get_user_service)
):
    results = await service.get_all()
    return [entity_to_schema(result) for result in results]


@router.post(
    '',
    status_code=201,
    response_model=UserDetailModel,
    responses={406: {}},
)
async def create_user(
    body: UserCreateModel,
    service: UserService = Depends(get_user_service)
):
    entity = schema_create_to_entity(body)
    return await service.add_user(entity)


@router.put(
    '/{user_id}',
    response_model=UserDetailModel,
    responses={404: {}},
)
async def update_user(
    user_id: int,
    body: UserUpdateModel,
    service: UserService = Depends(get_user_service),
    session: AsyncSession = Depends(get_db),
):
    entity = schema_update_to_entity(body)
    return await service.update(user_id=user_id, body=entity, session=session)


@router.put(
    '/{user_id}/password',
    response_model=UserDetailModel,
    responses={404: {}, 406: {}},
)
async def change_user_password(
    user_id: int,
    body: UserChangePasswordModel,
    service: UserService = Depends(get_user_service),
):
    entity = await service.change_password(user_id, body.old_password, body.new_password)
    return entity_to_schema(entity)


@router.delete('/{user_id}', status_code=204, responses={404: {}})
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    return await service.delete(user_id=user_id, session=session)
