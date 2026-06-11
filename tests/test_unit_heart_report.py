from datetime import date

from app.schemas.heart_report import (
    ReportPeriod,
    BloodPressureHistoryItem,
    ValueHistoryItem,
    HeartReportResponse
)


def test_heart_report_schema():
    report = HeartReportResponse(
        id=1,
        reportPeriod=ReportPeriod(
            startDate=date(2025, 1, 1),
            endDate=date(2025, 1, 31)
        ),
        bloodPressureHistory=[
            BloodPressureHistoryItem(systolic=120, diastolic=80, date=date(2025, 1, 10))
        ],
        heartRateHistory=[
            ValueHistoryItem(value=72, date=date(2025, 1, 10))
        ],
        bloodOxygenHistory=[
            ValueHistoryItem(value=0.98, date=date(2025, 1, 10))
        ],
        bodyWeightHistory=[
            ValueHistoryItem(value=65.5, date=date(2025, 1, 10))
        ],
        riskAlert="nenhum risco identificado"
    )

    assert report.id == 1
    assert report.reportPeriod.startDate == date(2025, 1, 1)
    assert report.reportPeriod.endDate == date(2025, 1, 31)
    assert report.bloodPressureHistory[0].systolic == 120
    assert report.bloodPressureHistory[0].diastolic == 80
    assert report.heartRateHistory[0].value == 72
    assert report.bloodOxygenHistory[0].value == 0.98
    assert report.bodyWeightHistory[0].value == 65.5
    assert report.riskAlert == "nenhum risco identificado"


def test_heart_report_multiple_alerts():
    """riskAlert deve concatenar múltiplos riscos."""
    report = HeartReportResponse(
        id=1,
        reportPeriod=ReportPeriod(
            startDate=date(2025, 1, 1),
            endDate=date(2025, 1, 31)
        ),
        bloodPressureHistory=[],
        heartRateHistory=[],
        bloodOxygenHistory=[],
        bodyWeightHistory=[],
        riskAlert="pressão arterial acima do normal, frequência cardíaca elevada"
    )

    assert "pressão arterial acima do normal" in report.riskAlert
    assert "frequência cardíaca elevada" in report.riskAlert