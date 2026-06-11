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
        "confirmar_senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    })

    assert response.status_code == 201

    data = response.json()
    assert data["email"] == email
    assert data["nome"] == "Auth"


def test_register_password_mismatch():
    email = f"auth_{uuid.uuid4()}@email.com"

    response = client.post("/register", json={
        "nome": "Auth",
        "sobrenome": "User",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "confirmar_senha": "999999",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    })

    assert response.status_code == 422


def test_register_duplicate_email():
    email = f"auth_{uuid.uuid4()}@email.com"

    payload = {
        "nome": "Auth",
        "sobrenome": "User",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "confirmar_senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    }

    client.post("/register", json=payload)
    response = client.post("/register", json=payload)

    assert response.status_code == 409


def test_login_user():
    email = f"login_{uuid.uuid4()}@email.com"

    client.post("/register", json={
        "nome": "Login",
        "sobrenome": "Test",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "confirmar_senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "M",
        "pais": "Brasil"
    })

    response = client.post("/login", json={
        "email": email,
        "senha": "123456"
    })

    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "access_token" in data
    assert data["token_type"] == "bearer"