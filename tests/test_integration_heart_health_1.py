from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def _register_and_login(email: str) -> tuple[int, str]:
    """Cria usuário e retorna (user_id, access_token)."""
    user_response = client.post("/register", json={
        "nome": "Heart",
        "sobrenome": "Create",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "confirmar_senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "F",
        "pais": "Brasil"
    })
    assert user_response.status_code == 201
    user_id = user_response.json()["id"]

    login_response = client.post("/login", json={
        "email": email,
        "senha": "123456"
    })
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    return user_id, token


def test_create_heart_health_record():
    email = f"heart_create_{int(time.time())}@email.com"
    user_id, token = _register_and_login(email)

    response = client.post(
        "/heartHealth",
        json={
            "userId": user_id,
            "bloodPressure": {"systolic": 120, "diastolic": 80},
            "heartRate": 70,
            "bloodOxygenLevel": 0.97,
            "bodyWeight": 65.4,
            "symptoms": {
                "shortnessOfBreath": False,
                "chestPain": False,
                "dizziness": False
            }
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["heartRate"] == 70
    assert data["bloodPressure"]["systolic"] == 120
    assert data["bloodPressure"]["diastolic"] == 80


def test_create_heart_health_unauthenticated():
    """Sem token deve retornar 401."""

    response = client.post("/heartHealth", json={
        "userId": 1,
        "bloodPressure": {
            "systolic": 120,
            "diastolic": 80
        },
        "heartRate": 70,
        "bloodOxygenLevel": 0.97,
        "bodyWeight": 65.4,
        "symptoms": {
            "shortnessOfBreath": False,
            "chestPain": False,
            "dizziness": False
        }
    })

    assert response.status_code == 401


def test_create_heart_health_user_not_found():
    email = f"heart_notfound_{int(time.time())}@email.com"
    _, token = _register_and_login(email)

    response = client.post(
        "/heartHealth",
        json={
            "userId": 999999,
            "bloodPressure": {"systolic": 120, "diastolic": 80},
            "heartRate": 70,
            "bloodOxygenLevel": 0.97,
            "bodyWeight": 65.4,
            "symptoms": {
                "shortnessOfBreath": False,
                "chestPain": False,
                "dizziness": False
            }
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"