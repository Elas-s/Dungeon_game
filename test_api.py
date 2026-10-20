import pytest
from fastapi.testclient import TestClient
from api import app
from scores import create_table

@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    create_table()
    return TestClient(app)

def test_stats_on_empty_database(client):
    response = client.get("/stats")
    assert response.status_code == 200
    assert response.json()["games"] == 0


def test_post_score_saves(client):
    response = client.post("/scores", json={"name": "Alex", "gold": 99, "survived": True})
    assert response.status_code == 201
    assert client.get("/scores").json() == [{"name": "Alex", "gold": 99}]


def test_post_score_with_wrong_gold(client):
    response = client.post("/scores", json={"name": "Alex", "gold": "full", "survived": True})
    assert response.status_code == 422