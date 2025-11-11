import pytest
from fastapi.testclient import TestClient
from server import app, AppMode

client = TestClient(app)

def test_ping_returns_pong(monkeypatch):
    app.state.mode = AppMode.DEV
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"

    app.state.mode = AppMode.PROD
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"

def test_visits_dev_returns_minus_one(monkeypatch):
    app.state.mode = AppMode.DEV
    response = client.get("/visits")
    assert response.status_code == 200
    assert response.text == "-1"
