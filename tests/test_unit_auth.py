from app.schemas.user import UserCreate
from app.utils.security import hash_password
import pytest


def test_user_create_schema():
    user = UserCreate(
        nome="João",
        sobrenome="Silva",
        email="joao@email.com",
        telefone="21999999999",
        senha="123456",
        confirmar_senha="123456",
        data_nascimento="2000-01-01",
        sexo="M",
        pais="Brasil"
    )

    assert user.nome == "João"
    assert user.sobrenome == "Silva"
    assert user.email == "joao@email.com"
    assert user.telefone == "21999999999"
    assert user.pais == "Brasil"


def test_password_mismatch_raises():
    with pytest.raises(Exception):
        UserCreate(
            nome="João",
            sobrenome="Silva",
            email="joao@email.com",
            telefone="21999999999",
            senha="123456",
            confirmar_senha="654321",
            data_nascimento="2000-01-01",
            sexo="M",
            pais="Brasil"
        )


def test_password_is_hashed():
    senha = "123456"
    senha_hash = hash_password(senha)

    assert senha_hash != senha
    assert isinstance(senha_hash, str)