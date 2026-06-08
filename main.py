from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)