from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.infrastructure.api import livre_router
from src.infrastructure.persistance.database import engine
from src.infrastructure.persistance.models import Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Écrin Littéraire",
    description="API pour la gestion de l'Écrin Littéraire",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(livre_router.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenue sur l'API de l'Écrin Littéraire"}