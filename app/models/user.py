# app/models/user.py
from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    sobrenome = Column(String(100))
    email = Column(String(120), unique=True, index=True)
    telefone = Column(String(20))
    senha = Column(String(255))
    data_nascimento = Column(Date)
    sexo = Column(String(10))
    pais = Column(String(50))