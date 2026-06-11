from fastapi import HTTPException

from app.database import SessionLocal
from app.models.heart_health import HeartHealthRecord
from app.models.user import User


def create_record(data):

    db = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(User.id == data.userId)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado"
            )

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

        return new_record

    finally:
        db.close()


def get_record(record_id):

    db = SessionLocal()

    try:

        return (
            db.query(HeartHealthRecord)
            .filter(HeartHealthRecord.id == record_id)
            .first()
        )

    finally:
        db.close()