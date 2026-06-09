from fastapi import APIRouter
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.services.auth_service import register_user, login_user

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    return register_user(user)


@router.post("/login")
def login(user: UserLogin):
    db_user, message = login_user(user.email, user.senha)

    if not db_user:
        return {"error": message}

    return {
        "message": message,
        "user": {
            "id": db_user.id,
            "email": db_user.email
        }
    }