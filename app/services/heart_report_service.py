from datetime import date
from typing import List

from fastapi import HTTPException

from app.database import SessionLocal
from app.models.heart_health import HeartHealthRecord


def generate_heart_report(
    user_id: int,
    start_date: date,
    end_date: date
):
    db = SessionLocal()

    try:
        records = (
            db.query(HeartHealthRecord)
            .filter(HeartHealthRecord.user_id == user_id)
            .filter(HeartHealthRecord.created_at >= start_date)
            .filter(HeartHealthRecord.created_at <= end_date)
            .order_by(HeartHealthRecord.created_at.asc())
            .all()
        )

        if not records:
            raise HTTPException(
                status_code=404,
                detail="Relatório não encontrado para o período informado"
            )

        blood_pressure_history = []
        heart_rate_history = []
        blood_oxygen_history = []
        body_weight_history = []

        risk_alerts: List[str] = []

        for record in records:

            blood_pressure_history.append({
                "recordId": record.id,
                "systolic": record.systolic,
                "diastolic": record.diastolic,
                "date": record.created_at.strftime("%Y-%m-%d"),
                "time": record.created_at.strftime("%H:%M:%S"),
                "datetime": record.created_at.isoformat()
            })

            heart_rate_history.append({
                "recordId": record.id,
                "value": record.heart_rate,
                "date": record.created_at.strftime("%Y-%m-%d"),
                "time": record.created_at.strftime("%H:%M:%S"),
                "datetime": record.created_at.isoformat()
            })

            blood_oxygen_history.append({
                "recordId": record.id,
                "value": record.blood_oxygen_level,
                "date": record.created_at.strftime("%Y-%m-%d"),
                "time": record.created_at.strftime("%H:%M:%S"),
                "datetime": record.created_at.isoformat()
            })

            body_weight_history.append({
                "recordId": record.id,
                "value": record.body_weight,
                "date": record.created_at.strftime("%Y-%m-%d"),
                "time": record.created_at.strftime("%H:%M:%S"),
                "datetime": record.created_at.isoformat()
            })

            if record.systolic > 130:
                risk_alerts.append(
                    "pressão arterial acima do normal"
                )

            if record.heart_rate > 100:
                risk_alerts.append(
                    "frequência cardíaca elevada"
                )

            if record.blood_oxygen_level < 0.95:
                risk_alerts.append(
                    "nível de oxigenação abaixo do ideal"
                )

            if record.chest_pain:
                risk_alerts.append(
                    "dor no peito relatada"
                )

            if record.shortness_of_breath:
                risk_alerts.append(
                    "falta de ar relatada"
                )

            if record.dizziness:
                risk_alerts.append(
                    "tontura relatada"
                )

        seen = set()
        unique_alerts = []

        for alert in risk_alerts:
            if alert not in seen:
                seen.add(alert)
                unique_alerts.append(alert)

        risk_alert = (
            ", ".join(unique_alerts)
            if unique_alerts
            else "nenhum risco identificado"
        )

        return {
            "id": user_id,

            "totalRecords": len(records),

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

    finally:
        db.close()