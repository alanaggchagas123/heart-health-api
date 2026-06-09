from pydantic import BaseModel
from datetime import date
from typing import List

class ReportPeriod(BaseModel):
    startDate: date
    endDate: date

class BloodPressureHistoryItem(BaseModel):
    systolic: int
    diastolic: int
    date: date

class ValueHistoryItem(BaseModel):
    value: float
    date: date

class HeartReportResponse(BaseModel):
    id: int

    reportPeriod: ReportPeriod

    bloodPressureHistory: List[BloodPressureHistoryItem]

    heartRateHistory: List[ValueHistoryItem]

    bloodOxygenHistory: List[ValueHistoryItem]

    bodyWeightHistory: List[ValueHistoryItem]

    riskAlert: str