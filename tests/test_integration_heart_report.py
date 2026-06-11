from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def _register_and_login(email: str) -> tuple[int, str]:
    user_response = client.post("/register", json={
        "nome": "Report",
        "sobrenome": "Test",
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


def test_get_heart_report():
    email = f"report_{int(time.time())}@email.com"
    user_id, token = _register_and_login(email)
    auth = {"Authorization": f"Bearer {token}"}

    client.post(
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

    response = client.get(
        "/heartReport",
        params={"userId": user_id, "startDate": "2000-01-01", "endDate": "2100-01-01"},
        headers=auth
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == user_id
    assert "reportPeriod" in data
    assert "bloodPressureHistory" in data
    assert "heartRateHistory" in data
    assert "bloodOxygenHistory" in data
    assert "bodyWeightHistory" in data
    assert "riskAlert" in data
    assert len(data["bloodPressureHistory"]) > 0


def test_heart_report_invalid_dates():
    email = f"report_dates_{int(time.time())}@email.com"

    user_id, token = _register_and_login(email)

    response = client.get(
        "/heartReport",
        params={
            "userId": user_id,
            "startDate": "2026-12-31",
            "endDate": "2026-01-01"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "A data inicial não pode ser maior que a data final"
    )


def test_heart_report_not_found():
    email = f"report_404_{int(time.time())}@email.com"
    user_id, token = _register_and_login(email)

    response = client.get(
        "/heartReport",
        params={"userId": user_id, "startDate": "2025-01-01", "endDate": "2025-01-02"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404


def test_heart_report_forbidden():
    """Usuário B não pode ver relatório do usuário A."""
    email_a = f"report_a_{int(time.time())}@email.com"
    email_b = f"report_b_{int(time.time()) + 1}@email.com"

    user_a_id, _ = _register_and_login(email_a)
    _, token_b = _register_and_login(email_b)

    response = client.get(
        "/heartReport",
        params={"userId": user_a_id, "startDate": "2000-01-01", "endDate": "2100-01-01"},
        headers={"Authorization": f"Bearer {token_b}"}
    )

    assert response.status_code == 403