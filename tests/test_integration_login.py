from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def test_login():
    email = f"login_{int(time.time())}@email.com"

    # cria usuário primeiro
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