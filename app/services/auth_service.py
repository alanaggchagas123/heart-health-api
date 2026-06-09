from app.database import SessionLocal
from app.models.user import User
import bcrypt


# ----------------------------
# HASH
# ----------------------------
def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str):
    return bcrypt.checkpw(password.encode(), hashed.encode())


# ----------------------------
# REGISTER
# ----------------------------
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


# ----------------------------
# LOGIN
# ----------------------------
def login_user(email, senha):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        db.close()
        return None, "Usuário não encontrado"

    if not verify_password(senha, user.senha):
        db.close()
        return None, "Senha incorreta"

    db.close()

    return user, "Login realizado com sucesso"