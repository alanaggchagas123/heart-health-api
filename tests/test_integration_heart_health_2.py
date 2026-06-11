from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def _register_and_login(email: str) -> tuple[int, str]:
    user_response = client.post("/register", json={
        "nome": "Heart",
        "sobrenome": "Get",
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

    login_response = client.post("/login", json={"email": email, "senha": "123456"})
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    return user_id, token


def test_get_heart_health_record():
    email = f"heart_get_{int(time.time())}@email.com"
    user_id, token = _register_and_login(email)
    auth = {"Authorization": f"Bearer {token}"}

    create_response = client.post(
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
        headers=auth
    )

    assert create_response.status_code == 201
    record_id = create_response.json()["id"]

    get_response = client.get(f"/heartHealth/{record_id}", headers=auth)

    assert get_response.status_code == 200

    data = get_response.json()
    assert data["id"] == record_id
    assert data["heartRate"] == 70


def test_get_heart_health_record_not_found():
    email = f"heart_404_{int(time.time())}@email.com"
    _, token = _register_and_login(email)

    response = client.get(
        "/heartHealth/999999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Registro não encontrado"


def test_get_heart_health_record_forbidden():
    """Usuário B não pode acessar registro do usuário A."""
    email_a = f"heart_a_{int(time.time())}@email.com"
    email_b = f"heart_b_{int(time.time()) + 1}@email.com"

    user_a_id, token_a = _register_and_login(email_a)
    _, token_b = _register_and_login(email_b)

    # usuário A cria registro
    create_response = client.post(
        "/heartHealth",
        json={
            "userId": user_a_id,
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
        headers={"Authorization": f"Bearer {token_a}"}
    )
    assert create_response.status_code == 201
    record_id = create_response.json()["id"]

    # usuário B tenta acessar — deve ser bloqueado
    response = client.get(
        f"/heartHealth/{record_id}",
        headers={"Authorization": f"Bearer {token_b}"}
    )
    assert response.status_code == 403