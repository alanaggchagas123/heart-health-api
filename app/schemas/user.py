from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    nome: str
    sobrenome: str
    email: str
    telefone: str
    senha: str
    data_nascimento: date
    sexo: str
    pais: str


class UserLogin(BaseModel):
    email: str
    senha: str


class UserResponse(BaseModel):
    id: int
    nome: str
    sobrenome: str
    email: str
    telefone: str
    data_nascimento: date
    sexo: str
    pais: str

    class Config:
        from_attributes = True