from fastapi import APIRouter
from app.schemas.heart_health import HeartHealthCreate
from app.services.heart_health_service import create_record, get_record

router = APIRouter()


@router.post("/heartHealth")
def create_heart_health(data: HeartHealthCreate):
    record = create_record(data)

    return {
        "id": record.id,
        "bloodPressure": {
            "systolic": record.systolic,
            "diastolic": record.diastolic
        },
        "heartRate": record.heart_rate,
        "bloodOxygenLevel": record.blood_oxygen_level,
        "bodyWeight": record.body_weight,
        "symptoms": {
            "shortnessOfBreath": record.shortness_of_breath,
            "chestPain": record.chest_pain,
            "dizziness": record.dizziness
        }
    }


@router.get("/heartHealth/{record_id}")
def get_heart_health(record_id: int):
    record = get_record(record_id)

    if not record:
        return {"error": "Registro não encontrado"}

    return {
        "id": record.id,
        "bloodPressure": {
            "systolic": record.systolic,
            "diastolic": record.diastolic
        },
        "heartRate": record.heart_rate,
        "bloodOxygenLevel": record.blood_oxygen_level,
        "bodyWeight": record.body_weight,
        "symptoms": {
            "shortnessOfBreath": record.shortness_of_breath,
            "chestPain": record.chest_pain,
            "dizziness": record.dizziness
        }
    }