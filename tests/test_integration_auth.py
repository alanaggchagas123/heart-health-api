from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def test_register_user():
    email = f"auth_{uuid.uuid4()}@email.com"

    response = client.post("/register", json={
        "nome": "Auth",
        "sobrenome": "User",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    })

    assert response.status_code == 200

    data = response.json()
    assert "email" in data or "user" in data


def test_login_user():
    email = f"login_{uuid.uuid4()}@email.com"

    # cria usuário primeiro (necessário para integração real)
    client.post("/register", json={
        "nome": "Login",
        "sobrenome": "Test",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    })

    # tenta login
    response = client.post("/login", json={
        "email": email,
        "senha": "123456"
    })

    assert response.status_code == 200

    data = response.json()
    assert "message" in data