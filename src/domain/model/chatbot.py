from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.model.utilisateur import Utilisateur

class ChaBot(BaseModel): 
    id: UUID
    nom: str
    utilisateur: list[Utilisateur]