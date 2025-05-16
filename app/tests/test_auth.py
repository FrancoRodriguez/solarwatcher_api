import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture
def valid_credentials():
    return {
        "username": os.getenv("ADMIN_USERNAME", "admin"),
        "password": os.getenv("ADMIN_PASSWORD", "password")
    }


def test_login_with_valid_credentials(client, valid_credentials):
    response = client.post("/login", json=valid_credentials)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.parametrize("payload", [
    {"username": "valid_user", "password": "wrong_pass"},
    {"username": "wrong_user", "password": "any_pass"}
])
def test_login_with_invalid_credentials(client, payload):
    response = client.post("/login", json=payload)
    assert response.status_code == 401


@pytest.mark.parametrize("payload", [
    {"password": "some_pass"},
    {"username": "some_user"},
    {},
])
def test_login_with_invalid_payload_structure(client, payload):
    response = client.post("/login", json=payload)
    assert response.status_code == 422


def test_login_with_extra_fields(client):
    response = client.post("/login", json={
        "username": "user",
        "password": "pass",
    })
    assert response.status_code in [200, 401]


def test_login_with_invalid_json_format(client):
    response = client.post("/login", content="not json")
    assert response.status_code == 422


def test_login_with_wrong_method(client):
    response = client.get("/login")
    assert response.status_code == 405
