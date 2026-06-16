from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth_routes import router as auth_router
from app.routes.heart_health_routes import router as heart_health_router
from app.routes.heart_report_routes import router as heart_report_router
from app.database import Base, engine

from app.models.user import User
from app.models.heart_health import HeartHealthRecord

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(heart_health_router)
app.include_router(heart_report_router)