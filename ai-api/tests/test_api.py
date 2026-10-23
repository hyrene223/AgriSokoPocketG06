
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["groupCode"] == "G06"


def test_model_info_endpoint():
    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()
    assert data["groupCode"] == "G06"
    assert data["method"] == "TF-IDF with cosine similarity"
    assert data["memberCount"] == 6


def test_search_known_member():
    response = client.post(
        "/search",
        json={"query": "Who is Nsabimana?"},
    )

    assert response.status_code == 200

    data = response.json()
    assert data["matched"] is True
    assert data["member"]["fullName"] == "Nsabimana Irene"


def test_search_unrelated_query():
    response = client.post(
        "/search",
        json={"query": "Who is an astronaut from Mars?"},
    )

    assert response.status_code == 200
    assert response.json()["matched"] is False


def test_search_rejects_empty_query():
    response = client.post(
        "/search",
        json={"query": "   "},
    )

    assert response.status_code == 422


def test_search_rejects_missing_query():
    response = client.post("/search", json={})

    assert response.status_code == 422


def test_search_rejects_too_long_query():
    response = client.post(
        "/search",
        json={"query": "a" * 501},
    )

    assert response.status_code == 422
