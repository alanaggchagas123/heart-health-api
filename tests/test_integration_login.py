from fastapi.testclient import TestClient
from jose import jwt
from main import app
import time
import os

client = TestClient(app)


def test_login():
    email = f"login_{int(time.time())}@email.com"

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
    token = data["access_token"]

    payload = jwt.decode(
        token,
        os.getenv("SECRET_KEY"),
        algorithms=["HS256"]
    )

    assert payload["sub"] == email