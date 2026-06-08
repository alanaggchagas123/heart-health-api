from app.schemas.user import UserCreate, UserLogin


def test_user_create_schema():
    user = UserCreate(
        nome="João",
        sobrenome="Silva",
        email="joao@email.com",
        telefone="219999999",
        senha="123456",
        data_nascimento="2000-01-01",
        sexo="M",
        pais="Brasil"
    )

    assert user.email == "joao@email.com"
    assert user.nome == "João"


def test_user_login_schema():
    login = UserLogin(
        email="teste@email.com",
        senha="123456"
    )

    assert login.email == "teste@email.com"