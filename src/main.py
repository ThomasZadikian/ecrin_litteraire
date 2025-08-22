from fastapi import FastAPI
from src.infrastructure.api import livre_router

app = FastAPI(
    title="Écrin Littéraire",
    description="API pour la gestion de l'Écrin Littéraire",
    version="1.0.0"
)

app.include_router(livre_router.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenue sur l'API de l'Écrin Littéraire"}