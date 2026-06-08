from app.schemas.user import UserLogin

def test_user_login_schema():
    login = UserLogin(
        email="teste@email.com",
        senha="123456"
    )

    assert login.email == "teste@email.com"