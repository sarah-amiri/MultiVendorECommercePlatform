from src.app.core.configs import settings


def test_health_api_is_valid(test_client):
    response = test_client.get('/api/health')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json == {
        'name': settings.APP_NAME,
        'description': settings.APP_DESCRIPTION,
        'version': settings.APP_VERSION,
    }
