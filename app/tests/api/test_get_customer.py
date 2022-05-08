import uuid
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"msg": "Hello World"}

def test_statement(client):
    client.post("/deposit/{250}/account/{id}")
    response = client.get("/statement/{id}")
    assert response.status_code == 200