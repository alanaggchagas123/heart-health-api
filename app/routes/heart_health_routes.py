from fastapi import APIRouter, HTTPException, Depends, status

from app.schemas.heart_health import HeartHealthCreate
from app.schemas.api_responses import HEART_HEALTH_RESPONSES
from app.services.heart_health_service import create_record, get_record
from app.utils.security import get_current_user

router = APIRouter()


@router.post(
    "/heartHealth",
    status_code=status.HTTP_201_CREATED,
    responses=HEART_HEALTH_RESPONSES
)
def create_heart_health(
    data: HeartHealthCreate,
    current_user: dict = Depends(get_current_user)  # Fix #1: exige JWT
):
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


@router.get(
    "/heartHealth/{record_id}",
    responses=HEART_HEALTH_RESPONSES
)
def get_heart_health(
    record_id: int,
    current_user: dict = Depends(get_current_user)  # Fix #1: exige JWT
):
    record = get_record(record_id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Registro não encontrado"
        )

    # Fix #4: verifica se o registro pertence ao usuário autenticado
    if record.user_id != current_user["id"]:
        raise HTTPException(
            status_code=403,
            detail="Sem permissão para acessar este registro"
        )

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