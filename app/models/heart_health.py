from sqlalchemy import Column, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class HeartHealthRecord(Base):
    __tablename__ = "heart_health_records"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    systolic = Column(Integer, nullable=False)
    diastolic = Column(Integer, nullable=False)

    heart_rate = Column(Integer, nullable=False)

    blood_oxygen_level = Column(Float, nullable=False)

    body_weight = Column(Float, nullable=False)

    shortness_of_breath = Column(Boolean, default=False)

    chest_pain = Column(Boolean, default=False)

    dizziness = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())