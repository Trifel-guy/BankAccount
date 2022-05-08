import uuid
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_post_deposit(client):
    response = client.post("/deposit/{200}/account/{id}")
    assert response.status_code == 200
    assert response.json() == 1

def test_post_withdrawal(client):
    response = client.post("/withdrawal/{500}/account/{id}")
    assert response.status_code == 200
    assert response.json() == 1

def test_post_account_statement(client):
    response = client.post("/account/statement/{25tr}")
    assert response.status_code == 200
    assert response.json() == 1
