from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

class MockUserAPIResponse:
    content = {
        'id': 2,
        'user_type': 'customer',
        'status': 'approved'
    }


def test_success_login(mock_redis, mock_user_api):
    mock_user_api.return_value = MockUserAPIResponse
    mock_redis.set.return_value = None

    response = client.post('/api/auth/login', json={
        'username': 'test',
        'password': '1234',
    })
    assert response.status_code == 200
    mock_redis.set.assert_called_once()
