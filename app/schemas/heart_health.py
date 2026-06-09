from pydantic import BaseModel, ConfigDict
from typing import Optional


class BloodPressureSchema(BaseModel):
    systolic: int
    diastolic: int


class SymptomsSchema(BaseModel):
    shortnessOfBreath: bool
    chestPain: bool
    dizziness: bool


class HeartHealthCreate(BaseModel):
    userId: int
    
    bloodPressure: BloodPressureSchema
    heartRate: int
    bloodOxygenLevel: float
    bodyWeight: float
    symptoms: SymptomsSchema


class HeartHealthResponse(HeartHealthCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)