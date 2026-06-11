from app.schemas.user import UserLogin
from app.utils.security import hash_password, verify_password


def test_user_login_schema():
    login = UserLogin(
        email="teste@email.com",
        senha="123456"
    )

    assert login.email == "teste@email.com"
    assert login.senha == "123456"


def test_verify_password():
    senha = "123456"

    senha_hash = hash_password(senha)

    assert verify_password(senha, senha_hash) is True


def test_verify_wrong_password():
    senha_hash = hash_password("123456")

    assert verify_password("senha_errada", senha_hash) is False