from app.schemas.user import UserCreate
from app.utils.security import hash_password

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



def test_password_is_hashed():
    senha = "123456"

    senha_hash = hash_password(senha)

    assert senha_hash != senha