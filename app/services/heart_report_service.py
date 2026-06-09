from app.database import SessionLocal
from app.models.heart_health import HeartHealthRecord

from datetime import date


def generate_heart_report(user_id: int, start_date: date, end_date: date):

    db = SessionLocal()

    records = (
        db.query(HeartHealthRecord)
        .filter(HeartHealthRecord.user_id == user_id)
        .filter(HeartHealthRecord.created_at >= start_date)
        .filter(HeartHealthRecord.created_at <= end_date)
        .all()
    )

    db.close()

    blood_pressure_history = []

    heart_rate_history = []

    blood_oxygen_history = []

    body_weight_history = []

    risk_alert = "nenhum risco identificado"

    for record in records:

        record_date = record.created_at.date()

        blood_pressure_history.append({
            "systolic": record.systolic,
            "diastolic": record.diastolic,
            "date": record_date
        })

        heart_rate_history.append({
            "value": record.heart_rate,
            "date": record_date
        })

        blood_oxygen_history.append({
            "value": record.blood_oxygen_level,
            "date": record_date
        })

        body_weight_history.append({
            "value": record.body_weight,
            "date": record_date
        })

        if record.systolic > 130:
            risk_alert = "pressão arterial acima do normal"

        elif record.heart_rate > 100:
            risk_alert = "frequência cardíaca elevada"

        elif record.blood_oxygen_level < 0.95:
            risk_alert = "nível de oxigenação abaixo do ideal"

    return {
        "id": user_id,

        "reportPeriod": {
            "startDate": start_date,
            "endDate": end_date
        },

        "bloodPressureHistory": blood_pressure_history,

        "heartRateHistory": heart_rate_history,

        "bloodOxygenHistory": blood_oxygen_history,

        "bodyWeightHistory": body_weight_history,

        "riskAlert": risk_alert
    }