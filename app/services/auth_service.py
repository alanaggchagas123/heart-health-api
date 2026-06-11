from fastapi import HTTPException

from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password, verify_password


# REGISTER
def register_user(user):
    db = SessionLocal()
    try:
        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Usuário já cadastrado"
            )

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

        return new_user

    finally:
        db.close()


# LOGIN
def login_user(email, senha):
    db = SessionLocal()
    try:
        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None, "Usuário não encontrado"

        if not verify_password(senha, user.senha):
            return None, "Senha incorreta"

        user_data = {
            "id": user.id,
            "nome": user.nome,
            "email": user.email
        }

        return user_data, "Login realizado com sucesso"

    finally:
        db.close()
