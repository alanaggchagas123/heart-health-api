from app.database import SessionLocal
from app.models.user import User


# ----------------------------
# REGISTER
# ----------------------------
def register_user(user):
    db = SessionLocal()

    # cria usuário no banco
    new_user = User(
        nome=user.nome,
        sobrenome=user.sobrenome,
        email=user.email,
        telefone=user.telefone,
        senha=user.senha,
        data_nascimento=user.data_nascimento,
        sexo=user.sexo,
        pais=user.pais
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return new_user


# ----------------------------
# LOGIN
# ----------------------------
def login_user(email, senha):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    db.close()

    if not user:
        return None, "Usuário não encontrado"

    if user.senha != senha:
        return None, "Senha inválida"

    return user, "Login realizado com sucesso"