from fastapi import APIRouter
from datetime import date
from app.services.heart_report_service import generate_heart_report

router = APIRouter()

@router.get("/heartReport")
def get_heart_report(
    userId: int,
    startDate: date,
    endDate: date
):

    return generate_heart_report(
        user_id=userId,
        start_date=startDate,
        end_date=endDate
    )