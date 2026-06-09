from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password, verify_password


# REGISTER
def register_user(user):
    db = SessionLocal()

    new_user = User(
        nome=user.nome,
        sobrenome=user.sobrenome,
        email=user.email,
        telefone=user.telefone,
        senha=hash_password(user.senha),
        data_nascimento=user.data_nascimento,
        sexo=user.sexo,
        pais=user.pais
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return new_user

# LOGIN
def login_user(email, senha):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        db.close()
        return None, "Usuário não encontrado"

    if not verify_password(senha, user.senha):
        db.close()
        return None, "Senha incorreta"

    user_data = {
        "id": user.id,
        "nome": user.nome,
        "email": user.email
    }

    db.close()

    return user_data, "Login realizado com sucesso"