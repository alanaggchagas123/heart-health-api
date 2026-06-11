from pydantic import BaseModel, ConfigDict, model_validator
from datetime import date


class UserCreate(BaseModel):
    nome: str
    sobrenome: str
    email: str
    telefone: str
    senha: str
    confirmar_senha: str
    data_nascimento: date
    sexo: str
    pais: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserCreate":
        if self.senha != self.confirmar_senha:
            raise ValueError("Repetição da senha não confere")
        return self


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

    model_config = ConfigDict(from_attributes=True)
