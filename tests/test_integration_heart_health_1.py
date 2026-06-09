from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def test_create_heart_health_record():

    email = f"heart_create_{int(time.time())}@email.com"

    user_response = client.post("/register", json={
        "nome": "Heart",
        "sobrenome": "Create",
        "email": email,
        "telefone": "21999999999",
        "senha": "123456",
        "data_nascimento": "2000-01-01",
        "sexo": "F",
        "pais": "Brasil"
    })

    user_id = user_response.json()["id"]

    response = client.post("/heartHealth", json={
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
    })

    assert response.status_code == 200

    data = response.json()

    assert data["heartRate"] == 70
    assert data["bloodPressure"]["systolic"] == 120