from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_heart_health_record():
    create_response = client.post("/heartHealth", json={
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

    record_id = create_response.json()["id"]

    get_response = client.get(f"/heartHealth/{record_id}")

    assert get_response.status_code == 200

    data = get_response.json()

    assert data["id"] == record_id
    assert data["heartRate"] == 70