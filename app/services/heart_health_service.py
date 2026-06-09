from app.database import SessionLocal
from app.models.heart_health import HeartHealthRecord


def create_record(data):
    db = SessionLocal()

    new_record = HeartHealthRecord(
        user_id=data.userId,

        systolic=data.bloodPressure.systolic,
        diastolic=data.bloodPressure.diastolic,

        heart_rate=data.heartRate,
        blood_oxygen_level=data.bloodOxygenLevel,
        body_weight=data.bodyWeight,

        shortness_of_breath=data.symptoms.shortnessOfBreath,
        chest_pain=data.symptoms.chestPain,
        dizziness=data.symptoms.dizziness
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    db.close()

    return new_record


def get_record(record_id):
    db = SessionLocal()

    record = (
        db.query(HeartHealthRecord)
        .filter(HeartHealthRecord.id == record_id)
        .first()
    )

    db.close()

    return record