from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.schemas.api_responses import REGISTER_RESPONSES, LOGIN_RESPONSES
from app.services.auth_service import register_user, login_user
from app.utils.security import create_access_token

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses=REGISTER_RESPONSES
)
def register(user: UserCreate):
    return register_user(user)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,  # Fix #7: login não cria recurso, deve ser 200
    responses=LOGIN_RESPONSES
)
def login(user: UserLogin):
    db_user, message = login_user(user.email, user.senha)

    if not db_user:
        if message == "Usuário não encontrado":
            raise HTTPException(status_code=404, detail=message)
        if message == "Senha incorreta":
            raise HTTPException(status_code=401, detail=message)
        raise HTTPException(status_code=400, detail=message)

    token = create_access_token({
        "sub": db_user["email"],
        "id": db_user["id"]
    })

    return {
        "message": message,
        "access_token": token,
        "token_type": "bearer",
        "user": db_user
    }