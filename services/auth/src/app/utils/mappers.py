from src.app.api import LoginUsernamePasswordSchema, TokenSchema
from src.app.domain import TokenEntity, UsernamePasswordLoginMethod


def map_schema_to_entity_for_login(schema: LoginUsernamePasswordSchema):
    return UsernamePasswordLoginMethod(
        username=schema.username,
        password=schema.password
    )


def map_entity_to_schema_for_login_token(entity: TokenEntity):
    return TokenSchema(
        access_token=entity.access_token,
        token_type=entity.token_type,
    )
