from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_heart_health_record():
    response = client.post("/heartHealth", json={
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

    assert data["bloodPressure"]["systolic"] == 120
    assert data["bloodPressure"]["diastolic"] == 80
    assert data["heartRate"] == 70