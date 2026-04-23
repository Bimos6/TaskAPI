from fastapi.testclient import TestClient
from main import app


def test_full_flow():
    client = TestClient(app)

    # Пустой список
    resp = client.get("/tasks/")
    assert resp.status_code == 200
    assert resp.json() == []

    # Первая задача
    resp = client.post("/tasks/", json={"title": "Молоко", "status": "new"})
    assert resp.status_code == 201
    assert resp.json()["id"] == 1

    # Вторая задача
    resp = client.post("/tasks/", json={"title": "Хлеб", "status": "done"})
    assert resp.status_code == 201
    assert resp.json()["id"] == 2

    # Список
    resp = client.get("/tasks/")
    assert len(resp.json()) == 2

    # По ID
    resp = client.get("/tasks/1")
    assert resp.json()["title"] == "Молоко"

    # 404
    resp = client.get("/tasks/999")
    assert resp.status_code == 404


def test_validation():
    client = TestClient(app)

    # Пустой title
    resp = client.post("/tasks/", json={"title": "", "status": "new"})
    assert resp.status_code == 422

    # Плохой статус
    resp = client.post("/tasks/", json={"title": "Test", "status": "wtf"})
    assert resp.status_code == 422

    # Нет title
    resp = client.post("/tasks/", json={"status": "new"})
    assert resp.status_code == 422