from pydantic import BaseModel, EmailStr
from datetime import date


class RegisterRequest(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
    password: str
    birthDate: date
    gender: str
    country: str