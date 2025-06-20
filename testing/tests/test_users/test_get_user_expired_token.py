from auth.auth_handler import create_access_token
from datetime import timedelta
from fastapi.testclient import TestClient
from main import app
from testing.classes.user import User

import time
import pytest

client = TestClient(app)


@pytest.mark.expired_token
@pytest.mark.user
def test_expired_token():
    user = User()
    user.create_user()
    token = create_access_token(user.user_id, expires_delta=timedelta(seconds=1))  # expires_delta in seconds

    # Wait for token to expire
    time.sleep(2)

    # Try to access a protected endpoint
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me", headers=headers)
    expected_status_code = 401
    assert response.status_code == expected_status_code
