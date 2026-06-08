from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


import time

def test_register_user():
    unique_email = f"teste_{int(time.time())}@email.com"

    response = client.post("/register", json={
        "nome": "Teste",
        "sobrenome": "User",
        "email": unique_email,
        "telefone": "21999999999",
        "senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    })

    assert response.status_code == 200
    assert "email" in response.json()


def test_login_user():
    response = client.post("/login", json={
        "email": "teste_unit@email.com",
        "senha": "123456"
    })

    assert response.status_code == 200