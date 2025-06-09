from fastapi import APIRouter, Cookie, Depends, Request, Response
from ..dependencies import get_auth_service, is_authenticated
from ..schemas import LoginUsernamePasswordSchema, TokenSchema
from src.app.core.interfaces import IAuthService
from src.app.utils.mappers import (
    map_entity_to_schema_for_login_token,
    map_schema_to_entity_for_login,
)

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    '/login',
    response_model=TokenSchema,
    responses={401: {}, 422: {}, 500: {}, 503: {}},
)
async def login(
    body: LoginUsernamePasswordSchema,
    response: Response,
    service: IAuthService = Depends(get_auth_service),
):
    login_data = map_schema_to_entity_for_login(body)
    token_data = await service.login(login_data)
    response.set_cookie(
        key='refresh_token',
        value=token_data.refresh_token,
        httponly=True,
        samesite='lax',
        secure=True,
    )
    return map_entity_to_schema_for_login_token(token_data)


@router.post(
    '/refresh',
    response_model=TokenSchema,
    responses={401: {}, 422: {}},
)
async def refresh_the_token(
    response: Response,
    refresh_token: str = Cookie(...),
    service: IAuthService = Depends(get_auth_service),
):
    token_data = await service.refresh_token(refresh_token)
    response.set_cookie(
        key='refresh_token',
        value=token_data.refresh_token,
        httponly=True,
        samesite='lax',
        secure=True,
    )
    return map_entity_to_schema_for_login_token(token_data)


@router.post(
    '/logout',
    status_code=200,
    responses={401: {}},
    dependencies=[Depends(is_authenticated)],
)
async def logout(
    request: Request,
    response: Response,
    service: IAuthService = Depends(get_auth_service),
):
    await service.logout(request.headers.get('Authorization'))
    response.delete_cookie('refresh_token')
