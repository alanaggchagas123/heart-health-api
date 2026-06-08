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