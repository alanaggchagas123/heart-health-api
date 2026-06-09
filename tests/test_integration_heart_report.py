from fastapi.testclient import TestClient
from main import app

import time
from datetime import date

client = TestClient(app)


def test_get_heart_report():

    email = f"report_{int(time.time())}@email.com"

    user_response = client.post(
        "/register",
        json={
            "nome": "Report",
            "sobrenome": "Test",
            "email": email,
            "telefone": "21999999999",
            "senha": "123456",
            "data_nascimento": "2000-01-01",
            "sexo": "F",
            "pais": "Brasil"
        }
    )

    user_id = user_response.json()["id"]

    client.post(
        "/heartHealth",
        json={
            "userId": user_id,
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
        }
    )

    response = client.get(
        "/heartReport",
        params={
            "userId": user_id,
            "startDate": "2000-01-01",
            "endDate": "2100-01-01"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert "bloodPressureHistory" in data
    assert "heartRateHistory" in data
    assert "bloodOxygenHistory" in data
    assert "bodyWeightHistory" in data