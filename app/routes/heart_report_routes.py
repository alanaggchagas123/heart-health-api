from datetime import date

from fastapi import APIRouter, HTTPException, Depends, status

from app.schemas.api_responses import HEART_REPORT_RESPONSES
from app.services.heart_report_service import generate_heart_report
from app.utils.security import get_current_user

router = APIRouter()


@router.get(
    "/heartReport",
    status_code=status.HTTP_200_OK,
    responses=HEART_REPORT_RESPONSES
)
def get_heart_report(
    userId: int,
    startDate: date,
    endDate: date,
    current_user: dict = Depends(get_current_user)  # Fix #1: exige JWT
):
    # Fix #4: usuário só pode ver o próprio relatório
    if userId != current_user["id"]:
        raise HTTPException(
            status_code=403,
            detail="Sem permissão para acessar este relatório"
        )

    if startDate > endDate:
        raise HTTPException(
            status_code=400,
            detail="A data inicial não pode ser maior que a data final"
        )

    return generate_heart_report(
        user_id=userId,
        start_date=startDate,
        end_date=endDate
    )
