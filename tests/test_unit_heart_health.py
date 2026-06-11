from app.schemas.heart_health import HeartHealthCreate


def test_heart_health_schema():
    record = HeartHealthCreate(
        userId=1,
        bloodPressure={
            "systolic": 120,
            "diastolic": 80
        },
        heartRate=70,
        bloodOxygenLevel=0.97,
        bodyWeight=65.4,
        symptoms={
            "shortnessOfBreath": False,
            "chestPain": False,
            "dizziness": False
        }
    )

    assert record.userId == 1

    assert record.bloodPressure.systolic == 120
    assert record.bloodPressure.diastolic == 80

    assert record.heartRate == 70
    assert record.bloodOxygenLevel == 0.97
    assert record.bodyWeight == 65.4

    assert record.symptoms.shortnessOfBreath is False
    assert record.symptoms.chestPain is False
    assert record.symptoms.dizziness is False