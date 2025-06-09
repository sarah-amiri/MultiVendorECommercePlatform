import pytest
from starlette import status
from unittest.mock import AsyncMock, patch
from src.app.core.exceptions import (
    NotFoundException,
    InternalServerError,
    ServiceUnavailableErrorException,
    UnauthorizedException,
)
from src.app.domain import (
    AuthenticatedUserEntity,
    TokenEntity,
    UsernamePasswordLoginMethod,
)
from src.app.services.auth import AuthService

error_401 = status.HTTP_401_UNAUTHORIZED
error_404 = status.HTTP_404_NOT_FOUND
error_500 = status.HTTP_500_INTERNAL_SERVER_ERROR
error_503 = status.HTTP_503_SERVICE_UNAVAILABLE
incorrect_username_or_password = 'username or password is incorrect'
internal_server = 'An unexpected error occurred'
invalid_refresh_token = 'expired or invalid refresh token'
not_authenticated_error = 'not authenticated'
unavailable_service = 'user service is not available'


class FakeAuthenticatedUser:
    sub: int = 1
    data: dict = {'user_type': 'customer', 'status': 'approved'}


@pytest.mark.asyncio
async def test_success_authentication(auth_service_setup):
    service, mock_repo = auth_service_setup
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='password')
    fake_user_data = {'id': 1, 'user_type': 'customer', 'status': 'approved'}
    mock_repo.authenticate.return_value = fake_user_data
    result = await service.authenticate(fake_login_data)

    assert isinstance(result, AuthenticatedUserEntity)
    assert result.user_id == 1
    assert result.user_type == "customer"
    assert result.user_status == "approved"


@pytest.mark.asyncio
async def test_authenticate_failed_with_wrong_credentials(auth_service_setup):
    service, mock_repo = auth_service_setup
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    mock_repo.authenticate.side_effect = NotFoundException(incorrect_username_or_password)
    with pytest.raises(NotFoundException) as exc_info:
        _ = await service.authenticate(fake_login_data)

    assert exc_info.value.status_code == error_404
    assert incorrect_username_or_password in str(exc_info.value)


@pytest.mark.asyncio
async def test_authenticate_failed_when_user_service_not_working(auth_service_setup):
    service, mock_repo = auth_service_setup
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    mock_repo.authenticate.side_effect = ServiceUnavailableErrorException(unavailable_service)
    with pytest.raises(ServiceUnavailableErrorException) as exc_info:
        _ = await service.authenticate(fake_login_data)

    assert exc_info.value.status_code == error_503
    assert unavailable_service in str(exc_info.value)


@pytest.mark.asyncio
async def test_authenticate_failed_when_error_occurred(auth_service_setup):
    service, mock_repo = auth_service_setup
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    mock_repo.authenticate.side_effect = InternalServerError(internal_server)
    with pytest.raises(InternalServerError) as exc_info:
        _ = await service.authenticate(fake_login_data)

    assert exc_info.value.status_code == error_500
    assert internal_server in str(exc_info.value)


@pytest.mark.asyncio
async def test_login_success(auth_service_setup):
    service, _ = auth_service_setup
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    fake_authenticated_user = FakeAuthenticatedUser()
    with patch.object(AuthService, 'authenticate', new_callable=AsyncMock) as mock_auth:
        mock_auth.return_value = fake_authenticated_user
        result = await service.login(fake_login_data)
        mock_auth.assert_awaited_once_with(fake_login_data)

    assert isinstance(result, TokenEntity)
    assert hasattr(result, 'access_token')
    assert hasattr(result, 'refresh_token')
    assert hasattr(result, 'token_type')
    assert isinstance(result.access_token, str)
    assert isinstance(result.refresh_token, str)
    assert isinstance(result.token_type, str)


@pytest.mark.asyncio
async def test_login_failed_with_wrong_credentials(auth_service_setup):
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    with patch.object(AuthService, 'authenticate', new_callable=AsyncMock) as mock_auth:
        mock_auth.side_effect = NotFoundException(incorrect_username_or_password)
        with pytest.raises(NotFoundException) as exc_info:
            service, _ = auth_service_setup
            _ = await service.login(fake_login_data)

        assert exc_info.value.status_code == error_404
        assert incorrect_username_or_password in str(exc_info.value)


@pytest.mark.asyncio
async def test_login_failed_when_user_service_is_not_available(auth_service_setup):
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    with patch.object(AuthService, 'authenticate', new_callable=AsyncMock) as mock_auth:
        mock_auth.side_effect = ServiceUnavailableErrorException(unavailable_service)
        with pytest.raises(ServiceUnavailableErrorException) as exc_info:
            service, _ = auth_service_setup
            _ = await service.login(fake_login_data)

            assert exc_info.value.status_code == error_503
            assert unavailable_service in str(exc_info.value)


@pytest.mark.asyncio
async def test_login_failed_when_error_occurred(auth_service_setup):
    fake_login_data = UsernamePasswordLoginMethod(username='test', password='pass')
    with patch.object(AuthService, 'authenticate', new_callable=AsyncMock) as mock_auth:
        mock_auth.side_effect = InternalServerError(internal_server)
        with pytest.raises(InternalServerError) as exc_info:
            service, _ = auth_service_setup
            _ = await service.login(fake_login_data)

            assert exc_info.value.status_code == error_500
            assert internal_server in str(exc_info.value)


@pytest.mark.asyncio
async def test_refresh_token_success(auth_service_setup):
    fake_payload = {'sub': '1', 'user_type': 'customer', 'status': 'approved'}
    with patch('src.app.services.auth.verify_refresh_token', return_value=fake_payload):
        service, _ = auth_service_setup
        result = await service.refresh_token('test-refresh-token')
        assert isinstance(result, TokenEntity)


@pytest.mark.asyncio
async def test_failed_refresh_token(auth_service_setup):
    with patch('src.app.services.auth.verify_refresh_token', return_value=None):
        with pytest.raises(UnauthorizedException) as exc:
            service, _ = auth_service_setup
            _ = await service.refresh_token('invalid-refresh-token')

        assert exc.value.status_code == error_401
        assert invalid_refresh_token in str(exc.value)


@pytest.mark.parametrize('token', [None, 'invalid-token', 'Token valid-token'])
@pytest.mark.asyncio
async def test_logout_failed_when_token_is_invalid(auth_service_setup, token):
    with pytest.raises(UnauthorizedException) as exc:
        service, _ = auth_service_setup
        _ = await service.logout(token)

    assert not_authenticated_error in str(exc.value)
    assert exc.value.status_code == error_401


@pytest.mark.asyncio
async def test_logout_failed_when_refresh_token_is_not_valid(auth_service_setup):
    with patch('src.app.services.auth.invalidate_token', return_value=None):
        with pytest.raises(UnauthorizedException) as exc:
            token = 'Bearer invalid-token'
            service, _ = auth_service_setup
            _ = await service.logout(token)

        assert not_authenticated_error in str(exc.value)
        assert exc.value.status_code == error_401


@pytest.mark.asyncio
async def test_logout_succeeded(auth_service_setup):
    with patch('src.app.services.auth.invalidate_token', return_value=1):
        token = 'Bearer valid-token'
        service, _ = auth_service_setup
        result = await service.logout(token)
        assert result is None
