from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_login_user():
    response = client.post("/login", json={
        "email": "teste_unit@email.com",
        "senha": "123456"
    })

    assert response.status_code == 200