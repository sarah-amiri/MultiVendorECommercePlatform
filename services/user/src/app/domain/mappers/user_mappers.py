from src.app.api.schemas import (
    UserCreateModel,
    UserDetailModel, UserUpdateModel,
)
from src.app.domain import UserAccountStatus
from src.app.infrastructure.models import User as UserModel
from src.app.domain.entities import UserEntity
from src.app.domain.value_objects import EmailAddress, MobileNumber


def orm_to_entity(model: UserModel) -> UserEntity:
    return UserEntity(
        id=model.id,
        username=model.username,
        email=EmailAddress(model.email) if model.email else None,
        mobile=MobileNumber(model.mobile) if model.mobile else None,
        user_type=model.user_type,
        status=model.status,
        first_name=model.first_name,
        last_name=model.last_name,
        date_of_birth=model.date_of_birth,
        created_at=model.created_at,
    )


def entity_to_orm(entity: UserEntity) -> UserModel:
    return UserModel(
        username=entity.username,
        email=str(entity.email) if entity.email else None,
        mobile=str(entity.mobile) if entity.mobile else None,
        password=entity.password,
        user_type=entity.user_type,
        status=entity.status,
        first_name=entity.first_name,
        last_name=entity.last_name,
        date_of_birth=entity.date_of_birth,
    )


def entity_to_schema(entity: UserEntity) -> UserDetailModel:
    return UserDetailModel(
        id=entity.id,
        username=entity.username,
        email=str(entity.email) if entity.mobile else None,
        mobile=str(entity.mobile) if entity.mobile else None,
        user_type=entity.user_type,
        status=entity.status,
        first_name=entity.first_name,
        last_name=entity.last_name,
        date_of_birth=entity.date_of_birth,
        created_at=entity.created_at,
    )


def schema_create_to_entity(schema: UserCreateModel) -> UserEntity:
    return UserEntity(
        username=schema.username,
        email=schema.email,
        mobile=schema.mobile,
        password=schema.password,
        user_type=schema.user_type,
        status=UserAccountStatus.default(),
        first_name=schema.first_name,
        last_name=schema.last_name,
        date_of_birth=schema.date_of_birth,
    )


def schema_update_to_entity(schema: UserUpdateModel) -> UserEntity:
    return UserEntity(
        email=EmailAddress(schema.email) if schema.email else None,
        mobile=MobileNumber(schema.mobile) if schema.mobile else None,
        first_name=schema.first_name,
        last_name=schema.last_name,
        date_of_birth=schema.date_of_birth,
    )
